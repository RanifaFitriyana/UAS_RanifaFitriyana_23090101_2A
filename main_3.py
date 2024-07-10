import soal_3 as exe

def pilihan():
    print(f'Jumlah pesanan : {exe.jumlah_pesanan()}')
    print(f'Pilihan:')

    print(f'1. Tambah pesanan')
    print(f'2. pesanan Selanjutnya')
    print(f'3. Lihat jumlah pesanan')
    print(f'4. Keluar')
    pilihan = int(input('Masukkan Pilihan : '))
    if pilihan == 1:
        data = str(input('Masukkan Nama Pelanggan : '))
        exe.tambah_pesanan(data)
    elif pilihan == 2:
        f = exe.pesanan_selanjutnya()
        print(f'Pelanggan selanjutnya adalah {f}')
    
while True:
    pilihan()
