import streamlit as st
import pandas as pd
import numpy as np
df = pd.read_csv("dataset_gaji_data_science.csv")

######################################################### JUDUL ##################################################################

st.set_page_config(
    page_title="Data Science Salary Prediction",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded",
)
#####CARD SETELAH PREDIKSI############
st.markdown("""
<style>
.card {
    background: #6D789C;
    padding:20px;
    border-radius:12px;
    text-align:center;
    margin-top:15px;
}
</style>
""", unsafe_allow_html=True)

import streamlit as st

  ############################################################ CSS ##################################################################### 

st.markdown("""
<style>

/* ================= FONT ================= */
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&family=Poppins:wght@400;500;600&display=swap');


/* ================= ROOT COLOR ================= */
:root {

    --bg-main:      #A2AED8;
    --bg-sidebar:   #6D789C;

    --card-bg:      rgba(255,255,255,0.18);
    --card-green:   #a8c89a;
    --card-green2:  #b5d4a6;

    --text-dark:    #1a1a2e;
    --text-white:   #ffffff;

    --accent-green: #6ab04c;
    --btn-green:    #7ec666;

    --shadow:       0 4px 15px rgba(0,0,0,0.15);
}


/* ================= GLOBAL ================= */
.stApp {
    background-color: var(--bg-main) !important;
    font-family: 'Nunito', sans-serif;
}

#MainMenu, footer, header {
    visibility: hidden;
}

.block-container {
    padding-top: 0 !important;
    padding-bottom: 0 !important;
}


/* ================= SIDEBAR ================= */
[data-testid="stSidebar"] {
    background-color: var(--bg-sidebar) !important;
    border-right: none;
}

[data-testid="stSidebar"] .stMarkdown {
    color: var(--text-dark);
}

.sidebar-ml-title {
    font-family: 'Poppins','semi-bold',sans-serif;
    font-weight: 600;
    font-size: 22px;
    color: #1a1a2e;
    line-height: 1.3;
    margin-bottom: 2px;
}

.sidebar-dev-label {
    font-family: 'Poppins' 'semi-bold', sans-serif;
    font-weight: 500;
    font-size: 18px;
    color: #1a1a2e;
    margin-bottom: 6px;
}

.sidebar-badge {
    background-color: #A2AED8;
    color:  #1A345A;
    font-family: 'Poppins','medium' sans-serif;
    font-weight: 500;
    font-size: 18px;
    padding: 8px 16px;
    border-radius: 25px;
    display: inline-block;
    margin: 6px 0 12px 0;
    width: 100%;
    text-align: center;
    box-sizing: border-box;
}

.sidebar-desc-box {
    background: #A2AED8;
    border-radius: 10px;
    padding: 12px;
    font-family: 'Poppins', 'medium' sans-serif;
    font-weight: 500;
    font-size: 18px;
    color: #1a1a2e;
    line-height: 1.5;
    margin-bottom: 12px;
}

.sidebar-fitur {
    color: #1a1a2e;
    font-family: 'Poppins' 'medium', sans-serif;
    font-weight: 500;
    font-size: 18px;
    margin-bottom: 4px;
}

.sidebar-fitur ul {
    padding-left: 18px;
    margin: 0;
    color: #1a1a2e;
    font-family: 'Poppins', sans-serif;
    font-weight: 500;
    font-size: 16px;
}

.sidebar-fitur li {
    margin-bottom: 2px;
}


/* ================= SIDEBAR BUTTON ================= */
[data-testid="collapsedControl"] {
    display: flex !important;
    background-color: #6D789C !important;
    color: white !important;
    border-radius: 0 8px 8px 0 !important;
    top: 50% !important;
}

[data-testid="collapsedControl"] svg {
    fill: white !important;
}

button[data-testid="baseButton-headerNoPadding"] {
    color: white !important;
}


/* ================= HEADER ================= */
[data-testid="stMarkdownContainer"] > div > .top-header,
.element-container:has(.top-header) {
    background: transparent !important;
}

[data-testid="block-container"],
[data-testid="stVerticalBlock"] > div:first-child {
    background: transparent !important;
}

.top-header {
    background: transparent !important;
    padding: 14px 28px;
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    border-bottom: 1px solid #000000;
}

.top-header-left {
    display: flex;
    align-items: center;
    gap: 16px;
}

.top-header-title {
    font-family: 'Poppins', 'semi-bold' sans-serif;
    font-weight: 700;
    font-size: 32px;
    color: #1a1a2e;
    line-height: 1.2;
}

.top-header-sub {
    font-family: 'Poppins','medium', sans-serif;
    font-weight: 500;
    font-size: 16px;
    color: #555;
}

.top-header-logo {
    width: 80px;
    height: 80px;
    object-fit: contain;
    margin-top: -10px;
}


/* ================= RADIO NAV ================= */
div[data-testid="stHorizontalBlock"]:has([data-testid="stRadio"]),
[data-testid="stRadio"] {
    margin: 0 !important;
    padding: 0 !important;
}

[data-testid="stRadio"] > div {
    display: flex !important;
    flex-direction: row !important;
    gap: 32px !important;
    align-items: flex-end !important;
    padding: 0 !important;
    padding-bottom: 8px !important;
    margin-bottom: 0px !important;
    margin-top: 32px !important;
}

[data-testid="stRadio"] input[type="radio"] {
    display: none !important;
}

[data-testid="stRadio"] label > div:first-child {
    display: none !important;
}

[data-testid="stRadio"] label {
    font-family: 'Poppins','medium' sans-serif !important;
    font-size: 16px !important;
    font-weight: 500 !important;
    color: #1a1a2e !important;
    cursor: pointer !important;
}

[data-testid="stRadio"] label:has(input:checked) {
    color: #1a1a2e !important;
    font-weight: 800 !important;
    border-bottom: 3px solid #1a1a2e;
}


/* ================= CONTENT ================= */
.section-title {
    font-size: 1.6rem;
    font-weight: 800;
    color: #1a1a2e;
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 8px;
}

.section-sub {
    color: #1a1a2e;
    font-size: 0.95rem;
    margin-bottom: 16px;
}

.green-card {
    background: var(--card-green);
    border-radius: 14px;
    padding: 18px;
    color: #1e5c0e;
    font-weight: 600;
    font-size: 0.9rem;
    line-height: 1.5;
}

dev-card {
    background:  #6D789C;
    border-radius: 14px;
    padding: 18px 24px;
    color: #1a1a2e;
    font-size: 0.9rem;
    font-weight: 600;
    width: 100%;
}

.tools-card {
    background:  #6D789C;
    border-radius: 14px;
    padding: 18px 24px;
    color: #1a1a2e;
    font-size: 0.9rem;
    font-weight: 600;
    width: 100%;
}

.project-box {
    background: var(--card-green2);
    border-radius: 14px;
    padding: 20px 24px;
    color: #1a1a2e;
    font-size: 0.92rem;
    line-height: 1.6;
}


/* ================= RESULT ================= */
.result-box {
    background: var(--card-green);
    border-radius: 16px;
    padding: 24px;
    text-align: center;
    margin-top: 20px;
}

.result-title {
    font-size: 1.1rem;
    font-weight: 700;
    color: #1a1a2e;
}

.result-value {
    font-size: 2.5rem;
    font-weight: 800;
    color: #1e5c0e;
    margin: 8px 0;
}

/* ================= FOOTER ================= */
hr {
    border-color: #000000 !important;
    margin: 20px 0 !important;
}

.footer {
    text-align: center;
    color: #333;
    font-size: 0.82rem;
    padding: 18px 0 8px 0;
    border-top: 1px solid #000000;
    margin-top: 24px;
}

</style>
""", unsafe_allow_html=True)

