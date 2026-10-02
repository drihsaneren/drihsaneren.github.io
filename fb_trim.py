# -*- coding: utf-8 -*-
# Ana sayfa: uzun giriş paragraflarını tek cümleye indir (anlam aynı kalır)
p = "site/index.html"
s = open(p, encoding="utf-8").read()
T = [
 ("İstanbul içinde evinize gelerek değerlendirme, tedavi ve egzersiz sürecinizi bulunduğunuz ortamda planlıyorum. Uygulanacak program; ihtiyaçlarınız, günlük yaşamınız ve değerlendirme bulgularınız doğrultusunda kişiye özel olarak oluşturulur.",
  "İstanbul içinde evinize geliyorum; değerlendirme, tedavi ve egzersiz programınız ihtiyaçlarınıza ve günlük yaşamınıza göre kişiye özel hazırlanır."),
 ("Kavrama gücü, yürüme hızı, denge ve yerden kalkabilmek; büyük bilimsel çalışmalarda uzun yaşamla en güçlü ilişkili göstergeler arasında. Bunları evinizde ölçüyor, fonksiyonel yaşınızı çıkarıyor ve size özel bir egzersiz reçetesine dönüştürüyorum.",
  "Bu göstergeleri evinizde ölçüyor, fonksiyonel yaşınızı çıkarıyor ve size özel bir egzersiz reçetesine dönüştürüyorum."),
 ("Kısa ve ücretsiz bir ön görüşmede neler yaşadığınızı dinleyeyim, evde nasıl bir yol izleyebileceğimizi birlikte konuşalım. Size uygun günü ve saat aralığını seçin; onaylayıp size dönüş yapayım.",
  "Kısa ve ücretsiz bir ön görüşmede tanışalım; sizi dinleyip evde nasıl bir yol izleyeceğimizi birlikte konuşalım."),
 ("bir mesajla anlatın; size en kısa sürede dönüş yapayım.", "bir mesajla anlatın; en kısa sürede size dönüş yapalım."),
 ("Evde 2–3 dakikada yapabileceğiniz dört basit test. Kas gücü, denge, günlük hareket ve kondisyon; bilimsel çalışmalarda uzun ve sağlıklı yaşamla ilişkili bulunan dört gösterge.",
  "Evde 2–3 dakikada yapabileceğiniz dört basit test: kas gücü, denge, günlük hareket ve kondisyon."),
 ("Evde dambılla uygulanan, gün aşırı ilerleyen örnek bir program. Her hareket animasyonla gösterilir. Isınma, günlük görevler ve güvenlik kuralları plana dahildir.",
  "Evde dambılla, gün aşırı ilerleyen örnek bir program; her hareket animasyonla gösterilir."),
]
for a, b in T:
    assert s.count(a) == 1, a[:60]
    s = s.replace(a, b)
open(p, "w", encoding="utf-8").write(s)
print("ok")
