import pandas as pd

df = pd.read_csv('data/raw/ispu_dki_all.csv')

# Rename columns to English
df = df.rename(columns={
    'tanggal' : 'date',
    'stasiun' : 'station',
    'pm25' : 'pm25',
    'pm10' : 'pm10',
    'so2' : 'so2',
    'co' : 'co',
    'o3' : 'o3',
    'no2' : 'no2',
    'max' : 'max',
    'critical' : 'critical',
    'categori' : 'category',
})

# Convert date column to datetime format
df['date'] = pd.to_datetime(df['date'])

print(df.head())

print("Unique Categories:")
print(df['category'].unique())

category_map = { 
    'BAIK': 'GOOD',
    'SEDANG': 'MODERATE',
    'TIDAK SEHAT': 'UNHEALTHY',
    'SANGAT TIDAK SEHAT': 'VERY UNHEALTHY',
    'BERBAHAYA': 'HAZARDOUS',
    'TIDAK ADA DATA': 'NO DATA',
}

# map the categories to the new values
df['category'] = df['category'].map(category_map)

print("Unique Categories after mapping:")
print(df['category'].unique())

# Fill all numeric columns missing values with median
numeric_cols = df.select_dtypes(include='number').columns

for col in numeric_cols:
    median_val = df[col].median()
    df[col] = df[col].fillna(median_val)

# Check if any missing values remain
print(df.isnull().sum())

print(df.info())
print(df['category'].value_counts())
print(df.head())

df.to_csv('data/processed/cleaned_data.csv', index=False)

