from tkinter import *
from  tkinter import ttk
import sqlite3

pencere  = Tk()
pencere.title('Katalog: Eserleri Listele')
pencere.geometry('1000x300')
pencere.resizable = True
pencere['bg'] = '#89CFF0'

eserTabloCercevesi = ttk.Frame(pencere, padding=25)
eserTabloCercevesi.pack()

eserTablosu = ttk.Treeview(eserTabloCercevesi)


eserTablosu['columns'] = ('eserID', 'eserAdi', 'eserISBN', 'eserBasimYeri', 'eserBasimTarihi','eserSayfaSayisi', 'eserDili', 'eserOrijinalDili')


eserTablosu.column("#0", width=0, stretch=NO)
eserTablosu.column("eserID", anchor=CENTER, width=50)
eserTablosu.column("eserAdi", anchor=CENTER, width=200)
eserTablosu.column("eserISBN", anchor=CENTER, width=200)
eserTablosu.column("eserBasimYeri", anchor=CENTER, width=100)
eserTablosu.column("eserBasimTarihi", anchor=CENTER, width=100)
eserTablosu.column("eserSayfaSayisi", anchor=CENTER, width=100)
eserTablosu.column("eserDili", anchor=CENTER, width=100)
eserTablosu.column("eserOrijinalDili", anchor=CENTER, width=100)


eserTablosu.heading("#0", text="", anchor=CENTER)
eserTablosu.heading("eserID", text="Eser ID", anchor=CENTER)
eserTablosu.heading("eserAdi", text="Eser Adı", anchor=CENTER)
eserTablosu.heading("eserISBN", text="Eser ISBN", anchor=CENTER)
eserTablosu.heading("eserBasimYeri", text="Eser Basım Yeri", anchor=CENTER)
eserTablosu.heading("eserBasimTarihi", text="Eser Basım Tarihi", anchor=CENTER)
eserTablosu.heading("eserSayfaSayisi", text="Eser Sayfa Sayısı", anchor=CENTER)
eserTablosu.heading("eserDili", text="Eser Dili", anchor=CENTER)
eserTablosu.heading("eserOrijinalDili", text="Eser Orijinal Dili", anchor=CENTER)

eserTablosu.pack()

baglanti = sqlite3.connect("iremtasci-vtys.db")
sorgu = baglanti.cursor()
sonuc = sorgu.execute("SELECT * FROM eser")

for index, eser in enumerate(sonuc.fetchall()):
    eserTablosu.insert(parent='',index='end',iid=index,text='',
    values=(eser[0],eser[1],eser[2],eser[3],eser[4],eser[5],eser[6],eser[7]))

pencere.mainloop()