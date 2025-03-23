from collections import defaultdict, deque
import heapq
from typing import Dict, List, Set, Tuple, Optional

class Istasyon:
    def __init__(self, idx: str, ad: str, hat: str):
        self.idx = idx
        self.ad = ad
        self.hat = hat
        self.komsular: List[Tuple['Istasyon', int]] = []  # (istasyon, süre) tuple'ları

    def komsu_ekle(self, istasyon: 'Istasyon', sure: int):
        self.komsular.append((istasyon, sure))

class MetroAgi:
    def __init__(self):
        self.istasyonlar: Dict[str, Istasyon] = {}
        self.hatlar: Dict[str, List[Istasyon]] = defaultdict(list)

    def istasyon_ekle(self, idx: str, ad: str, hat: str) -> None:
        if id not in self.istasyonlar:
            istasyon = Istasyon(idx, ad, hat)
            self.istasyonlar[idx] = istasyon
            self.hatlar[hat].append(istasyon)

    def baglanti_ekle(self, istasyon1_id: str, istasyon2_id: str, sure: int) -> None:
        istasyon1 = self.istasyonlar[istasyon1_id]
        istasyon2 = self.istasyonlar[istasyon2_id]
        istasyon1.komsu_ekle(istasyon2, sure)
        istasyon2.komsu_ekle(istasyon1, sure)
    
    def en_az_aktarma_bul(self, baslangic_id: str, hedef_id: str) -> Optional[List[Istasyon]]:
        """BFS algoritması kullanarak en az aktarmalı rotayı bulur
        
        Bu fonksiyonu tamamlayın:
        1. Başlangıç ve hedef istasyonların varlığını kontrol edin
        2. BFS algoritmasını kullanarak en az aktarmalı rotayı bulun
        3. Rota bulunamazsa None, bulunursa istasyon listesi döndürün
        4. Fonksiyonu tamamladıktan sonra, # TODO ve pass satırlarını kaldırın
        
        İpuçları:
        - collections.deque kullanarak bir kuyruk oluşturun, HINT: kuyruk = deque([(baslangic, [baslangic])])
        - Ziyaret edilen istasyonları takip edin
        - Her adımda komşu istasyonları keşfedin
        """

        # İstasyonların varlığını kontrol ediyoruz
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]
        ziyaret_edildi = {baslangic}

        # Bu kuyruk yapısında başlangıç istasyonundan başlayarak her elemanı
        # (mevcut istasyon, o noktaya kadar izlenen rota) şeklinde tutuyoruz.
        kuyruk = deque([(baslangic,[baslangic])])

        # Kuyruk boş olana kadar
        while kuyruk:
            # kuyruğun en önündeki elemanı mevcut istasyon ve o düğüme kadar izlenen rota şeklinde çıkarırız.
            mevcut_durak, rota = (kuyruk.popleft())

            # eğer hedefe ulaşılmışsa rotayı fonksiyonun çıktısı olarak döndürürüz.
            if mevcut_durak == hedef:
                return rota

            # mevcut istasyonu ziyaret edildi olarak işaretleriz.
            ziyaret_edildi.add(mevcut_durak)

            # mevcut durağın her bir komşusu için
            for komsu, _ in mevcut_durak.komsular:

                # eğer komşu ziyaret edilmediyse
                if komsu not in ziyaret_edildi:

                    # komşuyu kuyruğa ve o düğüme kadar izlenen rotaya ekleriz,
                    kuyruk.append((komsu, rota + [komsu]))

                    # ve komşuyu ziyaret edildi olarak işaretleriz.
                    ziyaret_edildi.add(komsu)

        # rota bulunamazsa None döndürürüz
        return None

    def en_hizli_rota_bul(self, baslangic_id: str, hedef_id: str) -> Optional[Tuple[List[Istasyon], int]]:

        """A* algoritması kullanarak en hızlı rotayı bulur
        
        Bu fonksiyonu tamamlayın:
        1. Başlangıç ve hedef istasyonların varlığını kontrol edin
        2. A* algoritmasını kullanarak en hızlı rotayı bulun
        3. Rota bulunamazsa None, bulunursa (istasyon_listesi, toplam_sure) tuple'ı döndürün
        4. Fonksiyonu tamamladıktan sonra, # TODO ve pass satırlarını kaldırın
        
        İpuçları:
        - heapq modülünü kullanarak bir öncelik kuyruğu oluşturun, HINT: pq = [(0, id(baslangic), baslangic, [baslangic])]
        - Ziyaret edilen istasyonları takip edin
        - Her adımda toplam süreyi hesaplayın
        - En düşük süreye sahip rotayı seçin
        """

        # İstasyonların varlığını kontrol ediyoruz
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]
        ziyaret_edildi = set()

        #graf yapısına uygun bir heuristic tablo ekleriz,
        #yani her istasyonun hedefe tahmini varış süresi içeren bir tablo
        heuristic={
            'M1':12,'M2':8,'M3':7,'M4':6,
            'K1':8,'K2':10,'K3':9,'K4':14,
            'T1':11,'T2':9,'T3':6,'T4':10
            }

        #Burada frontier adında tahmini maliyeti, şu anki maliyeti, istasyon id ve rotayı içeren .
        #bir priority queue oluşturuyoruz
        frontier=[]
        heapq.heappush(frontier,(heuristic[baslangic.idx],0,baslangic.idx,[baslangic]))

        #frontier boş olana kadar
        while frontier:

            #frontier kuyruğundan en düşük maliyete sahip elemanı çıkarıyoruz.
            _,toplam_sure,mevcut_id,rota=heapq.heappop(frontier)

            #mevcut_id'i kullanarak o istasyonu istasyonlar sözlüğünden alıyoruz.
            mevcut=self.istasyonlar[mevcut_id]

            #eğer mevcut durak ziyaret edilmişse döngüye devam ediyoruz
            if mevcut_id in ziyaret_edildi:
                continue

            #mevcut durağı ziyaret edildi olarak işaretliyoruz
            ziyaret_edildi.add(mevcut_id)

            #eğer hedefe ulaşmışsak rotayı ve süreyi geri döndürüyoruz
            if mevcut_id == hedef_id:
                return rota,toplam_sure

            #mevct durağın her bir komşusu ve komşuya olan süresi için
            for komsu, sure in mevcut.komsular:

                #eğer komşu ziyaret edilmediyse
                if komsu.idx not in ziyaret_edildi:

                    #gerçek maliyeti buluyoruz. (g(n))
                    yeni_sure=toplam_sure + sure

                    #f(n)=g(n)+h(n) denkleminden yardım alarak tahmini toplam süreyi buluyoruz.
                    tahmini_toplam = yeni_sure + heuristic[komsu.idx]

                    #frontier kuyruğuna komşunun f(n), g(n), id ve başlangıçtan itibaren rotayı önceliğe göre ekliyoruz.
                    heapq.heappush(frontier,(tahmini_toplam,yeni_sure,komsu.idx, rota+[komsu]))

        #rota bulunamazsa None döndürüyoruz.
        return None

