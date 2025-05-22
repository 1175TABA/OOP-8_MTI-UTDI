# Buat kelas dengan pewarisan kelas untuk kumpulan kelas berikut: 
# 1. Class Kambing memperluas class Binatang dan menambahkan variabel instan ekor dan metode susu( ) dan lompat(). 
# 2. Class Gajah memperluas class Binatang dan menambahkan variabel instan hidung dan metode makan(makanan) dan bersuara( ). 
# 3. Class Kuda memperluas class Binatang dan menambahkan variabel instan tinggi dan warna, serta metode lari() dan lompat(). 
# 4. Class Pembalap memperluas class Kuda dan menambahkan metode balapan(). 
# 5. Class Berkuda memperluas class Kuda, menambahkan bobot variabel instan dan metode berlari( ) dan dilatih( ).

# Kelas induk Binatang
class Binatang:
    def __init__(self, nama):
        self.nama = nama

    def bergerak(self):
        print(f"{self.nama} sedang bergerak.")

# Kelas Kambing mewarisi Binatang
class Kambing(Binatang):
    def __init__(self, nama, ekor):
        super().__init__(nama)
        self.ekor = ekor

    def susu(self):
        print(f"{self.nama} sedang menghasilkan susu.")

    def lompat(self):
        print(f"{self.nama} melompat dengan ekor {self.ekor}.")

# Kelas Gajah mewarisi Binatang
class Gajah(Binatang):
    def __init__(self, nama, hidung):
        super().__init__(nama)
        self.hidung = hidung

    def makan(self, makanan):
        print(f"{self.nama} makan {makanan} menggunakan hidung {self.hidung}.")

    def bersuara(self):
        print(f"{self.nama} bersuara: Teruuu!")

# Kelas Kuda mewarisi Binatang
class Kuda(Binatang):
    def __init__(self, nama, tinggi, warna):
        super().__init__(nama)
        self.tinggi = tinggi
        self.warna = warna

    def lari(self):
        print(f"{self.nama} berlari cepat dengan tinggi {self.tinggi} cm dan warna {self.warna}.")

    def lompat(self):
        print(f"{self.nama} melompat tinggi dengan tubuh {self.warna}.")

# Kelas Pembalap mewarisi Kuda
class Pembalap(Kuda):
    def __init__(self, nama, tinggi, warna):
        super().__init__(nama, tinggi, warna)

    def balapan(self):
        print(f"{self.nama} sedang balapan dengan kecepatan tinggi!")

# Kelas Berkuda mewarisi Kuda
class Berkuda(Kuda):
    def __init__(self, nama, tinggi, warna, bobot):
        super().__init__(nama, tinggi, warna)
        self.bobot = bobot

    def berlari(self):
        print(f"{self.nama} berlari dengan bobot {self.bobot} kg.")

    def dilatih(self):
        print(f"{self.nama} sedang dilatih untuk menjadi kuda berkuda yang lebih baik.")

# Contoh penggunaan kelas-kelas
if __name__ == "__main__":
    # Membuat objek Kambing
    kambing = Kambing("Kambing A", "pendiam")
    print("=== Kambing ===")
    kambing.bergerak()
    kambing.susu()
    kambing.lompat()

    # Membuat objek Gajah
    gajah = Gajah("Gajah B", "panjang")
    print("\n=== Gajah ===")
    gajah.bergerak()
    gajah.makan("rumput")
    gajah.bersuara()

    # Membuat objek Kuda
    kuda = Kuda("Kuda C", 150, "coklat")
    print("\n=== Kuda ===")
    kuda.bergerak()
    kuda.lari()
    kuda.lompat()

    # Membuat objek Pembalap
    pembalap = Pembalap("Pembalap D", 160, "hitam")
    print("\n=== Pembalap ===")
    pembalap.bergerak()
    pembalap.lari()
    pembalap.balapan()

    # Membuat objek Berkuda
    berkuda = Berkuda("Berkuda E", 155, "putih", 400)
    print("\n=== Berkuda ===")
    berkuda.bergerak()
    berkuda.lari()
    berkuda.berlari()
    berkuda.dilatih()