from gtts import gTTS
import sys
import time

metin = """
[Yıllar geçtikçe, Ali ve Ayşe birçok farklı ülkeyi ziyaret etti ve dünya kültürleri hakkında daha fazla şey öğrendiler. Her yolculuk, yeni arkadaşlıklar, yeni lezzetler ve yeni hikayelerle doluydu. Ancak en önemlisi, her yolculuk, Ali ve Ayşe'nin bağlarını daha da güçlendirdi.

Bu, Ali ve Ayşe'nin hikayesinin sonu, ama arkadaşlık, macera ve keşiflerin hikayesi hiçbir zaman bitmezdi. Ve bu hikayeler, yeni nesillere ilham verir, hayatın güzelliklerini ve değerini hatırlatır ve arkadaşlığın gücünü anlatan bir miras olarak yaşamaya devam ederdi.
]"""

tts = gTTS(text=metin, lang='tr')


ses_dosyasi_adi = "sesdosyasi.mp3"


print("Ses dosyası oluşturuluyor... ", end='', flush=True)


baslangic_zamani = time.time()


tts.save(ses_dosyasi_adi)


bitis_zamani = time.time()


isleme_suresi = bitis_zamani - baslangic_zamani


print(f"\nSes dosyası başarıyla oluşturuldu: {ses_dosyasi_adi}")


print(f"İşlem süresi: {isleme_suresi:.2f} saniye")


for i in range(101):
    sys.stdout.write(f"\rİlerleme: %{i} İşlem süresi: {isleme_suresi:.2f} saniye")
    sys.stdout.flush()
    time.sleep(isleme_suresi / 100)  # Yüzdeyi işlem süresine bölerek uygun gecikmeyi hesapla

print("\nİşlem tamamlandı.")
