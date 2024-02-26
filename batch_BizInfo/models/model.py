from sqlalchemy import BigInteger, CHAR, Column, DECIMAL, Date, DateTime, Double, ForeignKeyConstraint, Index, Integer, LargeBinary, MetaData, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import CHAR, DATETIME, INTEGER, TINYINT, VARCHAR
from sqlalchemy.orm.base import Mapped

metadata = MetaData()


t_BATCH_JOB_EXECUTION_SEQ = Table(
    'BATCH_JOB_EXECUTION_SEQ', metadata,
    Column('ID', BigInteger, nullable=False),
    Column('UNIQUE_KEY', CHAR(1), nullable=False),
    Index('UNIQUE_KEY_UN', 'UNIQUE_KEY', unique=True)
)

t_BATCH_JOB_INSTANCE = Table(
    'BATCH_JOB_INSTANCE', metadata,
    Column('JOB_INSTANCE_ID', BigInteger, primary_key=True),
    Column('VERSION', BigInteger),
    Column('JOB_NAME', String(100), nullable=False),
    Column('JOB_KEY', String(32), nullable=False),
    Index('JOB_INST_UN', 'JOB_NAME', 'JOB_KEY', unique=True)
)

t_BATCH_JOB_SEQ = Table(
    'BATCH_JOB_SEQ', metadata,
    Column('ID', BigInteger, nullable=False),
    Column('UNIQUE_KEY', CHAR(1), nullable=False),
    Index('UNIQUE_KEY_UN', 'UNIQUE_KEY', unique=True)
)

t_BATCH_STEP_EXECUTION_SEQ = Table(
    'BATCH_STEP_EXECUTION_SEQ', metadata,
    Column('ID', BigInteger, nullable=False),
    Column('UNIQUE_KEY', CHAR(1), nullable=False),
    Index('UNIQUE_KEY_UN', 'UNIQUE_KEY', unique=True)
)

t_DB_OTWL_DVCD = Table(
    'DB_OTWL_DVCD', metadata,
    Column('CODE', String(2, 'utf8mb4_general_ci')),
    Column('NAME', String(50, 'utf8mb4_general_ci')),
    Column('ID', INTEGER, primary_key=True),
    comment='DB Code Outwall'
)

t_DB_PLE_DVCD = Table(
    'DB_PLE_DVCD', metadata,
    Column('CODE', String(2, 'utf8mb4_general_ci')),
    Column('NAME', String(50, 'utf8mb4_general_ci')),
    Column('ID', INTEGER, primary_key=True),
    comment='DB Code Poll'
)

t_DB_ROF_DVCD = Table(
    'DB_ROF_DVCD', metadata,
    Column('CODE', String(2, 'utf8mb4_general_ci')),
    Column('NAME', String(50, 'utf8mb4_general_ci')),
    Column('ID', INTEGER, primary_key=True),
    comment='DB Code Roof'
)

