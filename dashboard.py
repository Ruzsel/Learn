import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.sidebar.write('Nama: Fairuz Mujahid Annabil')
st.sidebar.write('ID Dicoding: faimujahid')

customers_df = pd.read_csv('customers_dataset.csv')
customers_df.head()

orders_df = pd.read_csv('orders_dataset.csv')
orders_df.head()

products_df = pd.read_csv('products_dataset.csv')
products_df.head()

sales_df = pd.read_csv('order_items_dataset.csv')
sales_df.head()

orders_df.dropna(subset=['order_approved_at', 'order_delivered_carrier_date', 'order_delivered_customer_date'], how='any', inplace=True)
datetime_columns = ["order_purchase_timestamp", "order_approved_at", "order_delivered_carrier_date", "order_delivered_customer_date", "order_estimated_delivery_date"]
 
for column in datetime_columns:
  orders_df[column] = pd.to_datetime(orders_df[column])

products_df.dropna(axis=0, inplace=True)

bystate_df = customers_df.groupby(by="customer_state").customer_id.nunique().sort_values(ascending=False).head(7)
plt.figure(figsize=(10, 6))
sns.barplot(x=bystate_df.index, y=bystate_df.values, hue=bystate_df.index, palette='viridis', dodge=False)
plt.title('Top 7 Negara Bagian berdasarkan Jumlah Pelanggan', fontsize=15)
plt.xlabel('Negara Bagian', fontsize=12)
plt.ylabel('Jumlah Pelanggan', fontsize=12)
plt.xticks(rotation=45)
plt.show()

delivery_time = orders_df["order_delivered_customer_date"] - orders_df["order_purchase_timestamp"]
delivery_time = delivery_time.apply(lambda x: x.total_seconds())
orders_df["delivery_time"] = round(delivery_time / 86400)
plt.figure(figsize=(10, 6))
plt.hist(orders_df["delivery_time"], bins = 50, color='skyblue', edgecolor='black')
plt.title('Distribusi Waktu Pengiriman barang', fontsize=15)
plt.xlabel('Waktu dalam hari', fontsize=12)
plt.ylabel('Frekuensi', fontsize=12)
plt.show()

harga_ke_frekuensi = sales_df.groupby(by="price").order_id.nunique().sort_values(ascending=False).reset_index().head(10)
plt.figure(figsize=(12, 6))
plt.bar(harga_ke_frekuensi["price"], harga_ke_frekuensi["order_id"], color='skyblue')
plt.title('Top 10 Price Ranges by Order Frequency', fontsize=15)
plt.xlabel('Rentang Harga(Dollar)', fontsize=12)
plt.ylabel('Frekuensi Order Pelanggan', fontsize=12)
plt.xticks(rotation=45)
plt.show()

# Visualisasi 1: Bar chart untuk jumlah pelanggan berdasarkan negara bagian
st.title('Visualisasi Jumlah Pelanggan Berdasarkan Negara Bagian')
fig1, ax1 = plt.subplots()
bystate_df = customers_df.groupby(by="customer_state").customer_id.nunique().sort_values(ascending=False).head(7)
sns.barplot(x=bystate_df.index, y=bystate_df.values, hue=bystate_df.index, palette='viridis', dodge=False, legend=False)
plt.title('Top 7 Negara Bagian berdasarkan Jumlah Pelanggan', fontsize=15)
plt.xlabel('Negara Bagian', fontsize=12)
plt.ylabel('Jumlah Pelanggan', fontsize=12)
plt.xticks(rotation=45)
st.pyplot(fig1)

# Visualisasi 2: Histogram untuk distribusi waktu pengiriman
st.title('Visualisasi Distribusi Waktu Pengiriman Barang')
fig2, ax2 = plt.subplots()
delivery_time = orders_df["order_delivered_customer_date"] - orders_df["order_purchase_timestamp"]
delivery_time = delivery_time.apply(lambda x: x.total_seconds())
orders_df["delivery_time"] = round(delivery_time / 86400)
plt.hist(orders_df["delivery_time"], bins=50, color='skyblue', edgecolor='black')
plt.title('Distribusi Waktu Pengiriman barang', fontsize=15)
plt.xlabel('Waktu dalam hari', fontsize=12)
plt.ylabel('Frekuensi', fontsize=12)
st.pyplot(fig2)

# Visualisasi 3: Bar chart untuk rentang harga dengan frekuensi pembelian
st.title('Visualisasi Rentang Harga dengan Frekuensi Pembelian Pelanggan')
fig3, ax3 = plt.subplots()
harga_ke_frekuensi = sales_df.groupby(by="price").order_id.nunique().sort_values(ascending=False).reset_index().head(10)
plt.bar(harga_ke_frekuensi["price"], harga_ke_frekuensi["order_id"], color='skyblue')
plt.title('Top 10 Price Ranges by Order Frequency', fontsize=15)
plt.xlabel('Rentang Harga(Dollar)', fontsize=12)
plt.ylabel('Frekuensi Order Pelanggan', fontsize=12)
plt.xticks(rotation=45)
st.pyplot(fig3)