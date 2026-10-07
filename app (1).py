updated_app_code = import streamlit as st

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

# 체력 바
st.write("**내 체력 상태**")
st.progress(max(0, min(100, st.session_state.hp)) / 100)

if st.session_state.evidence:
    st.info(f"📁 **내가 확보한 증거 문서:** {', '.join(st.session_state.evidence)}")

st.divider()

# 게임 오버 조건 체크
if st.session_state.trust <= 0:
    st.error("💥 **게임 오버:** 사장님과의 신뢰가 깨져 해고당했습니다! 권리를 요구할 때는 감정적인 태도보다 예의 바르고 논리적인 대화가 필요합니다.")
    if st.button("🔄 다시 도전하기", use_container_width=True):
        reset_game()
        st.rerun()
    st.stop()

if st.session_state.hp <= 0:
    st.error("💥 **게임 오버:** 과로로 병원에 입원했습니다! 체력 관리와 휴게시간 확보는 필수입니다.")
    if st.button("🔄 다시 도전하기", use_container_width=True):
        reset_game()
        st.rerun()
    st.stop()

# --- 3. 스테이지별 시나리오 ---

# [STAGE 1] 계약서 작성과 서류 검토
if st.session_state.stage == 1:
    st.subheader("📍 1단계: 출근 첫날과 근로계약서")
    
    st.info("""
    **🏪 상황:** 편의점 출근 첫날, 사장님이 일부터 배우자고 하십니다.  
    **사장님:** "반가워! 지금 손님 밀리는 시간이니까 우선 일부터 하자. 계약서는 한 달 뒤에 손에 익으면 천천히 쓰면 돼~"
    """)

    st.markdown("### ❓ 나는 어떻게 대처할까요?")
    st.caption("각 보기의 속마음과 대사를 읽고 가장 지혜롭다고 생각하는 행동을 선택해보세요.")

    # A / B 분할 배치 (카드 형태)
    col_a, col_b = st.columns(2)
    
    with col_a:
        with st.container(border=True):
            st.markdown("#### 🅰️ 선택지 A")
            st.write("**💭 속마음:** '첫날부터 법을 딱 짚고 넘어가야 사장님이 날 만만하게 안 보겠지?'")
            st.write('**💬 대사:** *"사장님, 근로기준법상 출근 첫날 계약서를 안 쓰면 불법 아닌가요? 지금 당장 작성해 주세요."*')
            st.write("")
            if st.button("👉 A번 행동 선택하기", key="btn_s1_a", use_container_width=True):
                st.session_state.knowledge += 10
                st.session_state.trust -= 35
                st.session_state.history.append(("1단계", "직설적 법 언급", "첫날부터 강하게 법을 언급하여 사장님과의 신뢰도가 급격히 떨어졌습니다."))
                st.session_state.stage = 2
                st.rerun()

        with st.container(border=True):
            st.markdown("#### 퐶 선택지 C")
            st.write("**💭 속마음:** '바쁜 사장님한테 처음부터 실랑이하기보다는, 일하면서 스스로 증거를 남기는 게 깔끔하겠어.'")
            st.write('**📷 행동:** 계약서는 미루되, 매일 출퇴근 시간표와 사장님 메시지를 휴대폰 사진으로 기록해둔다.')
            st.write("")
            if st.button("👉 C번 행동 선택하기", key="btn_s1_c", use_container_width=True):
                st.session_state.evidence.append("출퇴근 기록 사진")
                st.session_state.knowledge += 10
                st.session_state.trust += 5
                st.session_state.history.append(("1단계", "출퇴근 증거 기록", "계약서는 못 썼지만 추후 입증할 출퇴근 사진 증거를 잘 보관했습니다."))
                st.session_state.stage = 2
                st.rerun()

    with col_b:
        with st.container(border=True):
            st.markdown("#### 🅱️ 선택지 B")
            st.write("**💭 속마음:** '사장님이 기분 나쁘지 않으시게, 작성하면 서로 왜 좋은지 차근차근 설명해보자.'")
            st.write('**💬 대사:** *"사장님, 시급이랑 시간을 문서로 적어두면 서로 오해도 없고 더 마음 편하게 일할 수 있을 것 같아요! 5분만 작성해주실 수 있을까요?"*')
            st.write("")
            if st.button("👉 B번 행동 선택하기", key="btn_s1_b", use_container_width=True):
                st.session_state.knowledge += 20
                st.session_state.trust += 10
                st.session_state.evidence.append("작성된 근로계약서 사본")
                st.session_state.history.append(("1단계", "논리적 정중한 요구", "서로의 이점을 설명하여 근로계약서를 기분 좋게 작성하고 사본을 확보했습니다."))
                st.session_state.stage = 2
                st.rerun()

        with st.container(border=True):
            st.markdown("#### <ctrl42> 선택지 D")
            st.write("**💭 속마음:** '이제 막 들어왔는데 사장님 말을 거스르면 찍힐지도 몰라. 그냥 시키는 대로 하자.'")
            st.write('**💬 대사:** *"네 사장님! 손에 익으면 그때 천천히 써요. 일 바로 시작하겠습니다!"*')
            st.write("")
            if st.button("👉 D번 행동 선택하기", key="btn_s1_d", use_container_width=True):
                st.session_state.trust += 10
                st.session_state.knowledge -= 15
                st.session_state.hp -= 10
                st.session_state.history.append(("1단계", "요구 없이 수락", "계약서 없이 일을 시작하여 불이익 위험에 노출되었습니다."))
                st.session_state.stage = 2
                st.rerun()

