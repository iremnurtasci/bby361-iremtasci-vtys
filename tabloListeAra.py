import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
import sqlite3

def eser_ara():
    def listele(selected_table, anahtar):
        sorgu_columns = table_columns.get(selected_table, [])
        if not sorgu_columns:
            return

        sorgu_str = f"SELECT {', '.join(sorgu_columns)} FROM {selected_table} WHERE "
        or_conditions = []

        for col in sorgu_columns:
            or_conditions.append(f"{col} LIKE '%{anahtar}%'")

        sorgu_str += " OR ".join(or_conditions)
        sorgu.execute(sorgu_str)

        sonuc = sorgu.fetchall()

        # Arama sonuçlarını temizliyor
        for row in eserTablosu.get_children():
            eserTablosu.delete(row)

        # Yeni verileri ekliyor
        for index, row_data in enumerate(sonuc):
            eserTablosu.insert(parent='', index='end', iid=index, text='', values=row_data)

        eserTablosu['columns'] = tuple(sorgu_columns)

        # Sütun başlıklarını tabloya ekliyor
        for col in eserTablosu['columns']:
            eserTablosu.column(col, anchor=tk.CENTER, width=200)
            eserTablosu.heading(col, text=col, anchor=tk.CENTER)

    def aramaYap():
        anahtar = arama.get()
        selected_table = combobox.get()
        listele(selected_table, anahtar)

    def kayit_sil():
        selected_item = eserTablosu.selection()
        if not selected_item:
            tk.messagebox.showinfo("Uyarı", "Lütfen bir kayıt seçin.")
            return

        kayit_id = eserTablosu.item(selected_item, 'values')[0]
        table_name = combobox.get()

        silme_sorgusu = f"DELETE FROM {table_name} WHERE {table_name}ID = {kayit_id}"
        sorgu.execute(silme_sorgusu)
        baglanti.commit()

        tk.messagebox.showinfo("Başarılı", "Kayıt başarıyla silindi.")
        aramaYap()

    def kayit_guncelle():
        selected_item = eserTablosu.selection()
        if not selected_item:
            tk.messagebox.showinfo("Uyarı", "Lütfen bir kayıt seçin.")
            return

        kayit_id = eserTablosu.item(selected_item, 'values')[0]
        table_name = combobox.get()

        yeni_veriler = simpledialog.askstring("Kayıt Güncelle", "Yeni verileri girin (virgülle ayırın):")

        if yeni_veriler is not None:
            try:
                columns = table_columns.get(table_name, [])
                update_data = tuple(yeni_veriler.split(", "))

                update_query = f"UPDATE {table_name} SET {', '.join([f'{columns[i]} = ?' for i in range(1, len(columns))])} WHERE {columns[0]} = ?"

                print("Columns:", columns)
                print("Update Data:", update_data)
                print("Update Query:", update_query)

                sorgu.execute(update_query, update_data + (kayit_id,))

                baglanti.commit()

                tk.messagebox.showinfo("Başarılı", "Kayıt başarıyla güncellendi.")
                aramaYap()
            except Exception as e:
                print("Hata:", e)
                tk.messagebox.showerror("Hata", f"Güncelleme işlemi sırasında bir hata oluştu:\n{e}")

    def update_record(table, record_id, data):

        try:
            columns = table_columns.get(table, [])
            if not columns:
                return

            update_query = f"UPDATE {table} SET {', '.join([f'{columns[i]} = ?' for i in range(len(columns))])} WHERE {columns[0]} = ?"
            sorgu.execute(update_query, data + (record_id,))

            baglanti.commit()
        except Exception as e:
            raise e

    pencere = tk.Tk()
    pencere.title('Katalog: Eserleri Listele ve Ara')
    pencere.geometry('1000x280')
    pencere.resizable = True
    pencere['bg'] = '#89CFF0'

    eserTabloCercevesi = ttk.Frame(pencere, padding=25)
    eserTabloCercevesi.pack()

    eserTablosu = ttk.Treeview(eserTabloCercevesi)

    eserTablosu['columns'] = ('eserID', 'eserAdi', 'eserISBN', 'eserBasimYeri', 'eserBasimTarihi', 'eserSayfaSayisi', 'eserDili', 'eserOrijinalDili')

    eserTablosu.column("#0", width=0, stretch=tk.NO)
    for col in eserTablosu['columns']:
        eserTablosu.column(col, anchor=tk.CENTER, width=200)
        eserTablosu.heading(col, text=col, anchor=tk.CENTER)

    eserTablosu.pack()

    baglanti = sqlite3.connect("iremtasci-vtys.db")
    global sorgu
    sorgu = baglanti.cursor()

    table_columns = {
        'eser': ['eserID', 'eserAdi', 'eserISBN', 'eserBasimYeri', 'eserBasimTarihi', 'eserSayfaSayisi', 'eserDili', 'eserOrijinalDili'],
        'yazar': ['yazarID', 'yazarAdi', 'yazarSoyadi', 'yazarDogumTarihi', 'yazarCinsiyet', 'yazarURL', 'yazarEposta'],
        'yayinevi': ['yayineviID', 'yayineviAdi', 'yayineviİL', 'yayineviKurulusTarihi', 'yayineviURL', 'yayineviTelefon', 'yayineviEposta'],
        'konuBaslikGenel': ['genelBaslikID', 'genelBasliklar'],
        'konuAltBaslik': ['konuAltBaslikID', 'altBasliklar']
    }

    combobox = ttk.Combobox(eserTabloCercevesi, values=list(table_columns.keys()))
    combobox.set('eser')
    combobox.pack(side=tk.LEFT, padx=5)

    aramaBaslik = tk.Label(eserTabloCercevesi, text="Arama:")
    arama = tk.Entry(eserTabloCercevesi, width=25)
    ara = tk.Button(eserTabloCercevesi, text="Ara", command=aramaYap)
    sil_butonu = tk.Button(eserTabloCercevesi, text="Kayıt Sil", command=kayit_sil)
    guncelle_butonu = tk.Button(eserTabloCercevesi, text="Kayıt Güncelle", command=kayit_guncelle)
    aramaBaslik.pack(side=tk.LEFT, padx=5)
    arama.pack(side=tk.LEFT, padx=5)
    ara.pack(side=tk.LEFT, padx=5)
    sil_butonu.pack(side=tk.LEFT, padx=5)
    guncelle_butonu.pack(side=tk.LEFT, padx=5)




