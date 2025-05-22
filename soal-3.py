# Buat program Python yang mensimulasikan sistem yang mendukung fungsi pembaca ebook. Anda harus menyertakan metode bagi pengguna sistem Anda untuk "membeli"
# buku baru, melihat daftar buku yang dibeli, dan membaca buku yang dibeli. 

class Buku:
    def __init__(self, judul, penulis, harga, konten):
        self.judul = judul
        self.penulis = penulis
        self.harga = harga
        self.konten = konten

    def baca(self):
        print(f"\nMembaca: '{self.judul}' oleh {self.penulis}")
        print("Isi buku:")
        print(self.konten)

class TokoBuku:
    def __init__(self):
        # Daftar buku yang tersedia di toko
        self.daftar_buku = [
            Buku("Laskar Pelangi", "Andrea Hirata", 50000, "Ini adalah cerita tentang perjuangan anak-anak di Belitung..."),
            Buku("Bumi Manusia", "Pramoedya Ananta Toer", 75000, "Sebuah kisah cinta di tengah kolonialisme..."),
            Buku("Dilan 1990", "Pidi Baiq", 45000, "Cinta remaja antara Dilan dan Milea...")
        ]

    def tampilkan_buku_tersedia(self):
        print("\n=== Daftar Buku di Toko ===")
        for i, buku in enumerate(self.daftar_buku, 1):
            print(f"{i}. {buku.judul} - {buku.penulis} (Rp{buku.harga})")

    def beli_buku(self, indeks):
        if 0 <= indeks < len(self.daftar_buku):
            return self.daftar_buku[indeks]
        return None

class Pengguna:
    def __init__(self, nama):
        self.nama = nama
        self.koleksi_buku = []
        self.saldo = 100000  # Saldo awal pengguna

    def beli_buku(self, toko):
        toko.tampilkan_buku_tersedia()
        try:
            pilihan = int(input("\nMasukkan nomor buku yang ingin dibeli (0 untuk batal): ")) - 1
            if pilihan == -1:
                print("Pembelian dibatalkan.")
                return
            buku = toko.beli_buku(pilihan)
            if buku:
                if self.saldo >= buku.harga:
                    self.saldo -= buku.harga
                    self.koleksi_buku.append(buku)
                    print(f"\nBerhasil membeli '{buku.judul}' seharga Rp{buku.harga}!")
                    print(f"Sisa saldo: Rp{self.saldo}")
                else:
                    print("\nSaldo tidak cukup untuk membeli buku ini.")
            else:
                print("\nNomor buku tidak valid.")
        except ValueError:
            print("\nInput harus berupa angka.")

    def lihat_koleksi(self):
        if not self.koleksi_buku:
            print("\nAnda belum membeli buku.")
        else:
            print("\n=== Koleksi Buku Anda ===")
            for i, buku in enumerate(self.koleksi_buku, 1):
                print(f"{i}. {buku.judul} - {buku.penulis}")

    def baca_buku(self):
        self.lihat_koleksi()
        if self.koleksi_buku:
            try:
                pilihan = int(input("\nMasukkan nomor buku yang ingin dibaca (0 untuk batal): ")) - 1
                if pilihan == -1:
                    print("Pembacaan dibatalkan.")
                    return
                if 0 <= pilihan < len(self.koleksi_buku):
                    self.koleksi_buku[pilihan].baca()
                else:
                    print("\nNomor buku tidak valid.")
            except ValueError:
                print("\nInput harus berupa angka.")

def main():
    # Inisialisasi sistem
    pengguna = Pengguna("Andi")
    toko = TokoBuku()

    while True:
        print(f"\n=== Sistem Pembaca eBook (Pengguna: {pengguna.nama}) ===")
        print("1. Beli Buku")
        print("2. Lihat Koleksi Buku")
        print("3. Baca Buku")
        print("4. Keluar")
        try:
            pilihan = int(input("Pilih menu (1-4): "))
            if pilihan == 1:
                pengguna.beli_buku(toko)
            elif pilihan == 2:
                pengguna.lihat_koleksi()
            elif pilihan == 3:
                pengguna.baca_buku()
            elif pilihan == 4:
                print("Terima kasih telah menggunakan sistem pembaca eBook!")
                break
            else:
                print("\nPilihan tidak valid.")
        except ValueError:
            print("\nInput harus berupa angka.")

if __name__ == "__main__":
    main()

#     Penjelasan Program:

# Kelas Buku:
# Menyimpan informasi buku seperti judul, penulis, harga, dan konten.
# Memiliki metode baca() untuk menampilkan isi buku.
# Kelas TokoBuku:
# Menyimpan daftar buku yang tersedia untuk dibeli.
# Memiliki metode tampilkan_buku_tersedia() untuk menampilkan daftar buku.
# Memiliki metode beli_buku() untuk mengembalikan buku berdasarkan indeks yang dipilih.
# Kelas Pengguna:
# Mengelola informasi pengguna seperti nama, saldo, dan koleksi buku.
# Memiliki metode beli_buku() untuk membeli buku dari toko.
# Memiliki metode lihat_koleksi() untuk menampilkan daftar buku yang dimiliki.
# Memiliki metode baca_buku() untuk membaca buku dari koleksi.
# Fungsi main():
# Menyediakan antarmuka berbasis teks untuk berinteraksi dengan sistem.
# Pengguna dapat memilih untuk membeli buku, melihat koleksi, membaca buku, atau keluar.
# Contoh Penggunaan:

# Pengguna memulai program dan melihat menu.
# Memilih opsi "Beli Buku", melihat daftar buku di toko, dan membeli salah satu buku.
# Memilih opsi "Lihat Koleksi Buku" untuk melihat buku yang sudah dibeli.
# Memilih opsi "Baca Buku" untuk membaca salah satu buku dari koleksi.
# Keluar dari program jika selesai.