# [STAGE 2] 직접 계산하는 주휴수당 미션
elif st.session_state.stage == 2:
    st.subheader("📍 2단계: 일주일 급여 날과 계산 공식")
    
    st.info("""
    **🏪 상황:** 일주일 동안 하루 5시간씩, 총 3일(주 15시간) 성실하게 일했습니다! (최저시급: 10,030원 기준)  
    **사장님:** "이번 주 고생했다! 총 15시간 일했으니 150,450원 계좌로 입금했다~"  
    **내 생각:** '음? 주 15시간 이상 약속된 날에 개근해서 일했으면 **주휴수당(성실 휴식 보너스)**도 함께 받아야 하는 것 같은데...?'
    """)

    st.warning("🧮 **[직접 계산 퀴즈]** 주 15시간 일했을 때 받아야 할 '주휴수당 포함 총 임금'은 얼마일까요?")
    st.caption("💡 힌트: 주휴수당은 1주일 동안 약속된 근무시간을 다 채우면 1일치(5시간) 일값을 추가로 더 지급하는 제도입니다.")

    user_calc = st.radio(
        "내가 직접 계산한 정확한 금액을 선택하세요:",
        [
            "1. 150,450원 (기본 근무 15시간 수당만 받는 것이 맞다)",
            "2. 200,600원 (기본 15시간 수당 + 주휴수당 5시간 = 총 20시간 수당)",
            "3. 250,750원 (기본 15시간 수당 + 주휴수당 10시간 = 총 25시간 수당)"
        ]
    )

    st.write("")
    if st.button("🧮 계산한 결과 제출하고 사장님께 말씀드리기", use_container_width=True):
        if "2. 200,600원" in user_calc:
            if "작성된 근로계약서 사본" in st.session_state.evidence or "출퇴근 기록 사진" in st.session_state.evidence:
                st.success("✅ 정확한 계산입니다! 지난번 챙겨둔 서류/사진 기록을 보여드리니 사장님께서 바로 인정하고 입금해주셨습니다.")
                st.session_state.money += 200600
                st.session_state.knowledge += 25
                st.session_state.trust += 5
                st.session_state.history.append(("2단계", "주휴수당 직접 계산 성공", "정확한 계산 수치와 챙겨둔 증거 문서로 정당한 주휴수당까지 받아냈습니다."))
            else:
                st.warning("⚠️ 계산 수치는 정확했으나 지난번 증거(계약서/기록)를 챙기지 않아 사장님이 '그런 기록 없다'며 일부 금액만 인정해주셨습니다.")
                st.session_state.money += 175000
                st.session_state.knowledge += 15
                st.session_state.trust -= 10
                st.session_state.history.append(("2단계", "증거 부족 난항", "계산은 맞았지만 출퇴근 입증 서류가 부족해 일부 수당만 인정받았습니다."))
            st.session_state.stage = 3
            st.rerun()
        else:
            st.error("❌ 잘못된 계산입니다! 수당 계산을 오인하여 정당한 수당을 챙기지 못하거나 사장님과의 대화에서 신뢰가 떨어졌습니다.")
            st.session_state.money += 150450
            st.session_state.knowledge -= 10
            st.session_state.trust -= 10
            st.session_state.history.append(("2단계", "수당 계산 오류", "주휴수당 계산을 잘못하여 기본 수당만 받았습니다."))
            st.session_state.stage = 3
            st.rerun()

