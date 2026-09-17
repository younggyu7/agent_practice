import streamlit as st

st.title("채팅과 파일 업로드")

# # 파일 업로드
# uploaded_file = st.file_uploader("파일을 선택하세요", type=["txt", "pdf"])
# if uploaded_file is not None:
#     st.write(f"업로드한 파일: {uploaded_file.name}")
#     st.write(f"크기: {uploaded_file.size}바이트")

# 대화 기록 초기화
with st.chat_message("user"):
    st.write("안녕하세요")

with st.chat_message("assistant", avatar="🤖"):
    st.write("무엇을 도와드릴까요?")

if "messages" not in st.session_state:
    st.session_state.messages = []

# 화면을 다시 그릴 때 이전 대화 표시
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# 새 메시지 입력
if prompt := st.chat_input("메시지를 입력하세요"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    answer = f"입력하신 내용: {prompt}"
    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.write(answer)
