import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

def run():
    #membuat judul
    st.title('E-Commerce Customer Churn Prediction EDA')
    
    #membuat batas dengan garis lurus
    st.markdown('---')

    #membuat sub header
    st.subheader('This EDA focuses on understanding the factors influencing customer churn in e-commerce')

    #menambahkan gambar
    image = Image.open('ecommerce.jpg')
    st.image(image, caption = 'Customer Churn Prediction')

    #menambahkan deskripsi
    st.write('Page ini dibuat oleh Ranie Sita - Phase 1 RMT 030')
    #menambahkan deskripsi
    st.write('Objective: Dalam industri e-commerce, mempertahankan pelanggan merupakan aspek kritis yang mempengaruhi keberlanjutan dan pertumbuhan pendapatan perusahaan. Studi menunjukkan bahwa tingkat retensi pelanggan sebesar 5% dapat meningkatkan keuntungan perusahaan hingga 25% sampai 95%. Mengingat persaingan yang ketat dan biaya akusisi pelanggan yang tinggi, perusahaan perlu memahami faktor-faktor yang berkontribusi terhadap churn pelanggan untuk mengembangkan strategi yang lebih efektif dalam mempertahakan pelanggan. Proyek ini bertujuan untuk mengembangkan model klasifikasi prediktif yang mengidentifikasi pelanggan yang berisiko tinggi untuk churn dari platform e-commerce.')
    
    #membuat batas dengan garis lurus
    st.markdown('---')

    #show dataframe
    data = pd.read_csv('ecommerce_customer_data_custom_ratios.csv')
    st.dataframe(data)

    #menampilkan distribusi variabel target
    st.write('## Distribusi Churn')
    fig = plt.figure(figsize=(15,8))
    sns.countplot(data=data, x='Churn')
    plt.title('Churn Distribution')
    st.pyplot(fig)

    #jumlah Pembelian Rata-rata berdasarkan Kategori Usia
    st.write('## Jumlah Pembelian Rata-rata berdasarkan Kategori Usia')
    fig = plt.figure(figsize=(10,8))
    sns.barplot(data=data, x='Age Category', y='Total Purchase Amount', palette='viridis')
    plt.title('Average Purchase Amount by Age Category')
    st.pyplot(fig)

    #jumlah Pembelian Berdasarkan Kategori Produk
    st.write('## Jumlah Pembelian Berdasarkan Kategori Produk')
    fig = plt.figure(figsize=(10,8))
    sns.countplot(data=data, x='Product Category', palette='bright')
    plt.title('Number of Purchases by Product Category')
    st.pyplot(fig)

    #jumlah Pembelian berdasarkan Jenis Kelamin
    st.write('## Jumlah Pembelian berdasarkan Jenis Kelamin')
    fig = plt.figure(figsize=(10,8))
    sns.boxplot(data=data, x='Gender', y='Total Purchase Amount')
    plt.title('Purchase Amount by Gender')
    st.pyplot(fig)

    #heatmap korelasi variabel numerik
    st.write('## Heatmap Korelasi Variabel Numerik')
    fig = plt.figure(figsize=(10,8))
    numerical_data = data.select_dtypes(include=[np.number])
    correlation_matrix = numerical_data.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation matrix')
    st.pyplot(fig)

    # Pairwise pada beberapa variabel numerik dalam dataset
    st.write('## Pairwise pada Beberapa Variabel Numerik dalam Dataset')
    sns.pairplot(data[['Total Purchase Amount', 'Customer Age', 'Quantity']])
    st.pyplot(plt)

if __name__ == '__main__':
    run()