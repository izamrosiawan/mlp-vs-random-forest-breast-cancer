# Deteksi Dini Kanker Payudara Menggunakan Multilayer Perceptron (MLP) pada Dataset Breast Cancer Wisconsin

## Tim Pengembang

Proyek ini dikerjakan oleh:

1. Muhammad Iqbal - 103102400020
2. Fira Adelia Septa - 103102430002
3. Yoan Natasya Agustin Sebastian - 103102430001
4. Retno Eka Sari - 103102400046
5. Clairine Anargya - 103102400031
6. Izam Rosiawan - 103102400049

## Deskripsi

Repositori ini berisi implementasi metode **Multilayer Perceptron (MLP)** untuk mendeteksi dini kanker payudara menggunakan **Breast Cancer Wisconsin Dataset**. Penelitian membandingkan performa model sebelum dan sesudah penerapan teknik **Synthetic Minority Oversampling Technique (SMOTE)**. Sebagai model pembanding digunakan algoritma **Random Forest**.

## Dataset

* **Nama Dataset** : Breast Cancer Wisconsin
* **Sumber** : UCI Machine Learning Repository
* **Jumlah Fitur** : 9 atribut
* **Target**

  * 2 = Benign (Tumor Jinak)
  * 4 = Malignant (Tumor Ganas)

## Tahapan Penelitian

1. Memuat dataset.
2. Melakukan preprocessing data.
3. Menghapus atribut `Sample_Code_Number`.
4. Mengganti nilai `?` menjadi `NaN`.
5. Menghapus data yang memiliki nilai kosong.
6. Mengubah tipe data menjadi numerik.
7. Membagi data menjadi data latih dan data uji.
8. Melakukan normalisasi menggunakan **StandardScaler**.
9. Melatih model MLP dan Random Forest tanpa SMOTE.
10. Menerapkan SMOTE pada data latih.
11. Melatih kembali model MLP dan Random Forest menggunakan data hasil SMOTE.
12. Membandingkan performa model sebelum dan sesudah SMOTE.

## Library yang Digunakan

```python
pandas
numpy
matplotlib
seaborn
scikit-learn
imbalanced-learn
```

Install seluruh library:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn imbalanced-learn
```

## Struktur Notebook

```text
breastcancer.ipynb
│
├── Import Library
├── Load Dataset
├── Exploratory Data Analysis
├── Data Preprocessing
├── Train Test Split
├── StandardScaler
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

| Model         | Balancing    |   Accuracy |   Precision |     Recall |   F1-Score |
| ------------- | ------------ | ---------: | ----------: | ---------: | ---------: |
| MLP           | Tanpa SMOTE  | **97.08%** | **100.00%** | **91.67%** | **95.65%** |
| MLP           | Dengan SMOTE | **96.35%** |  **97.78%** | **91.67%** | **94.62%** |
| Random Forest | Tanpa SMOTE  | **97.08%** |  **97.83%** | **93.75%** | **95.74%** |
| Random Forest | Dengan SMOTE | **96.35%** |  **95.74%** | **93.75%** | **94.74%** |

## Kesimpulan

Penelitian ini berhasil membangun model deteksi dini kanker payudara menggunakan algoritma **Multilayer Perceptron (MLP)** pada Dataset Breast Cancer Wisconsin serta membandingkannya dengan algoritma **Random Forest** sebelum dan sesudah penerapan **SMOTE**.

Hasil pengujian menunjukkan bahwa model **MLP tanpa SMOTE** memberikan performa terbaik dengan Accuracy **97.08%**, Precision **100.00%**, Recall **91.67%**, dan F1-Score **95.65%**. Sementara itu, Random Forest tanpa SMOTE memperoleh Accuracy **97.08%**, Precision **97.83%**, Recall **93.75%**, dan F1-Score **95.74%**.

Setelah dilakukan balancing menggunakan **SMOTE**, performa kedua model tidak mengalami peningkatan. Accuracy dan F1-Score pada MLP maupun Random Forest justru sedikit menurun, sedangkan nilai Recall tetap. Hasil ini menunjukkan bahwa distribusi kelas pada Dataset Breast Cancer Wisconsin sudah cukup seimbang sehingga penerapan SMOTE tidak memberikan manfaat yang signifikan terhadap performa model.

Berdasarkan hasil penelitian, **Multilayer Perceptron (MLP) tanpa SMOTE** menjadi model terbaik untuk klasifikasi kanker payudara pada dataset ini.

## Referensi

1. Dua, D., & Graff, C. (2019). UCI Machine Learning Repository. University of California, Irvine.
2. Chawla, N. V., Bowyer, K. W., Hall, L. O., & Kegelmeyer, W. P. (2002). SMOTE: Synthetic Minority Over-sampling Technique. Journal of Artificial Intelligence Research, 16, 321-357.
3. Pedregosa, F., et al. (2011). Scikit-learn: Machine Learning in Python. Journal of Machine Learning Research, 12, 2825-2830.
4. Arianda, G. R., Musayyanah, Aqvirandy, W., Farady, M. D., Cahya, M. N., & Hadiono, T. (2023). Deteksi Kanker Payudara Menggunakan Artificial Neural Network pada Deep Learning. INFOTECH: Jurnal Informatika & Teknologi, 4(2), 259-269.
5. Kusuma, J., Hayadi, B. H., Wanayumini, & Rosnelly, R. (2022). Komparasi Metode Multi Layer Perceptron (MLP) dan Support Vector Machine (SVM) untuk Klasifikasi Kanker Payudara. MIND (Multimedia Artificial Intelligent Networking Database) Journal, 7(1), 51-60.
