# 💱 Döviz Çevirici

Bu proje, kullanıcının belirttiği para birimini, yine kullanıcının seçtiği başka bir para birimine dönüştüren basit bir Python uygulamasıdır. Güncel döviz kuru verileri, ExchangeRate-API üzerinden alınmaktadır.

Kullanıcıdan şu bilgiler alınır:
- Bozulacak döviz türü (örneğin: USD)
- Alınacak döviz türü (örneğin: TRY)
- Bozdurulacak miktar

Girilen bilgilerle birlikte API'den alınan kur oranı kullanılarak dönüşüm yapılır ve sonuç terminalde gösterilir.

---

## 🔧 Kullanılan Teknolojiler

- **requests**: API'den veri çekmek için kullanılan HTTP kütüphanesi  
- **json**: API'den gelen verileri çözümlemek için  
- **ExchangeRate-API**: Döviz kuru verilerini sağlayan servis  

---
## 🖥️ Çıktı Örneği

<img width="600" height="300" alt="image" src="https://github.com/user-attachments/assets/9f9a891c-3aec-4d53-b514-7af58310c070" />
