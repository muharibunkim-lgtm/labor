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
st.caption("권리만 주장하기보다 '논리'와 '증거'로 사장님을 설득하는 고난도 시뮬레이션")

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

# [STAGE 1] 계약서 작성과 서류 검토
if st.session_state.stage == 1:
    st.subheader("📍 1단계: 근로계약서와 증거 확보")
    
    st.info("""
    **🏪 상황:** 출근 첫날, 사장님이 일부터 하라고 하십니다.  
    **사장님:** "바쁜 시간이니까 우선 일부터 배우자. 계약서는 한 달 뒤에 손에 익으면 쓰면 돼~"
    """)

    st.markdown("### ❓ 어떻게 대처할까요?")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("A. 무조건 따지기\n\n'법적으로 첫날 안 쓰면 불법인 거 모르세요?'", use_container_width=True):
            st.session_state.knowledge += 10
            st.session_state.trust -= 35
            st.session_state.history.append(("1단계", "감정적 대립", "법을 언급했지만 사장님과의 신뢰도가 급격히 떨어졌습니다."))
            st.session_state.stage = 2
            st.rerun()
            
        if st.button("B. 부드러운 논리적 요구\n\n'사장님, 서명하고 1부씩 보관하면 서로 깔끔해서 일하기 마음 편할 것 같아요!'", use_container_width=True):
            st.session_state.knowledge += 20
            st.session_state.trust += 10
            st.session_state.evidence.append("작성된 근로계약서 사본")
            st.session_state.history.append(("1단계", "지혜로운 작성 요구", "서로에게 유익함을 설명하여 근로계약서를 작성하고 사본을 챙겼습니다."))
            st.session_state.stage = 2
            st.rerun()

    with col2:
        if st.button("C. 조용히 증거만 남기기\n\n계약서는 안 쓰고 출퇴근 시간표와 사장님 문자를 사진 찍어 보관한다.", use_container_width=True):
            st.session_state.evidence.append("출퇴근 기록 사진")
            st.session_state.knowledge += 5
            st.session_state.trust += 5
            st.session_state.history.append(("1단계", "증거 수집", "계약서는 못 썼지만 추후 입증할 출퇴근 사진을 챙겼습니다."))
            st.session_state.stage = 2
            st.rerun()

        if st.button("D. 그냥 시키는 대로 하기\n\n'네 사장님, 나중에 바쁠 때 천천히 써요!'", use_container_width=True):
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

    if st.button("계산 결과 제출 및 사장님께 말씀드리기", use_container_width=True):
        if "2. 200,600원" in user_calc:
            if "작성된 근로계약서 사본" in st.session_state.evidence or "출퇴근 기록 사진" in st.session_state.evidence:
                st.success("✅ 정확한 계산입니다! 근로계약서/증거를 보여드리며 말씀드리니 사장님도 인정하셨습니다.")
                st.session_state.money += 200600
                st.session_state.knowledge += 25
                st.session_state.trust += 5
                st.session_state.history.append(("2단계", "주휴수당 계산 성공", "정확한 계산 수치와 증거로 정당한 주휴수당까지 수령했습니다."))
            else:
                st.warning("⚠️ 계산은 맞았지만 증거(계약서/기록)가 없어 사장님이 '그런 거 없었다'며 일부만 인정해 주셨습니다.")
                st.session_state.money += 175000
                st.session_state.knowledge += 15
                st.session_state.trust -= 10
                st.session_state.history.append(("2단계", "증거 부족 난항", "계산은 맞았으나 증거가 부족해 일부 금액만 받았습니다."))
            st.session_state.stage = 3
            st.rerun()
        else:
            st.error("❌ 잘못된 계산입니다! 사장님이 주신 기본 수당만 받거나 잘못된 요청으로 신뢰가 깎였습니다.")
            st.session_state.money += 150450
            st.session_state.knowledge -= 10
            st.session_state.trust -= 10
            st.session_state.history.append(("2단계", "계산 오류", "주휴수당 계산을 잘못하여 제 권리를 챙기지 못했습니다."))
            st.session_state.stage = 3
            st.rerun()

