import os
import sys
import time
import fs
import requests
import re
import json

from datetime import datetime, timedelta
from dotenv import load_dotenv
from sqlalchemy import Column, create_engine, text, desc, or_
from sqlalchemy.orm import sessionmaker

from pprint import pprint as pp

from models import model

load_dotenv()
file_path = "./last_updated"
ConnectionString = os.environ.get("ConnectionString")

# juso
JUSO_URL = os.environ.get("JUSO_URL")
JUSO_KEY = os.environ.get("JUSO_KEY")
JUSO_TIMEOUT = os.environ.get("JUSO_TIMEOUT")

# cover
COVER_URL = os.environ.get("COVER_URL")
COVER_KEY = os.environ.get("COVER_KEY")
COVER_TIMEOUT = os.environ.get("COVER_TIMEOUT")

Variable_tableName = "stm_fld_batch"
# 저장된시간 불러와서 30000
engine = create_engine(ConnectionString, echo=True)
connection = engine.connect()

Session = sessionmaker(bind=engine)
session = Session()


def ApiConnectAddress():
    juso_datas = []
    cover_datas = []

    res_all = (session.query(model.t_stm_fld_batch).filter(Column('address') != None)
               .filter(or_(Column('strct_cd_nm') == None, Column('strct_cd_nm') == ''))
               # .filter(Column('data_skip') == 0)
               # .filter(Column('id') == 663)
               .order_by(desc(Column('id')))
               .all())

    for rec in res_all:
        keyword = rec.address.split(',')[0]
        keyword = keyword.split('(')[0]
        juso_reqdata = {
            "confmKey": JUSO_KEY,
            "currentPage": 1,
            "countPerPage": 1,
            "keyword": keyword,
            "resultType": 'json',
            "hstryYn": 'N',
            "addInfoYn": 'N',
        }

        # pp(juso_reqdata)

        response = requests.request("POST", JUSO_URL, data=juso_reqdata, timeout=10.0)
        # pp(response)
        if response.status_code == 200:
            result_of_api = response.json().get('results').get('common').get('errorCode')
            totalCount = response.json().get('results').get('common').get('totalCount')
            # if result_of_api != '0' and totalCount > 0:
            juso_datas.append({"SEQ": rec.id, "response": response.json()})

    # pp(juso_datas)
    # exit()

    for juso_data in juso_datas:
        roadAddr = juso_data.get('response').get('results').get('juso')[0].get('roadAddr')
        jibunAddr = juso_data.get('response').get('results').get('juso')[0].get('jibunAddr')
        sggNm = juso_data.get('response').get('results').get('juso')[0].get('sggNm')
        siNm = juso_data.get('response').get('results').get('juso')[0].get('siNm')
        zipNo = juso_data.get('response').get('results').get('juso')[0].get('zipNo')
        admCd = juso_data.get('response').get('results').get('juso')[0].get('admCd')
        platGbCd = juso_data.get('response').get('results').get('juso')[0].get('platGbCd')
        lnbrMnnm = juso_data.get('response').get('results').get('juso')[0].get('lnbrMnnm')
        lnbrSlno = juso_data.get('response').get('results').get('juso')[0].get('lnbrSlno')
        mtYn = juso_data.get('response').get('results').get('juso')[0].get('mtYn')
        # pp(data.get('results').get('juso')[0])
        # response = requests.request("POST", JUSO_URL, data=juso_reqdata)
        sigungucd = admCd[0:5]
        bjdongcd = admCd[-5:]
        now = datetime.now()
        startDate = endDate = now.strftime("%Y%m%d")

        stm_fld_batch = session.query(model.t_stm_fld_batch).filter(Column('id') == juso_data['SEQ']).first()
        # stm_fld = session.query(model.t_stm_fld).filter(Column('id') == juso_data['SEQ']).first()
        # biz_type=stm_fld_batch.biz_type
        # search = "%{}%".format(stm_fld_batch.biz_type)
        # in103cr = session.query(model.t_IN103CR).where(Column('CODE').like(search)).first()

        PTYKORNM = "%{}%".format(stm_fld_batch.ceo_name)
        PTYBIZNM = "%{}%".format(stm_fld_batch.biz_name)

        BIZNO = "%{}%".format(stm_fld_batch.biz_no)
        in101tr = session.query(model.t_IN101TR).filter(Column('PTYKORNM').like(PTYKORNM)).filter(
            Column('PTYBIZNM').like(PTYBIZNM)).filter(Column('BIZNO').like(BIZNO)).first()
        # if stm_fld_batch.zipCode is None:
        to_update = {
            "bunjiAddr": jibunAddr,
            "zipCode": zipNo,
            "roadAddr": roadAddr,
            "capitalDo": compress_capital_si(siNm),
            "si": compress_sido(sggNm),

        }

        # pp(to_update)

        session.query(model.t_stm_fld_batch).filter(Column('id') == stm_fld_batch.id).update(to_update)
        session.query(model.t_stm_fld).filter(Column('id') == stm_fld_batch.id).update(to_update)
        # # session.query(model.t_stm_fld_batch).filter(Column('id') == stm_fld_batch.id).update({"db_processed": 1})
        # pp(in101tr)
        if in101tr is not None:
            to_update = {
                "phoneNum": in101tr.TELNO,
                "birthDate": in101tr.INR_BIRTH,
                "sex": 'F' if int(in101tr.INR_GENDER) % 2 == 0 else 'M',
            }

            # pp(to_update)

            session.query(model.t_stm_fld_batch).filter(Column('id') == stm_fld_batch.id).update(to_update)
            session.query(model.t_stm_fld).filter(Column('id') == stm_fld_batch.id).update(to_update)
            # # session.query(model.t_stm_fld_batch).filter(Column('id') == stm_fld_batch.id).update({"db_processed": 1})

        # stm_fld_batch = session.query(model.t_stm_fld_batch).filter(Column('id') == juso_data['SEQ']).first()
        # # stm_fld = session.query(model.t_stm_fld).filter(Column('id') == juso_data['SEQ']).first()
        # # biz_type=stm_fld_batch.biz_type
        # search = "%{}%".format(stm_fld_batch.biz_type)
        # in103cr = session.query(model.t_IN103CR).where(Column('CODE').like(search)).first()
        #
        # to_update = {
        #     "biz_type": in103cr.NAME,
        # }

        # pp(to_update)

        # session.query(model.t_stm_fld_batch).filter(Column('id') == stm_fld_batch.id).update(to_update)
        # session.query(model.t_stm_fld).filter(Column('id') == stm_fld_batch.id).update(to_update)
        # # session.query(model.t_stm_fld_batch).filter(Column('id') == stm_fld_batch.id).update({"db_processed": 1})
        session.commit()


