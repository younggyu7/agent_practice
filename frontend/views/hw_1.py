import streamlit as st

# =========================
# 페이지 설정
# =========================
st.set_page_config(
    page_title="우리들의 공간",
    page_icon="💬",
    layout="wide",
)


# =========================
# 상단 제목
# =========================
st.title("💬 우리들의 공간")
st.caption("간단한 채팅과 게시글을 함께 사용하는 예제입니다.")

st.divider()


# =========================
# 좌 / 우 영역
# =========================
chat_col, board_col = st.columns(2)


# =========================
# 왼쪽 : 채팅
# =========================
with chat_col:
    st.subheader("💬 채팅하기")

    with st.chat_message("assistant"):
        st.write("안녕하세요!")
        st.write("무엇을 도와드릴까요?")

    with st.chat_message("user"):
        st.write("이번 주말에 뭐 할까요?")

    with st.chat_message("assistant"):
        st.write("'이번 주말에 뭐 할까요?'에 대한 답변입니다!")
        st.write("좋은 하루 되세요 😄")

    message = st.chat_input("메시지를 입력하세요...")

    if message:
        with st.chat_message("user"):
            st.write(message)

        with st.chat_message("assistant"):
            st.write(f"'{message}'에 대한 답변입니다!")
            st.write("좋은 하루 되세요 😄")


# =========================
# 오른쪽 : 게시글
# =========================
with board_col:
    st.subheader("📄 게시글 목록")

    title = st.text_input(
        "제목",
        placeholder="제목을 입력하세요",
    )

    content = st.text_area(
        "내용",
        placeholder="내용을 입력하세요",
    )

    if st.button("게시글 등록", use_container_width=True):
        if title and content:
            st.success("게시글이 등록되었습니다.")
        else:
            st.warning("제목과 내용을 모두 입력해주세요.")

    st.divider()

    st.write("**1. 이번 주말에 뭐 할까요?**")
    st.write("이번 주말에 근교 여행을 가려고 하는데,")
    st.write("추천해주실 만한 곳이 있을까요?")
    st.caption("2025-06-10 10:24")

    st.divider()

    st.write("**2. 반갑습니다!**")
    st.write("안녕하세요. 잘 부탁드려요!")
    st.caption("2025-06-10 10:18")

    st.divider()

    st.write("**3. 맛집 추천**")
    st.write("강남 근처에 괜찮은 점심 맛집 있나요?")
    st.write("추천 부탁드립니다!")
    st.caption("2025-06-09 16:40")
