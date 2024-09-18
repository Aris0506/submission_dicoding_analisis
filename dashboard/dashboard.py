###########################
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

######################
# Page configuration
st.set_page_config(
    page_title="Bike_Sharing_Dashboard",
    page_icon="🚲",
    layout="wide",  
    initial_sidebar_state="expanded")


###########################
# Baca dataset
df = pd.read_csv('days_reshaped.csv')

###########################  
# Mengelompokkan data berdasarkan tahun dan menghitung agregat
df_grouped = df.groupby('tahun').agg({
    'total_pengguna': 'sum',
    'pengguna_kasual': 'sum',
    'pengguna_terdaftar': 'sum',
    'suhu': 'mean',
    'suhu_terasa': 'mean',
    'kelembapan': 'mean',
    'kecepatan_angin': 'mean'
}).reset_index()

# Pastikan tanggal dalam format datetime
df['tanggal'] = pd.to_datetime(df['tanggal'], errors='coerce')  # Gunakan errors='coerce' untuk mengubah yang tidak bisa dikonversi menjadi NaT

###########################
# Membuat sidebar
with st.sidebar:
    st.markdown("""<h1 style='text-align: center;
            font-weight: bold;
            border-radius: 10px;
            font-size: 20px;
            color: yellow; 
            margin-bottom: 10px;
            background-color: rgba(0, 0, 0, 0.9);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            '>PT. Bike Sharing Mundar-Mandir</h1>
            """, unsafe_allow_html=True)
    # Menambahkan gambar
    # st.image('wallpaper.jpg', use_column_width=True)

    st.title('Menu Pilihan')
    tahun_list = ['All Years'] + sorted(df_grouped['tahun'].unique().tolist())
    selected_year = st.selectbox('Pilih Tahun', tahun_list)

# Filter data berdasarkan pilihan tahun
if selected_year == 'All Years':
    df_selected = df  # Tampilkan semua data jika opsi 'All Years' dipilih
else:
    df_selected = df[df['tahun'] == int(selected_year)]  # Filter data sesuai tahun yang dipilih

#################################################################################

###########################

# # Judul Dashboard di tengah
st.markdown("""
            <h1 style='text-align: center;
            font-size: 40px;
            color: yellow; 
            margin-bottom: 20px;
            padding-bottom: 1px;
            border-radius: 10px; 
            background-color: rgba(0, 0, 0, 0.9);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            '>🚲BIKE SHARING ANALYSIS DASHBOARD<br>IN 2011 AND 2012</br> </h1>
            """, unsafe_allow_html=True)

# Membuat tiga kolom untuk chart pertama
col1, col2 = st.columns(2)
###########################
with col1:
    # Section 1: Overview dari kelompokk data yang sudah di hitung agregatnya
    st.markdown("""<h2 style='text-align: left;  
                color: yellow;
                border-radius: 10px;
                font-size: 20px;
                padding:10px; 
                padding-left: 20px;
                background-color: rgba(0, 0, 0, 0.9);
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);'>Overview Section</h2>""", unsafe_allow_html=True)



    # with col1:
    def total_pengguna(total_pengguna): 
            st.markdown("""
            <style>
            .glassy {
                border-radius: 10px;
                font-size: 35px;
                text-align: center;
                font-weight: bold;
                color: black;  
                padding: 10px;
                background-color: rgba(255, 255, 0, 0.9); /* Warna putih dengan alpha 0.5 untuk efek kaca */
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Bayangan lembut */
            }
            </style>
            """, unsafe_allow_html=True)
            
            return st.markdown(f"<div class='glassy'>Total Users:</br>{total_pengguna}</div>", unsafe_allow_html=True)

    # Jika tahun yang dipilih adalah 'All Years', tampilkan total pengguna dari semua tahun
    if selected_year == 'All Years':
        hasil = df_grouped['total_pengguna'].sum()  # Total pengguna dari semua tahun
    else:
        hasil = df_grouped[df_grouped['tahun'] == int(selected_year)]['total_pengguna'].values[0]  # Total pengguna untuk tahun yang dipilih

    # Menampilkan total pengguna
    total_pengguna(hasil)


        
    # with col1:
