from keuangan import KeuanganToko

app = KeuanganToko('transaksi.csv')

def menu():
    print("\n--- Menu Keuangan Toko ---")
    print("1. Tambah Transaksi")
    print("2. Tampilkan Semua Transaksi")
    print("3. Cari Transaksi")
    print("4. Hitung Saldo")
    print("5. Undo Transaksi Terakhir")
    print("6. Keluar")

while True:
    menu()
    pilihan = input("Pilih menu (1-6): ")
    
    if pilihan == '1':
        id = input("ID Transaksi: ")
        tipe = input("Tipe (masuk/keluar): ").lower()
        jumlah = input("Jumlah: ")
        app.tambah_transaksi(id, tipe, jumlah)
    elif pilihan == '2':
        app.tampilkan_semua()
    elif pilihan == '3':
        id = input("Masukkan ID: ")
        hasil = app.cari_transaksi(id)
        print(hasil if hasil else "Transaksi tidak ditemukan.")
    elif pilihan == '4':
        print(f"Saldo Saat Ini: {app.hitung_saldo()}")
    elif pilihan == '5':
        app.undo_transaksi()
    elif pilihan == '6':
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid.")
