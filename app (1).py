import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="편의점 노사 상생 시뮬레이션: 권리와 경영의 지혜",
    page_icon="🏪",
    layout="centered"
)

# --- 1. 세션 상태(Session State) 초기화 ---
if "role" not in st.session_state:
    st.session_state.role = None  # 'worker' 또는 'boss'
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
    st.session_state.evidence = []
if "history" not in st.session_state:
    st.session_state.history = []

def reset_game():
    st.session_state.role = None
    st.session_state.stage = 1
    st.session_state.hp = 100
    st.session_state.money = 0
    st.session_state.knowledge = 50
    st.session_state.trust = 50
    st.session_state.evidence = []
    st.session_state.history = []

# --- 2. 역할 선택 화면 ---
if st.session_state.role is None:
    st.title("🏪 편의점 노사 상생 협상 시뮬레이션")
    st.caption("근무자와 점주님의 서로 다른 입장과 노동 관계법을 배우는 대화형 시뮬레이션")
    st.write("---")
    
    st.subheader("🎭 플레이할 시점을 선택해 주세요")
    
    col_w, col_b = st.columns(2)
    
    with col_w:
        st.markdown("### 🧑‍💼 알바생 모드")
        st.write("""
        - **목표:** 정당한 수당과 권리를 지혜로운 대화와 소명 자료로 챙기기
        - **주요 난관:** 주휴수당 산정, 야간 근무 가산, 제품 손실 소명, 감정노동 대응
        """)
        if st.button("알바생으로 시작하기", use_container_width=True, key="start_worker"):
            st.session_state.role = "worker"
            st.session_state.money = 0
            st.rerun()

    with col_b:
        st.markdown("### 👨‍💼 점주님(사장님) 모드")
        st.write("""
        - **목표:** 인건비 및 매장 자금을 효율적으로 관리하며 법적 의무 준수하기
        - **주요 난관:** 계약서 교부, 주 15시간 미만 쪼개기 계약 고민, 매장 손실 처리, 근무자 보호
        """)
        if st.button("점주님으로 시작하기", use_container_width=True, key="start_boss"):
            st.session_state.role = "boss"
            st.session_state.money = 500000  # 매장 운용 예비 자금
            st.rerun()

    st.stop()

# --- 3. 게임 대시보드 (역할에 따른 지표 변화) ---
st.title("🏪 편의점 노사 상생 시뮬레이션")

if st.session_state.role == "worker":
    st.caption("🧑‍💼 [알바생 모드] 정당한 권리와 예의 바른 협상으로 상생하기")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("🔋 내 컨디션", f"{st.session_state.hp}%")
    col2.metric("🪙 누적 지급 보수", f"{st.session_state.money:,}원")
    col3.metric("🛡️ 권리 지수", f"{st.session_state.knowledge}점")
    col4.metric("🤝 점주님 신뢰", f"{st.session_state.trust}점")
    st.write("**내 컨디션 상태**")
    st.progress(max(0, min(100, st.session_state.hp)) / 100)

else:  # boss mode
    st.caption("👨‍💼 [점주님 모드] 준법 경영과 매장 자금 관리로 안심 매장 만들기")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("🏬 매장 피로도", f"{100 - st.session_state.hp}%")
    col2.metric("💰 매장 운용 자금", f"{st.session_state.money:,}원")
    col3.metric("📜 준법 지수", f"{st.session_state.knowledge}점")
    col4.metric("🤝 근무자 신뢰", f"{st.session_state.trust}점")
    st.write("**매장 운영 안정도**")
    st.progress(max(0, min(100, st.session_state.hp)) / 100)

if st.session_state.evidence:
    st.info(f"📁 **보관 중인 제출 서류/기록:** {', '.join(st.session_state.evidence)}")

st.divider()

