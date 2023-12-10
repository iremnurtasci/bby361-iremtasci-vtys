from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
def yazar_ekle():
    baglanti = sqlite3.connect("iremtasci-vtys.db")
    sorgu = baglanti.cursor()


    def yazarEkle():
        formVeri = (e1.get(), e2.get(), e3.get(), e4.get(), e5.get(), e6.get())
        sorgu.execute("INSERT INTO yazar (yazarAdi, yazarSoyadi, yazarDogumTarihi, yazarCinsiyet, yazarURL, yazarEposta) VALUES(?,?,?,?,?,?)", formVeri)
        baglanti.commit()
        messagebox.showinfo(title="Katalog Bilgi", message="Yazar başarıyla eklenmiştir!")
    def formTemizle():
        e1.delete(0, 'end')
        e2.delete(0, 'end')
        e3.delete(0, 'end')

    pencere = Tk()
    pencere.title('Katalog: Yazar Ekle')
    pencere.geometry('1000x300')
    pencere.resizable = True
    pencere['bg'] = '#89CFF0'

    eserCercevesi = ttk.Frame(pencere, padding=10)
    eserCercevesi.pack()

    l1 = Label(eserCercevesi, text="Yazar Adı:")
    l2 = Label(eserCercevesi, text="Yazar Soyadı:")
    l3 = Label(eserCercevesi, text="Yazar Doğum Tarihi:")
    l4 = Label(eserCercevesi, text="Yazar Cinsiyet:")
    l5 = Label(eserCercevesi, text="Yazar URL:")
    l6 = Label(eserCercevesi, text="Yazar Eposta:")
    e1 = Entry(eserCercevesi, width=25)
    e2 = Entry(eserCercevesi, width=25)
    e3 = Entry(eserCercevesi, width=25)
    e4 = Entry(eserCercevesi, width=25)
    e5 = Entry(eserCercevesi, width=25)
    e6 = Entry(eserCercevesi, width=25)
    b1 = Button(eserCercevesi, text="Yeni Yazar Ekle", command=yazarEkle)
    b2 = Button(eserCercevesi, text="Temizle", command=formTemizle)

    l1.grid(row=0, column=1, sticky=W, pady=2)
    e1.grid(row=0, column=2, pady=2)
    l2.grid(row=1, column=1, sticky=W, pady=2)
    e2.grid(row=1, column=2, pady=2)
    l3.grid(row=2, column=1, sticky=W, pady=2)
    e3.grid(row=2, column=2, pady=2)
    l4.grid(row=3, column=1, sticky=W, pady=2)
    e4.grid(row=3, column=2, pady=2)
    l5.grid(row=4, column=1, sticky=W, pady=2)
    e5.grid(row=4, column=2, pady=2)
    l6.grid(row=5, column=1, sticky=W, pady=2)
    e6.grid(row=5, column=2, pady=2)
    b1.grid(row=7, column=2, pady=2)
    b2.grid(row=7, columnspan=2, pady=2)

    pencere.mainloop()