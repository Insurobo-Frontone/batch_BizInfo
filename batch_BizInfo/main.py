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


def check_and_create():
    if not engine.dialect.has_table(connection, Variable_tableName):  # If table don't exist, Create.
        with open("./create_batch_table.sql") as file:
            query = text(file.read())
            connection.execute(query)
            connection.commit()


def data_copy_for_batch():
    sql = ("insert into stm_fld_batch (id, biz_name, ceo_name, biz_type, building_division, `address`, detail_address, "
           "`area`, biz_site_lease, ugrnd_flr_cnt, bld_tot_lyr_num, input_bld_st, input_bld_ed, strct_cd_nm, "
           "roof_strc, otwl_strc, worker_num_standard_under_yn, worker_num, sales_standard_under_yn, "
           "sales, biz_no, termsA1, termsA2, termsA3, termsA4, termsA6, termsA7, imputation_reason_confirm_yn, "
           "create_date, termsA8, difStmFldJoinYn, phoneNum, birthDate, sex, jehuCd, roadAddr, zipCode, squareMeter, "
           "bunjiAddr, capitalDo, si, grade,"
           "data_processed,db_processed, data_skip) select a.id id, a.biz_name biz_name, a.ceo_name ceo_name, "
           "a.biz_type biz_type,a.building_division building_division,a.address `address`,a.detail_address "
           "detail_address,a.area area, "
           "a.biz_site_lease biz_site_lease,a.ugrnd_flr_cnt ugrnd_flr_cnt,a.bld_tot_lyr_num bld_tot_lyr_num,"
           "a.input_bld_st input_bld_st,a.input_bld_ed input_bld_ed,a.strct_cd_nm strct_cd_nm,a.roof_strc roof_strc,"
           "a.otwl_strc otwl_strc,a.worker_num_standard_under_yn worker_num_standard_under_yn,a.worker_num "
           "worker_num,a.sales_standard_under_yn sales_standard_under_yn, a.sales sales,"
           "a.biz_no biz_no,a.termsA1 termsA1,a.termsA2 termsA2, a.termsA3 termsA3, a.termsA4 termsA4, "
           "a.termsA6 termsA6, a.termsA7 termsA7,a.imputation_reason_confirm_yn imputation_reason_confirm_yn, "
           "a.create_date create_date, a.termsA8 termsA8, a.difStmFldJoinYn difStmFldJoinYn,a.phoneNum phoneNum, "
           "a.birthDate birthDate, a.sex sex, a.jehuCd jehuCd, a.roadAddr roadAddr, a.zipCode zipCode, "
           "a.squareMeter squareMeter, a.bunjiAddr bunjiAddr, a.capitalDo capitalDo,a.si si, a.grade grade,  "
           "0 data_processed, 0 db_processed,"
           "0 data_skip FROM stm_fld a LEFT JOIN stm_fld_batch b ON a.id = b.id WHERE b.id IS NULL GROUP BY a.id "
           "ORDER BY a.id")
    connection.execute(text(sql))
    skip_sql = "update stm_fld_batch set data_skip = 1 where address is null"
    connection.execute(text(skip_sql))
    result = connection.commit()


