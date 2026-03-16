import streamlit as st
import re
st.set_page_config(
    page_title="Backend Logic Validator v1.0", 
    page_icon="⚙️",                          
    layout="centered"                         
)
st.markdown("""
    <style>
    h1 { color: #00D4FF; font-family: 'Courier New', Courier, monospace; }
    .stButton>button { border-radius: 5px; border: 1px solid #00D4FF; } 
    </style>
""", unsafe_allow_html=True)
def check_invoice(inv_no, inv_amt, order_amt):
    clean_no = str(inv_no).strip().upper()
    taiwan_inv_pattern = r'^[A-Z]{2}\d{8}$'
    
    if not re.match(taiwan_inv_pattern, clean_no):
        return {"status": "ERROR", "msg": "發票號碼格式錯誤 (需為8位數字)"}
    
    if abs(inv_amt - order_amt) > 0:
        return {"status": "WARNING", "msg": f"金額不符！落差 {inv_amt - order_amt} 元"}
    
    return {"status": "SUCCESS", "msg": "對帳完全正確"}


st.title("AI 財務對帳代理人 (Demo)")

inv_no = st.text_input("輸入發票號碼", value="AA12345678")
inv_amt = st.number_input("發票金額", value=1000)
order_amt = st.number_input("訂單金額", value=1000)

if st.button("開始對帳"):
    result = check_invoice(inv_no, inv_amt, order_amt)
    if result["status"] == "SUCCESS":
        st.success(result["msg"])
    elif result["status"] == "WARNING":
        st.warning(result["msg"])
    else:
        st.error(result["msg"])
