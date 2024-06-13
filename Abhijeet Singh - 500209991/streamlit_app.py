import streamlit as st
import requests
import pandas as pd

st.title("Churn Prediction")

# Define the input fields for the features
# Collect all the necessary input features
age = st.number_input("AGE", value=0)
amount_rub_atm_prc = st.number_input("AMOUNT_RUB_ATM_PRC", value=0.0)
amount_rub_clo_prc = st.number_input("AMOUNT_RUB_CLO_PRC", value=0.0)
amount_rub_nas_prc = st.number_input("AMOUNT_RUB_NAS_PRC", value=0.0)
amount_rub_sup_prc = st.number_input("AMOUNT_RUB_SUP_PRC", value=0.0)
clnt_setup_tenor = st.number_input("CLNT_SETUP_TENOR", value=0.0)
cnt_accepts_mtp = st.number_input("CNT_ACCEPTS_MTP", value=0)
cnt_accepts_tk = st.number_input("CNT_ACCEPTS_TK", value=0)
cnt_tran_atm_tendency1m = st.number_input("CNT_TRAN_ATM_TENDENCY1M", value=0)
cnt_tran_atm_tendency3m = st.number_input("CNT_TRAN_ATM_TENDENCY3M", value=0)
cnt_tran_sup_tendency1m = st.number_input("CNT_TRAN_SUP_TENDENCY1M", value=0)
cnt_tran_sup_tendency3m = st.number_input("CNT_TRAN_SUP_TENDENCY3M", value=0)
cr_prod_cnt_cc = st.number_input("CR_PROD_CNT_CC", value=0)
cr_prod_cnt_ccfp = st.number_input("CR_PROD_CNT_CCFP", value=0)
cr_prod_cnt_il = st.number_input("CR_PROD_CNT_IL", value=0)
cr_prod_cnt_pil = st.number_input("CR_PROD_CNT_PIL", value=0)
cr_prod_cnt_tovr = st.number_input("CR_PROD_CNT_TOVR", value=0)
cr_prod_cnt_vcu = st.number_input("CR_PROD_CNT_VCU", value=0)
ldeal_grace_days_pct_med = st.number_input("LDEAL_GRACE_DAYS_PCT_MED", value=0.0)
prc_accepts_a_amobile = st.number_input("PRC_ACCEPTS_A_AMOBILE", value=0.0)
prc_accepts_a_atm = st.number_input("PRC_ACCEPTS_A_ATM", value=0.0)
prc_accepts_a_email_link = st.number_input("PRC_ACCEPTS_A_EMAIL_LINK", value=0.0)
prc_accepts_a_mtp = st.number_input("PRC_ACCEPTS_A_MTP", value=0.0)
prc_accepts_a_pos = st.number_input("PRC_ACCEPTS_A_POS", value=0.0)
prc_accepts_a_tk = st.number_input("PRC_ACCEPTS_A_TK", value=0.0)
prc_accepts_mtp = st.number_input("PRC_ACCEPTS_MTP", value=0.0)
prc_accepts_tk = st.number_input("PRC_ACCEPTS_TK", value=0.0)
rest_avg_cur = st.number_input("REST_AVG_CUR", value=0.0)
rest_avg_paym = st.number_input("REST_AVG_PAYM", value=0.0)
rest_dynamic_cc_1m = st.number_input("REST_DYNAMIC_CC_1M", value=0.0)
rest_dynamic_cc_3m = st.number_input("REST_DYNAMIC_CC_3M", value=0.0)
rest_dynamic_cur_1m = st.number_input("REST_DYNAMIC_CUR_1M", value=0.0)
rest_dynamic_cur_3m = st.number_input("REST_DYNAMIC_CUR_3M", value=0.0)
rest_dynamic_fdep_1m = st.number_input("REST_DYNAMIC_FDEP_1M", value=0.0)
rest_dynamic_fdep_3m = st.number_input("REST_DYNAMIC_FDEP_3M", value=0.0)
rest_dynamic_il_1m = st.number_input("REST_DYNAMIC_IL_1M", value=0.0)
rest_dynamic_il_3m = st.number_input("REST_DYNAMIC_IL_3M", value=0.0)
rest_dynamic_paym_1m = st.number_input("REST_DYNAMIC_PAYM_1M", value=0.0)
rest_dynamic_paym_3m = st.number_input("REST_DYNAMIC_PAYM_3M", value=0.0)
rest_dynamic_save_3m = st.number_input("REST_DYNAMIC_SAVE_3M", value=0.0)
sum_tran_atm_tendency1m = st.number_input("SUM_TRAN_ATM_TENDENCY1M", value=0.0)
sum_tran_atm_tendency3m = st.number_input("SUM_TRAN_ATM_TENDENCY3M", value=0.0)
sum_tran_sup_tendency1m = st.number_input("SUM_TRAN_SUP_TENDENCY1M", value=0.0)
sum_tran_sup_tendency3m = st.number_input("SUM_TRAN_SUP_TENDENCY3M", value=0.0)
trans_amount_tendency3m = st.number_input("TRANS_AMOUNT_TENDENCY3M", value=0.0)
trans_cnt_tendency3m = st.number_input("TRANS_CNT_TENDENCY3M", value=0.0)
trans_count_atm_prc = st.number_input("TRANS_COUNT_ATM_PRC", value=0.0)
trans_count_nas_prc = st.number_input("TRANS_COUNT_NAS_PRC", value=0.0)
trans_count_sup_prc = st.number_input("TRANS_COUNT_SUP_PRC", value=0.0)
turnover_cc = st.number_input("TURNOVER_CC", value=0.0)
turnover_dynamic_cc_1m = st.number_input("TURNOVER_DYNAMIC_CC_1M", value=0.0)
turnover_dynamic_cc_3m = st.number_input("TURNOVER_DYNAMIC_CC_3M", value=0.0)
turnover_dynamic_cur_1m = st.number_input("TURNOVER_DYNAMIC_CUR_1M", value=0.0)
turnover_dynamic_cur_3m = st.number_input("TURNOVER_DYNAMIC_CUR_3M", value=0.0)
turnover_dynamic_il_1m = st.number_input("TURNOVER_DYNAMIC_IL_1M", value=0.0)
turnover_dynamic_il_3m = st.number_input("TURNOVER_DYNAMIC_IL_3M", value=0.0)
turnover_dynamic_paym_1m = st.number_input("TURNOVER_DYNAMIC_PAYM_1M", value=0.0)
turnover_dynamic_paym_3m = st.number_input("TURNOVER_DYNAMIC_PAYM_3M", value=0.0)
turnover_paym = st.number_input("TURNOVER_PAYM", value=0.0)
clnt_job_position = st.text_input("CLNT_JOB_POSITION", value="missing")
pack = st.text_input("PACK", value="missing")

