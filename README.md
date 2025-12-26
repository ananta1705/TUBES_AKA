# Analisis Komprehensif: Quickselect vs Quicksort (Rekursif & Iteratif)

### Tugas Besar Mata Kuliah Analisis Kompleksitas Algoritma (AKA)

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Matplotlib](https://img.shields.io/badge/Library-Matplotlib-orange.svg)
![Type](https://img.shields.io/badge/Type-Algorithm%20Research-green.svg)

Repository ini berisi implementasi dan analisis perbandingan kinerja algoritma pencarian nilai ke-$k$ (k-th smallest element). Penelitian ini membandingkan **Quickselect** (Seleksi) melawan **Quicksort** (Pengurutan), dengan variasi implementasi secara **Rekursif** dan **Iteratif**.

## 👥 Anggota Tim
| Nama | NIM | Peran |
| :--- | :--- | :--- |
| **Ananta Puti Maharani** | 103122400040 | Implementasi Kode & Analisis |
| **Putri Naila Salsabila** | 103122400048 | Penyusunan Laporan & Visualisasi |

---

## 🎯 Tujuan & Revisi
Penelitian ini dikembangkan untuk menjawab tantangan berikut:
1.  **Efisiensi Algoritma:** Membuktikan apakah $O(n)$ pada Quickselect lebih cepat dibanding $O(n \log n)$ pada Sorting dalam implementasi yang setara (Python manual).
2.  **Rekursif vs Iteratif:** Menganalisis ketahanan memori dan kecepatan antara pendekatan *Divide and Conquer* klasik (Rekursif) dengan pendekatan berbasis *Stack/Loop* (Iteratif).

## 📋 Fitur Program
Program ini memiliki fitur *All-in-One Benchmark* yang menguji 4 metode sekaligus dalam satu grafik:

1.  **Quickselect Rekursif** ($O(n)$)
2.  **Quickselect Iteratif** ($O(n)$)
3.  **Quicksort Rekursif** ($O(n \log n)$)
4.  **Quicksort Iteratif** ($O(n \log n)$)

**Fitur Tambahan:**
* **Live Multi-Line Plotting:** Menampilkan 4 garis grafik secara real-time.
* **Manual Input:** Pengguna dapat menguji ketahanan algoritma pada berbagai ukuran $N$.
* **Stack Overflow Prevention:** Implementasi iteratif untuk menangani dataset yang sangat besar yang biasanya menyebabkan *maximum recursion depth exceeded*.

---

## 🚀 Cara Menjalankan

### 1. Prasyarat
Pastikan Python 3.x dan library `matplotlib` sudah terinstall.
```bash
pip install matplotlib
