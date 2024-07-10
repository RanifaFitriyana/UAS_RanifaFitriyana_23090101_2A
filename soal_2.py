import pandas as pd
import numpy as np

dataNilai = [
    [90, 80],
    [50, 60],
    [65, 70],
]

Nama = ['Mahasiswa 1', 'Mahasiswa 2', 'Mahasiswa 3']
MataKuliah = ['Algoritma dan Struktur Data 2', 'Matematika Numerik']

df = pd.DataFrame(dataNilai, index=Nama, columns=MataKuliah)
print(df)

rata_rata_matakuliah = df.mean(axis=0)
rata_rata_mahasiswa = df.mean(axis=1)
print("====================================")
print("Nilai Rata-rata Setiap Mata Kuliah :\n", rata_rata_matakuliah)
print("Nilai Rata-rata Setiap Mahasiswa :\n", rata_rata_mahasiswa)
print("====================================")
