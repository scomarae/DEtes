import json
import xmltodict

with open('doc.xml', 'r') as file:  # открываем файл
    xml_data = file.read()

dict_data = xmltodict.parse(xml_data)  # обрабатываем xml в словарь
json_data = json.dumps(dict_data)  # преобразуем в json

print(json_data)  # выводим результат
