# 5) Напишите скрипт, который преобразует время формата UNIX 1605697332 в формат 2020-11-18T11:02:12+06:00

import datetime  # библиотека для работы с датами

timestamp = 1605697332
tz = datetime.timezone(datetime.timedelta(hours=6))  # настраиваем часовой пояс
date_time = datetime.datetime.fromtimestamp(timestamp, tz).isoformat()  # форматируем

print(date_time)  # выводим результат
