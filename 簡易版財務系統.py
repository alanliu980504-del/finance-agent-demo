import streamlit as st
import re
import streamlit as st
st.set_page_config(
    page_title="Cloud Logic Console", 
    page_icon="⚙️", 
    layout="wide"
)
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    header { background-color: #FFFFFF !important; border-bottom: 1px solid #E0E0E0; }
    [data-testid="stSidebar"] {
        background-color: #F8F9FA !important;
        border-right: 1px solid #E0E0E0;
    }
    h1, h2, h3, p, span, label {
        color: #3C4043 !important;
        font-family: 'Roboto', sans-serif;
    }
    .stTextInput>div>div>input {
        border-radius: 4px !important;
        border: 1px solid #DADCE0 !important;
        background-color: white !important;
    }
    .stButton>button {
        background-color: #1A73E8 !important;
        color: white !important;
        border-radius: 4px !important;
        border: none !important;
        font-weight: 500 !important;
        padding: 0.5rem 2rem !important;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 4]) 

with col1:
    st.image("https://www.gstatic.com", width=40) 
    st.write("### 控制台")
    st.caption("專案編號：PRJ-2026-V1")

with col2:
    st.title("驗證引擎總覽")
    st.info("系統狀態：運行中 (Running)")
    
    # 建立卡片式區域
    with st.container():
        st.write("---")
        st.subheader("數據校驗輸入")
        inv_no = st.text_input("發票識別碼 (Identifier)")

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