def ApiConnectAddress():
    try:
        with open(file_path, 'r+') as file:
            temp_data = json.load(file)
        olddt = datetime.fromtimestamp(temp_data)
        for_comparision = olddt + timedelta(milliseconds=int(COVER_TIMEOUT))
        nowdt = datetime.now()
        # if for_comparision >= nowdt:
        #     sys.exit(1)

        juso_datas = []
        cover_datas = []
        res_all = (session.query(model.t_stm_fld_batch).filter(Column('address') != None)
                   # .filter(or_(Column('strct_cd_nm') == None, Column('strct_cd_nm') == ''))
                   # .filter(Column('db_processed') == 0)
                   # .filter(Column('data_processed') == 0)
                   # .filter(Column('data_skip') == 0)
                   .order_by(desc(Column('id')))
                   #.limit(200)
                   .all())

        for rec in res_all:
            keyword = rec.address.split(',')[0]
            keyword = keyword.split('(')[0]
            # pp(keyword)
            juso_reqdata = {
                "confmKey": JUSO_KEY,
                "currentPage": 1,
                "countPerPage": 1,
                "keyword": keyword,
                "resultType": 'json',
                "hstryYn": 'N',
                "addInfoYn": 'N',
            }

            response = requests.request("POST", JUSO_URL, data=juso_reqdata, timeout=15.0)
            if response.status_code == 200:
                result_of_api = response.json().get('results').get('common').get('errorCode')
                totalCount = response.json().get('results').get('common').get('totalCount')
                # if result_of_api != '0' and totalCount > 0:
                juso_datas.append({"SEQ": rec.id, "response": response.json()})

        for juso_data in juso_datas:
            # pp(response.json())
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

            cover_reqdata = {
                'serviceKey': COVER_KEY,
                "sigunguCd": sigungucd,  # admCd
                "bjdongCd": bjdongcd,  # admCd
                # "platGbCd": mtYn,  # mtYn
                "bun": lnbrMnnm.rjust(4, '0'),  # lnbrMnnm
                "ji": lnbrSlno.rjust(4, '0'),  # lnbrSlno
                # "zip": zipNo,
                # "startDate": startDate,  # YYYYMMDD
                # "endDate": endDate,  # YYYYMMDD
                "numOfRows": 100,  # 1
                # "pageNo": 1,  # 1
                "_type": "json",
            }
            cover_datas.append(
                {"cover_reqdata": cover_reqdata, "SEQ": juso_data.get('SEQ'), "zipcode": zipNo, "jibunAddr": jibunAddr,
                 'roadAddr': roadAddr, "cover_response": None})

        list(map(get_cover, cover_datas))
        # pp(cover_datas)

        list(map(data_process, cover_datas))

    finally:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(datetime.now().timestamp(), file)


def restore_to_origin():
    res_all = session.query(model.t_stm_fld_batch).filter(
        Column('db_processed') == 0).filter(
        Column('data_processed') == 1).filter(
        Column('data_skip') == 0).all()

    list(map(db_process, res_all))


def db_process(t_stm_fld_batch):
    stm_fld_batch = session.query(model.t_stm_fld_batch).filter(Column('id') == t_stm_fld_batch[0]).first()
    stm_fld = session.query(model.t_stm_fld).filter(Column('id') == t_stm_fld_batch[0]).first()
    to_update = {
        "address": stm_fld_batch.address,
        "roadAddr": stm_fld_batch.roadAddr,
        "bunjiAddr": stm_fld_batch.bunjiAddr,
        "zipCode": stm_fld_batch.zipCode,
        "si": stm_fld_batch.si,
        "capitalDo": stm_fld_batch.capitalDo,
        "bld_tot_lyr_num": stm_fld_batch.bld_tot_lyr_num,
        "ugrnd_flr_cnt": stm_fld_batch.ugrnd_flr_cnt,
        "strct_cd_nm": stm_fld_batch.strct_cd_nm,
        "roof_strc": stm_fld_batch.roof_strc,
        "otwl_strc": stm_fld_batch.otwl_strc,
    }
    session.query(model.t_stm_fld).filter(Column('id') == stm_fld_batch.id).update(to_update)
    session.query(model.t_stm_fld_batch).filter(Column('id') == stm_fld_batch.id).update({"db_processed": 1})
    session.commit()
    time.sleep(1)


