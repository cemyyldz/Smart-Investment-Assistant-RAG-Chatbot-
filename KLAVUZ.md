1. Paket Bağımlılıklarının Kurulumu
Projenin tüm kütüphanelere erişebilmesi için requirements.txt dosyasındaki paketleri kurun. (İdeal olarak, bu komutu izole bir sanal ortamda çalıştırmanız önerilir, ancak zorunlu değildir.)

# Gerekli tüm kütüphaneleri kurun
pip install -r requirements.txt

2. API Anahtarının Ayarlanması
Proje, Google Gemini API'yi (LLM ve Embedding için) kullanmaktadır. Anahtarınızı, proje kök dizininde bulunan .env dosyasına kaydederek güvenli bir şekilde ayarlayın.

2.1 .env Dosyası Oluşturun
Proje kök dizininde .env adında bir dosya oluşturun ve içine API anahtarınızı aşağıdaki formatta ekleyin:

# .env dosyasının içeriği:
GEMINI_API_KEY="SENIN_GOOGLE_GEMINI_API_ANAHTARIN_BURAYA"
2.2 Anahtar Erişimi
Google Gemini API Anahtarınızı Google AI Studio üzerinden alabilirsiniz.

3. Vektör Veritabanının Hazırlanması (Hafıza Oluşturma)
Web arayüzünü çalıştırmadan önce, RAG modelinin bilgi çekebilmesi için ChromaDB veritabanı (chroma_db_yatirim klasörü) oluşturulmalıdır.

yatirim_asistani.ipynb Notebook dosyasını açın (VS Code veya Jupyter).

Notebook'taki Hücre 1'den Hücre 4'e kadar olan adımları sırasıyla çalıştırın.

Hücre 1:Bağımlılıkları yükler.

Hücre 2: API anahtarını yükler.

Hücre 3: Veri setini okur ve parçalara böler.

Hücre 4: Parçaları vektörleştirir ve ChromaDB'yi oluşturur.

4. Uygulamayı Çalıştırın
Veritabanı hazırlandıktan sonra, Streamlit web arayüzünü başlatmak için terminalde aşağıdaki komutu kullanın:

streamlit run chatbot_app.py

Tarayıcınızda otomatik olarak açılacaktır (genellikle http://localhost:8501).
