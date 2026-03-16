import streamlit as st

st.set_page_config(page_title="MBTI 독서 추천", page_icon="📚")

st.title("📚 MBTI 성격 기반 독서 추천 앱")
st.subheader("성격 · 포켓몬 · 역사 속 지도자 · 책을 함께 알아보세요 🌱")

st.write(
"""
이 앱은 MBTI 성격 유형을 기반으로  
학생들에게 어울리는 **포켓몬 캐릭터**, **역사 속 지도자**,  
그리고 **청소년 문학 도서**를 추천합니다.

이를 통해 성격과 리더십, 독서를 함께 생각해볼 수 있습니다.
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
"desc":"전략적이고 미래를 계획하는 것을 좋아하는 성격입니다.",
"pokemon_img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png",
"pokemon":"뮤츠",
"president":"에이브러햄 링컨",
"pres_img":"https://upload.wikimedia.org/wikipedia/commons/a/a0/Abraham_Lincoln_head_on_shoulders_photo_portrait.jpg",
"pres_reason":"깊이 있는 사고와 신념으로 국가의 방향을 고민했던 지도자로 알려져 있습니다.",
"book":"데미안 - 헤르만 헤세",
"book_reason":"자아를 찾는 철학적인 이야기로 깊이 생각하는 INTJ에게 잘 맞습니다."
},

"ENTJ":{
"desc":"목표 지향적이고 리더십이 강한 성격입니다.",
"pokemon_img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png",
"pokemon":"리자몽",
"president":"프랭클린 루스벨트",
"pres_img":"https://upload.wikimedia.org/wikipedia/commons/4/42/FDR_1944_Color_Portrait.jpg",
"pres_reason":"대공황과 세계대전 시기에 강한 리더십으로 나라를 이끌었습니다.",
"book":"헝거게임",
"book_reason":"어려운 상황 속에서도 리더십과 결단력을 보여주는 이야기입니다."
},

"ENFJ":{
"desc":"사람들을 이끌고 돕는 것을 좋아하는 성격입니다.",
"pokemon_img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png",
"pokemon":"피카츄",
"president":"버락 오바마",
"pres_img":"https://upload.wikimedia.org/wikipedia/commons/8/8d/President_Barack_Obama.jpg",
"pres_reason":"소통과 공감을 바탕으로 많은 사람들을 하나로 모으는 리더십을 보여줬습니다.",
"book":"원더",
"book_reason":"다른 사람을 이해하고 공감하는 마음을 배울 수 있는 이야기입니다."
},

"ESTP":{
"desc":"활동적이고 도전적인 성격입니다.",
"pokemon_img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/94.png",
"pokemon":"팬텀",
"president":"시어도어 루스벨트",
"pres_img":"https://upload.wikimedia.org/wikipedia/commons/1/1e/Theodore_Roosevelt_portrait_1904.jpg",
"pres_reason":"행동력이 강하고 도전을 두려워하지 않는 지도자로 유명합니다.",
"book":"80일간의 세계일주",
"book_reason":"모험과 도전 정신을 보여주는 이야기입니다."
},

"ISTJ":{
"desc":"책임감이 강하고 원칙을 중요하게 생각하는 성격입니다.",
"pokemon_img":"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/143.png",
"pokemon":"잠만보",
"president":"조지 워싱턴",
"pres_img":"https://upload.wikimedia.org/wikipedia/commons/6/6f/George_Washington.jpg",
"pres_reason":"책임감과 원칙을 중요하게 생각했던 지도자로 알려져 있습니다.",
"book":"우리들의 일그러진 영웅",
"book_reason":"학교 사회 속에서 정의와 책임을 생각하게 하는 이야기입니다."
}

}

if st.button("📚 결과 보기"):

    st.balloons()

    if mbti in data:

        st.header("🧠 MBTI 성격 특징")
        st.write(data[mbti]["desc"])

        st.subheader("🎮 어울리는 포켓몬")
        st.image(data[mbti]["pokemon_img"], width=200)
        st.write(data[mbti]["pokemon"])

        st.subheader("🏛️ 역사 속 지도자 예시")
        st.image(data[mbti]["pres_img"], width=200)
        st.write(data[mbti]["president"])
        st.info(data[mbti]["pres_reason"])

        st.subheader("📖 추천 도서")
        st.write(data[mbti]["book"])
        st.success(data[mbti]["book_reason"])

        st.subheader("💡 생각해보기")
        st.write("이 책을 읽고 내가 배울 수 있는 리더십은 무엇일까요?")

    else:
        st.warning("이 MBTI 데이터는 준비 중입니다.")
