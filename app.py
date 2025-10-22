import streamlit as st
from google import genai
from google.genai import types

client = genai.Client(api_key="AIzaSyCo9MP15NaOiCt3pzz6HviP_pQKf9VjeUc")

model_name = "models/gemini-2.5-flash"

st.set_page_config(page_title="StudyMate RAG Sohbet Robotu", page_icon="🎓", layout="centered")
st.title("🎓 StudyMate RAG Sohbet Robotu")
st.write(f"Kullanılan model: **{model_name}**")
st.write("Gemini 2.5 Flash tabanlı akıllı soru-cevap asistanı!")

user_input = st.text_area("Sorunu buraya yaz 👇", placeholder="Örnek: Yapay zeka nedir?")

if st.button("Cevapla"):
    if not user_input.strip():
        st.warning("Lütfen bir soru yaz 😅")
    else:
        try:
            response = client.models.generate_content(model=model_name, contents=[user_input])
            st.markdown("### 💡 Yanıt:")
            st.write(response.text)
        except Exception as e:
            st.error(f"Bir hata oluştu: {e}")

st.markdown("---")
st.markdown("📘 **StudyMate-RAG**")
