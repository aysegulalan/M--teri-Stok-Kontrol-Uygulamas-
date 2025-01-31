import time


urunadilistesi = []
urunfiyatlistesi = []
urunstoklistesi = []
musterilistesi = []
sehirlistesi = []

uygulamacalisiyor = True

print("Python ile stok kontrol ve takip programı")

while uygulamacalisiyor:
    time.sleep(0.5)
    print(
        "İŞLEM LİSTESİ \n"
        "1. ÜRÜNLERİ LİSTELE.\n"
        "2. ÜRÜN EKLE.\n"
        "3. STOK KONTROLÜ.\n"
        "4. MÜŞTERİ EKLE\n"
        "5. MÜŞTERİ LİSTESİ\n"
        "6. TİCARİ İŞLEMLER"
        "a. PROGRAMDAN ÇIKIŞ."
    )
    islem = input("İŞLEM NUMARASINI GİRİNİZ: ").strip().lower()

    if islem == "a":
        uygulamacalisiyor = False
        print("Programdan çıkılıyor...")
        time.sleep(3)

    elif islem == "1":
        if not urunadilistesi:
            print("Ürün listesi şu an boş.")
        else:
            print("Ürün Listesi:")
            for i, urun in enumerate(urunadilistesi):
                print(f"{i + 1}. {urun} - Fiyat: {urunfiyatlistesi[i]} - Stok: {urunstoklistesi[i]}")

    elif islem == "2":
        urunadi = input("Ürünün adını giriniz: ")
        urunfiyati = float(input("Ürünün fiyatını giriniz: "))
        urunstoğu = int(input("Ürünün stok miktarını giriniz: "))

        urunadilistesi.append(urunadi)
        urunfiyatlistesi.append(urunfiyati)
        urunstoklistesi.append(urunstoğu)

        print(f"{urunstoğu} adet {urunadi} sisteme eklendi...")
        time.sleep(3)

    elif islem == "3":
        kontrol_adi = input("Kontrol etmek istediğiniz ürünün adını giriniz: ")
        if kontrol_adi in urunadilistesi:
            index = urunadilistesi.index(kontrol_adi)
            print(f"{kontrol_adi} üründen {urunstoklistesi[index]} adet vardır.")
        else:
            print("Bu ürün stokta yok.")

    elif islem == "4":
        
        musteri_ad = input("İşletme adını giriniz: ")
        sehir = input("İşletmenin bulunduğu şehri giriniz: ")

        musterilistesi.append(musteri_ad)
        sehirlistesi.append(sehir)

        print(f"{musteri_ad} isimli müşteri {sehir} şehrinde listeye eklendi.")
        time.sleep(3)

    elif islem == "5":
        if not musterilistesi:
            print("Müşteri listesi şu an boş.")
        else:
            print("Müşteri Listesi:")
            for i, musteri in enumerate(musterilistesi):
                print(f"{i + 1}. {musteri} - Şehir: {sehirlistesi[i]}")
                time.sleep(3)


    elif islem=="6":

         urunadi=input("verilen ürün ismi giriniiz")
         musteri_verilen_adet=input("verilen ürünün adedi nedir?")
         hesap=musteri_verilen_adet*urunfiyati
        
         print(f"müsteriye {musteri_verilen_adet} adet {urunadi} verilmiştir kişinin borcu")              

    else:
        print("Geçersiz işlem numarası! Lütfen listeden bir seçenek seçin.")
