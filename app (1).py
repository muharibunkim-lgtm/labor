import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="편의점 알바 영웅: 나의 첫 일터 약속",
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
    st.session_state.knowledge = 0
if "history" not in st.session_state:
    st.session_state.history = []

def reset_game():
    st.session_state.stage = 1
    st.session_state.hp = 100
    st.session_state.money = 0
    st.session_state.knowledge = 0
    st.session_state.history = []

# --- 2. 게임 헤더 및 대시보드 ---
st.title("🏪 편의점 알바 영웅")
st.caption("초등 고학년 ~ 중학생을 위한 근로권리 체험 시뮬레이션 웹게임")

# 대시보드 (상태 시각화)
col1, col2, col3 = st.columns(3)
col1.metric("🔋 내 체력", f"{st.session_state.hp}%")
col2.metric("🪙 누적 임금", f"{st.session_state.money:,}원")
col3.metric("🛡️ 권리 지수", f"{st.session_state.knowledge}점")

# 체력 바
st.progress(max(0, min(100, st.session_state.hp)) / 100)
st.divider()

# --- 3. 스테이지별 시나리오 ---

# [STAGE 1] 근로계약서 (일터 약속 문서)
if st.session_state.stage == 1:
    st.subheader("📍 1단계: 첫 출근과 일터 약속 문서")
    
    st.info("""
    **🏪 상황:** 편의점 사장님을 만났습니다.  
    **사장님:** "반가워! 오늘부터 바로 일 시작하면 돼. 서류 작성은 나중에 바쁠 때 천천히 하자고~"
    """)
    
    with st.expander("💡 [권리 힌트] 일하기 전에 꼭 해야 하는 약속이 있을까요?"):
        st.write("""
        - **일터 약속 문서(근로계약서)**는 일을 시작하기 전에 **반드시 작성**하고 1부를 받아야 합니다.
        - 시급, 근무 시간, 쉬는 시간, 하는 일 등이 정확히 적혀 있어야 나중에 불이익을 받지 않아요!
        """)

    col_a, col_b = st.columns(2)
    
    if col_a.button("1. '네 사장님! 나중에 쓸게요.' 하고 일 시작하기", use_container_width=True):
        st.session_state.hp -= 15
        st.session_state.knowledge -= 10
        st.session_state.history.append(("1단계: 근로계약서", "❌ 작성 미루기 수락", "계약서 없이 일을 시작하여 나중에 내 권리를 주장하기 어려워졌습니다."))
        st.session_state.stage = 2
        st.rerun()

    if col_b.button("2. '사장님, 시작 전에 일터 약속 문서를 먼저 쓰고 싶어요!'", use_container_width=True):
        st.session_state.knowledge += 25
        st.session_state.money += 10030
        st.session_state.history.append(("1단계: 근로계약서", "⭕ 즉시 작성 요청", "당당하게 근로계약서 작성을 요청하여 서면으로 시급과 근무시간을 보호받았습니다."))
        st.session_state.stage = 2
        st.rerun()

# [STAGE 2] 최저임금 (최소 약속 임금)
elif st.session_state.stage == 2:
    st.subheader("📍 2단계: 시급 결정의 순간")
    
    st.info("""
    **🏪 상황:** 첫날 일을 마치고 사장님이 시급에 대해 이야기합니다.  
    **사장님:** "아직 학생이고 일도 배우는 중이니까 시급은 7,000원만 줄게. 배우는 단계잖아?"
    """)
    
    with st.expander("💡 [권리 힌트] 학생이라고 시급을 적게 받아도 될까요?"):
        st.write("""
        - **최소 약속 임금(최저임금)**은 법으로 정해진 '최소한의 가치'입니다.
        - 나이가 어리거나, 수습/배우는 기간이라도 법적 기준 이상의 최저임금을 받아야 할 권리가 있습니다!
        """)

    col_a, col_b = st.columns(2)
    
    if col_a.button("1. '배우는 중이니까 어쩔 수 없지...' 수락하기", use_container_width=True):
        st.session_state.hp -= 10
        st.session_state.money += 21000  # 3시간 x 7000원
        st.session_state.knowledge -= 10
        st.session_state.history.append(("2단계: 최저임금", "❌ 불법 감액 수락", "최저임금보다 적은 시급을 받아 정당한 노동의 대가를 받지 못했습니다."))
        st.session_state.stage = 3
        st.rerun()

    if col_b.button("2. '학생이어도 법으로 정해진 최소 약속 임금은 보장되어야 해요!'", use_container_width=True):
        st.session_state.knowledge += 25
        st.session_state.money += 30090  # 3시간 x 최저임금 약 10,030원
        st.session_state.history.append(("2단계: 최저임금", "⭕ 최저임금 준수 요구", "법적 최저임금을 정당하게 요구하여 정당한 노동의 대가를 지켜냈습니다."))
        st.session_state.stage = 3
        st.rerun()

