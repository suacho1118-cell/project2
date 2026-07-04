import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="첫 웹페이지",
    page_icon="👋",
    layout="centered"
)

# CSS 스타일
st.markdown("""
<style>
.stApp {
    background-color: #0B1F4D;
}

/* 모든 글씨 흰색 */
h1, h2, h3, p, div, span, label {
    color: black !important;
}

/* 버튼 스타일 */
.stButton > button {
    width: 100%;
    background-color: white;
    color: #0B1F4D;
    font-size: 18px;
    font-weight: bold;
    border-radius: 10px;
    border: none;
    padding: 12px;
}

.stButton > button:hover {
    background-color: #DCE6FF;
    color: #0B1F4D;
}
</style>
""", unsafe_allow_html=True)

# 화면 상태 저장
if "page" not in st.session_state:
    st.session_state.page = "main"

# ---------------- 메인 화면 ----------------
if st.session_state.page == "main":

    st.markdown(
        "<h1 style='text-align:center;'>안녕하세요 👋</h1>",
        unsafe_allow_html=True
    )

    st.write("")

    if st.button("나도 인사하기"):
        st.session_state.page = "celebrate"
        st.rerun()

# ---------------- 축하 화면 ----------------
elif st.session_state.page == "celebrate":

    # 축하 효과
    st.balloons()

    st.markdown(
        """
        <h2 style='text-align:center;'>
        🎉 첫 웹페이지 제작을 축하해요! 🎉
        </h2>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    if st.button("돌아가기"):
        st.session_state.page = "main"
        st.rerun()