def data_process(data):
    if data.get("cover_response") == None:
        return
    stm_fld_batch = session.query(model.t_stm_fld_batch).filter(Column('id') == data.get('SEQ')).filter(
        Column('data_processed') == 0).first()
    # stm_fld_batch = session.query(model.t_stm_fld_batch).filter(Column('id') == data.get('SEQ')).first()
    if (True or (stm_fld_batch.address == None or stm_fld_batch.roadAddr == None) or (
            stm_fld_batch.zipCode == None) or (
            stm_fld_batch.bld_tot_lyr_num == None or stm_fld_batch.bld_tot_lyr_num == '' or int(
        stm_fld_batch.bld_tot_lyr_num) == 0) or (stm_fld_batch.strct_cd_nm == None) or (
            stm_fld_batch.roof_strc == None) or (stm_fld_batch.otwl_strc == None or stm_fld_batch.otwl_strc == False)):
        to_update = {
            "bunjiAddr": data.get("jibunAddr"),
            "roadAddr": data.get("roadAddr"),
            "zipCode": data.get("zipcode"),
            "bld_tot_lyr_num": data.get("cover_response").get('grndFlrCnt'),
            "ugrnd_flr_cnt": data.get("cover_response").get('ugrndFlrCnt'),
            "strct_cd_nm": data.get("cover_response").get('strct_cd_nm'),
            "roof_strc": data.get("cover_response").get('roof_strc'),
            "otwl_strc": data.get("cover_response").get('otwlStrc'),
            "data_processed": 1,
        }
        session.query(model.t_stm_fld_batch).filter(Column('id') == data.get('SEQ')).filter(
            Column('data_processed') == 0).update(to_update)
        grade = judge_grade(data.get("cover_response"))
        to_update = {"grade": grade}
        session.query(model.t_stm_fld_batch).filter(Column('id') == data.get('SEQ')).update(to_update)
        # session.query(model.t_stm_fld_batch).filter(Column('id') == data.get('SEQ')).update(to_update)
        #
        # session.commit()
        # if stm_fld_batch.zipCode == None or stm_fld_batch.zipCode == '':
        #     to_update_zip = {
        #         "zipCode": data.get("zipcode"),
        #     }
        # session.query(model.t_stm_fld_batch).filter(Column('id') == data.get('SEQ')).filter(
        #     Column('data_processed') == 1).update(to_update_zip)
        session.commit()


def get_cover(data):
    response_cover = requests.request("GET", COVER_URL, params=data.get('cover_reqdata'),
                                      timeout=15.0)
    try:
        got_json = response_cover.json()
        if (type(got_json['response']['body']['items']) is dict
                and got_json['response']['body']['totalCount'] > 0):
            if type(got_json['response']['body']['items']['item']) is dict:
                data["cover_response"] = judge_structure(got_json['response']['body']['items']['item'])
            elif type(response_cover.json()['response']['body']['items']['item']) is list:
                data["cover_response"] = judge_structure(
                    getSmallmainAtchGbCd(got_json['response']['body']['items']['item']))

            return data
    except Exception as e:
        return False
    # finally:
    #     pp(response_cover)
    #     pp(data)
    # with open(file_path, 'w', encoding='utf-8') as file:
    #     json.dump(datetime.now().timestamp(), file)
    # sys.exit(1)


def getSmallmainAtchGbCd(datas):
    for data in datas:
        if data["mainAtchGbCd"] == 0:
            # pp(data)
            return data


def judge_grade(data):
    # data['etcStrc']
    # data['etcRoof']
    # data['otwlStrc']
    if data is None:
        return None

    etcStrct = data.get('etcStrct')
    etcRoof = data.get('etcRoof')
    otwlStrc = data.get('otwlStrc')

    if etcStrct is None or etcRoof is None or otwlStrc is None:
        return None

    flag = 0

    if len(re.findall(r'블록|브럭|철골', etcStrct, re.IGNORECASE)) > 0:
        flag = flag - 1
    elif len(re.findall(r'조적|내화|철근|슬라브|콘크리트', etcStrct, re.IGNORECASE)) > 0:
        flag = flag + 1
    if len(re.findall(r'판넬|슬레트|슬레이트', etcRoof, re.IGNORECASE)) > 0:
        flag = flag + 0
    elif len(re.findall(r'조적|내화|철근|슬라브|스라브', etcRoof, re.IGNORECASE)) > 0:
        flag = flag + 1
    if len(re.findall(r'조적|내화|철근|슬라브|콘크리트', otwlStrc, re.IGNORECASE)) > 0:
        flag = flag + 1

    # 지하구분
    input_bld_st = data.get('input_bld_st')
    if input_bld_st is None:
        input_bld_st = '1'

    if len(re.findall(r'B|지하', input_bld_st, re.IGNORECASE)) > 0:
        flag = flag - 1

    if flag >= 3:
        grade = "1등급"
    elif flag == 2:
        grade = "2등급"
    elif flag == 1:
        grade = "3등급"
    else:
        grade = "4등급"

    return grade

    # if len(re.findall(r'벽돌|조적', etcStrct, re.IGNORECASE)) > 0:
    #     otwlStrc = "벽돌(조직) 외벽"
    # elif len(re.findall(r'블록|블럭', etcStrct, re.IGNORECASE)) > 0:
    #     otwlStrc = "블록 외벽"
    # elif len(re.findall(r'철판|판넬', etcStrct, re.IGNORECASE)) > 0:
    #     otwlStrc = "철판 / 판넬"
    # elif len(re.findall(r'목조', etcStrct, re.IGNORECASE)) > 0:
    #     otwlStrc = "목조"
    # elif len(re.findall(r'유리', etcStrct, re.IGNORECASE)) > 0:
    #     otwlStrc = "유리벽"
    # else:
    #     otwlStrc = "콘크리트 외벽"  # etcStrct 값: 콘크리트, 철근, 시멘트, 시맨트, 기타

    # data['otwlStrc'] = otwlStrc


