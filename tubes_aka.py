import random
import time
import sys
import matplotlib.pyplot as plt

# Meningkatkan batas rekursi
sys.setrecursionlimit(10**6)

# ==========================================
# BAGIAN 1: ALGORITMA (Quickselect & Sorting)
# ==========================================
def partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[high], arr[pivot_index] = arr[pivot_index], arr[high]
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickselect(arr, low, high, k):
    if low == high: return arr[low]
    pivot_index = partition(arr, low, high)
    if k == pivot_index: return arr[k]
    elif k < pivot_index: return quickselect(arr, low, pivot_index - 1, k)
    else: return quickselect(arr, pivot_index + 1, high, k)

def run_quickselect(data_asli, k):
    arr = data_asli[:]
    return quickselect(arr, 0, len(arr) - 1, k - 1)

def run_sorting(data_asli, k):
    arr = data_asli[:]
    arr.sort()
    return arr[k - 1]

# ==========================================
# BAGIAN 2: PROGRAM UTAMA (REAL-TIME GRAPH)
# ==========================================
def main():
    print("\n" + "="*80)
    print("PROGRAM PENELITIAN REAL-TIME".center(80))
    print("QUICKSELECT VS SORTING".center(80))
    print("="*80 + "\n")
    print("Instruksi:")
    print("1. Jendela Grafik akan muncul kosong.")
    print("2. Masukkan nilai N di terminal, grafik akan otomatis ter-update.")
    print("3. Ketik 'exit' untuk menutup program.\n")

    # --- SETUP GRAFIK INTERAKTIF ---
    plt.ion()  # Aktifkan Interactive Mode
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Inisialisasi garis kosong
    line_qs, = ax.plot([], [], 'b-o', label='Quickselect (O(n))')
    line_sort, = ax.plot([], [], 'r-x', label='Sorting (O(n log n))')
    
    ax.set_title('Monitoring Real-Time: Quickselect vs Sorting')
    ax.set_xlabel('Ukuran Data (N)')
    ax.set_ylabel('Waktu Eksekusi (Detik)')
    ax.legend()
    ax.grid(True)
    
    # Tampilkan jendela grafik (kosong dulu)
    plt.show()

    # Variabel penyimpanan data
    history_n = []
    history_qs = []
    history_sort = []

    while True:
        try:
            # Input user
            user_input = input(">>> Masukkan Ukuran Data (N): ")
            
            if user_input.lower() in ['exit', 'keluar', 'stop', 'selesai']:
                print("Program selesai. Grafik akhir ditampilkan.")
                break
            
            n = int(user_input)
            if n <= 0:
                print("   [!] Masukkan angka > 0")
                continue

            # Generate Data
            print(f"   -> Sedang generate {n} data acak...", end="\r")
            data = [random.randint(1, 10000000) for _ in range(n)]
            k = n // 2
            
            # --- MULAI BENCHMARK ---
            
            # 1. Ukur Quickselect
            start = time.perf_counter()
            res_qs = run_quickselect(data, k)
            t_qs = time.perf_counter() - start
            
            # 2. Ukur Sorting
            start = time.perf_counter()
            res_sort = run_sorting(data, k)
            t_sort = time.perf_counter() - start
            
            # Simpan data
            history_n.append(n)
            history_qs.append(t_qs)
            history_sort.append(t_sort)

            # --- TAMPILKAN HASIL DETAIL DI TERMINAL ---
            # Menghapus baris "sedang generate" sebelumnya dengan spasi kosong agar bersih
            print(" " * 50, end="\r") 
            
            print(f"   [Hasil N={n}]")
            print(f"   Quickselect (O(n))       : {t_qs:.6f} detik")
            print(f"   Sorting (O(n log n))     : {t_sort:.6f} detik")
            
            # Logika Kesimpulan
            if t_qs < t_sort:
                diff = t_sort / t_qs
                print(f"   => Quickselect {diff:.1f}x LEBIH CEPAT.")
            else:
                print(f"   => Sorting lebih cepat (efek overhead pada data kecil).")
            
            print("-" * 60) # Garis pemisah antar input

            # --- UPDATE GRAFIK SECARA REAL-TIME ---
            combined = sorted(zip(history_n, history_qs, history_sort))
            sorted_n, sorted_qs, sorted_sort = zip(*combined)

            line_qs.set_data(sorted_n, sorted_qs)
            line_sort.set_data(sorted_n, sorted_sort)

            ax.relim()
            ax.autoscale_view()

            plt.draw()
            plt.pause(0.1)

        except ValueError:
            print("   [!] Input tidak valid.")
        except Exception as e:
            print(f"   [!] Error: {e}")

    plt.ioff()
    plt.show()

if __name__ == "__main__":
    main()