# Örnek Kullanım
if __name__ == "__main__":
    metro = MetroAgi()
    
    # İstasyonlar ekleme
    # Kırmızı Hat
    metro.istasyon_ekle("K1", "Kızılay", "Kırmızı Hat")
    metro.istasyon_ekle("K2", "Ulus", "Kırmızı Hat")
    metro.istasyon_ekle("K3", "Demetevler", "Kırmızı Hat")
    metro.istasyon_ekle("K4", "OSB", "Kırmızı Hat")
    
    # Mavi Hat
    metro.istasyon_ekle("M1", "AŞTİ", "Mavi Hat")
    metro.istasyon_ekle("M2", "Kızılay", "Mavi Hat")  # Aktarma noktası
    metro.istasyon_ekle("M3", "Sıhhiye", "Mavi Hat")
    metro.istasyon_ekle("M4", "Gar", "Mavi Hat")
    
    # Turuncu Hat
    metro.istasyon_ekle("T1", "Batıkent", "Turuncu Hat")
    metro.istasyon_ekle("T2", "Demetevler", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T3", "Gar", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T4", "Keçiören", "Turuncu Hat")
    
    # Bağlantılar ekleme
    # Kırmızı Hat bağlantıları
    metro.baglanti_ekle("K1", "K2", 4)  # Kızılay -> Ulus
    metro.baglanti_ekle("K2", "K3", 6)  # Ulus -> Demetevler
    metro.baglanti_ekle("K3", "K4", 8)  # Demetevler -> OSB
    
    # Mavi Hat bağlantıları
    metro.baglanti_ekle("M1", "M2", 5)  # AŞTİ -> Kızılay
    metro.baglanti_ekle("M2", "M3", 3)  # Kızılay -> Sıhhiye
    metro.baglanti_ekle("M3", "M4", 4)  # Sıhhiye -> Gar
    
    # Turuncu Hat bağlantıları
    metro.baglanti_ekle("T1", "T2", 7)  # Batıkent -> Demetevler
    metro.baglanti_ekle("T2", "T3", 9)  # Demetevler -> Gar
    metro.baglanti_ekle("T3", "T4", 5)  # Gar -> Keçiören
    
    # Hat aktarma bağlantıları (aynı istasyon farklı hatlar)
    metro.baglanti_ekle("K1", "M2", 2)  # Kızılay aktarma
    metro.baglanti_ekle("K3", "T2", 3)  # Demetevler aktarma
    metro.baglanti_ekle("M4", "T3", 2)  # Gar aktarma
    
    # Test senaryoları
    print("\n=== Test Senaryoları ===")
    
    # Senaryo 1: AŞTİ'den OSB'ye
    print("\n1. AŞTİ'den OSB'ye:")
    rota = metro.en_az_aktarma_bul("M1", "K4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("M1", "K4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
    
    # Senaryo 2: Batıkent'ten Keçiören'e
    print("\n2. Batıkent'ten Keçiören'e:")
    rota = metro.en_az_aktarma_bul("T1", "T4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("T1", "T4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
    
    # Senaryo 3: Keçiören'den AŞTİ'ye
    print("\n3. Keçiören'den AŞTİ'ye:")
    rota = metro.en_az_aktarma_bul("T4", "M1")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("T4", "M1")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota)) 