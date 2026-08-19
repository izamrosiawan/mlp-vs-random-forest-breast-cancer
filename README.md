# Deteksi Dini Kanker Payudara Menggunakan Multilayer Perceptron (MLP) pada Dataset Breast Cancer Wisconsin

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Neural%20Network-orange.svg)](https://scikit-learn.org/)
[![Domain](https://img.shields.io/badge/Domain-Healthcare%20AI-red.svg)](#)
[![Tests](https://img.shields.io/badge/Tests-Pytest%20Passing-brightgreen.svg)](#)

## Tim Pengembang

Proyek ini dikerjakan oleh:
1. Muhammad Iqbal - 103102400020
2. Fira Adelia Septa - 103102430002
3. Yoan Natasya Agustin Sebastian - 103102430001
4. Retno Eka Sari - 103102400046
5. Clairine Anargya - 103102400031
6. Izam Rosiawan - 103102400049

---

## 1. Deskripsi & Latar Belakang Klinis

Repositori ini berisi implementasi metode **Multilayer Perceptron (MLP)** untuk mendeteksi dini kanker payudara menggunakan **Breast Cancer Wisconsin Dataset**. Penelitian membandingkan performa model sebelum dan sesudah penerapan teknik **Synthetic Minority Oversampling Technique (SMOTE)** serta algoritma pembanding **Random Forest**.

---

## 2. Struktur Repositori

```text
mlp-vs-random-forest-breast-cancer/
├── data/
│   └── dataset_breast_cancer_wisconsin.xlsx   # Dataset Breast Cancer Wisconsin
├── images/                                    # Grafik & hasil visualisasi 300 DPI
│   ├── distribusi_kelas_tumor.png
│   ├── heatmap_korelasi_fitur.png
│   ├── confusion_matrix_mlp.png
│   └── confusion_matrix_random_forest.png
├── src/                                       # Modular Python engine (BreastCancerMLPEngine)
├── tests/                                     # Automated unit tests (Pytest)
├── breastcancer.ipynb                         # Notebook eksperimen MLP vs Random Forest
├── .gitignore                                 # Git ignore file
├── requirements.txt                           # Daftar dependensi Python
└── README.md                                  # Dokumentasi proyek
```

---

## 3. Dataset & Variabel Klinis

* **Nama Dataset**: Breast Cancer Wisconsin
* **Sumber**: UCI Machine Learning Repository
* **Jumlah Fitur**: 9 atribut klinis citra sel tumor
* **Target Klasifikasi**:
  * 2 = Benign (Tumor Jinak)
  * 4 = Malignant (Tumor Ganas)

---

## 4. Hasil Pengujian & Evaluasi

| Model | Balancing | Accuracy | Precision | Recall | F1-Score | Karakteristik Klinis |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **MLP** | **Tanpa SMOTE** | **97.08%** | **100.00%** | **91.67%** | **95.65%** | **Model Terbaik**: Presisi 100% tanpa kesalahan diagnosis positif palsu |
| **MLP** | Dengan SMOTE | 96.35% | 97.78% | 91.67% | 94.62% | Sedikit penurunan presisi pasca oversampling |
| **Random Forest** | Tanpa SMOTE | **97.08%** | 97.83% | **93.75%** | **95.74%** | Recall tinggi untuk menangkap potensi tumor ganas |
| **Random Forest** | Dengan SMOTE | 96.35% | 95.74% | 93.75% | 94.74% | Performa stabil |

---

## 5. Implementasi Modular & Pengujian Otomatis

Modul inferensi neural network tersedia di `src/cancer_mlp_engine.py`:

```python
from src.cancer_mlp_engine import BreastCancerMLPEngine
import pandas as pd

engine = BreastCancerMLPEngine()
# Training dan inferensi
```

Jalankan automated test:
```bash
pytest tests/
```

---

## 6. Cara Menjalankan

1. **Pasang Dependensi**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Eksekusi Notebook**:
   ```bash
   jupyter notebook breastcancer.ipynb
   ```

---
*Breast Cancer Wisconsin MLP vs Random Forest Classification Project.*
