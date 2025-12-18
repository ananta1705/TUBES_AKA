# Perbandingan Algoritma Quickselect dan Algoritma Pengurutan dalam Mencari Nilai Tertentu pada Data

### Tugas Besar Mata Kuliah Analisis Kompleksitas Algoritma (AKA)

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Matplotlib](https://img.shields.io/badge/Library-Matplotlib-orange.svg)
![Status](https://img.shields.io/badge/Status-Completed-green.svg)

Repository ini berisi implementasi kode, visualisasi, dan hasil analisis untuk Tugas Besar mata kuliah **Analisis Kompleksitas Algoritma**.

Penelitian ini bertujuan untuk membandingkan efisiensi waktu eksekusi (*running time*) antara algoritma **Quickselect** (Seleksi Parsial) dengan algoritma **Sorting** (Pengurutan Penuh) dalam studi kasus pencarian nilai elemen ke-$k$ (seperti Median) pada kumpulan data besar.

## 👥 Anggota Tim
| Nama | NIM |
| :--- | :--- |
| **Ananta Puti Maharani** | 103122400040 |
| **Putri Naila Salsabila** | 103122400048 |

---

## 📋 Fitur Program
* **Real-Time Benchmarking:** Program memvisualisasikan grafik perbandingan kinerja secara langsung saat data diinput.
* **Interactive CLI:** Pengguna dapat memasukkan berbagai ukuran data ($N$) melalui terminal untuk melihat respons algoritma.
* **Analisis Otomatis:** Program menghitung selisih waktu dan memberikan kesimpulan algoritma mana yang lebih cepat pada setiap percobaan.
* **Implementasi Algoritma:**
    * **Quickselect:** $O(n)$ - Menggunakan pendekatan *Divide and Conquer* dengan pivot acak.
    * **Sorting (Timsort):** $O(n \log n)$ - Menggunakan fungsi bawaan Python `.sort()`.

## 🚀 Cara Menjalankan Program

### 1. Prasyarat
Pastikan Python 3.x sudah terinstall. Program ini memerlukan library `matplotlib`.

Install library dengan perintah:
```bash
pip install matplotlib