#### Pengguna per Kategori
    def pengguna_perkategori(pengguna_kasual, pengguna_terdaftar):
        st.markdown("""
        <style>
        .glassy2 {
            border-radius: 10px;
            text-align: center;
            font-size: 20px;
            font-weight: bold;
            color: black;
            padding: 10px;       
            background-color: rgba(255, 255, 0, 0.9); /* Warna putih dengan alpha 0.5 untuk efek kaca */
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Bayangan lembut */
            }
            </style>
        """, unsafe_allow_html=True)
        return st.markdown(f"<div class='glassy2'>Users by category: </br>casual: {pengguna_kasual}</br>Registered: {pengguna_terdaftar}</div>", unsafe_allow_html=True) 
    # Mendapatkan pengguna kasual dan terdaftar
    if selected_year == 'All Years':
        pengguna_kasual = df_grouped['pengguna_kasual'].sum()  # Total pengguna kasual dari semua tahun
        pengguna_terdaftar = df_grouped['pengguna_terdaftar'].sum()  # Total pengguna terdaftar dari semua tahun
    else:
        pengguna_kasual = df_grouped[df_grouped['tahun'] == int(selected_year)]['pengguna_kasual'].values[0]
        pengguna_terdaftar = df_grouped[df_grouped['tahun'] == int(selected_year)]['pengguna_terdaftar'].values[0]

    # Menampilkan pengguna per kategori
    pengguna_perkategori(pengguna_kasual, pengguna_terdaftar)
    

# with col1:
 # Rata-rata Pengguna Harian
    def rata_rata_pengguna_harian(rata_harian):
        st.markdown("""
        <style>
        .glassy3 {
            border-radius: 10px;
            text-align: center;
            font-size: 20px;
            font-weight: bold;
            color: black;
            padding: 10px;      
            background-color: rgba(255, 255, 0, 0.9); /* Warna putih dengan alpha 0.5 untuk efek kaca */
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Bayangan lembut */
        }
        </style>
        """, unsafe_allow_html=True)
        return st.markdown(f"<div class='glassy3'>Average Daily Users:</br>{rata_harian}</div>", unsafe_allow_html=True) 
    
    # Menghitung rata-rata pengguna harian berdasarkan pilihan tahun
    if selected_year == 'All Years':
        rata_harian = df_grouped['total_pengguna'].mean()  # Rata-rata dari semua tahun
    else:
        rata_harian = df_grouped[df_grouped['tahun'] == int(selected_year)]['total_pengguna'].mean()  # Rata-rata untuk tahun yang dipilih

    # Membulatkan rata-rata
    rata_harian_bulat = round(rata_harian)

    # Menampilkan rata-rata pengguna harian
    rata_rata_pengguna_harian(rata_harian_bulat)


# Tampilkan dataframe yang sudah difilter
st.markdown(f"""<h2 style='text-align: left;  
                color: black;
                font-size: 15px;
                padding: 10px;
                border-radius: 10px; 
                margin-bottom: 10px;
                padding-left: 20px;
                margin-top:5px; 
                font-weight: bold;
                background-color: rgba(255, 255, 0, 0.9); /* Warna putih dengan alpha 0.5 untuk efek kaca */
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);'>Dataset: {selected_year}</h2>""",
                unsafe_allow_html=True)
st.dataframe(df_selected.head())


#################################################################################


