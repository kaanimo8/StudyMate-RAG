# 🎓 StudyMate-RAG

**Akbank GAIH GenAI Bootcamp Projesi**  
Gemini 2.5 Flash tabanlı akıllı soru-cevap chatbotu.

---

## 🎯 Amaç
Bu proje, kullanıcıların eğitim ve genel bilgi alanlarında sorduğu sorulara **Google Gemini 2.5 Flash** modeliyle yanıt veren,  
Streamlit tabanlı bir web arayüzü chatbotudur.  
Amacı, **RAG (Retrieval-Augmented Generation)** temelli bir yapay zeka asistanı geliştirerek,  
doğal dilde akıllı yanıtlar üretmektir.

---

## 🧠 Kullanılan Teknolojiler
- 🐍 **Python 3.11**
- 🌐 **Streamlit** (Web arayüzü)
- 🤖 **Google Gemini 2.5 Flash API**
- 📦 **google-generativeai** kütüphanesi
- 🐳 (Opsiyonel) **Docker** — ortam izolasyonu için

---

## ⚙️ Kurulum ve Çalıştırma

1️⃣ Gerekli kütüphaneleri yükle:
```bash
pip install -r requirements.txt
```

2️⃣ Uygulamayı başlat:
```bash
streamlit run app.py
```

3️⃣ Tarayıcıda otomatik olarak şu adres açılır:  
👉 [http://localhost:8501](http://localhost:8501)

---

## 🌐 Web Arayüzü

Uygulama, **Streamlit** tabanlı modern bir web arayüzüne sahiptir.  
Kullanıcı metin kutusuna sorusunu yazar ve “Cevapla” butonuna tıkladığında,  
**Gemini 2.5 Flash** modeli tarafından üretilen yanıt aynı ekranda gösterilir.

### 👇 Örnek Arayüz
**Arayüz yapısı:**
- 🎓 Üstte proje başlığı  
- 💬 Orta kısımda kullanıcı girişi  
- 💡 Alt kısımda modelin cevabı  
- 📘 Alt bölümde proje bilgisi  

---

## 🧩 Çözüm Mimarisi

**Akış Şeması:**
```
Kullanıcı → Streamlit → Google Gemini API → Yanıt → Ekran
```

**Bileşenler:**
1. **Kullanıcı Arayüzü (Streamlit):** Kullanıcı girişini alır.  
2. **Gemini API Katmanı:** Soruyu işleyip modele gönderir.  
3. **Model Katmanı:** Yanıtı üretir.  
4. **Sunum Katmanı:** Yanıtı kullanıcıya gösterir.  

**Avantajlar:**
- ⚡ Gerçek zamanlı etkileşim  
- 🔧 Kolay kurulum  
- 🚀 Hafif ve hızlı çalışma  
- ☁️ Google Cloud uyumlu mimari  

---

## 📊 Veri Seti

Bu proje, **Gemini 2.5 Flash** modelinin kendi dahili bilgi tabanını kullanır.  
Ek bir dış veri seti **kullanılmamıştır.**  
Model, Google’ın geniş bilgi tabanı sayesinde genel bilgiye erişebilir.

---

## 📄 Sonuç

**StudyMate-RAG**, yapay zeka destekli eğitim ortamlarında bilgiye erişimi kolaylaştırır.  
Kullanıcıların doğal dilde sordukları sorulara,  
gerçek zamanlı olarak **doğru ve anlamlı yanıtlar** üretir.


---

## 🚀 Gelecek Geliştirmeler
- 🧠 Kullanıcı geçmişi kaydı (Session Memory)  
- 📚 Kendi PDF veya notlarını yükleyip soru sorma (RAG veri katmanı)  
- 🔊 Sesli giriş/çıkış (Text-to-Speech)  


---

© 2025 StudyMate-RAG – Developed by Rabia Demir-Ahmet Kaan Kavaz