# Create a dataframe from the input fields
input_data = pd.DataFrame({
    'AGE': [age],
    'AMOUNT_RUB_ATM_PRC': [amount_rub_atm_prc],
    'AMOUNT_RUB_CLO_PRC': [amount_rub_clo_prc],
    'AMOUNT_RUB_NAS_PRC': [amount_rub_nas_prc],
    'AMOUNT_RUB_SUP_PRC': [amount_rub_sup_prc],
    'CLNT_SETUP_TENOR': [clnt_setup_tenor],
    'CNT_ACCEPTS_MTP': [cnt_accepts_mtp],
    'CNT_ACCEPTS_TK': [cnt_accepts_tk],
    'CNT_TRAN_ATM_TENDENCY1M': [cnt_tran_atm_tendency1m],
    'CNT_TRAN_ATM_TENDENCY3M': [cnt_tran_atm_tendency3m],
    'CNT_TRAN_SUP_TENDENCY1M': [cnt_tran_sup_tendency1m],
    'CNT_TRAN_SUP_TENDENCY3M': [cnt_tran_sup_tendency3m],
    'CR_PROD_CNT_CC': [cr_prod_cnt_cc],
    'CR_PROD_CNT_CCFP': [cr_prod_cnt_ccfp],
    'CR_PROD_CNT_IL': [cr_prod_cnt_il],
    'CR_PROD_CNT_PIL': [cr_prod_cnt_pil],
    'CR_PROD_CNT_TOVR': [cr_prod_cnt_tovr],
    'CR_PROD_CNT_VCU': [cr_prod_cnt_vcu],
    'LDEAL_GRACE_DAYS_PCT_MED': [ldeal_grace_days_pct_med],
    'PRC_ACCEPTS_A_AMOBILE': [prc_accepts_a_amobile],
    'PRC_ACCEPTS_A_ATM': [prc_accepts_a_atm],
    'PRC_ACCEPTS_A_EMAIL_LINK': [prc_accepts_a_email_link],
    'PRC_ACCEPTS_A_MTP': [prc_accepts_a_mtp],
    'PRC_ACCEPTS_A_POS': [prc_accepts_a_pos],
    'PRC_ACCEPTS_A_TK': [prc_accepts_a_tk],
    'PRC_ACCEPTS_MTP': [prc_accepts_mtp],
    'PRC_ACCEPTS_TK': [prc_accepts_tk],
    'REST_AVG_CUR': [rest_avg_cur],
    'REST_AVG_PAYM': [rest_avg_paym],
    'REST_DYNAMIC_CC_1M': [rest_dynamic_cc_1m],
    'REST_DYNAMIC_CC_3M': [rest_dynamic_cc_3m],
    'REST_DYNAMIC_CUR_1M': [rest_dynamic_cur_1m],
    'REST_DYNAMIC_CUR_3M': [rest_dynamic_cur_3m],
    'REST_DYNAMIC_FDEP_1M': [rest_dynamic_fdep_1m],
    'REST_DYNAMIC_FDEP_3M': [rest_dynamic_fdep_3m],
    'REST_DYNAMIC_IL_1M': [rest_dynamic_il_1m],
    'REST_DYNAMIC_IL_3M': [rest_dynamic_il_3m],
    'REST_DYNAMIC_PAYM_1M': [rest_dynamic_paym_1m],
    'REST_DYNAMIC_PAYM_3M': [rest_dynamic_paym_3m],
    'REST_DYNAMIC_SAVE_3M': [rest_dynamic_save_3m],
    'SUM_TRAN_ATM_TENDENCY1M': [sum_tran_atm_tendency1m],
    'SUM_TRAN_ATM_TENDENCY3M': [sum_tran_atm_tendency3m],
    'SUM_TRAN_SUP_TENDENCY1M': [sum_tran_sup_tendency1m],
    'SUM_TRAN_SUP_TENDENCY3M': [sum_tran_sup_tendency3m],
    'TRANS_AMOUNT_TENDENCY3M': [trans_amount_tendency3m],
    'TRANS_CNT_TENDENCY3M': [trans_cnt_tendency3m],
    'TRANS_COUNT_ATM_PRC': [trans_count_atm_prc],
    'TRANS_COUNT_NAS_PRC': [trans_count_nas_prc],
    'TRANS_COUNT_SUP_PRC': [trans_count_sup_prc],
    'TURNOVER_CC': [turnover_cc],
    'TURNOVER_DYNAMIC_CC_1M': [turnover_dynamic_cc_1m],
    'TURNOVER_DYNAMIC_CC_3M': [turnover_dynamic_cc_3m],
    'TURNOVER_DYNAMIC_CUR_1M': [turnover_dynamic_cur_1m],
    'TURNOVER_DYNAMIC_CUR_3M': [turnover_dynamic_cur_3m],
    'TURNOVER_DYNAMIC_IL_1M': [turnover_dynamic_il_1m],
    'TURNOVER_DYNAMIC_IL_3M': [turnover_dynamic_il_3m],
    'TURNOVER_DYNAMIC_PAYM_1M': [turnover_dynamic_paym_1m],
    'TURNOVER_DYNAMIC_PAYM_3M': [turnover_dynamic_paym_3m],
    'TURNOVER_PAYM': [turnover_paym],
    'CLNT_JOB_POSITION': [clnt_job_position],
    'PACK': [pack]
})

if st.button("Predict"):
    # Send the data to the Flask API
    response = requests.post("http://127.0.0.1:5000/predict", json=input_data.to_dict(orient='records'))
    prediction = response.json()

    # Display the prediction
    st.write(f"Prediction: {prediction[0]}")

