import pandas as pd

def input_data():
    mahasiswa = []
    while True:
        nim = input("Masukkan NIM: ")
        nama = input("Masukkan Nama: ")
        mahasiswa.append({'NIM': nim, 'Nama': nama})

        tambah_lagi = input("Apakah Anda ingin menambahkan data lagi? (y/t): ").lower()
        if tambah_lagi != 'y':
            break
    return mahasiswa

def tampilkan_data(mahasiswa):
    df = pd.DataFrame(mahasiswa)
    print("\nData Mahasiswa:")
    print(df)

if __name__ == "__main__":
    data_mahasiswa = input_data()
    tampilkan_data(data_mahasiswa)