with col2:
    st.markdown("""<h2 style='text-align: left;  
                color: black;
                font-size: 20px;
                padding: 10px;
                border-radius: 10px; 
                margin-bottom: 10px;
                padding-left: 20px;
                font-weight: bold;
                background-color: rgba(255, 255, 0, 0.9); /* Warna putih dengan alpha 0.5 untuk efek kaca */
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);'>User trends by Years</h2>""",
                unsafe_allow_html=True)

    def tren_pengguna_berdasarkan_tahun(df_selected):
        # Visualisasi tren menggunakan bar chart
        plt.figure(figsize=(10, 8))
        sns.barplot(data=df_selected, x='tahun', y='total_pengguna', hue='tahun', palette='muted')
        
        # plt.title('Total Pengguna Bike-sharing per Tahun', fontsize=16)
        plt.xlabel('Tahun', fontsize=14)
        plt.ylabel('Total Pengguna', fontsize=14)
        plt.xticks(fontsize=14)
        plt.yticks(fontsize=14)
        
        # Menyesuaikan tata letak
        plt.tight_layout()
        
        # Menampilkan grafik di Streamlit
        st.pyplot(plt)
     # Panggil fungsi visualisasi dengan data yang difilter
    tren_pengguna_berdasarkan_tahun(df_selected)


col1, col2 = st.columns(2)    
with col1:
    # # Panggil fungsi visualisasi
    # tren_pengguna_berdasarkan_musim(df_selected)
    def tren_pengguna_berdasarkan_musim(df_selected):
        st.markdown("""<h3 style= 'border-radius: 10px;
                font-size: 15px; 
                text-align:left;
                color: black;
                font-weight: bold;
                border-radius: 10px;
                padding:10px;
                background-color: rgba(255, 255, 0, 0.9);
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);'>The Impact of Seasons on Users.</h3>""", unsafe_allow_html=True) 
    
    # Mengelompokkan data berdasarkan musim
        df_grouped_musim = df_selected.groupby('musim').agg({
            'total_pengguna': 'sum'
        }).reset_index()

        # Mengatur warna untuk setiap musim
        palette = sns.color_palette("muted", len(df_grouped_musim))

        # Membuat figure dan axis
        fig, ax1 = plt.subplots(figsize=(10, 7))

        # Bar plot
        sns.barplot(x='musim', y='total_pengguna', data=df_grouped_musim, palette=palette, ax=ax1, alpha=0.6, legend=False)

        # Line plot
        ax2 = ax1.twinx()  # Membuat axis kedua
        ax2.plot(df_grouped_musim['musim'], df_grouped_musim['total_pengguna'], marker='o', color='blue', label='Total Pengguna')

        # Menambahkan label dan title
        # ax1.set_title('Penggunaan Bike-sharing Berdasarkan Musim', fontsize=16)
        ax1.set_xlabel('Musim', fontsize=14)
        ax1.set_ylabel('Total Pengguna', fontsize=14)
        # ax2.set_ylabel('Total Pengguna (Trend)', fontsize=14)

        # Menambahkan legend
        ax2.legend(loc='upper left')

        # Mengatur tampilan
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.tight_layout()

        # Menampilkan plot dengan Streamlit
        st.pyplot(fig)

    # Panggil fungsi visualisasi hanya jika df_selected tidak kosong
    if not df_selected.empty:
        tren_pengguna_berdasarkan_musim(df_selected)
    else:
        st.warning("Data tidak tersedia untuk tahun yang dipilih.")

  ############  
with col2:  
    def pengaruh_cuaca_terhadap_pengguna(df_selected):

        st.markdown("""<h3 style= 'border-radius: 10px;
                font-size: 15px; 
                text-align:left;
                color: black;
                font-weight: bold;
                border-radius: 10px;
                padding:10px;
                background-color: rgba(255, 255, 0, 0.9);
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);'>The Impact of Weather Conditions on Total Users.</h3>""", unsafe_allow_html=True)
        # Mengelompokkan data berdasarkan kondisi cuaca
        df_grouped_cuaca = df_selected.groupby('kondisi_cuaca').agg({
            'total_pengguna': 'sum'
        }).reset_index()

        # Membuat figure
        plt.figure(figsize=(14, 9.5))

        # Bar plot
        sns.barplot(y='kondisi_cuaca', x='total_pengguna', data=df_grouped_cuaca, hue='kondisi_cuaca', palette='muted', legend=False)
        # plt.title('Pengaruh Kondisi Cuaca terhadap Total Pengguna', fontsize=16)
        plt.xlabel('Total Pengguna', fontsize=16)
        plt.yticks(rotation=90)
        plt.ylabel('Kondisi Cuaca', fontsize=16)
        plt.tight_layout()

        # Menampilkan plot dengan Streamlit
        st.pyplot(plt)

    # Panggil fungsi visualisasi jika ada data yang tersedia
    if not df_selected.empty:
        pengaruh_cuaca_terhadap_pengguna(df_selected)
    else:
        st.warning("Tidak ada data untuk tahun yang dipilih.")

