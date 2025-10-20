# Akıllı Yatırım Asistanı (RAG Chatbot)

## Projenin Amacı 
Akıllı Yatırım Asistanı görevi görecek, RAG (Retrieval Augmented Generation) temelli bir Chatbot geliştirmektir. Bu asistan, kullanıcıların yatırım ve finansal konular hakkındaki sorularını, belirlenen veri seti üzerinden doğru ve dengeli bilgilerle yanıtlayarak uzun vadede sürdürülebilir bir strateji oluşturmalarına yardımcı olmayı hedeflemektedir.

## [cite_start] Veri Seti Hakkında Bilgi 
Bu projede kullanılan veri seti, yatırım ve finans alanlarına yönelik olarak tarafımdan oluşturulmuş, çeşitli yatırım araçları hakkında bilgiler içeren tek bir metin dosyasıdır (yatirim_verileri.txt).

Veri seti, RAG Chatbot'un bilgi tabanını oluşturmaktadır ve aşağıdaki temel yatırım araçlarını ve kavramlarını kapsamaktadır:

* Altın Yatırımı
* Hisse Senedi Yatırımı
* Döviz Yatırımı
* Yatırım Fonları
* Tahvil & Eurobond
* Risk Yönetimi ve Portföy Dağılımı
* Kripto Para Yatırımı

## Kullanılan Yöntemler (Çözüm Mimarisi) 

Bu proje, bir RAG hattı (pipeline) kurmak için LangChain'in en güncel **Runnable** arayüzünü kullanmıştır.

| Bileşen | Seçilen Teknoloji | Rolü |
| :--- | :--- | :--- |
| **Büyük Dil Modeli (LLM)** | Google **Gemini 2.5 Flash API** | Kullanıcı sorgularına cevap oluşturmak ve bağlamı sentezlemek. |
| **Embedding Modeli** | **Google'ın Metin Embedding Modeli** (`text-embedding-004`) | Veri setindeki metin parçalarını sayısal vektörlere dönüştürmek. |
| **Vektör Veritabanı (Vector DB)** | **ChromaDB** | Oluşturulan vektörleri depolamak ve sorgu anında en alakalı 3 metin parçasını çekmek (**k=3**). |
| **RAG Çatısı (Framework)** | **LangChain** (Runnable Interface) | Veri işleme, Retriever ve LLM'i birleştirerek dinamik bir sorgu zinciri oluşturmak. |
| **Web Arayüzü** | **Streamlit** | Chatbot'u etkileşimli ve kullanıcı dostu bir arayüzle sunmak. |

## Elde Edilen Sonuçlar [cite: 88]
*(Projenin son test aşamaları tamamlandıktan sonra, chatbot'un yetenekleri, başarı oranı ve genel performans özeti bu bölüme eklenecektir.)*

## Uygulama Web Linki [cite: 89]
*(Bu bölüme, Streamlit Community Cloud veya benzeri bir platforma yapılan **dağıtım (deployment) sonrası elde edilen herkese açık link** eklenecektir.)*

---

### Proje Dosyaları

* **`yatirim_asistani.ipynb`**: RAG hattının kurulumu, testi ve adım adım teknik anlatımın yer aldığı geliştirme notebook'udur.
* **`chatbot_app.py`**: Streamlit tabanlı web arayüzü uygulamasını içeren ana Python dosyasıdır.
* **`requirements.txt`**: Projenin çalışması için gerekli tüm Python bağımlılıklarını içerir.
* **`KILAVUZ.md`**: Projenin Çalışma Kılavuzunu (venv, kurulum) ve Product Kılavuzunu (test senaryoları) içerir.
