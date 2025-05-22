# Buat kelas Python, Bunga, yang memiliki tiga variabel instan bertipe str, int, dan float,
# yang masing-masing mewakili nama bunga, jumlah kelopaknya, dan harganya. Kelas Anda
# harus menyertakan metode konstruktor yang menginisialisasi setiap variabel ke nilai yang
# sesuai, dan kelas Anda harus menyertakan metode untuk memberikan nilai setiap jenis,
# dan mengambil nilai setiap jenis.

class Bunga:
    def __init__(self, nama: str, jumlah_kelopak: int, harga: float):
        self.nama = nama
        self.jumlah_kelopak = jumlah_kelopak
        self.harga = harga

    # Metode untuk mengatur nilai (setter)
    def set_nama(self, nama: str):
        self.nama = nama

    def set_jumlah_kelopak(self, jumlah_kelopak: int):
        self.jumlah_kelopak = jumlah_kelopak

    def set_harga(self, harga: float):
        self.harga = harga

    # Metode untuk mengambil nilai (getter)
    def get_nama(self) -> str:
        return self.nama

    def get_jumlah_kelopak(self) -> int:
        return self.jumlah_kelopak

    def get_harga(self) -> float:
        return self.harga

# Contoh penggunaan kelas Bunga
if __name__ == "__main__":
    bunga = Bunga("Mawar", 5, 15000.0)
    
    # Mengambil nilai awal
    print("Nama bunga:", bunga.get_nama())
    print("Jumlah kelopak:", bunga.get_jumlah_kelopak())
    print("Harga:", bunga.get_harga())

    # Mengatur nilai baru
    bunga.set_nama("Melati")
    bunga.set_jumlah_kelopak(4)
    bunga.set_harga(20000.0)

    # Mengambil nilai setelah diubah
    print("\nSetelah diubah:")
    print("Nama bunga:", bunga.get_nama())
    print("Jumlah kelopak:", bunga.get_jumlah_kelopak())
    print("Harga:", bunga.get_harga())