import streamlit as st

# =========================
# 페이지 설정
# =========================
st.set_page_config(
    page_title="퍼스트존 관리자",
    page_icon="🛒",
    layout="wide",
)


# =========================
# 예제 주문 데이터
# =========================
orders = [
    {
        "주문번호": "ORD-24081",
        "주문일시": "09-21 09:14",
        "고객": "김민준",
        "상품명": "무선 이어폰 프로",
        "카테고리": "가전",
        "수량": 1,
        "결제금액": 129000,
        "상태": "결제 완료",
        "결제수단": "카드",
    },
    {
        "주문번호": "ORD-24082",
        "주문일시": "09-21 10:41",
        "고객": "이서연",
        "상품명": "캠핑 체어 2인용",
        "카테고리": "레저",
        "수량": 2,
        "결제금액": 98000,
        "상태": "배송 준비",
        "결제수단": "카드",
    },
    {
        "주문번호": "ORD-24083",
        "주문일시": "09-21 10:52",
        "고객": "박도윤",
        "상품명": "SF 노트북 파우치",
        "카테고리": "패션",
        "수량": 3,
        "결제금액": 42000,
        "상태": "배송 중",
        "결제수단": "간편결제",
    },
    {
        "주문번호": "ORD-24084",
        "주문일시": "09-21 10:35",
        "고객": "최지우",
        "상품명": "USB-C 충전기 65W",
        "카테고리": "가전",
        "수량": 1,
        "결제금액": 34000,
        "상태": "결제 완료",
        "결제수단": "간편결제",
    },
    {
        "주문번호": "ORD-24085",
        "주문일시": "09-21 11:08",
        "고객": "정하은",
        "상품명": "여행용 가방",
        "카테고리": "패션",
        "수량": 1,
        "결제금액": 89000,
        "상태": "취소",
        "결제수단": "카드",
    },
    {
        "주문번호": "ORD-24086",
        "주문일시": "09-21 11:22",
        "고객": "김지수",
        "상품명": "무드 식탁 세트",
        "카테고리": "가구",
        "수량": 1,
        "결제금액": 320000,
        "상태": "배송 준비",
        "결제수단": "무통장",
    },
    {
        "주문번호": "ORD-24087",
        "주문일시": "09-21 12:01",
        "고객": "윤아름",
        "상품명": "런닝 셔츠 화이트",
        "카테고리": "패션",
        "수량": 2,
        "결제금액": 56000,
        "상태": "배송 완료",
        "결제수단": "카드",
    },
    {
        "주문번호": "ORD-24088",
        "주문일시": "09-21 12:44",
        "고객": "임준호",
        "상품명": "텀블러 500ml",
        "카테고리": "생활",
        "수량": 4,
        "결제금액": 28000,
        "상태": "환불",
        "결제수단": "간편결제",
    },
]


# =========================
# Sidebar
# =========================
with st.sidebar:
    st.title("퍼스트존 관리자")
    st.caption("피커스 운영팀")

    st.divider()

    st.write("메뉴")

    menu = st.radio(
        "관리 메뉴",
        [
            "대시보드",
            "주문 관리",
            "상품 관리",
            "정산",
        ],
        index=1,
    )

    st.divider()

    st.write("조회 기간")

    period = st.selectbox(
        "기간",
        [
            "오늘",
            "최근 7일",
            "최근 30일",
            "전체",
        ],
    )

    hide_cancel = st.checkbox("취소·환불 숨기기")

    st.caption("v0.1 데모 데이터")


# =========================
# 제목
# =========================
st.title("🛒 주문 관리")
st.caption("오늘 들어온 주문을 확인하고 배송 상태를 관리합니다.")


# =========================
# Metric
# =========================
metric1, metric2, metric3, metric4 = st.columns(4)

with metric1:
    st.metric(
        "오늘 주문",
        "128",
    )

with metric2:
    st.metric(
        "결제 완료",
        "96",
        "+12",
    )

with metric3:
    st.metric(
        "배송 준비",
        "18",
        "-3",
    )

with metric4:
    st.metric(
        "취소·환불",
        "6",
    )


st.divider()


# =========================
# 검색 조건
# =========================
search_col, status_col, payment_col = st.columns([3, 1, 2])

with search_col:
    keyword = st.text_input(
        "검색",
        placeholder="주문번호 또는 상품명",
    )

