import random
import time
import sys
import matplotlib.pyplot as plt

# Meningkatkan batas rekursi untuk menangani metode rekursif pada data besar
sys.setrecursionlimit(10**6)

# ==========================================
# BAGIAN 1: FUNGSI PARTISI (Dipakai Semua Algoritma)
# ==========================================
def partition(arr, low, high):
    """
    Fungsi inti untuk membagi array menjadi dua bagian berdasarkan pivot.
    Menggunakan Randomized Pivot untuk menghindari worst-case O(n^2).
    """
    rand_idx = random.randint(low, high)
    arr[high], arr[rand_idx] = arr[rand_idx], arr[high]
    
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# ==========================================
# BAGIAN 2: IMPLEMENTASI ALGORITMA
# ==========================================

# --- A. QUICKSELECT ---

def quickselect_recursive(arr, low, high, k):
    """Quickselect versi Rekursif"""
    if low == high:
        return arr[low]
    
    pivot_index = partition(arr, low, high)
    
    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return quickselect_recursive(arr, low, pivot_index - 1, k)
    else:
        return quickselect_recursive(arr, pivot_index + 1, high, k)

def quickselect_iterative(arr, k):
    """Quickselect versi Iteratif (Pakai While Loop)"""
    low = 0
    high = len(arr) - 1
    while low <= high:
        if low == high:
            return arr[low]
        
        pivot_index = partition(arr, low, high)
        
        if k == pivot_index:
            return arr[k]
        elif k < pivot_index:
            high = pivot_index - 1
        else:
            low = pivot_index + 1
    return None

# --- B. SORTING (QUICKSORT) ---

def quicksort_recursive(arr, low, high):
    """Quicksort versi Rekursif"""
    if low < high:
        pi = partition(arr, low, high)
        quicksort_recursive(arr, low, pi - 1)
        quicksort_recursive(arr, pi + 1, high)

def quicksort_iterative(arr):
    """Quicksort versi Iteratif (Pakai Stack Manual)"""
    low = 0
    high = len(arr) - 1
    
    # Buat stack manual
    stack = [(low, high)]
    
    while stack:
        l, h = stack.pop()
        if l < h:
            pi = partition(arr, l, h)
            # Dorong bagian kiri dan kanan ke stack
            # (Tips: Dorong yang lebih besar dulu agar stack tidak terlalu dalam)
            if pi - 1 > l:
                stack.append((l, pi - 1))
            if pi + 1 < h:
                stack.append((pi + 1, h))

# ==========================================
# BAGIAN 3: WRAPPER FUNCTION (Untuk Benchmark)
# ==========================================

def run_qs_recursive(data_asli, k):
    arr = data_asli[:]
    return quickselect_recursive(arr, 0, len(arr)-1, k-1)

def run_qs_iterative(data_asli, k):
    arr = data_asli[:]
    return quickselect_iterative(arr, k-1)

def run_sort_recursive(data_asli, k):
    arr = data_asli[:]
    quicksort_recursive(arr, 0, len(arr)-1)
    return arr[k-1]

def run_sort_iterative(data_asli, k):
    arr = data_asli[:]
    quicksort_iterative(arr)
    return arr[k-1]

# ==========================================
# BAGIAN 4: PROGRAM UTAMA
# ==========================================
def main():
    print("\n" + "="*90)
    print("PROGRAM PENELITIAN: PERBANDINGAN KOMPREHENSIF".center(90))
    print("QUICKSELECT (Rec/Iter) vs SORTING (Rec/Iter)".center(90))
    print("="*90 + "\n")
    
    # --- SETUP GRAFIK INTERAKTIF ---
    plt.ion()
    fig, ax = plt.subplots(figsize=(12, 7))
    
    # Inisialisasi 4 Garis untuk 4 Metode
    line_qs_rec, = ax.plot([], [], 'b-o', label='Quickselect Rekursif (O(n))', linewidth=2)
    line_qs_iter, = ax.plot([], [], 'c--o', label='Quickselect Iteratif (O(n))')
    line_sort_rec, = ax.plot([], [], 'r-x', label='Quicksort Rekursif (O(n log n))', linewidth=2)
    line_sort_iter, = ax.plot([], [], 'm--x', label='Quicksort Iteratif (O(n log n))')
    
    ax.set_title('Perbandingan Kinerja: Rekursif vs Iteratif')
    ax.set_xlabel('Ukuran Data (N)')
    ax.set_ylabel('Waktu Eksekusi (Detik)')
    ax.legend()
    ax.grid(True)
    
    plt.show()

    # Penyimpanan Data
    hist_n = []
    hist_qs_rec, hist_qs_iter = [], []
    hist_sort_rec, hist_sort_iter = [], []

    while True:
        try:
            user_input = input(">>> Masukkan N (atau 'exit'): ")
            if user_input.lower() in ['exit', 'selesai']:
                print("Program selesai.")
                break
            
            n = int(user_input)
            if n <= 0: continue

            # Generate Data
            print(f"   -> Generate {n} data...", end="\r")
            data = [random.randint(1, 10000000) for _ in range(n)]
            k = n // 2
            
            # --- 1. Quickselect Rekursif ---
            start = time.perf_counter()
            run_qs_recursive(data, k)
            t_qs_rec = time.perf_counter() - start

            # --- 2. Quickselect Iteratif ---
            start = time.perf_counter()
            run_qs_iterative(data, k)
            t_qs_iter = time.perf_counter() - start

            # --- 3. Sorting (Quicksort) Rekursif ---
            start = time.perf_counter()
            run_sort_recursive(data, k)
            t_sort_rec = time.perf_counter() - start

            # --- 4. Sorting (Quicksort) Iteratif ---
            start = time.perf_counter()
            run_sort_iterative(data, k)
            t_sort_iter = time.perf_counter() - start

            # Simpan History
            hist_n.append(n)
            hist_qs_rec.append(t_qs_rec)
            hist_qs_iter.append(t_qs_iter)
            hist_sort_rec.append(t_sort_rec)
            hist_sort_iter.append(t_sort_iter)

            # Tampilkan Tabel Hasil
            print(" " * 50, end="\r")
            print(f"   [Hasil Pengujian N={n}]")
            print(f"   1. Quickselect (Rekursif) : {t_qs_rec:.6f} s")
            print(f"   2. Quickselect (Iteratif) : {t_qs_iter:.6f} s")
            print(f"   3. Quicksort   (Rekursif) : {t_sort_rec:.6f} s")
            print(f"   4. Quicksort   (Iteratif) : {t_sort_iter:.6f} s")
            print("-" * 60)

            # Update Grafik
            combined = sorted(zip(hist_n, hist_qs_rec, hist_qs_iter, hist_sort_rec, hist_sort_iter))
            sn, sqr, sqi, ssr, ssi = zip(*combined)

            line_qs_rec.set_data(sn, sqr)
            line_qs_iter.set_data(sn, sqi)
            line_sort_rec.set_data(sn, ssr)
            line_sort_iter.set_data(sn, ssi)

            ax.relim()
            ax.autoscale_view()
            plt.draw()
            plt.pause(0.1)

        except ValueError:
            print("   [!] Input angka tidak valid.")
        except RecursionError:
             print("   [!] Error: Stack Overflow pada metode Rekursif (N terlalu besar).")

    plt.ioff()
    plt.show()

if __name__ == "__main__":
    main()