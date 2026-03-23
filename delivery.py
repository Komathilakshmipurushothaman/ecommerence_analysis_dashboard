import pandas as pd
import numpy as np
from sqlalchemy import create_engine

# Load dataset
df = pd.read_csv(r"C:\Users\Komathi lakshmi P\OneDrive\Desktop\finalproject\food_delivery_analyticss.csv")

# Basic Info
print(df.head())
print("Shape:", df.shape)
print(df.info())
print(df.describe())

# -------------------------------
# 🔹 Data Cleaning
# -------------------------------

# Sort by order_id
df = df.sort_values("order_id")

# Fill missing values
df["city"] = df["city"].fillna("Unknown")

df["delivery_time_minutes"] = df["delivery_time_minutes"].fillna(df["delivery_time_minutes"].median())

df["order_amount"] = df["order_amount"].fillna(df["order_amount"].median())

# -------------------------------
# 🔹 Date & Time Feature Engineering
# -------------------------------

# Convert to datetime
df["order_datetime"] = pd.to_datetime(df["order_datetime"])

# Extract date features
df["order_date"] = df["order_datetime"].dt.date
df["order_time"] = df["order_datetime"].dt.time
df["day"] = df["order_datetime"].dt.day_name()
df["month"] = df["order_datetime"].dt.month
df["year"] = df["order_datetime"].dt.year

# -------------------------------
# 🔹 Delivery Speed Category
# -------------------------------

def delivery_speed_category(minutes):
    if minutes <= 30:
        return "FAST"
    elif minutes <= 45:
        return "MEDIUM"
    else:
        return "SLOW"

df["delivery_speed"] = df["delivery_time_minutes"].apply(delivery_speed_category)

# -------------------------------
# 🔹 Customer Rating Based on Delivery Time
# -------------------------------

def generate_rating(minutes):
    if minutes <= 30:
        return 5
    elif minutes <= 45:
        return 4
    elif minutes <= 60:
        return 3
    elif minutes <= 75:
        return 2
    else:
        return 1

df["rating"] = df["delivery_time_minutes"].apply(generate_rating)

# -------------------------------
# 🔹 Final Check
# -------------------------------

print(df.head())
print(df.isnull().sum()) 
sername="root",
password="komathi",
host="localhost",
port="3306",
database="final_project"
# it is used to start the connector
# f reprsent the push
engine = create_engine(f"mysql+pymysql://root:komathi@localhost:3306/final_project"
)
table_name="finalproject"
df.to_sql(table_name,engine,if_exists="replace",index=False)