import openpyxl
import pandas as pd


workbook = openpyxl.load_workbook('3.xlsx')  # читаем файл в workbook и выбираем нужный лист
sheet = workbook['Лист1']


rows_to_delete = []  # список индексов строк для удаления


for row in sheet.iter_rows(min_row=6, min_col=1, max_col=1):  # перебираем строки
    for cell in row:
        if cell.font.bold:  # если шрифт жирный
            rows_to_delete.append(row[0].row - 2)  # добавляем строку в список


df = pd.read_excel('3.xlsx')  # загружаем датафрейм
df = df.drop(rows_to_delete)  # удаляем в нем строки
print(df)  # выводим на экран


df.to_excel('new_3.xlsx', index=False, header=['' for _ in range(16)])  # записываем в новый xlsx-файл