# [STAGE 3] 휴게시간 (에너지 충전 시간)
elif st.session_state.stage == 3:
    st.subheader("📍 3단계: 연속 근무와 휴식")
    
    st.info("""
    **🏪 상황:** 물건 정리와 손님 응대로 4시간 연속 일했습니다.  
    **사장님:** "오늘 물건 들어오는 날이라 바쁘다! 쉬지 말고 계속 정리하자!"
    """)
    
    with st.expander("💡 [권리 힌트] 얼마나 일하면 쉬어야 할까요?"):
        st.write("""
        - **에너지 충전 시간(휴게시간)**: **4시간 일하면 30분 이상**, **8시간 일하면 1시간 이상** 쉬어야 합니다.
        - 휴식은 작업 능률을 올리고 안전사고를 예방하는 소중한 권리입니다.
        """)

    col_a, col_b = st.columns(2)
    
    if col_a.button("1. '참고 계속 일하자!' 쉬지 않고 계속 일하기", use_container_width=True):
        st.session_state.hp -= 30
        st.session_state.history.append(("3단계: 휴게시간", "❌ 휴식 없이 강행", "휴식 시간 없이 무리하게 일하여 피로도가 극심해졌습니다."))
        st.session_state.stage = 4
        st.rerun()

    if col_b.button("2. '4시간 일했으니 30분 충전 시간을 갖겠습니다!'", use_container_width=True):
        st.session_state.hp = min(100, st.session_state.hp + 20)
        st.session_state.knowledge += 25
        st.session_state.history.append(("3단계: 휴게시간", "⭕ 휴게시간 확보", "30분의 휴식 시간을 통해 체력을 회복하고 안전하게 근무를 이어갔습니다."))
        st.session_state.stage = 4
        st.rerun()

# [STAGE 4] 실수 및 유통기한 (손실 부담)
elif st.session_state.stage == 4:
    st.subheader("📍 4단계: 폐기 상품과 실수")
    
    st.info("""
    **🏪 상황:** 유통기한이 지난 삼각김밥을 발견했습니다.  
    **사장님:** "이거 왜 미리 안 팔았어? 손해 본 금액은 네 알바비에서 깎을 테니 그런 줄 알아!"
    """)
    
    with st.expander("💡 [권리 힌트] 매장 손실을 알바생 돈에서 마음대로 깎아도 되나요?"):
        st.write("""
        - 고의로 부순 것이 아니라면, **사업장의 일반적인 관리 손실을 근로자에게 일방적으로 덮어씌우거나 임금에서 마음대로 차감(공제)할 수 없습니다.**
        """)

    col_a, col_b = st.columns(2)
    
    if col_a.button("1. '제 잘못인가 봐요...' 내 돈으로 메우기", use_container_width=True):
        st.session_state.money -= 3000
        st.session_state.hp -= 15
        st.session_state.knowledge -= 10
        st.session_state.history.append(("4단계: 손실 차감", "❌ 부당 공제 수락", "고의가 아닌 매장 손실을 내 임금에서 부당하게 차감당했습니다."))
        st.session_state.stage = 5
        st.rerun()

    if col_b.button("2. '고의가 아닌 손실을 임금에서 일방적으로 깎는 것은 부당해요!'", use_container_width=True):
        st.session_state.knowledge += 25
        st.session_state.hp += 10
        st.session_state.history.append(("4단계: 손실 차감", "⭕ 부당 차감 거부", "부당한 임금 차감 요구에 대처하여 내 권리와 소중한 임금을 지켰습니다."))
        st.session_state.stage = 5
        st.rerun()

# [STAGE 5] 결과 리포트 및 엔딩
elif st.session_state.stage == 5:
    st.balloons()
    st.subheader("🎉 근무 완료! 나의 근로 권리 리포트")
    
    # 평가 등급
    total_score = st.session_state.knowledge
    if total_score >= 80:
        grade = "🏆 당당한 근로 권리 수호자!"
        badge_color = "success"
    elif total_score >= 50:
        grade = "🥈 성실하게 성장하는 알바생!"
        badge_color = "info"
    else:
        grade = "🐤 권리 지식이 더 필요한 풋내기!"
        badge_color = "warning"

    st.subheader(f"나의 칭호: {grade}")
    
    st.write("### 📊 최종 결과 Summary")
    col1, col2, col3 = st.columns(3)
    col1.metric("남은 체력", f"{st.session_state.hp}%")
    col2.metric("최종 수령 임금", f"{st.session_state.money:,}원")
    col3.metric("최종 권리 지수", f"{st.session_state.knowledge}점")

    st.write("---")
    st.write("### 📋 내가 내린 선택의 순간들")
    for stage_name, choice_title, description in st.session_state.history:
        with st.container():
            st.markdown(f"**[{stage_name}] {choice_title}**")
            st.caption(description)
            st.write("")

    st.write("---")
    st.success("""
    🎓 **오늘 배운 핵심 요약!**
    1. **근로계약서(일터 약속 문서)**는 일하기 전에 꼭 작성하고 1부 보관하기!
    2. **최저임금(최소 약속 임금)**은 나이나 경험과 상관없이 법적으로 보장받는 권리!
    3. **휴게시간(에너지 충전 시간)**은 4시간당 30분씩 꼭 챙겨 쉬기!
    4. **부당한 임금 차감**에 당황하지 말고 정당하게 대화하기!
    """)

    if st.button("🔄 게임 다시 시작하기", use_container_width=True):
        reset_game()
        st.rerun()
