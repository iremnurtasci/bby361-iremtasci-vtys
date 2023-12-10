import sqlite3

con = sqlite3.connect("iremtasci-vtys.db")
cur = con.cursor()

kat = cur.execute("SELECT DISTINCT UPPER(SUBSTR(genelBasliklar, 1, 1)) || SUBSTR(genelBasliklar, 2) FROM konuBaslikGenel ORDER BY genelBasliklar")
katListe = kat.fetchall()

print("Kategori listesi:")
for count, katSatir in enumerate(katListe):
    print(str(count+1) +" - "+ katSatir[0])

kategoriID = int(input("Lütfen kategori ID giriniz: "))

if kategoriID == 1:
    secilenKategori = "Roman"
elif kategoriID == 2:
    secilenKategori = "Klasik Edebiyat"
elif kategoriID == 3:
    secilenKategori = "Şiir"
elif kategoriID == 4:
    secilenKategori = "Tiyatro"
elif kategoriID == 5:
    secilenKategori = "Kurgusal Olmayan"
elif kategoriID == 6:
    secilenKategori = "Bilim ve Teknoloji"
elif kategoriID == 7:
    secilenKategori = "Sanat ve Müzik"
elif kategoriID == 8:
    secilenKategori = "Tarih"
elif kategoriID == 9:
    secilenKategori = "Din ve Felsefe"
elif kategoriID == 10:
    secilenKategori = "Çocuk ve Gençlik"
elif kategoriID == 11:
    secilenKategori = "Gezi ve Doğa"
elif kategoriID == 12:
    secilenKategori = "Dergi"
else:
    print("Seçim Hatalı..!")

res = cur.execute(
    "SELECT * FROM konuBaslikGenel WHERE genelBasliklar = '{}'".format(secilenKategori)
)

veriler = res.fetchall()
for satir in veriler:
    print(satir)
print("Toplam kayıt sayısı " + str(len(veriler)))