import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# ==================================
# DATA TRAINING
# ==================================

X_train = np.array([
    [5, 10],
    [10, 20],
    [15, 5],
    [20, 25],
    [25, 15]
])

y_train = np.array([
    50,
    80,
    110,
    90,
    150
])

# ==================================
# MODEL MACHINE LEARNING
# ==================================

model = LinearRegression().fit(X_train, y_train)

# ==================================
# BASELINE
# ==================================

baseline_input = np.array([[10, 10]])
baseline_pred = model.predict(baseline_input)[0]

# ==================================
# FUNGSI SIMULASI
# ==================================

def run_simulation(new_iklan, new_diskon):

    intervention_input = np.array([[new_iklan, new_diskon]])

    prediction = model.predict(intervention_input)[0]

    delta_y = prediction - baseline_pred

    return prediction, delta_y


# ==================================
# STREAMLIT CONFIG
# ==================================

st.set_page_config(
    page_title="BeautyRich AI Promotion Simulator",
    page_icon="💎",
    layout="wide"
)

# ==================================
# HEADER
# ==================================

st.markdown("""
<div style="
background: linear-gradient(90deg,#E8D5FF,#FDE2F3);
padding:20px;
border-radius:15px;
text-align:center;
margin-bottom:20px;
">
<h1>💎 BeautyRich AI Promotion Simulator</h1>
<p>Smart What-If Analysis for Marketing Strategy</p>
</div>
""", unsafe_allow_html=True)

st.write(
    "Gunakan slider untuk menguji berbagai skenario promosi dan melihat dampaknya terhadap keuntungan."
)

# ==================================
# SIDEBAR
# ==================================

st.sidebar.header("🎯 Variabel Intervensi")

iklan_slider = st.sidebar.slider(
    "Anggaran Iklan (Juta)",
    min_value=0,
    max_value=50,
    value=10
)

diskon_slider = st.sidebar.slider(
    "Besaran Diskon (%)",
    min_value=0,
    max_value=50,
    value=10
)

# ==================================
# SIMULASI
# ==================================

hasil_pred, delta = run_simulation(
    iklan_slider,
    diskon_slider
)

# ==================================
# HASIL
# ==================================

col1, col2 = st.columns(2)

with col1:
    st.metric(
        label="💰 Prediksi Keuntungan",
        value=f"Rp {hasil_pred:.2f} Juta",
        delta=f"{delta:.2f} Juta"
    )

with col2:
    st.metric(
        label="📊 Baseline",
        value=f"Rp {baseline_pred:.2f} Juta"
    )

# ==================================
# GRAFIK
# ==================================

st.subheader("📈 Perbandingan Skenario")

data_plot = pd.DataFrame({
    "Skenario": ["Baseline", "Intervensi"],
    "Keuntungan": [baseline_pred, hasil_pred]
})

st.bar_chart(
    data=data_plot,
    x="Skenario",
    y="Keuntungan"
)

# ==================================
# STORYTELLING / REKOMENDASI
# ==================================

if delta > 0:
    st.success(
        f"✅ Strategi promosi ini diperkirakan meningkatkan keuntungan sebesar Rp {delta:.2f} juta dibanding baseline."
    )
elif delta < 0:
    st.error(
        f"❌ Strategi promosi ini diperkirakan menurunkan keuntungan sebesar Rp {abs(delta):.2f} juta dibanding baseline."
    )
else:
    st.info(
        "ℹ️ Hasil simulasi sama dengan kondisi baseline."
    )

# ==================================
# FOOTER
# ==================================

st.markdown("---")
st.caption("UAS Pemodelan dan Simulasi | BeautyRich AI Promotion Simulator")