# --- 4. 게임 오버 조건 체크 ---
if st.session_state.trust <= 0:
    st.error("💥 **시뮬레이션 종료:** 신뢰 관계가 상실되어 더 이상 원만한 매장 근무 및 운영을 지속하기 어려워졌습니다.")
    if st.button("🔄 처음으로 돌아가기"):
        reset_game()
        st.rerun()
    st.stop()

if st.session_state.hp <= 0:
    st.error("💥 **시뮬레이션 종료:** 과도한 피로 누적으로 인해 근무 수행 및 매장 운영이 불가능해졌습니다.")
    if st.button("🔄 처음으로 돌아가기"):
        reset_game()
        st.rerun()
    st.stop()


# ==============================================================================
# --- 5-A. 알바생 모드 시나리오 ---
# ==============================================================================
if st.session_state.role == "worker":

    # [STAGE 1] 서면 계약 체결
    if st.session_state.stage == 1:
        st.subheader("📍 1단계: 근로계약서 교부 요청")
        st.info("""
        **🏪 상황:** 출근 첫날, 점주님이 매장 정리부터 안내하십니다.  
        **점주님:** "요즘 매장이 많이 바쁘니 일부터 우선 배우자. 서면 계약서는 업무에 적응하고 난 뒤 천천히 쓰자꾸나."
        """)

        choice = st.radio(
            "어떻게 응대하는 것이 바람직할까요?",
            [
                "1. '점주님, 계약서를 서명해서 1부씩 보관하면 근무 조건도 명확해지고 저도 더 책임감 있게 일할 수 있을 것 같아요!'",
                "2. '점주님, 첫날 서면 계약을 미루는 것은 규정에 어긋납니다. 지금 즉시 작성해 주셔야 합니다.'",
                "3. (속마음: '직접 말씀드리기는 부담스러우니, 우선 오늘 출퇴근 기록 메세지만 사진으로 남겨두어야겠다.')",
                "4. '네, 점주님! 안내해 주신 대로 일부터 먼저 배우겠습니다.'"
            ]
        )

        if st.button("선택 결정하기", use_container_width=True, key="w_btn_1"):
            if choice.startswith("1."):
                st.session_state.knowledge += 20
                st.session_state.trust += 10
                st.session_state.evidence.append("작성된 근로계약서 사본")
                st.session_state.history.append(("1단계", "지혜로운 서류 교부 요청", "상호 유익함을 설명하여 계약서를 교부받았습니다."))
            elif choice.startswith("2."):
                st.session_state.knowledge += 10
                st.session_state.trust -= 30
                st.session_state.history.append(("1단계", "경직된 규정 지적", "원칙을 강조했으나 점주님과의 관계가 다소 경색되었습니다."))
            elif choice.startswith("3."):
                st.session_state.evidence.append("출퇴근 기록 사진")
                st.session_state.knowledge += 5
                st.session_state.trust += 5
                st.session_state.history.append(("1단계", "기록 보관", "직접적 요청은 미루었으나 정황 사진을 보관했습니다."))
            elif choice.startswith("4."):
                st.session_state.trust += 10
                st.session_state.knowledge -= 15
                st.session_state.hp -= 10
                st.session_state.history.append(("1단계", "기준 미확립", "서면 계약 없이 일을 시작하여 조건 명확화 기회를 놓쳤습니다."))
            
            st.session_state.stage = 2
            st.rerun()

    # [STAGE 2] 주휴수당 산정
    elif st.session_state.stage == 2:
        st.subheader("📍 2단계: 주휴수당 산정 미션")
        st.info("""
        **🏪 상황:** 일주일 동안 하루 5시간씩 3일(총 주 15시간) 성실하게 만근했습니다! (최저시급: 10,030원)  
        **점주님:** "고생 많았다! 이번 주 15시간 일한 분량으로 150,450원을 입금했단다."
        """)

        user_calc = st.radio(
            "주 15시간 이상 만근 시 지급받아야 할 올바른 총 금액은 얼마일까요?",
            [
                "1. 150,450원 (기본 근무 15시간 수당만 산정)",
                "2. 200,600원 (기본 15시간 + 주휴 산정 5시간 = 총 20시간 수당)",
                "3. 250,750원 (기본 15시간 + 주휴 산정 10시간 = 총 25시간 수당)"
            ]
        )

        if st.button("산정 결과 제출하기", use_container_width=True, key="w_btn_2"):
            if "2. 200,600원" in user_calc:
                if "작성된 근로계약서 사본" in st.session_state.evidence or "출퇴근 기록 사진" in st.session_state.evidence:
                    st.success("✅ 정확한 산정입니다! 작성한 서류 및 사진을 함께 확인시켜 드리니 점주님께서 기꺼이 수용하셨습니다.")
                    st.session_state.money += 200600
                    st.session_state.knowledge += 25
                    st.session_state.trust += 5
                    st.session_state.history.append(("2단계", "주휴수당 산정 성공", "정확한 계산과 정황 서류로 정당한 수당을 수령했습니다."))
                else:
                    st.warning("⚠️ 계산은 타당하나 서명 서류가 부족하여 일부 합의된 조정 금액만 산정되었습니다.")
                    st.session_state.money += 175000
                    st.session_state.knowledge += 15
                    st.session_state.trust -= 10
                    st.session_state.history.append(("2단계", "증빙 부족으로 인한 조정", "계산은 맞았으나 자료 부족으로 조정 수령했습니다."))
            else:
                st.error("❌ 산정이 정확하지 않아 기본 수당만 적용되었습니다.")
                st.session_state.money += 150450
                st.session_state.knowledge -= 10
                st.session_state.trust -= 10
                st.session_state.history.append(("2단계", "산정 오류", "수당 산정 착오로 권리를 확인받지 못했습니다."))
            
            st.session_state.stage = 3
            st.rerun()

    # [STAGE 3] 상품 파손 및 손실 공제
    elif st.session_state.stage == 3:
        st.subheader("📍 3단계: 매장 상품 손실 소명")
        st.info("""
        **🏪 상황:** 혼잡한 시간에 손님이 상품을 꺼내다 바닥에 떨어뜨려 깨졌습니다.  
        **점주님:** "미리 주의를 주지 못했으니, 파손 금액 15,000원을 이번 보수에서 공제하겠다."
        """)

        choice = st.radio(
            "어떤 대사와 행동으로 소명하시겠습니까?",
            [
                "1. '점주님, 매장 녹화 영상을 확인해 보시면 이용객 과실임을 확인하실 수 있습니다. 임금 전액 지급 원칙에 따라 일방 공제는 어려움을 말씀드립니다.'",
                "2. '제가 깬 것도 아닌데 저한테 왜 그러세요! 절대 제 돈으로 차감 못 합니다!'",
                "3. '제 주의도 부족했으니 7,500원씩 나누어 부담하겠습니다.'",
                "4. '죄송합니다, 점주님... 제 보수에서 15,000원 빼주세요.'"
            ]
        )

        if st.button("선택 결정하기", use_container_width=True, key="w_btn_3"):
            if choice.startswith("1."):
                st.session_state.knowledge += 25
                st.session_state.trust += 5
                st.session_state.history.append(("3단계", "녹화 영상 확증 및 전액 지급 설명", "객관적 녹화 자료 확인 요청으로 부당한 공제를 예방했습니다."))
            elif choice.startswith("2."):
                st.session_state.trust -= 25
                st.session_state.money -= 15000
                st.session_state.history.append(("3단계", "감정적 언쟁", "논리적 소명 없이 감정이 앞서 차감을 막지 못했습니다."))
            elif choice.startswith("3."):
                st.session_state.money -= 7500
                st.session_state.trust += 10
                st.session_state.history.append(("3단계", "절충안 분담", "원만한 해결을 위해 손실 일부를 부담했습니다."))
            elif choice.startswith("4."):
                st.session_state.money -= 15000
                st.session_state.trust += 15
                st.session_state.knowledge -= 20
                st.session_state.history.append(("4단계", "부담 수용", "원칙 확인 없이 손실 전액을 스스로 부담했습니다."))

            st.session_state.stage = 4
            st.rerun()

    # [STAGE 4] 감정노동 및 손님 폭언 대처
    elif st.session_state.stage == 4:
        st.subheader("📍 4단계: 감정노동 보호 및 대응")
        st.info("""
        **🏪 상황:** 한 손님이 반말을 하며 매장 내에서 모욕적인 언사를 퍼붓고 있습니다!  
        **손님:** "서비스가 왜 이 모양이야! 당장 사장 불러오고 계산 다시 해!"
        """)

        with st.expander("💡 [노동 법률 참고] 감정노동자 보호 규정"):
            st.write("""
            - **산업안전보건법 제41조**: 고객의 폭언 등으로 인한 건강장해 예방을 위해 점주는 근무자의 휴식 요구, 업무 일시 중단, 치료 지원 등의 보호 조치를 이행할 의무가 있습니다.
            """)

        choice = st.radio(
            "어떻게 대처하는 것이 안전하고 정당할까요?",
            [
                "1. '손님, 반말과 무례한 언사는 삼가 주시기 바랍니다. 지속되시면 매장 매뉴얼에 따라 점주님 호출 및 보호 조치를 요청하겠습니다.'",
                "2. '너나 잘해! 매장에서 행패 부리지 말고 당장 나가!'",
                "3. 무서워서 아무 말도 못 하고 눈물만 흘리며 무조건 죄송하다고 사과한다.",
                "4. 즉시 점주님께 상황을 신속히 알리고 매뉴얼에 따라 잠시 휴게 공간으로 피신하여 보호 조치를 요청한다."
            ]
        )

        if st.button("선택 결정하기", use_container_width=True, key="w_btn_4"):
            if choice.startswith("1."):
                st.session_state.knowledge += 20
                st.session_state.trust += 10
                st.session_state.hp -= 10
                st.session_state.history.append(("4단계", "차분한 매뉴얼 대처", "단호하고 예의 바르게 대응하여 추가 마찰을 예방했습니다."))
            elif choice.startswith("2."):
                st.session_state.trust -= 30
                st.session_state.hp -= 30
                st.session_state.history.append(("4단계", "맞대응 언쟁", "손님과의 맞대응으로 매장 혼란이 커지고 마음의 상처를 입었습니다."))
            elif choice.startswith("3."):
                st.session_state.hp -= 40
                st.session_state.trust += 5
                st.session_state.history.append(("4단계", "무조건 수용", "감정적 상처가 커지고 정당한 보호 조치를 받지 못했습니다."))
            elif choice.startswith("4."):
                st.session_state.knowledge += 25
                st.session_state.trust += 15
                st.session_state.hp -= 5
                st.session_state.history.append(("4단계", "점주 보고 및 피신", "보호 매뉴얼을 준수하여 정당한 보호 조치를 이끌어냈습니다."))

            st.session_state.stage = 5
            st.rerun()

    # [STAGE 5] 알바생 엔딩 리포트
    elif st.session_state.stage == 5:
        st.balloons()
        st.subheader("🎉 [알바생 모드] 최종 시뮬레이션 평가")
        score = st.session_state.knowledge
        trust = st.session_state.trust

        if score >= 80 and trust >= 50:
            ending_title = "🏆 [S급] 스마트한 상생 협상가"
            ending_desc = "규정을 명확히 알고, 감정적이 아닌 논리와 정황 서류로 점주님과의 신뢰를 지켜낸 최고의 협상 리더입니다!"
        elif score >= 70 and trust < 50:
            ending_title = "⚔️ [A급] 소신 있는 원칙 준수자"
            ending_desc = "정당한 권리는 확실히 지켰으나, 소통 과정에서 신뢰 유지를 강화하면 더 훌륭해질 수 있습니다!"
        elif trust >= 70 and score < 50:
            ending_title = "😇 [B급] 배려형 알바생 (권리 보완 필요)"
            ending_desc = "점주님과의 관계는 훌륭하지만 정당한 수당과 휴식을 양보하셨네요. 법적 기준을 좀 더 챙겨보세요!"
        else:
            ending_title = "🐣 [C급] 초보 근무자"
            ending_desc = "근무 권리와 정당한 대화 방식에 대한 학습이 필요합니다."

        st.success(f"### 최종 판정: {ending_title}")
        st.write(ending_desc)
        
        st.write("---")
        st.write("### 📋 결정 이력 리포트")
        for stage_name, title, desc in st.session_state.history:
            st.write(f"- **[{stage_name}] {title}**: {desc}")

        st.write("---")
        if st.button("🔄 역할 선택 화면으로 돌아가기", use_container_width=True):
            reset_game()
            st.rerun()