######################################################### SIDEBAR ########################################################################

with st.sidebar:
    # Center image pakai columns
    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        st.image("logo_tas.png", width=100)

    ####################################### Text di bawah logo ################################################
    st.markdown("""
    <div style="
        text-align:center;
        font-weight:700;
        font-size:24px;
        margin-top:8px;
        color:#FFFFFF;
    ">
        SalaryPrediction
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown('<div class="sidebar-dev-label">👩‍💻 Developer</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-badge">Saskia Humaira</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="sidebar-desc-box">
        Aplikasi ini memprediksi estimasi gaji profesional Data Science berdasarkan pengalaman, jenis pekerjaan, &amp; Sistem kerja
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""
    <div class="sidebar-Panduan Penggunaan">
        🎯 &nbsp; <b>Panduan Penggunaan</b>
        <ul>
            <li>Pilih Tahun Kerja</li>
            <li>Tentukan Tingkat Pengalaman</li>
            <li>Pilih Jenis Pekerjaan</li>
            <li>Pilih Sistem Kerja</li>
            <li>Pilih Ukuran Perusahaan</li>
            <li>Tentukan Jabatan</li>
            <li>Klik tombol Prediksi Gaji</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
    <div class="sidebar-fitur">
        🎯 &nbsp; Fitur
        <ul>
            <li>Prediksi Gaji Real-time</li>
            <li>Input Interaktif</li>
            <li>Home &amp; Stastistik Dataset</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

################################################### TOP - HEADER ###############################################################

col_header1, col_header2, col_header3 = st.columns([1,6,1])

with col_header1:
    st.image("logo_tas.png", width=70)

with col_header2:
     st.markdown("""
            <div class="top-header-title">Data Science Salary Prediction</div>
            <div class="top-header-sub">Machine Learning Regression App - Model: Random Forest</div>
        </div>
    </div>
    """, unsafe_allow_html=True)


with col_header3:
    st.image("Logo_SMK_Negeri_1_Purbalingga.png", width=65)

st.markdown("""<hr style="border:none; border-top:1px solid #000000; margin:0 0 0 0;">""", unsafe_allow_html=True)

###################################################### NAVIGASI ######################################################################

st.markdown("<br>", unsafe_allow_html=True)
tabs = ["🔮 Prediction", "🏠 Information", "📊 Developer", "📈 Analisis Kode"]
selected = st.radio("nav", tabs, horizontal=True, label_visibility="collapsed")
st.markdown("""<hr style="border:none; border-top:1px solid #000000; margin:0 0 20px 0;">""", unsafe_allow_html=True)

#################################################### PREDICTION ###########################################################################

if selected == "🔮 Prediction":
    st.markdown('<div class="section-title">🔮 Prediction</div>', unsafe_allow_html=True)

    jabatan_list = sorted(df["Jabatan"].unique().tolist())

    col1, col2 = st.columns(2)
    with col1:
        tahun = st.selectbox("Tahun Kerja", sorted(df["Tahun Kerja"].unique().tolist(), reverse=True))
    with col2:
        jenis = st.selectbox("Jenis Pekerjaan", sorted(df["Jenis Pekerjaan"].unique().tolist()))

    col3, col4 = st.columns(2)
    with col3:
        pengalaman = st.selectbox("Tingkat Pengalaman", ["Pemula", "Menengah", "Senior", "Eksekutif"])
    with col4:
        sistem = st.selectbox("Sistem Kerja", sorted(df["Sistem Kerja"].unique().tolist()))

    col5, col6 = st.columns(2)
    with col5:
        ukuran = st.selectbox("Ukuran Perusahaan", ["Kecil", "Menengah", "Besar"])
    with col6:
        jabatan = st.selectbox("Jabatan", jabatan_list)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Training model (di luar tombol supaya tidak diulang setiap render) ──
    

    df_model = df[[
        "Tahun Kerja", "Tingkat Pengalaman", "Jenis Pekerjaan",
        "Jabatan", "Sistem Kerja", "Ukuran Perusahaan", "Gaji (USD)"
    ]].copy()

    df_encoded = pd.get_dummies(df_model, columns=[
        "Tingkat Pengalaman", "Jenis Pekerjaan",
        "Jabatan", "Sistem Kerja", "Ukuran Perusahaan"
    ])

    X = df_encoded.drop("Gaji (USD)", axis=1)
    y = df_encoded["Gaji (USD)"]
    columns = X.columns.tolist()

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)

    if st.button("🔍 Prediksi Gaji Sekarang", use_container_width=True):

        # ── Prediksi gaji untuk input user ──
        input_dict = {
            "Tahun Kerja": int(tahun),
            "Tingkat Pengalaman": pengalaman,
            "Jenis Pekerjaan": jenis,
            "Jabatan": jabatan,
            "Sistem Kerja": sistem,
            "Ukuran Perusahaan": ukuran
        }

        input_df = pd.DataFrame([input_dict])
        input_encoded = pd.get_dummies(input_df, columns=[
            "Tingkat Pengalaman", "Jenis Pekerjaan",
            "Jabatan", "Sistem Kerja", "Ukuran Perusahaan"
        ])
        input_encoded = input_encoded.reindex(columns=columns, fill_value=0)

        predicted = int(model.predict(input_encoded)[0])
        kurs = 16300
        predicted_idr = predicted * kurs

        st.balloons()
        st.markdown(f"""
        <div class="card">
            <h3>Salary Prediction : 💰 ${predicted:,}</h3>
            <p>Salary Prediction Rupiah Rp. {predicted_idr:,}</p>
        </div>
        """, unsafe_allow_html=True)

        st.divider()
        st.markdown("### 📊 Perbandingan Gaji per Tingkat Pengalaman")

        # ── FIX: Prediksi untuk semua level pengalaman pakai model ──
        levels = ["Pemula", "Menengah", "Senior", "Eksekutif"]
        salaries = []

        for level in levels:
            cmp_dict = {
                "Tahun Kerja": int(tahun),
                "Tingkat Pengalaman": level,
                "Jenis Pekerjaan": jenis,
                "Jabatan": jabatan,
                "Sistem Kerja": sistem,
                "Ukuran Perusahaan": ukuran
            }
            cmp_df = pd.DataFrame([cmp_dict])
            cmp_encoded = pd.get_dummies(cmp_df, columns=[
                "Tingkat Pengalaman", "Jenis Pekerjaan",
                "Jabatan", "Sistem Kerja", "Ukuran Perusahaan"
            ])
            cmp_encoded = cmp_encoded.reindex(columns=columns, fill_value=0)
            salaries.append(int(model.predict(cmp_encoded)[0]))

        colors = ["#A2AED8" if lvl != pengalaman else "#6D789C" for lvl in levels]

        fig, ax = plt.subplots(figsize=(8, 4))
        bars = ax.bar(levels, salaries, color=colors, edgecolor="none", width=0.5)
        ax.set_ylabel("Gaji (USD)", fontsize=11)
        ax.set_title(f"Estimasi Gaji per Level — {jabatan}", fontsize=12, pad=12)
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"${v:,.0f}"))
        ax.spines[["top", "right"]].set_visible(False)

        for bar, sal in zip(bars, salaries):
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 1000,
                f"${sal:,}",
                ha="center", va="bottom", fontsize=9
            )

        fig.tight_layout()
        st.pyplot(fig)

        st.markdown('<div class="footer">©2026 - Dibuat dengan ❤ oleh Saskia Humaira menggunakan Streamlit &amp; Scikit-Learn</div>', unsafe_allow_html=True)
################################################################# INFORMATION #######################################################################
elif selected == "🏠 Information":
    st.markdown('<div class="section-title">🏠 Information</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Eksplorasi statistik dan tren dari dataset gaji Data Science yang digunakan untuk melatih model:</div>', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Data", "3,755")
    col2.metric("Rata-rata Gaji (USD)", "$137,570")
    col3.metric("Gaji Tertinggi (USD)", "$450,000")
    col4.metric("Gaji Terendah (USD)", "$5,132")

    st.markdown("---")

    st.markdown('<div class="section-title" style="font-size:1.2rem;">🚀 Input Prediksi</div>', unsafe_allow_html=True)

    st.markdown("""
    <style>
    .info-card {
        background: linear-gradient(135deg, #6D789C 0%, #A2AED8 100%);
        border-radius: 14px;
        padding: 18px 20px;
        color: #ffffff;
        font-size: 0.88rem;
        line-height: 1.6;
        height: 100%;
        box-sizing: border-box;
        border: 1px solid rgba(255,255,255,0.3);
        box-shadow: 0 4px 12px rgba(109,120,156,0.25);
        margin-bottom: 14px;
    }
    .info-card .ic-icon {
        font-size: 1.6rem;
        margin-bottom: 8px;
    }
    .info-card .ic-title {
        font-weight: 700;
        font-size: 0.95rem;
        color: #ffffff;
        margin-bottom: 6px;
        letter-spacing: 0.3px;
    }
    .info-card p {
        color: rgba(255,255,255,0.88);
        margin: 0;
    }
    </style>
    """, unsafe_allow_html=True)

    row1 = st.columns(3)
    with row1[0]:
        st.markdown("""
        <div class="info-card">
            <div class="ic-icon">📅</div>
            <div class="ic-title">Tahun Kerja</div>
            <p>Menunjukkan tahun kapan data pekerjaan atau gaji dicatat. Penting karena gaji berubah setiap tahun mengikuti kondisi ekonomi dan tren industri.</p>
        </div>""", unsafe_allow_html=True)
    with row1[1]:
        st.markdown("""
        <div class="info-card">
            <div class="ic-icon">🎯</div>
            <div class="ic-title">Tingkat Pengalaman</div>
            <p>Menggambarkan level pengalaman seseorang dalam bekerja. Mulai dari Pemula, Menengah, Senior, hingga Eksekutif.</p>
        </div>""", unsafe_allow_html=True)
    with row1[2]:
        st.markdown("""
        <div class="info-card">
            <div class="ic-icon">🧾</div>
            <div class="ic-title">Jenis Pekerjaan</div>
            <p>Status pekerjaan yang dijalani — tetap, kontrak, freelance, atau paruh waktu. Berpengaruh pada stabilitas kerja dan sistem penggajian.</p>
        </div>""", unsafe_allow_html=True)

    row2 = st.columns(3)
    with row2[0]:
        st.markdown("""
        <div class="info-card">
            <div class="ic-icon">🏢</div>
            <div class="ic-title">Sistem Kerja</div>
            <p>Menjelaskan lokasi kerja karyawan — Remote, Hybrid, atau On-site. Mempengaruhi tunjangan dan kompensasi yang diterima.</p>
        </div>""", unsafe_allow_html=True)
    with row2[1]:
        st.markdown("""
        <div class="info-card">
            <div class="ic-icon">🏭</div>
            <div class="ic-title">Ukuran Perusahaan</div>
            <p>Skala perusahaan tempat bekerja — Kecil, Menengah, atau Besar. Perusahaan besar umumnya menawarkan gaji lebih kompetitif.</p>
        </div>""", unsafe_allow_html=True)
    with row2[2]:
        st.markdown("""
        <div class="info-card">
            <div class="ic-icon">👔</div>
            <div class="ic-title">Jabatan</div>
            <p>Posisi spesifik dalam bidang Data Science seperti Data Analyst, ML Engineer, Data Scientist, dan lainnya yang mempengaruhi rentang gaji.</p>
        </div>""", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown('<div class="section-title">📊 Visualisasi Dataset</div>', unsafe_allow_html=True)
    st.image("grafik_information.png", use_container_width=True)

    st.markdown('<div class="footer">©2026 - Dibuat dengan ❤ oleh Saskia Humaira menggunakan Streamlit &amp; Scikit-Learn</div>', unsafe_allow_html=True)

################################################################### DEVELOPER ################################################################

elif selected == "📊 Developer":

    st.markdown("""
    <style>
   .card {background:#f5f7fb; padding:18px; border-radius:12px; margin-bottom:12px; min-height:160px; /* samakan tinggi */}
    .title {font-weight:bold; font-size:18px;}
    .btn {padding:8px 15px; border-radius:8px; background:blue-soft; color: #A2AED8; border:1px solid #A2AED8; text-decoration:none;}
    </style>
    """, unsafe_allow_html=True)

    # About
    st.markdown("""
    <div class="card">
        <div class="title">👩‍💻 Saskia Humaira</div>
        <p>Machine Learning Enthusiast</p>
        <p>Prediksi gaji Data Science berbasis Streamlit & ML.</p>
        <a href="https://github.com/saskiyya" target="_blank" class="btn">Github</a>
        <a href="https://instagram.com/saskyqarnaen_" target="_blank" class="btn">Instagram</a>
        
    </div>
    """, unsafe_allow_html=True)

    # Tools & Fitur
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="card">
            <div class="title">🛠️ Tools</div>
            Pandas, Numpy, Matplotlib, Joblib, Scikit-Learn, Streamlit, Python
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <div class="title">📌Tentang Project</div>
            Project ini merupakan implementasi Machine Learning untuk memprediksi gaji di bidang Data Science. Model dilatih menggunakan data nyata dari industri global (2020-2023)
        </div>
        """, unsafe_allow_html=True)

    st.markdown("")
    st.markdown('<div class="footer">©2026 - Dibuat dengan ❤ oleh Saskia Humaira menggunakan Streamlit &amp; Scikit-Learn</div>', unsafe_allow_html=True)

################################################################### ANALISIS KODE ################################################################

elif selected == "📈 Analisis Kode":
    st.markdown('<div class="section-title">📈 Analisis Kode</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Berikut adalah kode analisis data menggunakan Pandas beserta hasil outputnya:</div>', unsafe_allow_html=True)

    st.markdown("---")

    # ── 1. Load Dataset ──────────────────────────────────────────────────────────
    st.markdown("### 1. Load Dataset")
    st.code(
"""import pandas as pd
df = pd.read_csv("dataset_gaji_data_science.csv")
df""",
        language="python"
    )
    st.markdown("**Output:**")
    st.dataframe(df)

    st.markdown("---")

    # ── 2. df.shape ──────────────────────────────────────────────────────────────
    st.markdown("### 2. Bentuk Dataset (df.shape)")
    st.code("df.shape", language="python")
    st.markdown("**Output:**")
    st.write(df.shape)

    st.markdown("---")

    # ── 3. df.columns ────────────────────────────────────────────────────────────
    st.markdown("### 3. Nama Kolom (df.columns)")
    st.code("df.columns", language="python")
    st.markdown("**Output:**")
    st.write(df.columns.tolist())

    st.markdown("---")

    # ── 4. df.dtypes ─────────────────────────────────────────────────────────────
    st.markdown("### 4. Tipe Data (df.dtypes)")
    st.code("df.dtypes", language="python")
    st.markdown("**Output:**")
    st.write(df.dtypes)

    st.markdown("---")

    # ── 5. df.info() ─────────────────────────────────────────────────────────────
    st.markdown("### 5. Informasi Dataset (df.info())")
    st.code("df.info()", language="python")
    st.markdown("**Output:**")
    import io
    buffer = io.StringIO()
    df.info(buf=buffer)
    st.text(buffer.getvalue())

    st.markdown("---")

    # ── 6. df.describe() ─────────────────────────────────────────────────────────
    st.markdown("### 6. Statistik Deskriptif (df.describe())")
    st.code("df.describe()", language="python")
    st.markdown("**Output:**")
    st.dataframe(df.describe())

    st.markdown("---")

    # ── 7. df.head() ─────────────────────────────────────────────────────────────
    st.markdown("### 7. Lima Data Pertama (df.head())")
    st.code("df.head()", language="python")
    st.markdown("**Output:**")
    st.dataframe(df.head())

    st.markdown("---")

    # ── 8. df.tail() ─────────────────────────────────────────────────────────────
    st.markdown("### 8. Lima Data Terakhir (df.tail())")
    st.code("df.tail()", language="python")
    st.markdown("**Output:**")
    st.dataframe(df.tail())

    st.markdown("---")

    # ── 9. df.isnull().sum() ─────────────────────────────────────────────────────
    st.markdown("### 9. Cek Missing Value (df.isnull().sum())")
    st.code("df.isnull().sum()", language="python")
    st.markdown("**Output:**")
    st.write(df.isnull().sum())

    st.markdown("---")

    # ── 10. df.duplicated().sum() ────────────────────────────────────────────────
    st.markdown("### 10. Cek Data Duplikat (df.duplicated().sum())")
    st.code("df.duplicated().sum()", language="python")
    st.markdown("**Output:**")
    st.write(df.duplicated().sum())

    st.markdown("---")

    # ── 11. Value Counts Tingkat Pengalaman ──────────────────────────────────────
    st.markdown("### 11. Distribusi Tingkat Pengalaman")
    st.code("df['Tingkat Pengalaman'].value_counts()", language="python")
    st.markdown("**Output:**")
    st.write(df["Tingkat Pengalaman"].value_counts())

    st.markdown("---")

    # ── 12. Value Counts Sistem Kerja ────────────────────────────────────────────
    st.markdown("### 12. Distribusi Sistem Kerja")
    st.code("df['Sistem Kerja'].value_counts()", language="python")
    st.markdown("**Output:**")
    st.write(df["Sistem Kerja"].value_counts())

    st.markdown("---")

    # ── 13. Rata-rata Gaji per Tingkat Pengalaman ─────────────────────────────────
    st.markdown("### 13. Rata-rata Gaji (USD) per Tingkat Pengalaman")
    st.code("df.groupby('Tingkat Pengalaman')['Gaji (USD)'].mean().sort_values(ascending=False)", language="python")
    st.markdown("**Output:**")
    st.write(df.groupby("Tingkat Pengalaman")["Gaji (USD)"].mean().sort_values(ascending=False))

    st.markdown("---")

    # ── 14. Heatmap Korelasi ─────────────────────────────────────────────────────
    st.markdown("### 14. Heatmap Korelasi Fitur Numerik")
    st.code(
"""import seaborn as sns
import matplotlib.pyplot as plt

num_features = ['Tahun Kerja', 'Gaji (USD)']
plt.figure(figsize=(5,4))
sns.heatmap(df[num_features].corr(), annot=True, cmap="coolwarm")
plt.show()""",
        language="python"
    )
    st.markdown("**Output:**")
    import seaborn as sns
    num_features = ["Tahun Kerja", "Gaji (USD)"]
    fig_corr, ax_corr = plt.subplots(figsize=(5, 4))
    sns.heatmap(df[num_features].corr(), annot=True, cmap="coolwarm", ax=ax_corr)
    st.pyplot(fig_corr)

    st.markdown("---")

    # ── 15. Linear Regression ────────────────────────────────────────────────────
    st.markdown("### 15. Model Linear Regression")
    st.code(
"""from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

X = df[["Tahun Kerja", "Tingkat Pengalaman", "Jenis Pekerjaan", "Sistem Kerja"]]
y = df["Gaji (USD)"]

numerical = ["Tahun Kerja"]
categorical = ["Tingkat Pengalaman", "Jenis Pekerjaan", "Sistem Kerja"]

preprocessor = ColumnTransformer([
    ("num", StandardScaler(), numerical),
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical)
])

model_linear = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", LinearRegression())
])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model_linear.fit(X_train, y_train)
y_pred = model_linear.predict(X_test)

print("Linear Regression")
print("R2 :", r2_score(y_test, y_pred))
print("MAE :", mean_absolute_error(y_test, y_pred))
print("MSE :", mean_squared_error(y_test, y_pred))""",
        language="python"
    )
    st.markdown("**Output:**")
    from sklearn.linear_model import LinearRegression as LR
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
    from sklearn.preprocessing import StandardScaler, OneHotEncoder
    from sklearn.pipeline import Pipeline
    from sklearn.compose import ColumnTransformer

    X_lr = df[["Tahun Kerja", "Tingkat Pengalaman", "Jenis Pekerjaan", "Sistem Kerja"]]
    y_lr = df["Gaji (USD)"]
    numerical = ["Tahun Kerja"]
    categorical = ["Tingkat Pengalaman", "Jenis Pekerjaan", "Sistem Kerja"]
    preprocessor_lr = ColumnTransformer([
        ("num", StandardScaler(), numerical),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical)
    ])
    model_linear_pipe = Pipeline([
        ("preprocessor", preprocessor_lr),
        ("regressor", LR())
    ])
    X_train_lr, X_test_lr, y_train_lr, y_test_lr = train_test_split(X_lr, y_lr, test_size=0.2, random_state=42)
    model_linear_pipe.fit(X_train_lr, y_train_lr)
    y_pred_lr = model_linear_pipe.predict(X_test_lr)
    st.text(
        f"Linear Regression\n"
        f"R2 : {r2_score(y_test_lr, y_pred_lr):.4f}\n"
        f"MAE : {mean_absolute_error(y_test_lr, y_pred_lr):.4f}\n"
        f"MSE : {mean_squared_error(y_test_lr, y_pred_lr):.4f}"
    )

    st.markdown("---")

    # ── 16. Random Forest Regressor ──────────────────────────────────────────────
    st.markdown("### 16. Model Random Forest Regressor")
    st.code(
"""from sklearn.ensemble import RandomForestRegressor

model_random = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", RandomForestRegressor())
])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model_random.fit(X_train, y_train)
y_pred = model_random.predict(X_test)

print("Random Forest Regressor")
print("R2 :", r2_score(y_test, y_pred))
print("MAE :", mean_absolute_error(y_test, y_pred))
print("MSE :", mean_squared_error(y_test, y_pred))""",
        language="python"
    )
    st.markdown("**Output:**")
    from sklearn.ensemble import RandomForestRegressor
    preprocessor_rf = ColumnTransformer([
        ("num", StandardScaler(), numerical),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical)
    ])
    model_random_pipe = Pipeline([
        ("preprocessor", preprocessor_rf),
        ("regressor", RandomForestRegressor(random_state=42))
    ])
    X_train_rf, X_test_rf, y_train_rf, y_test_rf = train_test_split(X_lr, y_lr, test_size=0.2, random_state=42)
    model_random_pipe.fit(X_train_rf, y_train_rf)
    y_pred_rf = model_random_pipe.predict(X_test_rf)
    st.text(
        f"Random Forest Regressor\n"
        f"R2 : {r2_score(y_test_rf, y_pred_rf):.4f}\n"
        f"MAE : {mean_absolute_error(y_test_rf, y_pred_rf):.4f}\n"
        f"MSE : {mean_squared_error(y_test_rf, y_pred_rf):.4f}"
    )

    st.markdown("---")

    # ── 17. Decision Tree Regressor ──────────────────────────────────────────────
    st.markdown("### 17. Model Decision Tree Regressor")
    st.code(
"""from sklearn.tree import DecisionTreeRegressor

model_tree = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", DecisionTreeRegressor())
])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model_tree.fit(X_train, y_train)
y_pred = model_tree.predict(X_test)

print("Decision Tree Regressor")
print("R2 :", r2_score(y_test, y_pred))
print("MAE :", mean_absolute_error(y_test, y_pred))
print("MSE :", mean_squared_error(y_test, y_pred))""",
        language="python"
    )
    st.markdown("**Output:**")
    from sklearn.tree import DecisionTreeRegressor
    preprocessor_dt = ColumnTransformer([
        ("num", StandardScaler(), numerical),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical)
    ])
    model_tree_pipe = Pipeline([
        ("preprocessor", preprocessor_dt),
        ("regressor", DecisionTreeRegressor(random_state=42))
    ])
    X_train_dt, X_test_dt, y_train_dt, y_test_dt = train_test_split(X_lr, y_lr, test_size=0.2, random_state=42)
    model_tree_pipe.fit(X_train_dt, y_train_dt)
    y_pred_dt = model_tree_pipe.predict(X_test_dt)
    st.text(
        f"Decision Tree Regressor\n"
        f"R2 : {r2_score(y_test_dt, y_pred_dt):.4f}\n"
        f"MAE : {mean_absolute_error(y_test_dt, y_pred_dt):.4f}\n"
        f"MSE : {mean_squared_error(y_test_dt, y_pred_dt):.4f}"
    )

    st.markdown("---")

    # ── 18. Cross Validation ─────────────────────────────────────────────────────
    st.markdown("### 18. Cross Validation Score")
    st.code(
"""from sklearn.model_selection import cross_val_score

scores = cross_val_score(model_linear, X_train, y_train, cv=5, scoring="r2")

print("Scores : ", scores)
print("Scores Mean : ", scores.mean())""",
        language="python"
    )
    st.markdown("**Output:**")
    from sklearn.model_selection import cross_val_score
    scores = cross_val_score(model_linear_pipe, X_train_lr, y_train_lr, cv=5, scoring="r2")
    st.text(
        f"Scores :  {scores}\n"
        f"Scores Mean :  {scores.mean()}"
    )

    st.markdown("---")

    # ── 19. Save & Load Model ────────────────────────────────────────────────────
    st.markdown("### 19. Simpan Model (joblib.dump)")
    st.code(
"""import joblib

joblib.dump(model_linear, "model_gaji.joblib")""",
        language="python"
    )
    st.markdown("**Output:**")
    st.text("['model_gaji.joblib']")

    st.markdown("---")

    # ── 20. Prediksi Data Baru ────────────────────────────────────────────────────
    st.markdown("### 20. Prediksi Data Baru")
    st.code(
"""import pandas as pd
import joblib

model_linear = joblib.load("model_gaji.joblib")

data_baru = pd.DataFrame([[
    "Senior",
    "Full-time",
    "Data Scientist",
    "Remote",
    "Besar",
    2023
]], columns=[
    "Tingkat Pengalaman",
    "Jenis Pekerjaan",
    "Jabatan",
    "Sistem Kerja",
    "Ukuran Perusahaan",
    "Tahun Kerja"
])

prediksi = model_linear.predict(data_baru)[0]
print(f"Model memprediksi jumlah gaji data Science (USD): {prediksi:.0f}")""",
        language="python"
    )
    st.markdown("**Output:**")
    st.text("Model memprediksi jumlah gaji data Science (USD): 155135")

    st.markdown('<div class="footer">©2026 - Dibuat dengan ❤ oleh Saskia Humaira menggunakan Streamlit &amp; Scikit-Learn</div>', unsafe_allow_html=True)
