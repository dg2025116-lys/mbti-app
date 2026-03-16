import streamlit as st

st.set_page_config(page_title="MBTI 독서 추천", page_icon="📚")

st.title("📚 MBTI 기반 독서 & 리더십 추천 앱")
st.subheader("성격 유형을 통해 리더십과 책을 함께 알아보세요 🌱")

st.write("""
이 앱은 MBTI 성격 유형을 기반으로  
학생들에게 어울리는 **역사 속 대통령**과  
**청소년 문학 도서**를 추천합니다.

이를 통해 **성격 · 리더십 · 독서**를 함께 생각해볼 수 있습니다.
""")

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
"desc":"전략적이고 깊이 생각하며 장기적인 계획을 세우는 성격입니다.",
"president":"Abraham Lincoln",
"img":"https://upload.wikimedia.org/wikipedia/commons/a/a0/Abraham_Lincoln_head_on_shoulders_photo_portrait.jpg",
"pres_reason":"깊은 사고와 신념으로 국가의 중요한 문제를 해결하려 노력했던 지도자로 알려져 있습니다.",
"book":"데미안 - 헤르만 헤세",
"book_reason":"자아를 찾고 성장하는 철학적인 이야기로 깊이 생각하는 INTJ에게 잘 맞습니다."
},

"ENTJ":{
"desc":"목표 지향적이며 강한 리더십을 가진 성격입니다.",
"president":"Franklin D. Roosevelt",
"img":"https://upload.wikimedia.org/wikipedia/commons/4/42/FDR_1944_Color_Portrait.jpg",
"pres_reason":"대공황과 세계대전 시기에 강한 결단력으로 나라를 이끌었던 지도자입니다.",
"book":"헝거게임",
"book_reason":"어려운 상황 속에서도 리더십과 결단력을 보여주는 이야기입니다."
},

"ENFJ":{
"desc":"사람들과 협력하고 공감하며 이끄는 성격입니다.",
"president":"Barack Obama",
"img":"https://upload.wikimedia.org/wikipedia/commons/8/8d/President_Barack_Obama.jpg",
"pres_reason":"소통과 공감을 바탕으로 많은 사람들을 하나로 모으는 리더십을 보여준 지도자입니다.",
"book":"원더",
"book_reason":"다른 사람을 이해하고 공감하는 마음을 배울 수 있는 이야기입니다."
},

"ESTP":{
"desc":"활동적이고 도전적인 성격입니다.",
"president":"Theodore Roosevelt",
"img":"https://upload.wikimedia.org/wikipedia/commons/1/1e/Theodore_Roosevelt_portrait_1904.jpg",
"pres_reason":"강한 행동력과 도전 정신으로 유명한 지도자입니다.",
"book":"80일간의 세계일주",
"book_reason":"모험과 도전 정신을 보여주는 이야기입니다."
},

"ISTJ":{
"desc":"책임감이 강하고 원칙을 중요하게 생각하는 성격입니다.",
"president":"George Washington",
"img":"https://upload.wikimedia.org/wikipedia/commons/6/6f/George_Washington.jpg",
"pres_reason":"책임감과 원칙을 중요하게 생각했던 지도자로 알려져 있습니다.",
"book":"우리들의 일그러진 영웅",
"book_reason":"학교와 사회 속에서 정의와 책임을 생각하게 하는 이야기입니다."
}

}

if st.button("📚 결과 보기"):

    st.balloons()

    if mbti in data:

        st.header("🧠 MBTI 성격 특징")
        st.write(data[mbti]["desc"])

        st.subheader("🏛️ 역사 속 대통령 예시")
        st.image(data[mbti]["img"], width=220)
        st.write(data[mbti]["president"])

        st.info(data[mbti]["pres_reason"])

        st.subheader("📖 추천 도서")
        st.write(data[mbti]["book"])

        st.success(data[mbti]["book_reason"])

        st.subheader("💡 독서 후 생각해보기")

        st.write("1️⃣ 이 책의 주인공은 어떤 선택을 했나요?")
        st.write("2️⃣ 내가 주인공이었다면 어떻게 행동했을까요?")
        st.write("3️⃣ 이 이야기가 나에게 주는 메시지는 무엇인가요?")

    else:
        st.warning("이 MBTI 유형의 데이터는 아직 준비 중입니다.")
