import tkinter as tk
from eserEkle import eser_ekle
from tabloListeAra import eser_ara
from yazarEkle import yazar_ekle
from yayineviEkle import yayinevi_ekle

def main():

    root = tk.Tk()
    root.title("Kütüphane Katalogu")
    root.geometry('1000x300')

    welcome_label = tk.Label(root, text="Hoş Geldiniz!", font=("Helvetica", 16))
    welcome_label.pack(pady=10)


    eser_ekle_button = tk.Button(root, text="Eser Ekle", command=eser_ekle)
    eser_ekle_button.pack(pady=5)

    yazar_ekle_button = tk.Button(root, text="Yazar Ekle", command=yazar_ekle)
    yazar_ekle_button.pack(pady=5)

    yayinevi_ekle_button = tk.Button(root, text="Yayinevi Ekle", command=yayinevi_ekle)
    yayinevi_ekle_button.pack(pady=5)

    ara_button = tk.Button(root, text="Eserleri Listele ve Ara", command=eser_ara)
    ara_button.pack(pady=5)

    root.mainloop()
if __name__ == "__main__":
    main()









