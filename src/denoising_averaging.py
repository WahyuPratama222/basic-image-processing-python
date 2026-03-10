import cv2
import numpy as np
import glob

# Mengambil semua path file foto dari folder image_soal2, diurutkan by nama
paths = sorted(glob.glob("img/image_soal2/*.jpg"))
print(f"Ditemukan {len(paths)} foto")

# Membaca foto pertama sebagai referensi ukuran
ref = cv2.imread(paths[0])

# Mengambil tinggi dan lebar referensi
height, width = ref.shape[:2]

# Membuat array kosong (semua nol) sebagai tempat akumulasi penjumlahan piksel
# dtype float64 agar tidak overflow saat menjumlahkan banyak gambar
acc = np.zeros((height, width, 3), dtype=np.float64)

# Menjumlahkan semua foto piksel per piksel dan di-resize dulu agar ukurannya sama
for p in paths:
    acc += cv2.resize(cv2.imread(p), (width, height)).astype(np.float64)

# Di-cast ke uint8 karena nilai piksel harus 0-255
averaged = (acc / len(paths)).astype(np.uint8)

# Menyimpan hasil
cv2.imwrite("img/hasil_soal2/soal2_before.jpg",   ref)      # salah satu foto mentah (noisy)
cv2.imwrite("img/hasil_soal2/soal2_averaged.jpg", averaged) # hasil setelah averaging (denoised)

print("Soal 2 done → hasil_soal2/")