# [STAGE 3] 복합 딜레마 (대타 야간근무 & 휴게시간)
elif st.session_state.stage == 3:
    st.subheader("📍 3단계: 갑작스러운 대타 부탁과 야간 근무")
    
    st.info("""
    **🏪 상황:** 밤 10시가 다 되었는데, 다음 타임 알바생이 갑자기 구멍을 냈습니다.  
    **사장님:** "야, 미안한데 오늘 밤 10시부터 새벽 2시까지 4시간만 더 대타 뛰어주라. 시급은 평소처럼 똑같이 줄게! 안 해주면 매장 문 닫아야 해..."
    """)

    with st.expander("💡 [법률 지식] 밤 10시 이후 야간근무는 시급이 다를까요?"):
        st.write("""
        - **야간근무 수당 (밤 10시 ~ 다음 날 아침 6시)**: 밤 10시 이후 일할 때 상시 5인 이상 사업장에서는 **시급의 1.5배**를 지급해야 합니다.
        - 또한 청소년의 경우 야간 근무에 동의가 필요하며, 피로도가 급격히 높아집니다.
        """)

    choice = st.selectbox(
        "어떻게 대처하는 것이 가장 지혜로울까요?",
        [
            "선택하세요...",
            "1. '사장님 사정이 딱하니 그냥 평소 시급 받고 밤샘 대타 해드릴게요.'",
            "2. '밤 10시 이후는 야간 수당(1.5배)이 적용되고 4시간 일하면 30분 쉬어야 해요. 수당과 휴식시간을 주시면 도울게요!'",
            "3. '싫어요! 밤 10시 이후 일 시키는 건 불법이에요! 신고할 거예요!'",
            "4. '내일 시험도 있고 너무 피곤해서 죄송하지만 오늘은 어렵습니다. 대신 사장님이 오실 때까지만 30분 기다려 드릴게요.'"
        ]
    )

    if st.button("선택 결정하기", use_container_width=True):
        if choice.startswith("1."):
            st.session_state.hp -= 45
            st.session_state.money += 40120  # 기본 시급 4시간
            st.session_state.trust += 15
            st.session_state.knowledge -= 10
            st.session_state.history.append(("3단계", "무리한 야간대타", "사장님 신뢰는 얻었지만 체력이 바닥나고 가산 수당을 못 받았습니다."))
            st.session_state.stage = 4
            st.rerun()
        elif choice.startswith("2."):
            st.session_state.hp -= 20
            st.session_state.money += 60180  # 1.5배 야간 수당
            st.session_state.knowledge += 20
            st.session_state.trust += 5
            st.session_state.history.append(("3단계", "야간수당 & 휴게 협상", "조건(야간수당 1.5배 + 휴식)을 정확히 협상하여 윈윈했습니다."))
            st.session_state.stage = 4
            st.rerun()
        elif choice.startswith("3."):
            st.session_state.trust -= 40
            st.session_state.knowledge += 10
            st.session_state.history.append(("3단계", "극단적 거절", "사장님과 싸우게 되어 신뢰도가 크게 떨어졌습니다."))
            st.session_state.stage = 4
            st.rerun()
        elif choice.startswith("4."):
            st.session_state.hp -= 5
            st.session_state.money += 5015  # 30분 수당
            st.session_state.trust += 5
            st.session_state.knowledge += 15
            st.session_state.history.append(("3단계", "현명한 거절과 대안", "자기 상황을 솔직히 밝히고 가능한 대안을 제시해 신뢰와 정당성을 지켰습니다."))
            st.session_state.stage = 4
            st.rerun()

