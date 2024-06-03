# E-Commerce-Churn-Prediction

## Objective
Dalam industri e-commerce, mempertahankan pelanggan merupakan aspek kritis yang mempengaruhi keberlanjutan dan pertumbuhan pendapatan perusahaan. Studi menunjukkan bahwa tingkat retensi pelanggan sebesar 5% dapat meningkatkan keuntungan perusahaan hingga 25% sampai 95%. Mengingat persaingan yang ketat dan biaya akusisi pelanggan yang tinggi, perusahaan perlu memahami faktor-faktor yang berkontribusi terhadap churn pelanggan untuk mengembangkan strategi yang lebih efektif dalam mempertahakan pelanggan. 
Proyek ini bertujuan untuk mengembangkan model klasifikasi prediktif yang mengidentifikasi pelanggan yang berisiko tinggi untuk churn dari platform e-commerce. Dengan menggunakan teknik machine learning, model akan dilatih untuk mengenali pola dalam data pelanggan yang berkorelasi dengan kemungkinan pelanggan berhenti menggunakan layanan. Tujuan utama adalah untuk memberikan wawasan yang memungkinkan perusahaan melakukan intervensi yang tepat waktu dan personalisasi tawaran dalam memperbaiki pengalaman pelanggan, sehingga meningkatkan kepuasan dan retensi pelanggan. Pada model ini digunakan metrik F1-score dan ROC-AUC. Menggunakan F1-score karena akan membantu memastikan model secara efektif menangkap pelanggan yang berisiko churn (high recall) dengan meminimalkan gangguan terhadap pelanggan yang sebenarnya berlangganan (high precision). Menggunakan ROC-AUC untuk memberikan gambaran kemampuan model dalam membedakan antar pelanggan yang akan churn dan yang tidak, independen dari ambang klasifikasi yang dipilih.  

## Dataset
File: ecommerce_customer_data_custom_ratios.csv
Jumlah Data: 6000

## Exploratory Data Analysis (EDA)
- Memvisualisasikan dan menganalisis distribusi fitur.
- Mengidentifikasi pola dan korelasi penting.
  
## Feature Engineering
- Split X dan y
- Split train dan test
- Drop Unnecessary Columns
- Feature Selection menggunakan Feature Importance
- Split Numeric Columns and Categorical Columns
- Handling cardinality, outlier, dan missing value
- Column Transformer

## Model Training and Evaluation
- Melatih model seperti Decision Tree, Random Forest, XGBoost, KNN, dan SVM.
- Mengevaluasi menggunakan metrik F1-score dan ROC-AUC.

## Model Optimization
- Melakukan tuning hyperparameter.

## Hasil
- Model Decision Tree memiliki performa terbaik berdasarkan ROC-AUC dan F1-Score.
- Model ini memiliki keterbatasan dalam mengklasifikasikan kelas minoritas (churn).

# Future Work
- Menerapkan teknik resampling untuk mengatasi ketidakseimbangan kelas.
- Mengoptimalkan parameter model untuk mengurangi overfitting.

# Aplikasi Industri
- Identifikasi dini risiko churn memungkinkan strategi retensi yang lebih terarah.
- Integrasi dengan sistem CRM untuk otomatisasi pemasaran dan penawaran personalisasi dapat meningkatkan kepuasan pelanggan dan keberlanjutan bisnis.
