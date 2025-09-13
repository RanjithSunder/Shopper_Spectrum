# app.py

import streamlit as st
import pandas as pd
import pickle

# Load models
kmeans = pickle.load(open("rfm_kmeans_model.pkl", "rb"))
scaler = pickle.load(open("rfm_scaler.pkl", "rb"))
similarity_df = pd.read_pickle("product_similarity.pkl")

# Streamlit UI
st.set_page_config(page_title="Shopper Spectrum", layout="centered")

st.title("🛍️ Shopper Spectrum – Customer Intelligence App")
st.markdown("Built with 💡RFM Segmentation & 🎯 Product Recommendation")

# Tab UI
tab1, tab2 = st.tabs(["🛒 Product Recommendation", "👥 Customer Segmentation"])

# -----------------------
# Tab 1: Product Recommendation
# -----------------------
with tab1:
    st.header("🔍 Find Similar Products")

    product_name = st.text_input("Enter a Product Name (case-sensitive)", value="WHITE HANGING HEART T-LIGHT HOLDER")

    if st.button("Get Recommendations"):
        if product_name in similarity_df.index:
            top_products = similarity_df[product_name].sort_values(ascending=False)[1:6]
            st.success("✅ Top 5 similar products:")
            for i, (prod, score) in enumerate(top_products.items(), 1):
                st.markdown(f"**{i}. {prod}** (Similarity: {score:.2f})")
        else:
            st.warning("❗Product not found. Try another name from your dataset.")

# -----------------------
# Tab 2: Customer Segmentation
# -----------------------
with tab2:
    st.header("📊 Predict Customer Segment")

    recency = st.number_input("Recency (Days since last purchase)", min_value=0, max_value=1000, value=30)
    frequency = st.number_input("Frequency (Number of Purchases)", min_value=0, max_value=1000, value=5)
    monetary = st.number_input("Monetary (Total Spend)", min_value=0.0, value=100.0, step=10.0)

    if st.button("Predict Cluster"):
        user_data = pd.DataFrame([[recency, frequency, monetary]], columns=['Recency', 'Frequency', 'Monetary'])
        user_scaled = scaler.transform(user_data)
        cluster = kmeans.predict(user_scaled)[0]

        cluster_labels = {
            0: "High-Value",
            1: "Regular",
            2: "Occasional",
            3: "At-Risk"
        }

        st.success(f"🧠 Predicted Segment: **{cluster_labels.get(cluster, 'Unknown')}** (Cluster {cluster})")
