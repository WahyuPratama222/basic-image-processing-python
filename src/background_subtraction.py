import cv2
import numpy as np

bg  = cv2.imread("img/image_soal1/no_object.jpeg")
obj = cv2.imread("img/image_soal1/with_object.jpeg")

# Mengambil tinggi dan lebar dari gambar background sebagai referensi ukuran
height, width = bg.shape[:2]

# Menyamakan ukuran gambar objek dengan gambar background
obj = cv2.resize(obj, (width, height))

# Mengubah kedua gambar ke grayscale
bg_gray  = cv2.cvtColor(bg,  cv2.COLOR_BGR2GRAY)
obj_gray = cv2.cvtColor(obj, cv2.COLOR_BGR2GRAY)

# Operasi pengurangan: with_object - no_object
# clip(0, 255) agar nilai negatif tidak wrap-around
diff = np.clip(obj_gray.astype(np.int16) - bg_gray.astype(np.int16), 0, 255).astype(np.uint8)

# Menyimpan hasil
cv2.imwrite("img/hasil_soal1/soal1_before.jpg", bg_gray)   # background grayscale
cv2.imwrite("img/hasil_soal1/soal1_after.jpg",  obj_gray)  # gambar dengan objek grayscale
cv2.imwrite("img/hasil_soal1/soal1_diff.jpg",   diff)      # hasil pengurangan (objek putih, bg hitam)

print("Soal 1 done → hasil_soal1/")