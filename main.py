import streamlit as st

st.set_page_config(page_title="MBTI 독서 추천", page_icon="📚")

st.title("📚 MBTI 기반 청소년 문학 추천 앱")
st.subheader("나의 성격과 어울리는 책과 포켓몬을 찾아보세요! 🎮✨")

st.write(
"""
이 앱은 **MBTI 성격 유형**을 기반으로  
학생들에게 어울리는 **청소년 문학 도서**를 추천합니다.

또한 성격과 비슷한 **포켓몬 캐릭터**를 함께 보여주어  
자신의 성격을 더 재미있게 이해할 수 있도록 도와줍니다.
"""
)

mbti = st.selectbox(
"🧠 MBTI 유형을 선택하세요",
[
"INTJ","INTP","ENTJ","ENTP",
"INFJ","INFP","ENFJ","ENFP",
"ISTJ","ISFJ","ESTJ","ESFJ",
"ISTP","ISFP","ESTP","ESFP"
]
)

data = {

"INTJ":{
"desc":"전략적이고 미래를 계획하는 것을 좋아하는 유형입니다.",
"pokemon":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png",
"pname":"뮤츠",
"book":"데미안 - 헤르만 헤세",
"reason":"자아를 찾고 스스로 성장하는 이야기가 깊은 사고를 좋아하는 INTJ에게 잘 맞습니다.",
"lesson":"스스로의 신념을 가지고 자신의 길을 찾는 것이 중요합니다."
},

"INFP":{
"desc":"감수성이 풍부하고 이상적인 가치를 중요하게 생각합니다.",
"pokemon":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/151.png",
"pname":"뮤",
"book":"어린 왕자 - 생텍쥐페리",
"reason":"순수함과 인간 관계의 의미를 다루는 이야기가 공감 능력이 높은 INFP에게 잘 맞습니다.",
"lesson":"세상을 바라보는 따뜻한 마음이 큰 힘이 됩니다."
},

"ENTJ":{
"desc":"리더십이 강하고 목표를 이루려는 의지가 강한 유형입니다.",
"pokemon":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png",
"pname":"리자몽",
"book":"헝거게임 - 수잔 콜린스",
"reason":"위기 속에서도 리더십과 용기를 보여주는 이야기가 ENTJ의 성향과 잘 맞습니다.",
"lesson":"진정한 리더는 책임감과 용기를 함께 가져야 합니다."
},

"ISFJ":{
"desc":"책임감이 강하고 다른 사람을 배려하는 따뜻한 성격입니다.",
"pokemon":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png",
"pname":"피카츄",
"book":"강아지똥 - 권정생",
"reason":"작은 존재도 세상에 의미가 있다는 메시지가 따뜻한 ISFJ와 잘 어울립니다.",
"lesson":"작은 친절이 세상을 더 좋은 곳으로 만듭니다."
},

"ENTP":{
"desc":"창의적이고 새로운 아이디어를 좋아하는 유형입니다.",
"pokemon":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/94.png",
"pname":"팬텀",
"book":"이상한 나라의 앨리스 - 루이스 캐럴",
"reason":"독특하고 창의적인 세계관이 상상력이 풍부한 ENTP에게 잘 맞습니다.",
"lesson":"새로운 생각은 세상을 바꾸는 시작이 될 수 있습니다."
},

"ISTJ":{
"desc":"성실하고 책임감이 강한 현실적인 성격입니다.",
"pokemon":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/143.png",
"pname":"잠만보",
"book":"우리들의 일그러진 영웅 - 이문열",
"reason":"학교와 사회 속에서 규칙과 정의를 생각하게 하는 이야기입니다.",
"lesson":"원칙과 책임감은 사회를 건강하게 만드는 중요한 가치입니다."
}

}

if st.button("📚 추천 보기"):

    st.balloons()

    if mbti in data:

        st.header(f"🧠 {mbti} 성격 특징")
        st.write(data[mbti]["desc"])

        st.subheader("🎮 당신과 어울리는 포켓몬")

        st.image(data[mbti]["pokemon"], width=200)

        st.write(f"**추천 포켓몬:** {data[mbti]['pname']}")

        st.subheader("📖 추천 도서")
        st.write(f"**{data[mbti]['book']}**")

        st.subheader("⭐ 추천 이유")
        st.info(data[mbti]["reason"])

        st.subheader("🌱 이 책을 통해 배울 수 있는 점")
        st.success(data[mbti]["lesson"])

        st.subheader("💡 독서 후 생각해보기")

        st.write("1️⃣ 이 책의 주인공은 어떤 선택을 했나요?")
        st.write("2️⃣ 내가 주인공이었다면 어떤 선택을 했을까요?")
        st.write("3️⃣ 이 이야기가 나에게 주는 메시지는 무엇일까요?")

    else:

        st.warning("이 MBTI 데이터는 준비 중입니다.")
