# Deteksi Dini Kanker Payudara Menggunakan Multilayer Perceptron (MLP) pada Dataset Breast Cancer Wisconsin

## Tim Pengembang

Proyek ini dikerjakan oleh:

1. Nama Anggota 1 (NIM)
2. Nama Anggota 2 (NIM)
3. Nama Anggota 3 (NIM)
4. Nama Anggota 4 (NIM)


## Deskripsi

Repositori ini berisi implementasi metode **Multilayer Perceptron (MLP)** untuk mendeteksi dini kanker payudara menggunakan **Breast Cancer Wisconsin Dataset**. Penelitian membandingkan performa model sebelum dan sesudah penerapan teknik **Synthetic Minority Oversampling Technique (SMOTE)**. Sebagai pembanding, digunakan juga algoritma **Random Forest**.

## Dataset

* **Nama Dataset** : Breast Cancer Wisconsin
* **Sumber** : UCI Machine Learning Repository
* **Jumlah Fitur** : 9 atribut
* **Target** :

  * 2 = Benign (Tumor Jinak)
  * 4 = Malignant (Tumor Ganas)

## Tahapan Penelitian

1. Memuat dataset.
2. Melakukan preprocessing data.
3. Menghapus atribut yang tidak digunakan (`Sample_Code_Number`).
4. Mengganti nilai `?` menjadi `NaN`.
5. Menghapus data yang memiliki nilai kosong.
6. Mengubah tipe data menjadi numerik.
7. Melakukan normalisasi menggunakan **StandardScaler**.
8. Membagi data menjadi data latih dan data uji.
9. Melatih model tanpa SMOTE.
10. Menerapkan SMOTE pada data latih.
11. Melatih model setelah SMOTE.
12. Membandingkan performa MLP dan Random Forest.

## Library yang Digunakan

```python
pandas
numpy
matplotlib
seaborn
scikit-learn
imbalanced-learn
```

Install seluruh library dengan:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn imbalanced-learn
```

## Struktur Notebook

```
breastcancer2.ipynb
│
├── Import Library
├── Load Dataset
├── Exploratory Data Analysis
├── Data Preprocessing
├── Feature Scaling
├── Train Test Split
├── MLP Tanpa SMOTE
├── Random Forest Tanpa SMOTE
├── SMOTE
├── MLP Dengan SMOTE
├── Random Forest Dengan SMOTE
├── Evaluasi Model
└── Perbandingan Hasil
```

## Metode Evaluasi

Performa model dievaluasi menggunakan:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix
* Classification Report

## Hasil Pengujian

| Model         | Balancing    | Accuracy | Precision |  Recall | F1 Score |
| ------------- | ------------ | -------: | --------: | ------: | -------: |
| MLP           | Tanpa SMOTE  |   98.54% |    96.00% | 100.00% |   97.96% |
| MLP           | Dengan SMOTE |   98.54% |    96.00% | 100.00% |   97.96% |
| Random Forest | Tanpa SMOTE  |   97.81% |    94.12% | 100.00% |   96.97% |
| Random Forest | Dengan SMOTE |   97.81% |    94.12% | 100.00% |   96.97% |

## Kesimpulan

Model **Multilayer Perceptron (MLP)** memberikan performa terbaik dibandingkan Random Forest pada Dataset Breast Cancer Wisconsin. MLP memperoleh Accuracy sebesar **98.54%**, Precision **96.00%**, Recall **100.00%**, dan F1-Score **97.96%**.

Penerapan **SMOTE** tidak meningkatkan performa kedua model. Hal ini menunjukkan bahwa distribusi kelas pada dataset sudah cukup seimbang sehingga model mampu mempelajari pola data dengan baik meskipun tanpa proses balancing.

## Referensi

1. Dua, D., & Graff, C. (2019). *UCI Machine Learning Repository*. University of California, Irvine. https://archive.ics.uci.edu/
2. Chawla, N. V., Bowyer, K. W., Hall, L. O., & Kegelmeyer, W. P. (2002). SMOTE: Synthetic Minority Over-sampling Technique. *Journal of Artificial Intelligence Research*, 16, 321-357.
3. Pedregosa, F., et al. (2011). Scikit-learn: Machine Learning in Python. *Journal of Machine Learning Research*, 12, 2825-2830.
