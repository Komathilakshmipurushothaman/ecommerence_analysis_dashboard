import pandas as pd
import numpy as np
from sqlalchemy import create_engine


#  Load Dataset

df = pd.read_csv(r"C:\Users\Komathi lakshmi P\OneDrive\Desktop\finalproject\ecommerce_update.csv")

print(df.head())

print(df.info())
print(df.describe())

#  Sort Data

df = df.sort_values("order_id")


#  Handle Missing Values


df["city"] = df["city"].fillna("Unknown")
df["gender"] = df["gender"].fillna("Female")
df["product_name"] = df["product_name"].fillna(df["product_name"].mode()[0])
df["brand"] = df["brand"].fillna(df["brand"].mode()[0])
df["category"] = df["category"].fillna(df["category"].mode()[0])
df["payment_mode"] = df["payment_mode"].fillna(df["payment_mode"].mode()[0])
df["order_status"] = df["order_status"].fillna(df["order_status"].mode()[0])


df["return_reason"] = df["return_reason"].fillna("Not Returned")
df["return_date"] = df["return_date"].fillna("Not Returned")


df["age"] = df["age"].fillna(df["age"].median())
df["price"] = df["price"].fillna(df["price"].median())
df["quantity"] = df["quantity"].fillna(df["quantity"].median())


df["order_date"] = df["order_date"].fillna(df["order_date"].mode()[0])

df["order_date"] = pd.to_datetime(df["order_date"])
df["signup_date"] = pd.to_datetime(df["signup_date"])
df["last_order_date"] = pd.to_datetime(df["last_order_date"])


df["order_date"] = df["order_date"].fillna(df["order_date"].mode()[0])
df["last_order_date"] = df["last_order_date"].fillna(df["last_order_date"].mode()[0])
df["order_year"] = df["order_date"].dt.year
df["order_month"] = df["order_date"].dt.month
df["order_day"] = df["order_date"].dt.day_name()
df["order_month"] = df["order_date"].dt.month_name()

customers = df[["customer_id","customer_name","gender","age","signup_date","last_order_date","city"]]

products = df[["product_id","product_name","brand","category","price"]]

orders = df[["order_id","order_date","customer_id","product_id","quantity","payment_mode","order_status","return_date","return_reason","order_year","order_month","order_day"]]

df["order_month"] = df["order_date"].dt.month_name()

print(df.head())
print(df.isnull().sum())



username="root",
password="komathi",
host="localhost",
port="3306",
database="final_project2"
engine = create_engine(f"mysql+pymysql://root:komathi@localhost:3306/final_project2"
)
table_name="finalproject"
df.to_sql(table_name,engine,if_exists="replace",index=False)
customers.to_sql("customers", engine, if_exists="replace", index=False)
products.to_sql("products", engine, if_exists="replace", index=False)
orders.to_sql("orders", engine, if_exists="replace", index=False)