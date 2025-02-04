# IMDb Movie Scraper

##  Proje Açıklaması
Bu proje, **Selenium** kullanarak IMDb'deki belirli filtrelere sahip filmleri tarayıp bilgilerini çeken bir **web scraping** uygulamasıdır.
Scraper, filmlerin **isim, yıl, süre, IMDb puanı, oy sayısı, Metascore ve açıklama** bilgilerini alır ve **Excel dosyası** olarak kaydeder.

## Kullanılan Teknolojiler
- **Python**: Proje ana dili
- **Selenium**: Web sayfası gezinme ve veri çekme
- **Pandas**: Verileri işleme ve Excel'e yazma
- **Openpyxl**: Excel dosyasına yazma

## 📂 Kurulum & Çalıştırma

### 1️⃣ Gerekli Bağımlılıkları Yükleyin
Proje çalıştırılmadan önce aşağıdaki kütüphaneleri yükleyin:
```bash
pip install selenium pandas openpyxl
```

### 2️⃣ ChromeDriver'ı İndirin
Scraper'ın çalışması için **ChromeDriver** gereklidir.
- Chrome sürümünüzle uyumlu olan sürümü şu adresten indirin: [ChromeDriver](https://sites.google.com/chromium.org/driver/)
- ChromeDriver'ı **proje klasörüne** yerleştirin.

### 3️⃣ IMDb Scraper'ı Çalıştırın
Proje dizininde terminal veya komut istemcisi açarak aşağıdaki komutu çalıştırın:
```bash
python imdb_scraper.py
```
Scraper çalıştırıldığında IMDb'ye giderek belirlenen filtreler doğrultusunda **Aksiyon ve Oscar Adayı** olan filmleri listeleyecek ve bilgilerini çekecektir.

## 📊 Çekilen Film Verileri
Scraper, aşağıdaki bilgileri toplar ve `movies.xlsx` dosyasına kaydeder:
- **Film Adı**
- **Yıl**
- **Süre**
- **IMDb Puanı**
- **Oy Sayısı**
- **Metascore** (Varsa)
- **Açıklama**

## ⚠️ Dikkat Edilmesi Gerekenler
- IMDb sayfa yapısı zaman zaman değişebilir. Eğer scraper çalışmazsa **XPATH veya CSS Selector** değerlerini güncellemek gerekebilir.
- Selenium işlemleri sırasında **sayfa yüklenme süreleri** değişebilir. `sleep()` fonksiyonlarının süresini arttırabilirsiniz.
- `WebDriverWait` kullanarak öğelerin yüklenmesini beklemek en sağlıklı yaklaşımdır.

## 📌 Geliştirme & Katkı
Bu projeye katkıda bulunmak isterseniz **pull request (PR) açabilir** veya **hata raporu (issue) oluşturabilirsiniz**. Geri bildirimleriniz geliştirme sürecine büyük katkı sağlayacaktır. 😊

---
**📧 İletişim**: Eğer herhangi bir sorunuz varsa, [LinkedIn]([https://linkedin.com/](https://www.linkedin.com/in/emre-y%C4%B1ld%C4%B1r%C4%B1m1998/)) üzerinden ulaşabilirsiniz. ✨



------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

IMDb Movie Scraper
Project Description
This project is a web scraping application that uses Selenium to scrape movies from IMDb with specific filters, extracting details like name, year, duration, IMDb rating, number of votes, Metascore, and description, and saves the data as an Excel file.

Technologies Used
Python: The main programming language
Selenium: For navigating the webpage and scraping data
Pandas: For data processing and writing to Excel
Openpyxl: For writing to Excel files
📂 Installation & Running
1️⃣ Install Required Dependencies
Before running the project, install the necessary libraries:

bash
Kopyala
Düzenle
pip install selenium pandas openpyxl
2️⃣ Download ChromeDriver
The scraper requires ChromeDriver to run.

Download the version compatible with your Chrome from: ChromeDriver
Place the ChromeDriver in the project folder.
3️⃣ Run IMDb Scraper
Open a terminal or command prompt in the project directory and run the following command:

bash
Kopyala
Düzenle
python imdb_scraper.py
When the scraper is run, it will navigate to IMDb and list movies with the Action and Oscar Nominee filters, extracting their details.

📊 Scraped Movie Data
The scraper collects the following information and saves it in the movies.xlsx file:

Movie Name
Year
Duration
IMDb Rating
Number of Votes
Metascore (if available)
Description
⚠️ Things to Keep in Mind
IMDb’s page structure may change over time. If the scraper stops working, you may need to update the XPATH or CSS Selector values.
The page load times might vary during Selenium operations. You can increase the sleep() durations.
Using WebDriverWait to wait for elements to load is the best approach.
📌 Development & Contributions
If you would like to contribute to this project, feel free to open a pull request (PR) or create an issue. Your feedback will greatly help in improving the development process. 😊

📧 Contact: If you have any questions, feel free to reach out to me on LinkedIn. ✨