# [STAGE 3] 복합 딜레마 (대타 야간근무 & 휴게시간)
elif st.session_state.stage == 3:
    st.subheader("📍 3단계: 밤 10시 갑작스러운 대타 요청")
    
    st.info("""
    **🏪 상황:** 퇴근 시각인 밤 10시가 다 되었는데, 다음 타임 알바생이 갑자기 못 나온다고 연락이 왔습니다.  
    **사장님:** "아이고 큰일 났다... 미안한데 오늘 밤 10시부터 새벽 2시까지 4시간만 더 대타 뛰어주라! 시급은 평소처럼 똑같이 줄게. 안 그러면 문 닫아야 해..."
    """)

    with st.expander("💡 [법률 지식] 밤 10시 이후 야간근무는 수당이 다를까요?"):
        st.write("""
        - **야간근무 수당 (밤 10시 ~ 다음 날 아침 6시)**: 밤 10시 이후 근무 시 상시 5인 이상 사업장에서는 **시급의 1.5배**를 지급해야 합니다.
        - 또한 청소년/학생의 경우 야간 근무에 본인 동의가 필요하며, 4시간 연속 일하면 30분의 휴식시간이 필수입니다.
        """)

    st.markdown("### ❓ 나는 사장님께 어떻게 대답할까요?")

    col_1, col_2 = st.columns(2)
    
    with col_1:
        with st.container(border=True):
            st.markdown("#### 1️⃣ 첫 번째 대화")
            st.write('**💬 대사:** *"사장님 사정이 정 그러시다면 제가 오늘 밤 10시부터 새벽 2시까지 4시간 더 일할게요! 시급은 평소 받는 기본 시급으로 주셔도 돼요."*')
            st.write("")
            if st.button("👉 1번 대화 선택", key="btn_s3_1", use_container_width=True):
                st.session_state.hp -= 45
                st.session_state.money += 40120
                st.session_state.trust += 15
                st.session_state.knowledge -= 10
                st.session_state.history.append(("3단계", "기본 시급으로 야간대타", "사장님 신뢰는 얻었지만 야간 가산 수당과 휴식 없이 일해 체력이 바닥났습니다."))
                st.session_state.stage = 4
                st.rerun()

        with st.container(border=True):
            st.markdown("#### 3️⃣ 세 번째 대화")
            st.write('**💬 대사:** *"저는 야간 알바 신청한 적 없는데요? 그리고 밤 10시 넘어서 일 시키면서 수당도 안 주는 건 불법이에요! 신고할 수도 있어요!"*')
            st.write("")
            if st.button("👉 3번 대화 선택", key="btn_s3_3", use_container_width=True):
                st.session_state.trust -= 40
                st.session_state.knowledge += 10
                st.session_state.history.append(("3단계", "감정적 거절", "사장님과 날카롭게 대립하여 사장님과의 신뢰도가 급격히 깎였습니다."))
                st.session_state.stage = 4
                st.rerun()

    with col_2:
        with st.container(border=True):
            st.markdown("#### 2️⃣ 두 번째 대화")
            st.write('**💬 대사:** *"사장님, 급한 사정이니 도와드리고 싶어요! 다만 밤 10시 이후 야간근무는 1.5배 수당과 30분 휴식이 필요해요. 이 조건 맞춰주시면 힘내서 일하겠습니다!"*')
            st.write("")
            if st.button("👉 2번 대화 선택", key="btn_s3_2", use_container_width=True):
                st.session_state.hp -= 20
                st.session_state.money += 60180
                st.session_state.knowledge += 20
                st.session_state.trust += 5
                st.session_state.history.append(("3단계", "야간 수당 및 휴게 협상", "야간 수당(1.5배)과 휴식시간 조건으로 지혜롭게 협상하여 근무했습니다."))
                st.session_state.stage = 4
                st.rerun()

        with st.container(border=True):
            st.markdown("#### 4️⃣ 네 번째 대화")
            st.write('**💬 대사:** *"사장님, 도와드리지 못해 죄송해요. 내일 시험이 있어서 오늘은 어렵습니다. 대신 사장님이 매장에 오실 때까지만 30분 더 자리를 지켜드릴게요."*')
            st.write("")
            if st.button("👉 4번 대화 선택", key="btn_s3_4", use_container_width=True):
                st.session_state.hp -= 5
                st.session_state.money += 5015
                st.session_state.trust += 5
                st.session_state.knowledge += 15
                st.session_state.history.append(("3단계", "정중한 거절과 대안 제시", "자신의 사정을 정중히 알리고 현실적인 대안을 제시하여 관계를 지켰습니다."))
                st.session_state.stage = 4
                st.rerun()

