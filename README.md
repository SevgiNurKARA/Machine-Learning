# 🤖 Machine Learning Projects

Makine öğrenmesi algoritmaları, veri ön işleme teknikleri ve model değerlendirme projeleri koleksiyonu.

## 📚 İçerik

### 🌳 Decision Tree (Karar Ağacı)
- Heart Disease Classification projesi
- Decision Tree algoritması ile sınıflandırma
- Model performans analizi

**Dosya:** `Decision Tree/heartdisease.ipynb`

### 📊 Naive Bayes
- Heart Disease Classification projesi
- Naive Bayes algoritması ile sınıflandırma
- Olasılık tabanlı makine öğrenmesi

**Dosya:** `Naive Bayes/heartdisease-nb.ipynb`

### 🧹 Veri Ön İşleme (Kütüphane Kullanmadan)
Sıfırdan implementasyonlar:
- **Data Encoding**: Kategorik veri kodlama
- **Discretization**: Sürekli verileri ayrıklaştırma
- **k-Means**: Kümeleme algoritması
- **Missing Value**: Eksik veri doldurma
- **Oversampling**: Veri dengesizliği giderme

**Klasör:** `Veri Ön İşleme Kütüphane Kullanmadan/`

### 📈 ML Article - Kapsamlı Veri Ön İşleme ve Model Değerlendirme
Hava kirliliği, öğrenci akademik başarıları ve hava koşulları veri setleri üzerinde:
- Eksik veri doldurma yöntemleri (Mean, Mode, KNN, Multiple Imputation)
- SMOTE ile veri dengesizliği giderme
- KNN, Naive Bayes, Decision Tree algoritmaları
- Performans değerlendirme ve karşılaştırma

**Klasör:** `ML_article/`

Detaylı bilgi için: [ML_article/README.md](ML_article/README.md)

## 🚀 Başlangıç

### Gereksinimler

```bash
# Tüm bağımlılıkları yüklemek için
pip install -r requirements.txt
```

### Temel Kütüphaneler
- Python 3.8+
- NumPy
- Pandas
- Scikit-learn
- Imbalanced-learn (SMOTE için)
- SciPy
- Matplotlib (görselleştirme için)

## 📖 Kullanım

### Decision Tree Projesi
```bash
# Jupyter Notebook'u açın
jupyter notebook "Decision Tree/heartdisease.ipynb"
```

### Naive Bayes Projesi
```bash
# Jupyter Notebook'u açın
jupyter notebook "Naive Bayes/heartdisease-nb.ipynb"
```

### ML Article Projesi
```bash
cd ML_article
python preprocessing.py
python knn.py
python naive_bayes.py
python tree.py
python best_result.py
```

## 🎯 Öğrenme Hedefleri

Bu repo ile öğrenebilecekleriniz:
- ✅ Makine öğrenmesi algoritmalarının implementasyonu
- ✅ Veri ön işleme teknikleri
- ✅ Eksik veri doldurma yöntemleri
- ✅ Model performans değerlendirme
- ✅ Veri dengesizliği problemleri ve çözümleri
- ✅ Sıfırdan algoritma implementasyonu

## 📊 Proje Yapısı

```
Machine-Learning/
├── Decision Tree/
│   └── heartdisease.ipynb
├── Naive Bayes/
│   └── heartdisease-nb.ipynb
├── Veri Ön İşleme Kütüphane Kullanmadan/
│   ├── Data Encoding/
│   ├── discretization/
│   ├── k-Mean/
│   ├── Missing Value/
│   └── oversampling/
├── ML_article/
│   ├── README.md
│   ├── preprocessing.py
│   ├── knn.py
│   ├── naive_bayes.py
│   ├── tree.py
│   └── best_result.py
├── README.md
└── requirements.txt
```

## 🔬 Teknolojiler

- **Python**: Ana programlama dili
- **Scikit-learn**: Makine öğrenmesi algoritmaları
- **NumPy & Pandas**: Veri işleme
- **Imbalanced-learn**: Veri dengesizliği teknikleri
- **Jupyter Notebook**: İnteraktif geliştirme

## 👤 Yazar

[Sevgi Nur Kara](https://github.com/SevgiNurKARA)

## 📄 Lisans

Bu projeler öğrenme amaçlıdır ve açık kaynaklıdır.

## 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz! Pull request göndermekten çekinmeyin.

## ⭐ Yıldız Vermeyi Unutmayın!

Bu repo size yardımcı olduysa, yıldız vermeyi unutmayın! ⭐

