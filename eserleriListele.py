import tkinter as tk
from tkinter import ttk
import sqlite3
def eserleri_listele():
        table_columns = {
            'eser': ['eserID', 'eserAdi', 'eserISBN', 'eserBasimYeri', 'eserBasimTarihi','eserSayfaSayisi','eserDili', 'eserOrijinalDili'],
            'yazar': ['yazarID', 'yazarAdi', 'yazarSoyadi', 'yazarDogumTarihi', 'yazarCinsiyet', 'yazarURL', 'yazarEposta'],
            'yayinevi': ['yayineviID', 'yayineviAdi', 'yayineviİL', 'yayineviKurulusTarihi', 'yayineviURL', 'yayineviTelefon', 'yayineviEposta'],
            'konuBaslikGenel': ['genelBaslikID', 'genelBasliklar'],
            'konuAltBaslik': ['konuAltBaslikID', 'altBasliklar']
        }

        def listele(selected_table):
            baglanti = sqlite3.connect("iremtasci-vtys.db")
            sorgu = baglanti.cursor()


            sorgu_columns = table_columns.get(selected_table, [])
            if not sorgu_columns:
                return

            sorgu_str = f"SELECT {', '.join(sorgu_columns)} FROM {selected_table}"

            sorgu.execute(sorgu_str)
            sonuc = sorgu.fetchall()

            pencere = tk.Tk()
            pencere.title(f'Katalog: {selected_table.capitalize()} Listele')
            pencere.geometry('1000x300')
            pencere.resizable = True
            pencere['bg'] = '#89CFF0'

            eserTabloCercevesi = ttk.Frame(pencere, padding=25)
            eserTabloCercevesi.pack()

            eserTablosu = ttk.Treeview(eserTabloCercevesi)


            eserTablosu['columns'] = tuple(sorgu_columns)

            for col in sorgu_columns:
                eserTablosu.column(col, anchor=tk.CENTER, width=200)
                eserTablosu.heading(col, text=col, anchor=tk.CENTER)

            for index, row in enumerate(sonuc):
                eserTablosu.insert(parent='', index='end', iid=index, text='', values=row)

            def aramaYap():
                anahtar = arama.get()
                aramaSonuc = sorgu.execute(
                    "SELECT * FROM eser WHERE eserAdi LIKE('%{}%') OR eserOrijinalDili LIKE('%{}%') OR eserBasimTarihi LIKE('%{}%') ORDER BY eserAdi DESC".format(
                        anahtar,
                        anahtar, anahtar)
                )

                for row in eserTablosu.get_children():
                    eserTablosu.delete(row)

                for index, eser in enumerate(sorgu.fetchall()):
                    eserTablosu.insert(parent='', index='end', iid=index, text='',
                                       values=(eser[0], eser[1], eser[2], eser[3], eser[4], eser[5], eser[6], eser[7]))

            aramaBaslik = tk.Label(eserTabloCercevesi, text="Arama:")
            arama = tk.Entry(eserTabloCercevesi, width=25)
            ara = tk.Button(eserTabloCercevesi, text="Arama Yap!", command=aramaYap)
            aramaBaslik.pack()
            arama.pack()
            ara.pack()

            eserTablosu.pack()

        #Açılır menüyü oluşturan kodlar
        def on_combobox_change(event):
            selected_table = combobox.get()
            listele(selected_table)

        root = tk.Tk()
        root.title("Veritabanı Tablo Listeleme")

        table_names = ['eser', 'yazar', 'yayinevi', 'konuBaslikGenel', 'konuAltBaslik']

        combobox = ttk.Combobox(root, values=table_names)
        combobox.pack(pady=10)
        combobox.set(table_names[0])
        combobox.bind("<<ComboboxSelected>>", on_combobox_change)
        root.mainloop()