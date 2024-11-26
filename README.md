Nama : Anugrah Ahmad Wiranto 
Nim : F55123069
Kelas : TI B

# Analisis Quiz 2
- Naive Sort
Naive Sort (seperti Bubble Sort) memiliki kompleksitas terbaik pada kasus O(n) ketika daftar sudah terurut. Dalam kasus terbaik, algoritma hanya melakukan satu kali iterasi melalui elemen-elemen untuk memeriksa bahwa tidak ada yang perlu ditukar. Karena tidak ada operasi penukaran yang dilakukan, waktu eksekusinya sangat efisien dibandingkan dengan kasus rata-rata atau terburuk, yang memiliki kompleksitas O(n²). Namun, pada daftar besar, metode ini tetap tidak efisien dibandingkan dengan algoritma yang lebih canggih.

- Merge Sort
Merge Sort menggunakan pendekatan divide and conquer untuk membagi masalah menjadi sub-masalah yang lebih kecil. Kasus terbaik Merge Sort juga memiliki kompleksitas waktu O(n log n), karena algoritma tetap membagi array dan menggabungkannya kembali terlepas dari apakah array sudah terurut. Namun, waktu penggabungan lebih efisien pada kasus terbaik jika elemen-elemen di masing-masing sub-array sudah berada dalam urutan yang sesuai. Merge Sort unggul dalam menangani daftar besar dibandingkan dengan Naive Sort karena efisiensi struktur rekursifnya.

Kesimpulan
Naive Sort paling cocok untuk daftar kecil atau ketika data sudah hampir seluruhnya terurut, karena waktu eksekusinya bisa mendekati O(n).
Merge Sort lebih unggul untuk dataset besar karena kompleksitasnya tetap O(n log n), terlepas dari kondisi input.