# ==============================================================================
# --- 5-B. 점주님(사장님) 모드 시나리오 ---
# ==============================================================================
else:

    # [STAGE 1] 첫 채용과 계약서 서면 작성
    if st.session_state.stage == 1:
        st.subheader("📍 1단계: 신규 근무자 채용과 서면 계약")
        st.info("""
        **🏪 상황:** 신규 알바생이 첫 출근했습니다. 손님이 몰리는 바쁜 시간대입니다.  
        **내 마음:** '매장이 정신없이 바쁜데... 계약서는 나중에 수습기간 지난 다음에 써도 되지 않을까?'
        """)

        choice = st.radio(
            "점주로서 어떤 결정을 내리시겠습니까?",
            [
                "1. '바쁘더라도 근로조건(시급, 근무시간, 휴게시간)을 서면으로 명확히 작성하고 사본 1부를 즉시 교부한다.'",
                "2. '일단 일부터 배우게 하고, 한 달 뒤 일에 적응되면 천천히 써야겠다.'",
                "3. '요즘 서면 작성은 번거로우니 대충 모바일 메세지로 시급만 찍어 보내준다.'"
            ]
        )

        if st.button("경영 결정 내리기", use_container_width=True, key="b_btn_1"):
            if choice.startswith("1."):
                st.session_state.knowledge += 25
                st.session_state.trust += 20
                st.session_state.history.append(("1단계", "서면 계약 즉시 교부", "법적 분쟁 위험을 완전히 제거하고 근무자의 신뢰를 얻었습니다."))
            elif choice.startswith("2."):
                st.session_state.knowledge -= 15
                st.session_state.trust -= 10
                st.session_state.hp -= 15
                st.session_state.history.append(("1단계", "계약서 작성 미루기", "서면 계약 미교부 위험에 노출되고 불확실성이 증가했습니다."))
            elif choice.startswith("3."):
                st.session_state.knowledge -= 20
                st.session_state.trust -= 20
                st.session_state.history.append(("1단계", "구두/약식 체결", "명확한 입증 서류가 부족하여 분쟁 여지를 남겼습니다."))

            st.session_state.stage = 2
            st.rerun()

    # [STAGE 2] 인건비 절감과 쪼개기 계약 딜레마
    elif st.session_state.stage == 2:
        st.subheader("📍 2단계: 인건비 계획과 주휴수당 고민")
        st.info("""
        **🏪 상황:** 매장 임대료와 재료비가 올라 이번 달 수익이 줄었습니다.  
        **고민:** '주 15시간 이상 일시키면 주휴수당(5시간분 추가)을 줘야 하는데... 근무시간을 주 14시간 이하로 쪼개서 알바생 여럿을 쓸까?'
        """)

        with st.expander("💡 [경영 리포트] 주 15시간 미만(쪼개기) 스케줄링의 장단점"):
            st.write("""
            - **장점**: 단기 인건비 지출 절감 (주휴수당 미발생)
            - **단점**: 근무자 교체 주기가 빨라짐, 잦은 교육 피로도 증가, 알바생의 매장 숙련도 및 책임감 저하
            """)

        choice = st.radio(
            "어떤 근무 스케줄링 전략을 선택하시겠습니까?",
            [
                "1. 주 15시간 이상 근무를 보장하고 정당한 주휴수당을 반영하여, 숙련된 근무자의 장기 근무를 유도한다.",
                "2. 인건비 지출을 최우선으로 줄이기 위해 모든 알바생을 주 14시간 이하로 쪼개서 채용한다.",
                "3. 주 15시간 이상 일을 시키고, 주휴수당은 슬그머니 빼고 기본 시급만 입금해 본다."
            ]
        )

        if st.button("경영 결정 내리기", use_container_width=True, key="b_btn_2"):
            if choice.startswith("1."):
                st.session_state.money -= 50000  # 정당 수당 지출
                st.session_state.knowledge += 20
                st.session_state.trust += 20
                st.session_state.hp += 10  # 숙련자로 인해 피로 감소
                st.session_state.history.append(("2단계", "정당 수당 보장 및 숙련 관리", "상생 경영으로 매장 안정성과 알바생 충성도를 확보했습니다."))
            elif choice.startswith("2."):
                st.session_state.knowledge += 5
                st.session_state.trust -= 15
                st.session_state.hp -= 25  # 잦은 채용과 교육으로 피로 누적
                st.session_state.history.append(("2단계", "쪼개기 채용 실행", "단기 인건비는 줄였으나 근무자 피로와 잦은 교체로 매장 관리가 힘들어졌습니다."))
            elif choice.startswith("3."):
                st.session_state.knowledge -= 30
                st.session_state.trust -= 40
                st.session_state.history.append(("2단계", "수당 미지급", "근무자의 반발로 신뢰도가 급격히 하락했습니다."))

            st.session_state.stage = 3
            st.rerun()

    # [STAGE 3] 상품 파손 손실 처리
    elif st.session_state.stage == 3:
        st.subheader("📍 3단계: 매장 손실 발생 시 책임 처리")
        st.info("""
        **🏪 상황:** 매장에서 15,000원 상당의 와인이 깨져 파손되었습니다. 근무자가 손님이 떨어뜨렸다고 소명합니다.  
        **고민:** '이번 달 매장 손실도 많은데, 알바비에서 차감하는 게 맞을까?'
        """)

        choice = st.radio(
            "어떻게 매장 손실을 처리하시겠습니까?",
            [
                "1. 매장 녹화 영상을 함께 확인한 후 이용객 과실임이 입증되면 매장 로스(손실) 비용으로 처리하고 근무자를 안심시킨다.",
                "2. '매장 관리 소홀도 책임이야'라며 알바생 임금에서 15,000원을 일방적으로 공제한다.",
                "3. 근무자와 대화하여 안타까운 상황임을 나누고 7,500원씩 절반씩 손실을 부담하기로 합의한다."
            ]
        )

        if st.button("경영 결정 내리기", use_container_width=True, key="b_btn_3"):
            if choice.startswith("1."):
                st.session_state.money -= 15000  # 매장 로스 비용 처리
                st.session_state.knowledge += 20
                st.session_state.trust += 15
                st.session_state.history.append(("3단계", "매장 손실 자발 수용", "임금 전액 지급 원칙을 준수하고 책임감 있는 점주 이미지를 구축했습니다."))
            elif choice.startswith("2."):
                st.session_state.knowledge -= 25
                st.session_state.trust -= 35
                st.session_state.history.append(("3단계", "일방 임금 공제", "임금 전액 지급 규정을 위반하여 분쟁 가능성이 발생했습니다."))
            elif choice.startswith("3."):
                st.session_state.money -= 7500
                st.session_state.trust += 5
                st.session_state.history.append(("3단계", "절반 분담 합의", "상호 협의를 통해 손실을 나누어 부담했습니다."))

            st.session_state.stage = 4
            st.rerun()

    # [STAGE 4] 근무자 보호 및 감정노동 대응
    elif st.session_state.stage == 4:
        st.subheader("📍 4단계: 폭언 손님 발생과 근무자 보호")
        st.info("""
        **🏪 상황:** 매장에서 악성 손님이 알바생에게 폭언과 모욕을 주어 알바생이 겁에 질려 있습니다.  
        **고민:** '손님도 중요하지만, 알바생이 너무 힘들어하는데 어떻게 해야 하지?'
        """)

        choice = st.radio(
            "점주로서 어떤 보호 조치를 취하시겠습니까?",
            [
                "1. 즉시 알바생을 휴게 공간으로 피신시키고, 본인이 직접 응대하여 폭언 손님에게 자제를 요청하거나 매뉴얼대로 조치한다.",
                "2. '손님은 왕이야. 네가 참고 사과해서 빨리 손님 보내라'라며 알바생에게 참으라고 강요한다.",
                "3. 상황을 모른 척하며 알아서 해결될 때까지 카운터 뒤에 서 있는다."
            ]
        )

        if st.button("경영 결정 내리기", use_container_width=True, key="b_btn_4"):
            if choice.startswith("1."):
                st.session_state.knowledge += 25
                st.session_state.trust += 25
                st.session_state.hp += 10
                st.session_state.history.append(("4단계", "근무자 보호 조치 이행", "산업안전보건법상 감정노동자 보호 조치를 완벽히 이행하여 명품 점주가 되었습니다."))
            elif choice.startswith("2."):
                st.session_state.knowledge -= 20
                st.session_state.trust -= 40
                st.session_state.history.append(("4단계", "보호 의무 방치", "근무자의 정신적 상처를 방치하여 신뢰가 무너졌습니다."))
            elif choice.startswith("3."):
                st.session_state.trust -= 20
                st.session_state.history.append(("4단계", "소극적 방관", "적절한 분쟁 해결 태도를 보이지 못했습니다."))

            st.session_state.stage = 5
            st.rerun()

    # [STAGE 5] 점주님 엔딩 리포트
    elif st.session_state.stage == 5:
        st.balloons()
        st.subheader("🎉 [점주님 모드] 최종 경영 리포트")
        score = st.session_state.knowledge
        trust = st.session_state.trust

        if score >= 80 and trust >= 50:
            ending_title = "🏆 [S급] 모범 준법 경영인"
            ending_desc = "노동 법률을 철저히 준수하면서도 근무자를 따뜻하게 보호하여 매장의 안정과 높은 신뢰를 동시에 이뤄낸 최고 리더입니다!"
        elif score >= 60 and trust >= 50:
            ending_title = "🤝 [A급] 원만한 상생 점주님"
            ending_desc = "근무자와 적극적으로 소통하며 매장을 안정적으로 운영하고 계십니다!"
        elif trust < 50:
            ending_title = "⚠️ [B급] 경악 모드 경영 (분쟁 위험)"
            ending_desc = "근무자와의 신뢰가 하락했습니다. 근로계약서 교부와 임금 전액 지급 원칙을 다시 한번 점검해 보세요!"
        else:
            ending_title = "🐣 [C급] 초보 자영업자"
            ending_desc = "매장 운영에 법적 기준과 소통 기술을 도입하면 훨씬 편안한 경영이 가능해집니다."

        st.success(f"### 최종 종합 평가: {ending_title}")
        st.write(ending_desc)
        
        st.write("---")
        st.write("### 📋 경영 결정 이력 리포트")
        for stage_name, title, desc in st.session_state.history:
            st.write(f"- **[{stage_name}] {title}**: {desc}")

        st.write("---")
        if st.button("🔄 역할 선택 화면으로 돌아가기", use_container_width=True):
            reset_game()
            st.rerun()