t_IN011TR = Table(
    'IN011TR', metadata,
    Column('QUOTE_NO', VARCHAR(191), primary_key=True),
    Column('INS_DATE', DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP')),
    Column('TERMSA_1', VARCHAR(191)),
    Column('TERMSA_2', VARCHAR(191)),
    Column('TERMSA_3', VARCHAR(191)),
    Column('TERMSA_4', VARCHAR(191)),
    Column('TERMSA_5', VARCHAR(191)),
    Column('TERMSA_6', VARCHAR(191)),
    Column('TERMSA_7', VARCHAR(191)),
    Column('TERMSA_8', VARCHAR(191)),
    Column('TERMSB_1', VARCHAR(191)),
    Column('TERMSB_2', VARCHAR(191)),
    Column('TERMSB_3', VARCHAR(191)),
    Column('TERMSC_1', VARCHAR(191)),
    Column('TERMSC_2', VARCHAR(191)),
    Column('TERMSC_3', VARCHAR(191)),
    Column('TERMSC_4', VARCHAR(191)),
    Column('TERMSC_5', VARCHAR(191)),
    Column('TERMSD_1', VARCHAR(191)),
    Column('TERMSD_2', VARCHAR(191)),
    Column('TERMSD_3', VARCHAR(191)),
    Column('TERMSE_1', VARCHAR(191)),
    Column('TERMSE_2', VARCHAR(191)),
    Column('TERMSE_3', VARCHAR(191)),
    Column('TERMSF_1', VARCHAR(191)),
    Column('TERMSG_1', VARCHAR(191))
)

t_IN101CR = Table(
    'IN101CR', metadata,
    Column('IDX', Integer, primary_key=True),
    Column('CODE', VARCHAR(191), nullable=False),
    Column('NAME', VARCHAR(191), nullable=False)
)

t_IN101TR = Table(
    'IN101TR', metadata,
    Column('QUOTE_NO', Integer, primary_key=True),
    Column('USER_ID', VARCHAR(191)),
    Column('INR_BIRTH', VARCHAR(191), nullable=False),
    Column('INR_GENDER', VARCHAR(191), nullable=False),
    Column('EMAIL', VARCHAR(191)),
    Column('AGMTKIND', VARCHAR(191)),
    Column('BLDTOTLYRNUM', VARCHAR(191)),
    Column('HSAREA', VARCHAR(191)),
    Column('LSGCCD', VARCHAR(191)),
    Column('POLESTRC', VARCHAR(191)),
    Column('ROOFSTRC', VARCHAR(191)),
    Column('OTWLSTRC', VARCHAR(191)),
    Column('OBJCAT', VARCHAR(191)),
    Column('BLDFLOORS1', VARCHAR(191)),
    Column('BLDFLOORS2', VARCHAR(191)),
    Column('LOBZCD', VARCHAR(191)),
    Column('GITDTARIFCAT1', VARCHAR(191)),
    Column('OBJTYPCD1', VARCHAR(191)),
    Column('OBJTYPCD2', VARCHAR(191)),
    Column('OBJTYPCD3', VARCHAR(191)),
    Column('ELAGORGNINSDAMT1', VARCHAR(191)),
    Column('ELAGORGNINSDAMT2', VARCHAR(191)),
    Column('ELAGORGNINSDAMT3', VARCHAR(191)),
    Column('PTYKORNM', VARCHAR(191)),
    Column('TELCAT', VARCHAR(191)),
    Column('TELNO', VARCHAR(191)),
    Column('PTYBIZNM', VARCHAR(191)),
    Column('BIZNO', VARCHAR(191)),
    Column('OBJONNADDRCAT', VARCHAR(191)),
    Column('OBJZIP', VARCHAR(191)),
    Column('OBJADDR1', VARCHAR(191)),
    Column('OBJADDR2', VARCHAR(191)),
    Column('OBJROADNMCD', VARCHAR(191)),
    Column('OBJTRBDCD', VARCHAR(191)),
    Column('OBJTRBDADDR', VARCHAR(191)),
    Column('PARTNERNO', VARCHAR(191)),
    Column('TPYMPREM', VARCHAR(191)),
    Column('PERPREM', VARCHAR(191)),
    Column('GOVTPREM', VARCHAR(191)),
    Column('LGOVTPREM', VARCHAR(191)),
    Column('APPLNO', VARCHAR(191)),
    Column('SCNO', VARCHAR(191)),
    Column('INSERT_DATE', DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP')),
    Column('PURPOSE', VARCHAR(191)),
    Column('LOCALURLTMP', VARCHAR(191)),
    Column('MAPPINGNO', VARCHAR(191)),
    Column('INSSTDT', VARCHAR(191)),
    Column('INSEDDT', VARCHAR(191)),
    Column('INSSTTM', VARCHAR(191)),
    Column('INSEDTM', VARCHAR(191)),
    Column('PRDINS', VARCHAR(191)),
    Column('SESSIONEXECTIME', VARCHAR(191)),
    Column('SESSIONID', VARCHAR(191)),
    Column('CERTCONFMSEQNO', VARCHAR(191)),
    Column('ESIGNURL', VARCHAR(191)),
    Column('GIID0410VO_JSON', VARCHAR(191))
)

t_IN103CR = Table(
    'IN103CR', metadata,
    Column('CODE', VARCHAR(191), primary_key=True),
    Column('OBJ_TYPE', VARCHAR(191), nullable=False),
    Column('NAME', VARCHAR(191), nullable=False),
    Column('SEQ', Integer, nullable=False)
)

t_stm_fld = Table(
    'stm_fld', metadata,
    Column('id', Integer, primary_key=True),
    Column('biz_name', String(100), comment='상호명'),
    Column('ceo_name', String(100), comment='대표자'),
    Column('biz_type', String(100), comment='영위업종'),
    Column('building_division', CHAR(2), comment='건물구분'),
    Column('address', String(100), comment='주소'),
    Column('detail_address', String(100), comment='상세주소'),
    Column('area', String(100), comment='실사용면적'),
    Column('biz_site_lease', String(100), comment='사업장임차여부'),
    Column('ugrnd_flr_cnt', String(100), comment='지하층수'),
    Column('bld_tot_lyr_num', String(100), comment='건물전체층수(끝층)'),
    Column('input_bld_st', String(100), comment='가입층수(시작층)'),
    Column('input_bld_ed', String(100), comment='가입층수(끝층)'),
    Column('strct_cd_nm', String(100), comment='철근콘크리트구조'),
    Column('roof_strc', String(100), comment='지붕구조'),
    Column('otwl_strc', String(100), comment='외벽구조'),
    Column('worker_num_standard_under_yn', CHAR(2), comment='상시 근로자수 기준 미만 여부'),
    Column('worker_num', String(100), comment='상시 근로자수'),
    Column('sales_standard_under_yn', CHAR(2), comment='매출액 기준 미만 여부'),
    Column('sales', String(100), comment='매출액(백만원)'),
    Column('biz_no', String(100), comment='사업자번호'),
    Column('termsA1', CHAR(2), comment='소비자권익에 관한사항'),
    Column('termsA2', CHAR(2), comment='단체규약'),
    Column('termsA3', CHAR(2), comment='민감정보 및 고유식별정보의 처리에 관한 사항'),
    Column('termsA4', CHAR(2), comment='개인(신용)정보의 사전 수집.이용에 관한 사항'),
    Column('termsA6', CHAR(2), comment='개인(신용)정보의 조회에 관한 사항'),
    Column('termsA7', CHAR(2), comment='개인(신용)정보의 제공에 관한 사항'),
    Column('imputation_reason_confirm_yn', CHAR(2), comment='귀책 사유 확인'),
    Column('create_date', String(100), comment='생성일자'),
    Column('termsA8', CHAR(2), comment='마케팅이용 동의에 관한사항(선택)'),
    Column('difStmFldJoinYn', CHAR(2), comment='타 풍수해보험 가입 여부'),
    Column('phoneNum', String(100), comment='휴대폰 번호'),
    Column('birthDate', String(100), comment='생년월일'),
    Column('sex', CHAR(2), comment='성별'),
    Column('jehuCd', String(100), comment='제휴처'),
    Column('roadAddr', String(100)),
    Column('bunjiAddr', String(100)),
    Column('zipCode', String(100)),
    Column('squareMeter', DECIMAL(10, 2)),
    Column('capitalDo', String(100)),
    Column('si', String(100)),
    Column('etcStrct', String(100)),
    Column('etcRoof', String(100)),
    Column('grade', String(10)),
)

t_stm_fld_batch = Table(
    'stm_fld_batch', metadata,
    Column('id', Integer, primary_key=True),
    Column('biz_name', String(100), comment=' 상호명'),
    Column('ceo_name', String(100), comment=' 대표자'),
    Column('biz_type', String(100), comment=' 영위업종'),
    Column('building_division', CHAR(2), comment=' 건물구분'),
    Column('address', String(100), comment=' 주소'),
    Column('detail_address', String(100), comment=' 상세주소'),
    Column('area', String(100), comment=' 실사용면적'),
    Column('biz_site_lease', String(100), comment=' 사업장임차여부'),
    Column('ugrnd_flr_cnt', String(100), comment=' 지하층수'),
    Column('bld_tot_lyr_num', String(100), comment=' 건물전체층수(끝층)'),
    Column('input_bld_st', String(100), comment=' 가입층수(시작층)'),
    Column('input_bld_ed', String(100), comment=' 가입층수(끝층)'),
    Column('strct_cd_nm', String(100), comment=' 철근콘크리트구조'),
    Column('roof_strc', String(100), comment=' 지붕구조'),
    Column('otwl_strc', String(100), comment=' 외벽구조'),
    Column('worker_num_standard_under_yn', CHAR(2), comment=' 상시 근로자수 기준 미만 여부'),
    Column('worker_num', String(100), comment=' 상시 근로자수'),
    Column('sales_standard_under_yn', CHAR(2), comment=' 매출액 기준 미만 여부'),
    Column('sales', String(100), comment=' 매출액(백만원)'),
    Column('biz_no', String(100), comment=' 사업자번호'),
    Column('termsA1', CHAR(2), comment=' 소비자권익에 관한사항'),
    Column('termsA2', CHAR(2), comment=' 단체규약'),
    Column('termsA3', CHAR(2), comment=' 민감정보 및 고유식별정보의 처리에 관한 사항'),
    Column('termsA4', CHAR(2), comment=' 개인(신용)정보의 사전 수집.이용에 관한 사항'),
    Column('termsA6', CHAR(2), comment=' 개인(신용)정보의 조회에 관한 사항'),
    Column('termsA7', CHAR(2), comment=' 개인(신용)정보의 제공에 관한 사항'),
    Column('imputation_reason_confirm_yn', CHAR(2), comment=' 귀책 사유 확인'),
    Column('create_date', String(100), comment=' 생성일자'),
    Column('termsA8', CHAR(2), comment=' 마케팅이용 동의에 관한사항(선택)'),
    Column('difStmFldJoinYn', CHAR(2)),
    Column('phoneNum', String(100)),
    Column('birthDate', String(100)),
    Column('sex', CHAR(2)),
    Column('jehuCd', String(100)),
    Column('roadAddr', String(100)),
    Column('bunjiAddr', String(100)),
    Column('zipCode', String(100)),
    Column('squareMeter', DECIMAL(10, 2)),
    Column('capitalDo', String(100)),
    Column('si', String(100)),
    Column('etcStrct', String(100)),
    Column('etcRoof', String(100)),
    Column('grade', String(10)),
    # Column('db_code_roof', String(100)),
    # Column('db_code_wall', String(100)),
    # Column('db_code_poll', String(100)),
    # Column('db_code_biztype', String(100)),
    Column('data_processed', TINYINT(1), server_default=text("'0'")),
    Column('db_processed', TINYINT(1), server_default=text("'0'")),
    Column('data_skip', TINYINT(1), server_default=text("'0'"))
)

t_tb_agreement = Table(
    'tb_agreement', metadata,
    Column('id', BigInteger, primary_key=True, comment='시퀀스'),
    Column('agreement_title', String(100), comment='약관동의 제목'),
    Column('agreement_content', String(4000), comment='약관동의 내용'),
    Column('important_yn', CHAR(1), comment='약관동의 필수 여부'),
    Column('created_date', DateTime, comment='약관동의 작성 일자'),
    Column('created_by', String(20), comment='약관동의 작성자'),
    Column('updated_date', DateTime, comment='약관동의 수정 일자'),
    Column('updated_by', String(20), comment='약관동의 수정자'),
    Column('delete_yn', CHAR(1), server_default=text("'N'"), comment='약관동의 삭제 여부')
)

t_tb_auth_log = Table(
    'tb_auth_log', metadata,
    Column('id', BigInteger, primary_key=True, comment='시퀀스'),
    Column('user_id', String(50), comment='대상자 식별정보'),
    Column('auth_content', String(200), comment='접근 권한에 관한 정보'),
    Column('auth_type', String(20), comment='유형(부여/변경/말소)'),
    Column('reason', String(100), comment='변경 사유(신규입사, 조직변경,퇴사 등)'),
    Column('approver', String(50), comment='승인자'),
    Column('approver_date', DateTime, comment='승인일시')
)

t_tb_community = Table(
    'tb_community', metadata,
    Column('id', BigInteger, primary_key=True),
    Column('category', String(20), nullable=False),
    Column('code', String(20)),
    Column('title', String(100), nullable=False),
    Column('content', String(1000), nullable=False),
    Column('created_date', DateTime),
    Column('updated_date', DateTime),
    Column('created_by', String(20)),
    Column('updated_by', String(20)),
    Column('delete_yn', CHAR(1)),
    comment='커뮤니티 테이블'
)

t_tb_consulting = Table(
    'tb_consulting', metadata,
    Column('id', BigInteger, primary_key=True, comment='시퀀스'),
    Column('name', String(10), comment='신청자 이름'),
    Column('phone_role', String(11), comment='신청자 전화번호'),
    Column('business', String(40), comment='업종'),
    Column('consulting_yn', CHAR(1), server_default=text("'N'"), comment='상담 여부'),
    Column('consulting_success_date', DateTime, comment='상담 완료 일자'),
    Column('created_date', DateTime, comment='상담 등록 일자'),
    Column('created_by', String(20), comment='등록자'),
    Column('updated_date', DateTime, comment='수정 일자'),
    Column('updated_by', String(20), comment='수정자'),
    Column('delete_yn', CHAR(1), server_default=text("'N'"), comment='삭제 여부')
)

t_tb_domestic_tour = Table(
    'tb_domestic_tour', metadata,
    Column('id', BigInteger, primary_key=True),
    Column('user_id', BigInteger),
    Column('user_name', String(100)),
    Column('jumin_front', String(6)),
    Column('jumin_back', String(7)),
    Column('phone_num', String(11)),
    Column('email', String(100)),
    Column('age', String(10), comment='나이'),
    Column('sex', CHAR(1), comment='성별'),
    Column('period', String(10), comment='여행기간'),
    Column('gubun', String(1), comment='1든든,3안심'),
    Column('start_date', DateTime, comment='여행시작일'),
    Column('end_date', DateTime, comment='여행마감일'),
    Column('diseases_three_years_agreement', String(1)),
    Column('danger_leisure_sports_agreement', String(1)),
    Column('privacy_info_agreement', String(1), server_default=text("'Y'")),
    Column('foreigner_yn', String(1)),
    Column('before_payment', String(1)),
    Column('travel_purpose', String(100)),
    Column('third_parties_agreement', String(1), server_default=text("'Y'")),
    Column('marketing_agreement', String(1), server_default=text("'N'")),
    Column('delete_yn', String(1), server_default=text("'N'")),
    Column('fee', Integer),
    Column('created_date', DateTime),
    Column('created_by', VARCHAR(20)),
    Column('updated_date', DateTime),
    Column('updated_by', VARCHAR(20))
)

t_tb_infoplace = Table(
    'tb_infoplace', metadata,
    Column('id', BigInteger, primary_key=True, comment='번호'),
    Column('title', String(100)),
    Column('content', LargeBinary),
    Column('created_date', DateTime),
    Column('created_by', String(20)),
    Column('updated_date', DateTime),
    Column('updated_by', String(20)),
    Column('delete_yn', CHAR(1), server_default=text("'Y'"), comment='삭제 여부')
)

t_tb_insu_agent = Table(
    'tb_insu_agent', metadata,
    Column('id', BigInteger, primary_key=True, comment='시퀀스'),
    Column('company_name', String(50), comment='회사명'),
    Column('insu_id', String(50), comment='설계사id'),
    Column('insu_name', String(10), comment='설계사명'),
    Column('regdate', DateTime, comment='등록일'),
    Column('delete_yn', CHAR(1), server_default=text("'N'"))
)

t_tb_insu_status = Table(
    'tb_insu_status', metadata,
    Column('ID', BigInteger, primary_key=True, comment='시퀀스'),
    Column('POLHOLDER', String(50), comment='이름'),
    Column('REGI_BIRTH_FRONT', String(50)),
    Column('REGI_BIRTH_BACK', String(50)),
    Column('MOBILE', String(50)),
    Column('ADDRESS', String(100)),
    Column('DETAIL_ADDR', String(100)),
    Column('BUSINESS_TYPE', String(50)),
    Column('BUSINESS_NUMBER', String(50)),
    Column('BUSINESS_NAME', String(50)),
    Column('BUSINESS_OWNER', String(30)),
    Column('AREA', String(50)),
    Column('FLOOR_LOW', String(30)),
    Column('FLOOR_HIGH', String(30)),
    Column('REGDATE', DateTime),
    Column('FLAG', String(100)),
    Column('PER_PREM', Integer),
    Column('GOVT_PREM', Integer),
    Column('LGOVT_PREM', Integer),
    Column('TPYM_PREM', Integer),
    Column('FAIL_REASON', String(200)),
    Column('BUSINESS_CODE', String(50)),
    Column('BUSINESS_OBJCAT', String(30)),
    Column('REQUIRED1', String(10)),
    Column('REQUIRED2', String(10)),
    Column('REQUIRED3', String(10)),
    Column('MARKETING_OPTIONS', String(10)),
    Column('SAME_BSNUM', CHAR(1)),
    Index('BUSINESS_NUMBER', 'BUSINESS_NUMBER', unique=True)
)

t_tb_insu_status_temp = Table(
    'tb_insu_status_temp', metadata,
    Column('ID', BigInteger, primary_key=True, comment='시퀀스'),
    Column('POLHOLDER', String(50), comment='이름'),
    Column('REGI_BIRTH_FRONT', String(50)),
    Column('REGI_BIRTH_BACK', String(50)),
    Column('MOBILE', String(50)),
    Column('ADDRESS', String(100)),
    Column('DETAIL_ADDR', String(100)),
    Column('BUSINESS_TYPE', String(50)),
    Column('BUSINESS_NUMBER', String(50)),
    Column('BUSINESS_NAME', String(50)),
    Column('BUSINESS_OWNER', String(30)),
    Column('AREA', String(50)),
    Column('FLOOR_LOW', String(30)),
    Column('FLOOR_HIGH', String(30)),
    Column('REGDATE', DateTime),
    Column('FLAG', String(100)),
    Column('PER_PREM', Integer),
    Column('GOVT_PREM', Integer),
    Column('LGOVT_PREM', Integer),
    Column('TPYM_PREM', Integer),
    Column('FAIL_REASON', String(200)),
    Column('BUSINESS_CODE', String(50)),
    Column('BUSINESS_OBJCAT', String(30)),
    Column('REQUIRED1', String(10)),
    Column('REQUIRED2', String(10)),
    Column('REQUIRED3', String(10)),
    Column('MARKETING_OPTIONS', String(10)),
    Column('SAME_BSNUM', CHAR(1)),
    Index('BUSINESS_NUMBER', 'BUSINESS_NUMBER', unique=True)
)

t_tb_join_log = Table(
    'tb_join_log', metadata,
    Column('id', BigInteger, primary_key=True),
    Column('user_id', String(100), nullable=False),
    Column('join_date', DateTime),
    Column('logout_date', DateTime),
    Column('processing_user', String(20)),
    Column('task', String(20), nullable=False),
    Column('join_ip', String(20), nullable=False)
)

t_tb_manager = Table(
    'tb_manager', metadata,
    Column('id', Integer, primary_key=True, comment='번호'),
    Column('user_id', String(20), nullable=False, comment='관리자 아이디'),
    Column('user_pw', String(100)),
    Column('phone_role', String(11)),
    Column('has_role', String(20)),
    Column('created_date', DateTime),
    Column('created_by', String(20)),
    Column('updated_date', DateTime),
    Column('updated_by', String(20)),
    Column('error_count', Integer, server_default=text("'0'")),
    Column('delete_yn', CHAR(1), server_default=text("'N'"), comment='삭제 여부'),
    comment='admin페이지 관리자 테이블'
)

t_tb_mydata_insurance = Table(
    'tb_mydata_insurance', metadata,
    Column('id', BigInteger, primary_key=True),
    Column('user_name', String(100)),
    Column('mydata_insurance_product', String(20)),
    Column('mydata_insurance_title', String(50)),
    Column('mydata_insurance_content', LargeBinary),
    Column('keyword', String(100)),
    Column('delete_yn', String(1), server_default=text("'N'")),
    Column('created_date', DateTime),
    Column('created_by', String(20)),
    Column('updated_date', DateTime),
    Column('updated_by', String(20)),
    comment='마이데이터 보험 상품'
)

t_tb_mydata_user = Table(
    'tb_mydata_user', metadata,
    Column('id', BigInteger, primary_key=True),
    Column('user_name', String(100)),
    Column('user_email', String(100), comment='유저 이메일'),
    Column('phone_agency', String(100), comment='통신사'),
    Column('phone_role', String(11), comment='핸드폰번호'),
    Column('resident_number_front', String(100), comment='주민앞번호'),
    Column('resident_number_back', String(100), comment='주민뒷번호'),
    Column('company_name', String(100), comment='소속회사'),
    Column('housing_type', String(10), comment='주거형태'),
    Column('housing_division', String(10), comment='주거구분'),
    Column('business_income', String(30), comment='사업소득여부'),
    Column('car_owner', String(30), comment='자동차보유 여부'),
    Column('car_name', String(100), comment='차종이름'),
    Column('motorcycle', String(30)),
    Column('height', String(100)),
    Column('weight', String(100)),
    Column('disease', String(30)),
    Column('disease_name', String(100)),
    Column('blood_type', String(30)),
    Column('physical_disability', String(30)),
    Column('physical_disability_level', String(100)),
    Column('marriage', String(30)),
    Column('children', String(10)),
    Column('preschool_child', String(10)),
    Column('elderly_family', String(100)),
    Column('privacy_agreement', String(1), server_default=text("'Y'")),
    Column('third_parties_agreement', String(1), server_default=text("'Y'")),
    Column('marketing_agreement', String(1), server_default=text("'N'")),
    Column('created_date', DateTime),
    Column('delete_yn', String(1), server_default=text("'N'")),
    Column('created_by', VARCHAR(20)),
    Column('updated_date', DateTime),
    Column('updated_by', VARCHAR(20))
)

t_tb_notice = Table(
    'tb_notice', metadata,
    Column('id', Integer, primary_key=True, comment='번호'),
    Column('policy', String(100)),
    Column('title', String(100)),
    Column('content', LargeBinary),
    Column('created_date', DateTime),
    Column('created_by', String(20)),
    Column('updated_date', DateTime),
    Column('updated_by', String(20)),
    Column('delete_yn', CHAR(1), server_default=text("'N'"), comment='삭제 여부')
)

t_tb_payment_status = Table(
    'tb_payment_status', metadata,
    Column('id', Integer, primary_key=True),
    Column('dt_id', BigInteger, comment='tb_domestic_tour table join FK'),
    Column('merchant_uid', String(50), nullable=False, comment='가맹점 주문번호'),
    Column('amount', Integer, nullable=False, comment='결제 금액'),
    Column('completion_yn', CHAR(1), comment='결제 완료 유무'),
    Column('completion_date', Date, comment='결제 완료 시간'),
    Column('failure_date', Date, comment='결제 실패 시간')
)

t_tb_sms = Table(
    'tb_sms', metadata,
    Column('id', BigInteger, primary_key=True, comment='번호'),
    Column('group_id', String(100), comment='메세지 그룹 id'),
    Column('message_id', String(100), comment='메세지 id'),
    Column('account_id', String(50), comment='계정 id'),
    Column('auth_key', String(20)),
    Column('auth_yn', CHAR(1), server_default=text("'N'")),
    Column('status_code', String(10), comment='응답코드'),
    Column('status_message', String(100), comment='응답메세지'),
    Column('message_type', String(20), comment='메세지종류'),
    Column('country', String(10), comment='국가번호'),
    Column('message_to', String(15), comment='받는사람'),
    Column('message_from', String(15), comment='보낸사람'),
    Column('send_date', DateTime, comment='보낸 일자')
)

t_tb_trip_bojang = Table(
    'tb_trip_bojang', metadata,
    Column('id', BigInteger, primary_key=True),
    Column('b_code', Integer),
    Column('b_name', String(100)),
    Column('b_money', Integer),
    Column('b_self_money', Integer),
    Column('b_flag', CHAR(1), comment='1:알뜰 2:기본 3:고급'),
    Column('b_due_date', TIMESTAMP),
    Column('b_order', Integer),
    Column('category', Integer),
    Column('display_name', String(100))
)

t_tb_trip_fee = Table(
    'tb_trip_fee', metadata,
    Column('id', BigInteger, primary_key=True),
    Column('sex', CHAR(1), nullable=False),
    Column('age', CHAR(2), nullable=False),
    Column('period', CHAR(2), nullable=False),
    Column('ratio', Double(asdecimal=True), nullable=False),
    Column('fee', Integer, nullable=False),
    Column('due_date', DateTime),
    Column('gubun', CHAR(1), nullable=False, comment='1:알뜰 2: 기본 3:고급')
)

t_tb_user = Table(
    'tb_user', metadata,
    Column('id', BigInteger, primary_key=True, comment='번호'),
    Column('user_id', String(50), nullable=False, comment='관리자 아이디'),
    Column('agent_id', BigInteger),
    Column('user_pw', String(100)),
    Column('user_name', String(10), nullable=False),
    Column('phone_role', String(11)),
    Column('address', String(100)),
    Column('address_detail', String(100)),
    Column('login_type', String(20)),
    Column('created_date', DateTime),
    Column('created_by', String(20)),
    Column('updated_date', DateTime),
    Column('updated_by', String(20)),
    Column('marketing_yn', String(10)),
    Column('delete_yn', CHAR(1), server_default=text("'N'"), comment='삭제 여부'),
    comment='사용자 테이블'
)

t_BATCH_JOB_EXECUTION = Table(
    'BATCH_JOB_EXECUTION', metadata,
    Column('JOB_EXECUTION_ID', BigInteger, primary_key=True),
    Column('VERSION', BigInteger),
    Column('JOB_INSTANCE_ID', BigInteger, nullable=False),
    Column('CREATE_TIME', DATETIME(fsp=6), nullable=False),
    Column('START_TIME', DATETIME(fsp=6)),
    Column('END_TIME', DATETIME(fsp=6)),
    Column('STATUS', String(10)),
    Column('EXIT_CODE', String(2500)),
    Column('EXIT_MESSAGE', String(2500)),
    Column('LAST_UPDATED', DATETIME(fsp=6)),
    Column('JOB_CONFIGURATION_LOCATION', String(2500)),
    ForeignKeyConstraint(['JOB_INSTANCE_ID'], ['BATCH_JOB_INSTANCE.JOB_INSTANCE_ID'], name='JOB_INST_EXEC_FK'),
    Index('JOB_INST_EXEC_FK', 'JOB_INSTANCE_ID')
)

t_BATCH_JOB_EXECUTION_CONTEXT = Table(
    'BATCH_JOB_EXECUTION_CONTEXT', metadata,
    Column('JOB_EXECUTION_ID', BigInteger, primary_key=True),
    Column('SHORT_CONTEXT', String(2500), nullable=False),
    Column('SERIALIZED_CONTEXT', Text),
    ForeignKeyConstraint(['JOB_EXECUTION_ID'], ['BATCH_JOB_EXECUTION.JOB_EXECUTION_ID'], name='JOB_EXEC_CTX_FK')
)

t_BATCH_JOB_EXECUTION_PARAMS = Table(
    'BATCH_JOB_EXECUTION_PARAMS', metadata,
    Column('JOB_EXECUTION_ID', BigInteger, nullable=False),
    Column('TYPE_CD', String(6), nullable=False),
    Column('KEY_NAME', String(100), nullable=False),
    Column('STRING_VAL', String(250)),
    Column('DATE_VAL', DATETIME(fsp=6)),
    Column('LONG_VAL', BigInteger),
    Column('DOUBLE_VAL', Double(asdecimal=True)),
    Column('IDENTIFYING', CHAR(1), nullable=False),
    ForeignKeyConstraint(['JOB_EXECUTION_ID'], ['BATCH_JOB_EXECUTION.JOB_EXECUTION_ID'], name='JOB_EXEC_PARAMS_FK'),
    Index('JOB_EXEC_PARAMS_FK', 'JOB_EXECUTION_ID')
)

t_BATCH_STEP_EXECUTION = Table(
    'BATCH_STEP_EXECUTION', metadata,
    Column('STEP_EXECUTION_ID', BigInteger, primary_key=True),
    Column('VERSION', BigInteger, nullable=False),
    Column('STEP_NAME', String(100), nullable=False),
    Column('JOB_EXECUTION_ID', BigInteger, nullable=False),
    Column('START_TIME', DATETIME(fsp=6), nullable=False),
    Column('END_TIME', DATETIME(fsp=6)),
    Column('STATUS', String(10)),
    Column('COMMIT_COUNT', BigInteger),
    Column('READ_COUNT', BigInteger),
    Column('FILTER_COUNT', BigInteger),
    Column('WRITE_COUNT', BigInteger),
    Column('READ_SKIP_COUNT', BigInteger),
    Column('WRITE_SKIP_COUNT', BigInteger),
    Column('PROCESS_SKIP_COUNT', BigInteger),
    Column('ROLLBACK_COUNT', BigInteger),
    Column('EXIT_CODE', String(2500)),
    Column('EXIT_MESSAGE', String(2500)),
    Column('LAST_UPDATED', DATETIME(fsp=6)),
    ForeignKeyConstraint(['JOB_EXECUTION_ID'], ['BATCH_JOB_EXECUTION.JOB_EXECUTION_ID'], name='JOB_EXEC_STEP_FK'),
    Index('JOB_EXEC_STEP_FK', 'JOB_EXECUTION_ID')
)

t_BATCH_STEP_EXECUTION_CONTEXT = Table(
    'BATCH_STEP_EXECUTION_CONTEXT', metadata,
    Column('STEP_EXECUTION_ID', BigInteger, primary_key=True),
    Column('SHORT_CONTEXT', String(2500), nullable=False),
    Column('SERIALIZED_CONTEXT', Text),
    ForeignKeyConstraint(['STEP_EXECUTION_ID'], ['BATCH_STEP_EXECUTION.STEP_EXECUTION_ID'], name='STEP_EXEC_CTX_FK')
)
