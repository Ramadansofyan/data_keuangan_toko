import csv
from struktur_data import Stack, HashMap

class KeuanganToko:
    def __init__(self, file_csv):
        self.file_csv = file_csv
        self.histori = Stack()
        self.transaksi = HashMap()
        self._muat_data()

    def _muat_data(self):
        try:
            with open(self.file_csv, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.transaksi.tambah(row['id'], row)
        except FileNotFoundError:
            open(self.file_csv, 'w').close()

    def tambah_transaksi(self, id, tipe, jumlah):
        transaksi = {
            'id': id,
            'tipe': tipe,
            'jumlah': int(jumlah)
        }
        self.transaksi.tambah(id, transaksi)
        self.histori.push(transaksi)
        self._simpan_csv()

    def undo_transaksi(self):
        data = self.histori.pop()
        if data:
            self.transaksi.map.pop(data['id'], None)
            self._simpan_csv()
            print("Transaksi berhasil dihapus.")
        else:
            print("Tidak ada transaksi yang bisa di-undo.")

    def tampilkan_semua(self):
        for t in self.transaksi.semua_data().values():
            print(t)

    def cari_transaksi(self, id):
        return self.transaksi.cari(id)

    def hitung_saldo(self):
        saldo = 0
        for t in self.transaksi.semua_data().values():
            jumlah = int(t['jumlah'])
            if t['tipe'] == 'masuk':
                saldo += jumlah
            else:
                saldo -= jumlah
        return saldo

    def _simpan_csv(self):
        with open(self.file_csv, mode='w', newline='') as file:
            fieldnames = ['id', 'tipe', 'jumlah']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for t in self.transaksi.semua_data().values():
                writer.writerow(t)
