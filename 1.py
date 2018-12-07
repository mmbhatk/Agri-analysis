import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('agridata.csv')

print("\nColumns in the dataframe: ")
ls = df.columns
print(ls)

print("\nMissing values: ")
print(df.isnull().sum())
df.dropna(axis='rows', inplace = True)
 
print("\nAfter removing missing values: ")
print(df.isnull().sum())

print("\nValues taken by all columns: ")
for col in ls:
    print("-------------------------")
    print(col)
    print(df[col].unique())

print(df[df['year']=='Year'])
df = df[df['year']!='Year']
print("\nAfter removing the rows where year is Year, all possible values taken by 'year': ")
print(df['year'].unique())

print(df.columns)
df.season.value_counts()

print("\nData types of all the columns: ")
print(df.dtypes)

print(len(df))

df['year'] = df['year'].str[:-3]
print("Converting years from range form: ")
print(df['year'].head())

df.corr()

print("\nPlotting one variable: ")

print("\nPloting state: ")
df['state'].value_counts().plot(kind='bar');

print("\nPlotting crops: ")
df['crop'].value_counts().plot(kind='bar');

print("\nPlotting years: ")
df['year'].value_counts().plot(kind='bar');

print("\nPlotting season: ")
df['season'].value_counts().plot(kind='bar');