import tkinter as tk

def konversi_matauang():
    try:
        jumlah = float(entry_jumlah.get())
        hasil = jumlah * kurs
        label_hasil.config(text=f"Hasil Konversi: {hasil:.2f} IDR")
    except ValueError:
        label_hasil.config(text="Masukkan Jumlah yang valid!")


#gui tkinter
root = tk.Tk()
root.title("Konversi Dollar USD To Rupiah")
root.geometry("400x300")

#Nilai tukar usd ke rupiah
kurs = 15000

#judul
label_judul = tk.Label(root, text="KONVERSI MATA UANG DOLLAR USD KE RUPIAH")
label_judul.pack(pady=10)

#label masukan jumlah uang
label_jumlah = tk.Label(root, text="jumlah uang (USD):")
label_jumlah.pack(pady=10)

entry_jumlah = tk.Entry(root)
entry_jumlah.pack(pady=10)

#tombol konversi
tombol_konversi = tk.Button(root, text="konversikan", command=konversi_matauang)
tombol_konversi.pack(pady=10)

#label hasil konversi
label_hasil = tk.Label(root, text="")
label_hasil.pack(pady=10)

#jalankan gui tkinter
root.mainloop()