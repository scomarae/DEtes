import pandas as pd  # библиотека для работы с датафреймами

df = pd.read_csv('2.csv')  # читаем csv-файл
print(df)  # выводим на экран

df['A'] = pd.to_datetime(df['A'])  # преобразуем столбец в формат datetime

# создаем новый столбец B со значениями из столбца A
df['B'] = df['A']

condition = (df['B'].dt.time >= pd.to_datetime('14:00').time()) \
            & (df['B'].dt.time <= pd.to_datetime('19:00').time())  # условие замены значения

df.loc[condition, 'B'] += pd.Timedelta(minutes=15)  # прибавляем минуты

df.to_csv('new_2.csv', index=False)  # записываем в новый файл