with status_col:
    status = st.selectbox(
        "상태",
        [
            "전체",
            "결제 완료",
            "배송 준비",
            "배송 중",
            "배송 완료",
            "취소",
            "환불",
        ],
    )

with payment_col:
    payment = st.multiselect(
        "결제수단",
        [
            "카드",
            "간편결제",
            "무통장",
        ],
    )


# =========================
# 데이터 필터
# =========================
filtered_orders = []

for order in orders:

    include = True

    if keyword:
        keyword_lower = keyword.lower()

        if (
            keyword_lower not in order["주문번호"].lower()
            and keyword_lower not in order["상품명"].lower()
            and keyword_lower not in order["고객"].lower()
        ):
            include = False

    if status != "전체":
        if order["상태"] != status:
            include = False

    if payment:
        if order["결제수단"] not in payment:
            include = False

    if hide_cancel:
        if order["상태"] in ["취소", "환불"]:
            include = False

    if include:
        filtered_orders.append(order)


total_price = 0

for order in filtered_orders:
    total_price += order["결제금액"]


st.write(f"**{len(filtered_orders)}건 / " f"결제 총액: {total_price:,}원**")


# =========================
# 주문 테이블
# =========================
st.dataframe(
    filtered_orders,
    use_container_width=True,
    hide_index=True,
    column_config={
        "수량": st.column_config.NumberColumn(
            "수량",
            format="%d개",
        ),
        "결제금액": st.column_config.NumberColumn(
            "결제금액",
            format="₩%d",
        ),
    },
)


st.divider()


# =========================
# 차트 / 배송 처리
# =========================
chart_col, delivery_col = st.columns([2, 1])


with chart_col:

    st.subheader("카테고리별 주문 수")

    category_data = {
        "카테고리": [
            "가구",
            "가전",
            "레저",
            "생활",
            "식품",
            "패션",
        ],
        "주문 수": [
            1,
            2,
            1,
            1,
            1,
            2,
        ],
    }

    st.bar_chart(
        category_data,
        x="카테고리",
        y="주문 수",
    )


with delivery_col:

    st.subheader("오늘 배송 처리")

    st.progress(
        0.72,
        text="상품 등록 · 72%",
    )

    st.info("결제 완료 96건 중 69건이 " "송장이 등록되었습니다.")

    st.warning("ORD-24086은 무통장 입금이 " "확인되지 않았습니다.")

    with st.expander("처리 지침 로그 보기"):
        st.code("""
09:20 ORD-24081 결제 확인
09:25 ORD-24082 배송 준비
09:41 ORD-24083 배송 시작
10:05 ORD-24084 결제 확인
            """)


st.divider()


# =========================
# 상품 관리
# =========================
product_tab, help_tab = st.tabs(
    [
        "새 상품 등록",
        "도움말",
    ]
)


with product_tab:

    st.subheader("새 상품 등록")

    with st.form("product_form"):

        input_col1, input_col2 = st.columns(2)

        with input_col1:

            product_code = st.text_input(
                "상품코드",
                placeholder="SKU-10293",
            )

            category = st.selectbox(
                "카테고리",
                [
                    "가전",
                    "가구",
                    "패션",
                    "생활",
                    "식품",
                    "레저",
                ],
            )

            price = st.text_input(
                "판매가(원)",
                placeholder="19800",
            )

        with input_col2:

            product_name = st.text_input(
                "상품명",
                placeholder="보온 머그컵 350ml",
            )

            sale_status = st.selectbox(
                "판매 상태",
                [
                    "판매 중",
                    "판매 중지",
                    "품절",
                ],
            )

            stock = st.text_input(
                "재고 수량",
                placeholder="120",
            )

        image = st.file_uploader(
            "상품 이미지 (png · jpg)",
            type=["png", "jpg", "jpeg"],
        )

        submitted = st.form_submit_button("등록")

    if submitted:

        if product_code and product_name and price and stock:
            st.success(f"{product_name} 상품이 등록되었습니다.")

        else:
            st.warning("상품 정보를 모두 입력해주세요.")


with help_tab:

    st.subheader("상품 등록 도움말")

    st.write("상품코드와 상품명은 필수 항목입니다.")

    st.write("상품 이미지는 PNG 또는 JPG 파일을 사용할 수 있습니다.")

    st.info("판매 중지 상태로 등록하면 고객에게 상품이 노출되지 않습니다.")