# [STAGE 4] 폐기/손실 및 배상 딜레마
elif st.session_state.stage == 4:
    st.subheader("📍 4단계: 매장 상품 손실과 책임 유무")
    
    st.info("""
    **🏪 상황:** 손님이 음료수를 집어 들다가 실수로 바닥에 떨어뜨려 깨졌습니다. 손님은 당황하더니 사과 없이 그냥 나가버렸습니다!  
    **사장님:** "네가 미리 주의를 안 줘서 깨진 거잖아? 음료수값 15,000원은 네 이번 알바비에서 깔 테니까 그렇게 알아!"
    """)

    st.markdown("### ❓ 이 상황에서 나는 사장님께 어떻게 말할까요?")

    col_a, col_b = st.columns(2)
    
    with col_a:
        with st.container(border=True):
            st.markdown("#### 🅰️ 반응 A")
            st.write('**💬 대사:** *"사장님! 제가 깬 것도 아니고 손님이 실수로 떨어뜨리고 도망친 건데 왜 제 알바비에서 까세요? 진짜 너무억울하고 화나요!"*')
            st.write("")
            if st.button("👉 A번 반응 선택", key="btn_s4_a", use_container_width=True):
                st.session_state.trust -= 20
                st.session_state.money -= 15000
                st.session_state.history.append(("4단계", "감정적 항의", "논리적인 설명 없이 감정만 앞세워 임금 차감을 막아내지 못했습니다."))
                st.session_state.stage = 5
                st.rerun()

        with st.container(border=True):
            st.markdown("#### 퐶 반응 C")
            st.write('**💬 대사:** *"제가 손님을 더 잘 주의 깊게 봤어야 했는데 죄송해요... 사장님도 손해가 크시니 음료수값 15,000원은 사장님과 제가 7,500원씩 반반 나눠 부담해요."*')
            st.write("")
            if st.button("👉 C번 반응 선택", key="btn_s4_c", use_container_width=True):
                st.session_state.money -= 7500
                st.session_state.trust += 10
                st.session_state.knowledge -= 5
                st.session_state.history.append(("4단계", "손실 절반 타협", "원만한 해결을 위해 본인이 고의로 만들지 않은 손실 일부를 부담했습니다."))
                st.session_state.stage = 5
                st.rerun()

    with col_b:
        with st.container(border=True):
            st.markdown("#### 🅱️ 반응 B")
            st.write('**💬 대사:** *"사장님, CCTV를 확인해보시면 손님 부주의로 발생한 일입니다. 근로기준법상 알바생의 고의가 아닌 손실을 임금에서 일방적으로 빼는 건 불가능하니 전액 지급해 주셨으면 합니다."*')
            st.write("")
            if st.button("👉 B번 반응 선택", key="btn_s4_b", use_container_width=True):
                st.session_state.knowledge += 25
                st.session_state.trust += 5
                st.session_state.history.append(("4단계", "CCTV 증거 & 법적 논리", "CCTV 확인 요청과 임금 전액 지급 원칙을 설명하여 부당한 차감을 완벽히 막았습니다."))
                st.session_state.stage = 5
                st.rerun()

        with st.container(border=True):
            st.markdown("#### <ctrl42> 반응 D")
            st.write('**💬 대사:** *"제가 일하는 시간에 일어난 일이니 제 불찰입니다. 음료수값 15,000원은 제 이번 달 알바비에서 빼고 입금해 주세요."*')
            st.write("")
            if st.button("👉 D번 반응 선택", key="btn_s4_d", use_container_width=True):
                st.session_state.money -= 15000
                st.session_state.trust += 15
                st.session_state.knowledge -= 20
                st.session_state.history.append(("4단계", "부당 공제 수락", "권리를 포기하고 매장의 손실을 본인의 알바비로 전부 지불했습니다."))
                st.session_state.stage = 5
                st.rerun()

# [STAGE 5] 다차원 평가 및 엔딩
elif st.session_state.stage == 5:
    st.balloons()
    st.subheader("🎉 근무 완료! 나의 근로 권리 평가 리포트")
    
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

with open("app.py", "w", encoding="utf-8") as f:
    f.write(updated_app_code)

print("Updated app.py with card layout and detailed monologues/dialogues successfully.")
