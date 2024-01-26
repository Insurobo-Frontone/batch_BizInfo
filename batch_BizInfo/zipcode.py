import json, os, sys, time, fs, requests, re

from datetime import datetime, timedelta
from dotenv import load_dotenv
from sqlalchemy import Column, create_engine, text, desc
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
               .filter(Column('data_skip') == 0)
               .order_by(desc(Column('id')))
               .all())

    for rec in res_all:
        keyword = rec.address.split(',')[0]
        juso_reqdata = {
            "confmKey": JUSO_KEY,
            "currentPage": 1,
            "countPerPage": 1,
            "keyword": keyword,
            "resultType": 'json',
            "hstryYn": 'N',
            "addInfoYn": 'N',
        }

        response = requests.request("POST", JUSO_URL, data=juso_reqdata, timeout=int(JUSO_TIMEOUT) / 1000)
        if response.status_code == 200:
            result_of_api = response.json().get('results').get('common').get('errorCode')
            totalCount = response.json().get('results').get('common').get('totalCount')
            # if result_of_api != '0' and totalCount > 0:
            juso_datas.append({"SEQ": rec.id, "response": response.json()})


    for juso_data in juso_datas:
        roadAddr = juso_data.get('response').get('results').get('juso')[0].get('roadAddr')
        jibunAddr = juso_data.get('response').get('results').get('juso')[0].get('jibunAddr')
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
        stm_fld = session.query(model.t_stm_fld).filter(Column('id') == juso_data['SEQ']).first()

        if stm_fld_batch.zipCode is None:
            to_update = {
                "zipCode": zipNo,
            }
            session.query(model.t_stm_fld_batch).filter(Column('id') == stm_fld_batch.id).update(to_update)
            session.query(model.t_stm_fld).filter(Column('id') == stm_fld_batch.id).update(to_update)
            # # session.query(model.t_stm_fld_batch).filter(Column('id') == stm_fld_batch.id).update({"db_processed": 1})
            session.commit()

def process():
    ApiConnectAddress()

if __name__ == '__main__':
    process()
