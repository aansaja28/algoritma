# Quick Sort Implementation
def quick_sort(arr):
    """
    Quick Sort menggunakan metode divide and conquer untuk mengurutkan array.
    Kasus Terbaik: O(n log n) - Terjadi jika pivot membagi array menjadi dua bagian yang hampir sama besar.
    Kasus Terburuk: O(n^2) - Terjadi jika pivot selalu menjadi elemen terkecil atau terbesar (contoh: array sudah terurut).
    Kasus Rata-rata: O(n log n) - Terjadi pada kondisi umum jika pivot dipilih secara acak atau mendekati nilai tengah.
    """
    if len(arr) <= 1:  # Kondisi dasar: array dengan 1 elemen atau kosong sudah terurut
        return arr
    else:
        pivot = arr[len(arr) // 2]  # Memilih elemen tengah sebagai pivot
        left = [x for x in arr if x < pivot]  # Elemen-elemen lebih kecil dari pivot
        middle = [x for x in arr if x == pivot]  # Elemen-elemen sama dengan pivot
        right = [x for x in arr if x > pivot]  # Elemen-elemen lebih besar dari pivot
        return quick_sort(left) + middle + quick_sort(right)  # Rekursif untuk mengurutkan dan menggabungkan

# Merge Sort Implementation
def merge_sort(arr):
    """
    Merge Sort menggunakan metode divide and conquer untuk mengurutkan array.
    Kasus Terbaik: O(n log n) - Terjadi tanpa memperhatikan urutan awal array karena array selalu dibagi dan digabung.
    Kasus Terburuk: O(n log n) - Sama seperti kasus terbaik karena proses pembagian dan penggabungan tetap konsisten.
    Kasus Rata-rata: O(n log n) - Waktu rata-rata sama dengan kasus terbaik dan terburuk karena strukturnya stabil.
    """
    if len(arr) > 1:
        mid = len(arr) // 2  # Menentukan titik tengah array
        left_half = arr[:mid]  # Membagi array menjadi bagian kiri
        right_half = arr[mid:]  # Membagi array menjadi bagian kanan

        # Rekursif untuk mengurutkan kedua bagian
        merge_sort(left_half)
        merge_sort(right_half)

        # Menggabungkan dua bagian yang sudah diurutkan
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Menyalin elemen yang tersisa dari bagian kiri (jika ada)
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Menyalin elemen yang tersisa dari bagian kanan (jika ada)
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

# Testing the Sorting Algorithms
import random

# Membuat 50 angka acak antara 0 dan 100
random_numbers = [random.randint(0, 100) for _ in range(50)]

# Uji Quick Sort
quick_sorted_numbers = quick_sort(random_numbers.copy())
print("Hasil Quick Sort:", quick_sorted_numbers)

# Uji Merge Sort
merge_sorted_numbers = merge_sort(random_numbers.copy())
print("Hasil Merge Sort:", merge_sorted_numbers)
