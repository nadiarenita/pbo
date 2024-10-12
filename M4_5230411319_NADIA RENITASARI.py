class KelolaDebitur:
    def _init_(self):
        self.debitur_list = []

    def tambah_debitur(self, nama, ktp, limit_pinjaman):
        for debitur in self.debitur_list:
            if debitur['ktp'] == ktp:
                print("Validasi gagal: KTP sudah terdaftar")
                return
        self.debitur_list.append({
            'nama': nama,
            'ktp': ktp,
            'limit_pinjaman': limit_pinjaman,
            'pinjaman_list': []
        })
        print("Debitur berhasil ditambahkan")

    def cari_debitur(self, nama):
        for debitur in self.debitur_list:
            if debitur['nama'] == nama:
                print("=======================================================")
                print(f"Nama: {debitur['nama']}")
                print(f"KTP: {debitur['ktp']}")
                print(f"Limit Pinjaman: {debitur['limit_pinjaman']}")
                print("=======================================================")
                return debitur
        print("Debitur tidak ditemukan")
        return None

    def tampilkan_debitur(self):
        if not self.debitur_list:
            print("Tidak ada debitur")
            return
        for debitur in self.debitur_list:
            print("=======================================================")
            print(f"Nama: {debitur['nama']}")
            print(f"KTP: {debitur['ktp']}")
            print(f"Limit Pinjaman: {debitur['limit_pinjaman']}")
            print("=======================================================")


class KelolaPinjaman:
    def tambah_pinjaman(self, debitur, pinjaman, bunga, bulan_angsuran):
        if pinjaman > debitur['limit_pinjaman']:
            print("Validasi gagal: Pinjaman melebihi limit")
            return
        angsuran_pokok = pinjaman * (bunga / 100)
        angsuran_bulanan = angsuran_pokok / bulan_angsuran
        total_angsuran = angsuran_pokok + angsuran_bulanan

        debitur['pinjaman_list'].append({
            'pinjaman': pinjaman,
            'bunga': bunga,
            'bulan_angsuran': bulan_angsuran,
            'angsuran_pokok': angsuran_pokok,
            'angsuran_bulanan': angsuran_bulanan,
            'total_angsuran': total_angsuran
        })
        print("Pinjaman berhasil ditambahkan")

    def tampilkan_pinjaman(self, debitur):
        if not debitur['pinjaman_list']:
            print(f"Tidak ada pinjaman untuk debitur {debitur['nama']}")
            return
        for pinjaman in debitur['pinjaman_list']:
            print("=======================================================")
            print(f"Nama: {debitur['nama']}")
            print(f"Pinjaman: {pinjaman['pinjaman']}")
            print(f"Bunga: {pinjaman['bunga']}%")
            print(f"Bulan Angsuran: {pinjaman['bulan_angsuran']}")
            print(f"Angsuran Pokok: {pinjaman['angsuran_pokok']}")
            print(f"Angsuran Bulanan: {pinjaman['angsuran_bulanan']}")
            print(f"Total Angsuran: {pinjaman['total_angsuran']}")
            print("=======================================================")


def main():
    kelola_debitur = KelolaDebitur()
    kelola_pinjaman = KelolaPinjaman()

    while True:
        print("=====================================")
        print("========PINJAMAN TANPA RIBET=========")
        print("1. Kelola Debitur")
        print("2. Kelola Pinjaman")
        print("3. Keluar")
        print("=====================================")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            while True:
                print("1. Tambah Debitur")
                print("2. Cari Debitur")
                print("3. Tampilkan Debitur")
                print("4. Keluar")

                sub_pilihan = input("Pilih Menu: ")

                if sub_pilihan == "1":
                    nama = input("Masukkan Nama Debitur: ")
                    ktp = input("Masukkan KTP Debitur: ")
                    limit_pinjaman = int(input("Masukkan Limit Pinjaman: "))
                    kelola_debitur.tambah_debitur(nama, ktp, limit_pinjaman)

                elif sub_pilihan == "2":
                    nama = input("Masukkan Nama debitur: ")
                    kelola_debitur.cari_debitur(nama)

                elif sub_pilihan == "3":
                    kelola_debitur.tampilkan_debitur()

                elif sub_pilihan == "4":
                    break
                else:
                    print("Menu tidak valid")
        
        elif pilihan == "2":
            while True:
                print("1. Tambah Pinjaman")
                print("2. Tampilkan Pinjaman")
                print("3. Keluar")

                sub_pilihan = input("Masukkan Pilihan Menu: ")

                if sub_pilihan == "1":
                    nama = input("Masukkan Nama Debitur: ")
                    debitur = kelola_debitur.cari_debitur(nama)
                    if debitur:
                        pinjaman = int(input("Masukkan pinjaman: "))
                        bunga = int(input("Masukkan bunga: "))
                        bulan_angsuran = int(input("Masukkan bulan angsuran: "))
                        kelola_pinjaman.tambah_pinjaman(debitur, pinjaman, bunga, bulan_angsuran)

                elif sub_pilihan == "2":
                    nama = input("Masukkan nama debitur: ")
                    debitur = kelola_debitur.cari_debitur(nama)
                    if debitur:
                        kelola_pinjaman.tampilkan_pinjaman(debitur)

                elif sub_pilihan == "3":
                    break
                else:
                    print("Menu tidak valid")

        elif pilihan == "3":
            break
        else:
            print("Menu tidak tersedia")  


if __name__ == "__main__":
    main()