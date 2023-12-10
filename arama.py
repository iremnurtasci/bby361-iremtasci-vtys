import sqlite3

con = sqlite3.connect("iremtasci-vtys.db")
cur = con.cursor()

anahtar = input("Anahtar kelimeyi giriniz: ")

res = cur.execute(
    "SELECT * FROM eser WHERE eserAdi LIKE('%{}%') OR eserBasimYeri LIKE('%{}%') ORDER BY eserAdi DESC".format(anahtar,anahtar)
)
veriler = res.fetchall()
for satir in veriler:
    print(satir)