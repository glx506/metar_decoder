'''Пробую написать модуль определения  погоды'''
import re

WEATHER_DATA_FILE = "weather.dat.txt"
WEATHER_TYPE = 'GR'

WEATHER_TYPE_MODIFIED = WEATHER_TYPE.replace('+', r'\+') # Добавляем \ для +
with open(WEATHER_DATA_FILE, encoding='utf-8') as weather_data:
    for line in weather_data:
        result = re.match(WEATHER_TYPE_MODIFIED, line.replace('"', '')) # Поиск погоды
        if result:
            found_string = line.replace('"', '') # Отрезаем из найденой строки ковычки
            print(found_string.split(",", 1)[1])
            ''' Делим строку на список из 2-х элементов разделителем служит запятая и выводим второе
             значение списка '''
