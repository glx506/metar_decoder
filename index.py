#!-*- codifn: utf-8 -*-
'''Парсер метео сводок в формате METAR'''
import re
import datetime

def _get_metar_data():
    '''Функция получения строки из файла с метеосводкой'''
    with open(METAR_STATION_FILE, "r") as metar_data:
        for number_one, line in enumerate(metar_data):
            if number_one == 1:
                metar_data = line

    return metar_data

class MetarParser:
    '''Класс разбора строки с метеосводкой'''
    def __init__(self, metar_data):
        '''Принимаем значение строки со сводкой'''
        self.metar_data = metar_data

    def airport_id(self):
        '''Метод поиска индекса аэропорта в формате ICAO'''
        airport_id = re.search(r'[A-Z]{4}', self.metar_data)
        print('IDENTIFIER: {0}'.format(airport_id[0]))

    def cut_id(self):
        '''Отрезаем индекс аэропорта'''
        self.metar_data = self.metar_data.split(' ')[1:]
        self.metar_data = str.join(',', self.metar_data)
        self.metar_data = self.metar_data.replace(',', ' ')

    def forecast_time(self):
        '''Время формирования отчета'''
        month = datetime.datetime.today().strftime("%B")
        forecast_time = re.search(r'[0-9]{6}[Z]', self.metar_data)
        print('TIME ISSUED: {0} {1} {2}'.format(forecast_time[0][:2], month, forecast_time[0][2:4]))

    def report_type(self):
        '''Тип формирования отчета AUTO - в случае если сформирован автоматом'''
        report_type = re.search(r'AUTO', self.metar_data)
        if report_type:
            print("REPORT TYPE: This is a fully automated report")

    def wind_type(self):
        '''Определение скорости и навправления ветра'''
        wind = re.search(r'[0-9]{5}MPS', self.metar_data)
        if wind:
            knots = int(wind[0][3:-3]) * 1.97
            knots = round(knots, 0)
            print("WIND: Winds from " + wind[0][:3] + "° at " + wind[0][3:-3]
                  + " mps (" + str(knots) + " knots)")

        wind = re.search(r'[0-9]{5}KT', self.metar_data)
        if wind:
            mps = int(wind[0][3:-2]) * 0.51
            mps = round(mps, 0)
            print("WIND: Winds from " + wind[0][:3] + "° at " + wind[0][3:-2]
                  + " knots (" + str(mps) + " mps)")

        wind = re.search(r'[0-9]{5}G[0-9]{2}MPS', self.metar_data)
        if wind:
            knots = int(wind[0][-5:-3]) * 1.97
            knots = round(knots, 0)
            print("WIND: Winds from " + wind[0][:3] + "° at " + wind[0][3:5]
                  + " mps with gusts up to " + wind[0][-5:-3] + " mps (" + str(knots) + " knots)")

        wind = re.search(r'[0-9]{5}G[0-9]{2}KT', self.metar_data)
        if wind:
            mps = int(wind[0][-4:-2]) * 0.51
            mps = round(mps, 0)
            print("WIND: Winds from " + wind[0][:3] + "° at " + wind[0][3:5]
                  + " knots with gusts up to " + wind[0][-4:-2] + " knots (" + str(mps) + " mps)")

        wind = re.search(r'[0-9]{3}V[0-9]{3}', self.metar_data)
        if wind:
            print("Variable wind direction between " + wind[0][:3] + "° and " + wind[0][4:] + "°")

        wind = re.search(r'VRB[0-9]{2}MPS', self.metar_data)
        if wind:
            knots = int(wind[0][3:-3]) * 1.97
            knots = round(knots, 0)
            print("Variable wind directions at " + wind[0][3:-3]
                  + " mps (" + str(knots) + " knots)")

        wind = re.search(r'VRB[0-9]{2}KT', self.metar_data)
        if wind:
            mps = int(wind[0][3:-2]) * 0.51
            mps = round(mps, 0)
            print("Variable wind directions at " + wind[0][3:-2] + " knots (" + str(mps) + " mps)")

    def visibility_value(self):
        '''Условия видимости'''
        visibility = re.search(r'\s[0-9]{4}\s', self.metar_data)
        if visibility:
            if visibility[0].replace(' ', '') == "9999":
                print("VISIBILITY: Visibility is 10km or more.")
            else:
                print("VISIBILITY: Visibility is " + visibility[0].replace(' ', '') + " meter")


if __name__ == "__main__":
    METAR_STATION_FILE = "UUEE.TXT" # Файл с метеосводкой
    _get_metar_data() # Вызыв функции извлечения строки метеосводки
    print(_get_metar_data()) # Выводим строку сводки на экран
    MMP = MetarParser(_get_metar_data()) # Передаем строку с данными в class MetarParser
    MMP.airport_id() # Вывод индекса аэропорта
    MMP.forecast_time() # Вывод времени формирования формирования отчета
    MMP.report_type() # Вывод типа формирования
    MMP.wind_type() # Вывод скорости и направления ветра
    MMP.visibility_value() # Вывод условий видимости
