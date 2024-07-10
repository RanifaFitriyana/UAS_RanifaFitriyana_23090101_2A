from collections import deque

pesanan = deque()

def tambah_pesanan(data):
    pesanan.append(data)

def pesanan_selanjutnya():
    if len(pesanan) < 1:
        return 'pesanan kosong'
    else:
        pesanan.popleft()

def jumlah_pesanan():
    return len(pesanan)

pesanan_selanjutnya()