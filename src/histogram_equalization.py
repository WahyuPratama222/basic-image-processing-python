import cv2

# Membaca gambar hasil averaging dari soal 2 sebagai input
img = cv2.imread("img/hasil_soal2/soal2_averaged.jpg")

# Mengubah ke grayscale karena histogram equalization bekerja pada 1 channel intensitas
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Histogram Equalization: meratakan distribusi histogram
hasil = cv2.equalizeHist(gray)

# Menyimpan hasil
cv2.imwrite("img/hasil_soal3/soal3_before.jpg", gray)  # gambar gelap sebelum equalization
cv2.imwrite("img/hasil_soal3/soal3_after.jpg",  hasil) # gambar setelah equalization

print("Soal 3 done → hasil_soal3/")