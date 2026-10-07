import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="편의점 알바 영웅: 정당한 권리와 지혜로운 협상",
    page_icon="🏪",
    layout="centered"
)

# --- 1. 초기 세션 상태(Session State) 설정 ---
if "stage" not in st.session_state:
    st.session_state.stage = 1
if "hp" not in st.session_state:
    st.session_state.hp = 100
if "money" not in st.session_state:
    st.session_state.money = 0
if "knowledge" not in st.session_state:
    st.session_state.knowledge = 50
if "trust" not in st.session_state:
    st.session_state.trust = 50
if "evidence" not in st.session_state:
    st.session_state.evidence = []  # 수집한 증거 목록
if "history" not in st.session_state:
    st.session_state.history = []

def reset_game():
    st.session_state.stage = 1
    st.session_state.hp = 100
    st.session_state.money = 0
    st.session_state.knowledge = 50
    st.session_state.trust = 50
    st.session_state.evidence = []
    st.session_state.history = []

# --- 2. 게임 헤더 및 대시보드 ---
st.title("🏪 편의점 알바 영웅: 정당한 권리와 지혜로운 협상")
st.caption("권리만 주장하기보다 '논리'와 '증거'로 사장님을 설득하는 시뮬레이션 웹게임")

# 4개 지표 대시보드
col1, col2, col3, col4 = st.columns(4)
col1.metric("🔋 내 체력", f"{st.session_state.hp}%")
col2.metric("🪙 누적 임금", f"{st.session_state.money:,}원")
col3.metric("🛡️ 권리 지수", f"{st.session_state.knowledge}점")
col4.metric("🤝 사장님 신뢰", f"{st.session_state.trust}점")

# 상태 바 (체력)
st.write("**내 체력 상태**")
st.progress(max(0, min(100, st.session_state.hp)) / 100)

if st.session_state.evidence:
    st.info(f"📁 **내가 확보한 증거 문서:** {', '.join(st.session_state.evidence)}")

st.divider()

# 게임 오버 조건 체크
if st.session_state.trust <= 0:
    st.error("💥 **게임 오버:** 사장님과의 신뢰가 깨져 해고당했습니다! 권리를 요구할 때는 감정적인 태도보다 예의 바르고 논리적인 대화가 필요합니다.")
    if st.button("🔄 다시 도전하기"):
        reset_game()
        st.rerun()
    st.stop()

if st.session_state.hp <= 0:
    st.error("💥 **게임 오버:** 과로로 병원에 입원했습니다! 체력 관리와 휴게시간 확보는 필수입니다.")
    if st.button("🔄 다시 도전하기"):
        reset_game()
        st.rerun()
    st.stop()

# --- 3. 스테이지별 시나리오 ---

# [STAGE 1] 근로계약서 작성과 서류 검토
if st.session_state.stage == 1:
    st.subheader("📍 1단계: 근로계약서와 증거 확보")
    
    st.info("""
    **🏪 상황:** 출근 첫날, 사장님이 일부터 하라고 하십니다.  
    **사장님:** "바쁜 시간이니까 우선 일부터 배우자. 계약서는 한 달 뒤에 손에 익으면 쓰면 돼~"
    """)

    st.markdown("### ❓ 어떻게 대처할까요?")
    
    choice_s1 = st.radio(
        "내가 취할 대화나 속마음을 선택하세요:",
        [
            "1. '사장님, 계약서를 서명해서 서로 1부씩 보관하면 근무 조건도 명확해지고, 저도 더 책임감 있게 일할 수 있을 것 같아요!'",
            "2. '사장님, 근로기준법상 첫날 계약서 안 쓰면 불법인 거 모르세요? 지금 당장 작성해 주세요.'",
            "3. (속마음: '사장님께 바로 말씀드리긴 부담스러우니... 일단 오늘 근무 시간표랑 출퇴근 문자메시지만 사진으로 찍어 보관해야겠다.')",
            "4. '네, 사장님! 매장이 바쁘니까 일 먼저 배울게요. 계약서는 나중에 한가할 때 천천히 쓰겠습니다.'"
        ]
    )

    if st.button("선택 결정하기", use_container_width=True, key="btn_s1"):
        if choice_s1.startswith("1."):
            st.session_state.knowledge += 20
            st.session_state.trust += 10
            st.session_state.evidence.append("작성된 근로계약서 사본")
            st.session_state.history.append(("1단계", "지혜로운 작성 요구", "서로에게 유익함을 설명하여 근로계약서를 작성하고 사본을 챙겼습니다."))
            st.session_state.stage = 2
            st.rerun()
        elif choice_s1.startswith("2."):
            st.session_state.knowledge += 10
            st.session_state.trust -= 35
            st.session_state.history.append(("1단계", "감정적 대립", "법을 언급했지만 사장님과의 신뢰도가 급격히 떨어졌습니다."))
            st.session_state.stage = 2
            st.rerun()
        elif choice_s1.startswith("3."):
            st.session_state.evidence.append("출퇴근 기록 사진")
            st.session_state.knowledge += 5
            st.session_state.trust += 5
            st.session_state.history.append(("1단계", "증거 수집", "계약서는 못 썼지만 추후 입증할 출퇴근 사진을 챙겼습니다."))
            st.session_state.stage = 2
            st.rerun()
        elif choice_s1.startswith("4."):
            st.session_state.trust += 10
            st.session_state.knowledge -= 15
            st.session_state.hp -= 10
            st.session_state.history.append(("1단계", "권리 포기", "계약서 없이 일을 시작하여 불이익의 위험에 노출되었습니다."))
            st.session_state.stage = 2
            st.rerun()

# [STAGE 2] 직접 계산하는 주휴수당 미션
elif st.session_state.stage == 2:
    st.subheader("📍 2단계: 직접 계산하는 소중한 주휴수당")
    
    st.info("""
    **🏪 상황:** 일주일 동안 하루 5시간씩, 총 3일(주 15시간) 성실하게 일했습니다! (최저시급: 10,030원)  
    **사장님:** "이번 주 고생했다! 총 15시간 일했으니 150,450원 입금했다~"  
    **내 생각:** '음? 주 15시간 이상 개근해서 일했으면 **주휴수당(성실 휴식 보너스)**도 추가로 받아야 하는 것 같은데...?'
    """)

    st.warning("🧮 **[직접 계산 퀴즈]** 주 15시간 일했을 때 꼭 받아야 할 '주휴수당 포함 총 임금'은 얼마일까요?")
    st.caption("💡 힌트: 주휴수당은 1주일 동안 약속된 근무시간을 모두 채우면 1일치(5시간) 일값을 추가로 더 주는 제도입니다!")

    user_calc = st.radio(
        "정확한 계산 금액을 선택하세요:",
        [
            "1. 150,450원 (기본 15시간 수당만 받는 게 맞다)",
            "2. 200,600원 (기본 15시간 + 주휴수당 5시간 = 총 20시간 수당)",
            "3. 250,750원 (기본 15시간 + 주휴수당 10시간 = 총 25시간 수당)"
        ]
    )

    if st.button("계산 결과 제출 및 사장님께 말씀드리기", use_container_width=True, key="btn_s2"):
        if "2. 200,600원" in user_calc:
            if "작성된 근로계약서 사본" in st.session_state.evidence or "출퇴근 기록 사진" in st.session_state
