# Metro Simülasyonu
Bu proje, belirli bir başlanngıç istasyonundan belirli bir hedef istasyonuna olan **en az aktarmalı rotayı** ve **en hızlı rotayı** bulan bir metro uygulamasıdır.
## Kullanılan teknolojiler ve Kütüphaneler
**Python programlama dili** : Uygulama, python dilinde yazılmıştır.

**Collections kütüphanesi** : İçe aktarılmış olan *collections* kütüphanesinden *deque(double-ended queue)* yapısıyla BFS algoritması için bir kuyruk yapısı oluşturulmuştur.Aynı kütüphaneden olan *defaultdict* yapısı ile eğer bir key bulunamazsa hata vermek yerine onu eklemesini sağlamaktadır. 

**Heapq kütüphanesi** : Bu kütüphane yardımıyla *kuyruk(queue)* veya *heap(yığın)* veri yapılarını belirli bir önceliğe göre dizmeyi sağlamaktadır. Projede öncelikli *kuyruk(priority queue)* oluşturmak için kullanılmıştır. *heappush.* fonksiyonuyla kuyruğa eleman eklerken, *heappop.* fonksiyonuyla kuyruktan eleman çıkarılmaktadır.

**Typing kütüphanesi** : Bu kütüphanedeki *dict, list, set, tuple, optional* türler ile daha iyi tip denetimi yapılmıştır, kodun daha okunabilir ve temiz olmasını sağlamaktadır.

## Algoritmaların çalışma mantığı

### BFS algoritmasının nasıl çalıştığı 
Bu uygulamada BFS algoritması en az aktarmalı yolu bulmak için kullanılmıştır. Başlangıç istasyonundan başlanarak komşu istasyonlar kuyruğa eklenmektedir. Daha sonra sırayla kuyruktaki elemanlar keşfedilmektedir. Bu algoritma *FIFO (first-in first-out)* prensibiyle çalışmaktadır. Kuyruğa ilk giren eleman ilk çıkmaktadır.
### A* algoritmasının nasıl çalıştığı 
Bu uygulamada A* algoritması en hızlı yolu bulmak için kullanılmıştır. Koddaki istasyon listesine göre oluşturulan bir *heuristic tabloyla* *f(n)=g(n)+h(n)* denklemini tamamlayarak en kısa süreyle gidiilen yani en az maliyetli olan yolu bulmaktadır. Bu algoritmada bir öncelikli kuyruk yapısı oluşturulur ve sırayla başlangıç noktasından itibaren en kısa süreye göre eklenen komşuları sürekli kuyrukta güncelleyerek hedefe doğru yol alır. Kuyruktan çıkan ilk eleman o an kuyrukta olan en az maliyetli elemandır.
### Neden bu algoritmaları kullandığımız
BFS algoritmasını *en az aktarmalı yolu* bulmak için kullanmamızın sebebi istasyon yapısını *ağırlıksız* yani her yol eşit uzunlukta varsayarak incelemektir. Burada yolların maliyeti yani süresi veya uzunluğu ihmal edilmektedir. BFS algoritması *seviye seviye* inceleme yaptığı için en az sayıda durağa uğrayarak hedefe gitmeyi amaçlamaktadır.
A* algoritması BFS'in temel prensibini geliştirmektedir. Bu algoritmada istasyon yapısı *ağırlıklı* olarak yani belli maliyetlerle oluşturulmaktadır. *Öncelikli kuyruk* yapısıyla en az maliyetli yol önce keşfedilmektedir bu da kısa yolları tercih ederek ilerleyeceğini belirtir. *En hızlı yolu* bulmak için ideal bir algoritmadır.
## Örnek kullanım ve test sonuçları


## Projeyi geliştirme fikirleri
Bu proje daha kullanışlı bir arayüzle zenginleştirilebilir. Dahası gerekli verilerle besleyerek yoğunluk saatine göre bir uyarı yapabilir. Sadece en az aktarmalı ve en hızlı rotayı göstermek yerine diğer rotaları da kullanıcıya gösterip daha da kullnışlı hale getirilebilir. Başka şehirler ve tüm durakların metro geliş saati eklenebilir.

