# 🛍️ Shopper Spectrum – Customer Segmentation & Product Recommendation

A capstone project for e-commerce analytics:
- **Customer Segmentation** using RFM (Recency, Frequency, Monetary) & KMeans  
- **Product Recommendation** using item-based Collaborative Filtering.

---

## 🚀 Features
- Clean & preprocess online retail data
- RFM feature engineering
- KMeans clustering → label customers
- Collaborative filtering → recommend top 5 similar products
- Interactive **Streamlit** app

---

## 📂 Structure
```
Shopper_Spectrum/
├── app.py
├── shopper_spectrum_training.ipynb
├── rfm_kmeans_model.pkl
├── rfm_scaler.pkl
├── product_similarity.pkl
├── requirements.txt
├── README.md
└── data
    └── online_retail.csv   # optional
```

---


## ⚙️ Installation
```bash
git clone https://github.com/<your-username>/Shopper_Spectrum.git
cd Shopper_Spectrum
python -m venv venv
venv\Scripts\activate   # or source venv/bin/activate
pip install -r requirements.txt
```

---

## ▶️ Usage
1. Train models (optional) with the notebook in `notebooks/`.  
2. Start the Streamlit app:
```bash
streamlit run app.py
```

---

## 📝 License
MIT License – see [LICENSE](LICENSE).