def compress_sido(sido):
    if sido != '':
        if re.search(r' ', sido, re.IGNORECASE):
            sido = sido.split(' ')[0]
        if re.search(r'시', sido[-1], re.IGNORECASE):
            sido = sido[0:-1]
        return sido


def compress_capital_si(sido):
    tmp = ""
    if re.findall(r'충청', sido, re.IGNORECASE):
        tmp += "충"
    elif re.findall(r'전라', sido, re.IGNORECASE):
        tmp += "전"
    elif re.findall(r'경상', sido, re.IGNORECASE):
        tmp += "경"

    if re.findall(r'남도', sido, re.IGNORECASE):
        tmp += "남"
    elif re.findall(r'북도', sido, re.IGNORECASE):
        tmp += "북"
    sinm = tmp

    if re.findall(r'서울', sido, re.IGNORECASE):
        sinm = "서울"
    elif re.findall(r'경기', sido, re.IGNORECASE):
        sinm = "경기"
    elif re.findall(r'인천', sido, re.IGNORECASE):
        sinm = "인천"
    elif re.findall(r'강원', sido, re.IGNORECASE):
        sinm = "강원"
    elif re.findall(r'제주', sido, re.IGNORECASE):
        sinm = "제주"
    elif re.findall(r'광주', sido, re.IGNORECASE):
        sinm = "광주"
    elif re.findall(r'대구', sido, re.IGNORECASE):
        sinm = "대구"
    elif re.findall(r'대전', sido, re.IGNORECASE):
        sinm = "대전"
    elif re.findall(r'울산', sido, re.IGNORECASE):
        sinm = "울산"
    elif re.findall(r'부산', sido, re.IGNORECASE):
        sinm = "부산"
    elif re.findall(r'세종', sido, re.IGNORECASE):
        sinm = "세종"
    elif re.findall(r'전북', sido, re.IGNORECASE):
        sinm = "전북"
    elif re.findall(r'전남', sido, re.IGNORECASE):
        sinm = "전남"
    elif re.findall(r'경북', sido, re.IGNORECASE):
        sinm = "경북"
    elif re.findall(r'경남', sido, re.IGNORECASE):
        sinm = "경남"
    elif re.findall(r'충북', sido, re.IGNORECASE):
        sinm = "충북"
    elif re.findall(r'충남', sido, re.IGNORECASE):
        sinm = "충남"
    return sinm


def process():
    ApiConnectAddress()


if __name__ == '__main__':
    process()
