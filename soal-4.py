# Membuat class dan sublcass berdasarkan gambar diagram yang di berikan

class CreditCard:
    def __init__(self, customer, bank, account, limit):
        self._customer = customer
        self._bank = bank
        self._account = account
        self._limit = limit
        self._balance = 0.0  # Saldo awal 0
    # Getter methods
    def get_customer(self):
        return self._customer
    def get_bank(self):
        return self._bank
    def get_account(self):
        return self._account
    def get_limit(self):
        return self._limit
    def get_balance(self):
        return self._balance
    # Metode untuk melakukan pembayaran (mengurangi saldo)
    def make_payment(self, amount):
        if amount < 0:
            raise ValueError("Jumlah pembayaran tidak boleh negatif")
        self._balance -= amount
    # Metode untuk melakukan pembelian (menambah saldo)
    def charge(self, price):
        if price < 0:
            raise ValueError("Harga tidak boleh negatif")
        if price + self._balance > self._limit:  # Cek jika melebihi limit
            return False
        else:
            self._balance += price
            return True
class PredatoryCreditCard(CreditCard):
    def __init__(self, customer, bank, account, limit, apr):
        super().__init__(customer, bank, account, limit)
        self._apr = apr  # Annual Percentage Rate (suku bunga tahunan)
    # Override metode charge dengan biaya tambahan jika gagal
    def charge(self, price):
        success = super().charge(price)  # Panggil metode charge dari kelas induk
        if not success:
            self._balance += 5000  # Biaya penalti Rp5000 jika gagal
        return success
    # Metode untuk menghitung bunga bulanan berdasarkan APR
    def process_month(self):
        if self._balance > 0:
            # Hitung bunga bulanan (APR dibagi 12 untuk mendapatkan bunga bulanan)
            monthly_factor = (self._apr / 100) / 12
            monthly_interest = self._balance * monthly_factor
            self._balance += monthly_interest

# Contoh penggunaan
if __name__ == "__main__":
    # Membuat objek CreditCard
    kartu_biasa = CreditCard("Andi", "Bank XYZ", "1234-5678", 100000)
    print("=== Kartu Biasa ===")
    print(f"Saldo awal: Rp{kartu_biasa.get_balance()}")
    print(f"Limit: Rp{kartu_biasa.get_limit()}")
    kartu_biasa.charge(30000)  # Berhasil
    print(f"Saldo setelah belanja Rp30000: Rp{kartu_biasa.get_balance()}")
    kartu_biasa.make_payment(10000)
    print(f"Saldo setelah bayar Rp10000: Rp{kartu_biasa.get_balance()}")

    # Membuat objek PredatoryCreditCard
    kartu_predatory = PredatoryCreditCard("Budi", "Bank ABC", "9876-5432", 50000, 20)  # APR 20%
    print("\n=== Kartu Predatory ===")
    print(f"Saldo awal: Rp{kartu_predatory.get_balance()}")
    print(f"Limit: Rp{kartu_predatory.get_limit()}")
    kartu_predatory.charge(40000)  # Berhasil
    print(f"Saldo setelah belanja Rp40000: Rp{kartu_predatory.get_balance()}")
    kartu_predatory.charge(20000)  # Gagal, melebihi limit, dikenakan penalti Rp5000
    print(f"Saldo setelah gagal belanja Rp20000: Rp{kartu_predatory.get_balance()}")
    kartu_predatory.process_month()  # Proses bunga bulanan
    print(f"Saldo setelah proses bunga bulanan: Rp{kartu_predatory.get_balance()}")

#     Penjelasan Program:

# Kelas CreditCard:
# Memiliki field _customer, _bank, _account, _limit, dan _balance.
# Metode getter (get_customer(), get_bank(), dll.) untuk mengakses field.
# Metode charge(price) untuk melakukan pembelian; mengembalikan True jika berhasil (tidak melebihi limit) dan False jika gagal.
# Metode make_payment(amount) untuk mengurangi saldo.
# Kelas PredatoryCreditCard:
# Mewarisi CreditCard.
# Menambahkan field _apr untuk suku bunga tahunan.
# Meng-override metode charge(price) untuk menambahkan penalti Rp5000 jika pembelian gagal.
# Memiliki metode process_month() untuk menghitung bunga bulanan berdasarkan APR (dibagi 12 untuk bulanan) dan menambahkannya ke saldo.
# Contoh Penggunaan:
# Membuat instance dari CreditCard dan PredatoryCreditCard.
# Menguji fungsi seperti pembelian, pembayaran, dan proses bunga bulanan.