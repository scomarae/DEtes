import pandas as pd  # библиотека для работы с датафреймами

df = pd.read_csv('1.csv')  # читаем csv-файл
print(df)  # выводим на экран

df['A'] = df['A'].str.replace(',', '.')
df['A'] = df['A'].str.replace(' ', '')  # форматируем столбец A, чтобы не было проблем с изменением типа
df['A'] = df['A'].astype(float)  # меняем тип

df['B'] = df['B'].fillna(0.0)  # форматируем столбец B
df['B'] = df['B'].astype(int)  # меняем тип

df['C'] = pd.to_datetime(df['C']).dt.date  # оставляем дату в столбце C

df['D'] = pd.to_datetime(df['D']).dt.time  # оставляем дату в столбце D

df.to_csv('new_1.csv', index=False)  # записываем в новый файл