def judge_structure(data):
    if data is None:
        return data

    if data.get("strctCdNm") is None:
        etcStrct = data.get("etcStrct")
    else:
        etcStrct = data.get("strctCdNm")

    # if data["etcRoof"] is None:
    #     etcRoof = data["etcRoof"]
    # else:
    #     etcRoof = data["roof_strc"]

    # // 외벽 판단
    if len(re.findall(r'벽돌|조적', etcStrct, re.IGNORECASE)) > 0:
        otwlStrc = "벽돌(조직) 외벽"
    elif len(re.findall(r'블록|블럭', etcStrct, re.IGNORECASE)) > 0:
        otwlStrc = "블록 외벽"
    elif len(re.findall(r'철판|판넬', etcStrct, re.IGNORECASE)) > 0:
        otwlStrc = "철판 / 판넬"
    elif len(re.findall(r'목조', etcStrct, re.IGNORECASE)) > 0:
        otwlStrc = "목조"
    elif len(re.findall(r'유리', etcStrct, re.IGNORECASE)) > 0:
        otwlStrc = "유리벽"
    else:
        otwlStrc = "콘크리트 외벽"  # etcStrct 값: 콘크리트, 철근, 시멘트, 시맨트, 기타

    data['otwlStrc'] = otwlStrc

    return data
    # # // 기둥 판단
    # if len(re.findall(r'벽돌|조적', etcStrct, re.IGNORECASE)) > 0:
    #     poleStrc = "벽돌조"
    # elif len(re.findall(r'블록|블럭', etcStrct, re.IGNORECASE)) > 0:
    #     poleStrc = "블럭조"
    # elif len(re.findall(r'경량철골|철골|H빔|에이치빔', etcStrct, re.IGNORECASE)) > 0:
    #     poleStrc = "철골"
    # elif len(re.findall(r'목조', etcStrct, re.IGNORECASE)) > 0:
    #     poleStrc = "목조"
    # elif len(re.findall(r'철파이프', etcStrct, re.IGNORECASE)) > 0:
    #     poleStrc = "철파이프조"
    # else:
    #     poleStrc = "콘크리트조"  # etcStrct 값: 콘크리트, 철근, 시멘트, 시맨트, 기타
    #
    # data['poleStrc'] = poleStrc
    #
    # # 지붕 판단
    # if len(re.findall(r'철판|판넬', etcRoof, re.IGNORECASE)) > 0:
    #     roofStrc = "판넬 지붕"
    # elif len(re.findall(r'연와|기와', etcRoof, re.IGNORECASE)) > 0:
    #     roofStrc = "목조"
    # elif len(re.findall(r'철골', etcRoof, re.IGNORECASE)) > 0:
    #     roofStrc = "철골지붕틀 위 슬레이트"
    # elif len(re.findall(r'목조', etcRoof, re.IGNORECASE)) > 0:
    #     roofStrc = "목조지붕틀 위 슬레이트"
    # else:
    #     roofStrc = "콘크리트 지붕"  # // etcRoof 값: 콘크리트, 철근, 슬래브, 슬라브, 기타
    #
    # data['roofStrc'] = roofStrc


def process():
    check_and_create()
    data_copy_for_batch()
    ApiConnectAddress()
    restore_to_origin()


if __name__ == '__main__':
    process()
