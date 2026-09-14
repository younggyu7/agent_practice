import streamlit as st

st.set_page_config(page_title="사내 업무 에이전트")

st.title("사내 업무 에이전트")
st.write("write는 화면에 텍스트를 출력하는 함수입니다.")

st.header("헤더 헤더")
st.subheader("서브 헤더")

st.markdown("- python\n" "- fastAPI\n" "- streamlit\n")

st.divider()
st.caption("출처 - streamlit 공식 문서")

count = 0  # 버튼을 눌러도 1 이상 안올라감 -> 계속 렌더링이 되기에 계속 초기화된다. -> 데이터가 쌓이지 않는다.

if st.button("문서 1건 추가"):
    count += 1

st.write("추가한 문서 수 : ", count)