# [STAGE 4] 폐기/손실 및 배상 딜레마
elif st.session_state.stage == 4:
    st.subheader("📍 4단계: 손님과의 마찰 및 상품 손실")
    
    st.info("""
    **🏪 상황:** 바쁜 시간대에 손님이 음료수를 집다가 실수로 바닥에 떨어뜨려 깨졌습니다. 손님은 그냥 나가버렸습니다!  
    **사장님:** "네가 미리 주의를 안 줘서 깨진 거잖아? 음료수 값 15,000원 네 이번 알바비에서 깔 테니까 그렇게 알아!"
    """)

    st.markdown("### 🔍 내 대응 전략 선택 (증거 및 법적 근거 활용)")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("전략 1. 감정적 억울함 호소\n\n'제가 깬 것도 아닌데 왜 저한테 그러세요! 진짜 너무하시네요!'", use_container_width=True):
            st.session_state.trust -= 20
            st.session_state.money -= 15000
            st.session_state.history.append(("4단계", "감정적 호소 실패", "논리적 근거 없이 감정만 앞세워 임금 차감을 막지 못했습니다."))
            st.session_state.stage = 5
            st.rerun()

        if st.button("전략 2. CCTV 증거 + 법적 근거 제시\n\n'CCTV 보시면 손님 실수입니다. 고의가 아닌 손실을 임금에서 일방적으로 공제하는 건 근로기준법상 불가능해요.'", use_container_width=True):
            st.session_state.knowledge += 25
            st.session_state.trust += 5
            st.session_state.history.append(("4단계", "CCTV & 법적 대응 성공", "CCTV 확인 요구와 임금 전액 지급 원칙을 설명하여 부당 차감을 완벽히 막았습니다."))
            st.session_state.stage = 5
            st.rerun()

    with col2:
        if st.button("전략 3. 반반씩 부담 제안\n\n'제 책임도 조금 있으니 7,500원씩 나누어 부담해요.'", use_container_width=True):
            st.session_state.money -= 7500
            st.session_state.trust += 10
            st.session_state.knowledge -= 5
            st.session_state.history.append(("4단계", "타협안 제시", "원만한 해결을 위해 손실 일부를 부담했습니다."))
            st.session_state.stage = 5
            st.rerun()

        if st.button("전략 4. 무조건 사과 및 전액 부담\n\n'죄송합니다. 제 알바비에서 빼주세요.'", use_container_width=True):
            st.session_state.money -= 15000
            st.session_state.trust += 15
            st.session_state.knowledge -= 20
            st.session_state.history.append(("4단계", "부당 공제 수락", "권리를 포기하고 매장 손실을 본인 돈으로 지불했습니다."))
            st.session_state.stage = 5
            st.rerun()

# [STAGE 5] 다차원 평가 및 엔딩
elif st.session_state.stage == 5:
    st.balloons()
    st.subheader("🎉 최종 평가: 나는 어떤 알바 영웅일까?")
    
    score = st.session_state.knowledge
    trust = st.session_state.trust
    
    # 멀티 엔딩 로직
    if score >= 80 and trust >= 50:
        ending_title = "🏆 [S급] 스마트한 근로권리 협상가"
        ending_desc = "당신은 법적 권리를 완벽히 이해하고, 감정적이 아닌 '증거'와 '예의바른 논리'로 사장님을 설득하는 최고의 리더입니다!"
    elif score >= 70 and trust < 50:
        ending_title = "⚔️ [A급] 강직한 권리 수호자"
        ending_desc = "권리는 잘 챙겼지만, 대화 과정에서 사장님과의 관계가 다소 경색되었습니다. 대화의 기술을 조금 더 연마해보세요!"
    elif trust >= 70 and score < 50:
        ending_title = "😇 [B급] 천사 알바생 (손해 보는 권리)"
        ending_desc = "사장님과의 관계는 아주 좋지만, 본인의 정당한 수당과 휴식 권리를 많이 양보했네요. 나를 지키는 권리 공부가 필요합니다!"
    else:
        ending_title = "🐣 [C급] 초보 알바생"
        ending_desc = "아직 근로 권리와 일터에서의 소통 방식에 익숙하지 않습니다. 퀴즈와 리포트를 통해 다시 학습해볼까요?"

    st.success(f"### 최종 결과: {ending_title}")
    st.write(ending_desc)
    
    st.write("---")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("최종 체력", f"{st.session_state.hp}%")
    col2.metric("최종 수령 임금", f"{st.session_state.money:,}원")
    col3.metric("권리 지수", f"{st.session_state.knowledge}점")
    col4.metric("사장님 신뢰도", f"{st.session_state.trust}점")

    st.write("---")
    st.write("### 📋 나의 시나리오 선택 기록")
    for stage_name, title, desc in st.session_state.history:
        st.write(f"- **[{stage_name}] {title}**: {desc}")

    st.write("---")
    if st.button("🔄 게임 처음부터 다시 도전하기", use_container_width=True):
        reset_game()
        st.rerun()
