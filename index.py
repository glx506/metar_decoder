#!-*- codifn: utf-8 -*-
'''Парсер метео сводок в формате METAR'''
import sys
import re
import datetime

WEATHER_DATA_FILE = "weather.dat.txt"
METAR_STATION_FILE = sys.argv[1] # Файл с метеосводкой

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
        '''Метод поиска времени формирования отчета'''
        month = datetime.datetime.today().strftime("%B")
        forecast_time = re.search(r'[0-9]{6}[Z]', self.metar_data)
        print('TIME ISSUED: {0} {1} {2}:{3}'.format(forecast_time[0][:2], month,
                                                    forecast_time[0][2:4], forecast_time[0][4:6]))
    def report_type(self):
        '''Определение типа формирования отчета AUTO - в случае если сформирован автоматом'''
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
        '''Метод определения условий видимости'''
        visibility = re.search(r'\s[0-9]{4}\s', self.metar_data)
        if visibility:
            if visibility[0].replace(' ', '') == "9999":
                print("VISIBILITY: Visibility is 10km or more.")
            else:
                print("VISIBILITY: Visibility is " + visibility[0].replace(' ', '') + " meter")

    def weather_type(self):
        '''Метод определения типа погоды'''
        weather = re.search(r'''[\-\+]DZ|DZ|[\-\+]RA|RA|[\-\+]SN|SN|[\-\+]SG|SG|[\-\+]PL|PL
                               |[\-\+]GS|GS|[\-\+]DS|DS|[\-\+]SS|SS|DU|SQ|BR|HZ|FU|IC|TS|FG
                               |VA|BLSN|FZFG|VCFG|MIFG|PRFG|BCFG|DRSN|DRSA|DRDU|BLDU|VCTS
                               |[\-\+]RASN|RASN|[\-\+]SNRA|SNRA|[\-\+]SHSN|SHSN|[\-\+]SHRA|SHRA
                               |[\-\+]SHGR|SHGR|[\-\+]TSGR|TSGR|[\-\+]FZRA|FZRA|[\-\+]FZDZ|FZDZ
                               |[\-\+]TSRA|TSRA|[\-\+]SHGR|SHGR|[\-\+]TSGS|TSGS|[\-\+]TSSN|TSSN
                               ''', self.metar_data)
        if weather:
            weather_type_modified = weather[0].replace('+', r'\+') # Добавляем \ для +
            weather_type_modified = '"{0}"'.format(weather_type_modified) # Добавляем ""

            with open(WEATHER_DATA_FILE, encoding='utf-8') as weather_data:
                for line in weather_data:
                    result = re.match(weather_type_modified, line) # Поиск погоды
                    if result:
                        found_string = line.replace('"', '') # Отрезаем из найденой строки ковычки
                        print("WEATHER: " + found_string.split(",", 1)[1].replace('\n', ''))

                        # Делим строку на список из 2 элементов разделителем служит запятаяи выводим
                        # второе значение списка

    def clouds_type(self):
        '''Метод определения типа облачности'''

        result = re.findall(r'''SKC[0-9]{3}|NSC[0-9]{3}|FEW[0-9]{3}|SCT[0-9]{3}|BKN[0-9]{3}
                                |OVC[0-9]{3}|VV[0-9]{3}|CAVOK''', self.metar_data)

        for type_cloud in result:
            if type_cloud == "SKC":
                print("CLOUDS: Sky is clear.")

            if type_cloud == "NSC":
                print("CLOUDS: No significant cloud clouds.")

            if type_cloud[:-3] == "FEW":
                cch_feet = (int(type_cloud[-3:]) * 100)
                cch_m = round(cch_feet * 0.3048, 2)
                print("CLOUDS: Few clouds at " + str(cch_feet) + " feet (" + str(cch_m) + " meter)")

            if type_cloud[:-3] == "SCT":
                cch_feet = (int(type_cloud[-3:]) * 100)
                cch_m = round(cch_feet * 0.3048, 2)
                print("CLOUDS: Scattered clouds at " + str(cch_feet)
                      + " feet (" + str(cch_m) + " meter)")

            if type_cloud[:-3] == "BKN":
                cch_feet = (int(type_cloud[-3:]) * 100)
                cch_m = round(cch_feet * 0.3048, 2)
                print("CLOUDS: Broken clouds at "
                      + str(cch_feet) + " feet (" + str(cch_m) + " meter)")
            if type_cloud[:-3] == "OVC":
                cch_feet = (int(type_cloud[-3:]) * 100)
                cch_m = round(cch_feet * 0.3048, 2)
                print("CLOUDS: Overcast clouds at " + str(cch_feet)
                      + " feet (" + str(cch_m) + " meter)")

            if type_cloud[:-3] == "VV":
                print("CLOUDS: Clouds cannot be seen because of fog or heavy precipitation.")

            if type_cloud == "CAVOK":
                print("CLOUDS: Ceiling And Visibility OK.")

    def temperature(self):
        '''Метод поиска температуры окр. среды и точки россы'''
        # Поиск значения температуры в строке
        celsius = re.search(r'[0-9]{2}[/][0-9]{2}|M[0-9]{2}[/]M[0-9]{2}|[0-9]{2}[/]M[0-9]{2}',
                            self.metar_data)
        # Для отрицательной температуры в цельсиях заменяем M на -
        celsius = re.split(r'\/', celsius[0].replace('M', '-'))

        # Convert °C to °F (Temperature)
        fahrenheit = (int(celsius[0]) * 9/5) + 32
        tffahr = round(fahrenheit, 2)

        # Convert °C to °F (Dewpoint)
        fahrenheit = (int(celsius[1]) * 9/5) + 32
        dfahr = round(fahrenheit, 2)
        print("Temperature " + celsius[0] + "°C (" + str(tffahr) + "°F) "
              + "Dewpoint " + celsius[1] + "°C (" + str(dfahr) + "°F)")


    def pressure_value(self):
        '''Метод поиска давления'''
        result = re.search(r'[Q][0-9]{4}', self.metar_data)
        if result:
            print("PRESSURE: QNH " + result[0][1:] + " hPa")

        result = re.search(r'[A][0-9]{4}', self.metar_data)
        if result:
            print("PRESSURE: Sea level pressure is " + result[0][1:-2]
                  + "." + result[0][3:] + " inHg")

    def trend_valuse(self):
        '''Прогнозирование изменений'''
        result = re.search(r'NOSIG|BECMG|TEMPO', self.metar_data)
        if result:
            if result[0] == "NOSIG":
                print("TRENDS: No significant change is expected to the " +
                      "reported conditions within the next 2 hours.")
            if result[0] == "BECMG":
                print("TRENDS: Sustained significant changes in weather conditions are expected.")
            if result[0] == "TEMPO":
                print("TRENDS: Temporary significant changes in weather conditions are expected.")

    def remarks(self):
        '''Примечания'''
        result = re.search(r'AO2', self.metar_data)
        if result:
            print("This station is automated with a precipitation discriminator (rain/snow) sensor")

        result = re.search(r'PWINO', self.metar_data)
        if result:
            print("Precipitation identifier sensor not available")

        result = re.search(r'\$', self.metar_data)
        if result:
            print("System needs maintance")


if __name__ == "__main__":
    _get_metar_data() # Вызыв функции извлечения строки метеосводки
    print(_get_metar_data()) # Выводим строку сводки на экран

    FORECAST = MetarParser(_get_metar_data()) # Передаем строку с данными в class MetarParser
    FORECAST.airport_id() # Вывод индекса аэропорта
    FORECAST.forecast_time() # Вывод времени формирования формирования отчета
    FORECAST.report_type() # Вывод типа формирования
    FORECAST.wind_type() # Вывод скорости и направления ветра
    FORECAST.visibility_value() # Вывод условий видимости
    FORECAST.weather_type() # Вывод типа погоды
    FORECAST.clouds_type() # Вывод типа облачноть
    FORECAST.temperature() # Вывод температуры
    FORECAST.pressure_value() # Давление
    FORECAST.trend_valuse() # Прогнозы
    FORECAST.remarks() # Примечания