############################
# Menampilkan judul aplikasi
st.markdown("""<h2 style='text-align: left;  
            font-size: 20px;
            color: yellow;
            margin-top: 40px;
            border-radius: 10px;
            margin-bottom: 10px;
            padding-left: 20px; 
            background-color: rgba(0, 0, 0, 0.9);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);'>RFM Analysis</h2>""",
            unsafe_allow_html=True)


col1, col2, col3 = st.columns(3)

with col1:
    # Menghitung Recency
    last_date = df_selected['tanggal'].max()
    df_selected['recency'] = (last_date - df_selected['tanggal']).dt.days 

    # Memfilter data untuk hanya menyertakan 10 hari terakhir
    df_filtered = df_selected[df_selected['recency'] <= 10]

    # Menghitung jumlah bins menggunakan aturan square-root
    n = len(df_filtered)
    bins = int(np.sqrt(n)) if n > 0 else 1

    # Visualisasi Recency
    st.markdown("""<h3 style= '
                border-radius: 10px;
                font-size: 15px; 
                text-align:left;
                color: black;
                font-weight: bold;
                padding:10px;
                background-color: rgba(255, 255, 0, 0.9);
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);'>Recency Distribution</h3>""",
                unsafe_allow_html=True)

    plt.figure(figsize=(6, 4.5))
    sns.histplot(df_filtered['recency'], bins=bins, color='salmon', kde=True)
    # plt.title('Recency Distribution', fontsize=16)
    plt.xlabel('Recency (days)', fontsize=14)
    plt.ylabel('Total Users', fontsize=14)
    st.pyplot(plt)

with col2:
    # Menghitung Frequency
    df_frequency = df_selected.groupby('tahun').agg({'total_pengguna': 'sum'}).reset_index()

    # Visualisasi Frequency
    st.markdown("""<h3 style= 'border-radius: 10px;
                font-size: 15px; 
                text-align:left;
                color: black;
                font-weight: bold;
                padding:10px; 
                background-color: rgba(255, 255, 0, 0.9);
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);'>Frequency Distribution</h3>""",
                unsafe_allow_html=True)

    plt.figure(figsize=(6, 4.5))
    sns.barplot(data=df_frequency, x='tahun', y='total_pengguna', color='#90EE90')
    # plt.title('Frequency Distribution', fontsize=16)
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Total Users', fontsize=14)
    # plt.xticks()
    st.pyplot(plt)

with col3:
    # Menghitung Monetary
    df_monetary = df_selected.groupby('tahun').agg({
        'pengguna_kasual': 'sum',
        'pengguna_terdaftar': 'sum'
    }).reset_index()

    # Visualisasi Monetary
    st.markdown("""<h3 style= 'border-radius: 10px;
                font-size: 15px; 
                text-align:left;
                color: black;
                font-weight: bold;
                padding:10px;
                background-color: rgba(255, 255, 0, 0.9);
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);'>Monetary Distribution</h3>""",
                unsafe_allow_html=True)

    plt.figure(figsize=(6, 4))
    df_monetary.set_index('tahun')[['pengguna_kasual', 'pengguna_terdaftar']].plot(kind='bar', stacked=True, color=['salmon', 'skyblue'])
    # plt.title('Monetary Distribution', fontsize=16)
    plt.xlabel('Year', fontsize=14)
    plt.xticks(rotation=360)
    plt.ylabel('Total Users', fontsize=14)
    plt.legend(title='Category')
    st.pyplot(plt)