import pandas as pd
import mysql.connector

# 1️⃣ Read CSV
file_path = r"C:\Users\Dell\OneDrive\Desktop\Personal Finance and Investment Analytics System\Personal_Finance_Dataset.csv"
df = pd.read_csv(file_path)

print("CSV Columns:", df.columns)

# 2️⃣ Rename CSV columns to match MySQL table
df.rename(columns={
    'Date': 'transaction_date',
    'Transaction Description': 'description',
    'Category': 'category',
    'Amount': 'amount',
    'Type': 'type'
}, inplace=True)

# 3️⃣ Clean Data
df = df.fillna('')

# Convert amount safely
df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
df = df.dropna(subset=['amount'])

# 4️⃣ Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",   # change if different
    database="personal_finance"
)

cursor = conn.cursor()

# 5️⃣ Insert Query
insert_query = """
INSERT INTO transactions 
(transaction_date, description, category, amount, type)
VALUES (%s, %s, %s, %s, %s)
"""

# 6️⃣ Insert Data
for _, row in df.iterrows():
    cursor.execute(insert_query, (
        row['transaction_date'],   # already in YYYY-MM-DD
        row['description'],
        row['category'],
        float(row['amount']),
        row['type']
    ))

conn.commit()

print("DONE ✅ Data inserted successfully!")

cursor.close()
conn.close()