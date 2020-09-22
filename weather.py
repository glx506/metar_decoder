'''Пробую написать модуль определения  погоды'''
import re

metar_data = "..."

def weather_type():
    '''Погодные условия'''
    result = re.search(r'''DZ|[\+\-]DZ|RA|[\+\-]RA|SN|[\-\+]SN|SG|[\+\-]SG|PL|[\+\-]PL
                           |GS|[\+\-]GS|RASN|[\+\-]RASN|SNRA|[\+\-]SNRA|SHSN|[\+\-]SHSN
                           |SHRA|[\+\-]SHRA|SHGR|[\+\-]SHGR|FZRA|[\+\-]FZRA|FZDZ|[\+\-]FZDZ
                           |TSRA|[\+\-]TSRA|TSGR|[\+\-]TSGR|TSGS|[\+\-]TSGS|TSSN|[\+\-]TSSN
                           |DS|[\+\-]DS|SS|[\+\-]SS|FG|FZFG|VCFG|MIFG|PRFG|BCFG|BR|HZ|FU
                           |DRSN|DRSA|DRDU|DU|BLSN|BLDU|SQ|IC|TS|VCTS|VA''', metar_data)
    if result:
        if result[0] == "DZ":
            print("WEATHER: Drizzle.")
        if result[0] == "-DZ":
            print("WEATHER: Light drizzle.")
        if result[0] == "+DZ":
            print("WEATHER: Heavy drizzle.")
        if result[0] == "RA":
            print("WEATHER: Rain.")
        if result[0] == "-RA":
            print("WEATHER: Light rain.")
        if result[0] == "+RA":
            print("WEATHER: Heavy rain.")
        if result[0] == "SN":
            print("WEATHER: Snow.")
        if result[0] == "-SN":
            print("WEATHER: Light snow.")
        if result[0] == "+SN":
            print("WEATHER: Heavy snow.")
        if result[0] == "SG":
            print("WEATHER: Snow grains.")
        if result[0] == "-SG":
            print("WEATHER: Light snow grains.")
        if result[0] == "+SG":
            print("WEATHER: Heavy snow grains.")
        if result[0] == "PL":
            print("WEATHER: Ice pellets.")
        if result[0] == "-PL":
            print("WEATHER: Light Ice pellets.")
        if result[0] == "+PL":
            print("WEATHER: Heavy Ice pellets.")
        if result[0] == "GS":
            print("WEATHER: Samll hail.")
        if result[0] == "-GS":
            print("WEATHER: Light Samll hail.")
        if result[0] == "+GS":
            print("WEATHER: Heavy Samll hail.")
        if result[0] == "GR":
            print("WEATHER: Hail.")
        if result[0] == "-GR":
            print("WEATHER: Light hail.")
        if result[0] == "+GR":
            print("WEATHER: Heavy hail.")
        if result[0] == "RASN":
            print("WEATHER: Rain and snow.")
        if result[0] == "-RASN":
            print("WEATHER: Light rain and snow.")
        if result[0] == "+RASN":
            print("WEATHER: Heavy rain and snow.")
        if result[0] == "SNRA":
            print("WEATHER: Snow and rain.")
        if result[0] == "-SNRA":
            print("WEATHER: Light snow and rain.")
        if result[0] == "+SNRA":
            print("WEATHER: Heavy snow and rain.")
        if result[0] == "SHSN":
            print("WEATHER: Snow showers.")
        if result[0] == "-SHSN":
            print("WEATHER: Light snow showers.")
        if result[0] == "+SHSN":
            print("WEATHER: Heavy snow showers.")
        if result[0] == "SHRA":
            print("WEATHER: Rain showers.")
        if result[0] == "-SHRA":
            print("WEATHER: Light rain showers.")
        if result[0] == "+SHRA":
            print("WEATHER: Heavy rain showers.")
        if result[0] == "SHGR":
            print("WEATHER: Hail showers.")
        if result[0] == "-SHGR":
            print("WEATHER: Light hail showers.")
        if result[0] == "+SHGR":
            print("WEATHER: Heavy hail showers.")
        if result[0] == "FZRA":
            print("WEATHER: Freezing rain.")
        if result[0] == "-FZRA":
            print("WEATHER: Light freezing rain.")
        if result[0] == "+FZRA":
            print("WEATHER: Heavy freezing rain.")
        if result[0] == "FZDZ":
            print("WEATHER: Freezing drizzle.")
        if result[0] == "-FZDZ":
            print("WEATHER: Light freezing drizzle.")
        if result[0] == "+FZDZ":
            print("WEATHER: Heavy freezing drizzle.")
        if result[0] == "TSRA":
            print("WEATHER: Thunderstorm with rain.")
        if result[0] == "-TSRA":
            print("WEATHER: Light thunderstorm with rain.")
        if result[0] == "+TSRA":
            print("WEATHER: Heavy thunderstorm with rain.")
        if result[0] == "TSGR":
            print("WEATHER: Thunderstorm with hail.")
        if result[0] == "-TSGR":
            print("WEATHER: Light thunderstorm with hail.")
        if result[0] == "+TSGR":
            print("WEATHER: Heavy thunderstorm with hail.")
        if result[0] == "TSGS":
            print("WEATHER: Thunderstorm with small hail.")
        if result[0] == "-TSGS":
            print("WEATHER: Light thunderstorm with small hail.")
        if result[0] == "+TSGS":
            print("WEATHER: Heavy thunderstorm with small hail.")
        if result[0] == "TSSN":
            print("WEATHER: Thunderstorm with snow.")
        if result[0] == "-TSSN":
            print("WEATHER: Light thunderstorm with snow.")
        if result[0] == "+TSSN":
            print("WEATHER: Heavy thunderstorm with snow.")
        if result[0] == "DS":
            print("WEATHER: Duststorm.")
        if result[0] == "-DS":
            print("WEATHER: Light duststorm.")
        if result[0] == "+DS":
            print("WEATHER: Heavy duststorm.")
        if result[0] == "SS":
            print("WEATHER: Sandstorm.")
        if result[0] == "-SS":
            print("WEATHER: Light sandstorm.")
        if result[0] == "+SS":
            print("WEATHER: Heavy sandstorm.")
        if result[0] == "FG":
            print("WEATHER: Fog.")
        if result[0] == "FZFG":
            print("WEATHER: Freezing fog.")
        if result[0] == "VCFG":
            print("WEATHER: Fog in vicinity.")
        if result[0] == "MIFG":
            print("WEATHER: Shallow fog.")
        if result[0] == "PRFG":
            print("WEATHER: Aerodrome partially covered by fog.")
        if result[0] == "BCFG":
            print("WEATHER: Fog patches.")
        if result[0] == "BR":
            print("WEATHER: Mist.")
        if result[0] == "HZ":
            print("WEATHER: Haze.")
        if result[0] == "FU":
            print("WEATHER: Smoke.")
        if result[0] == "DRSN":
            print("WEATHER: Low drifting snow.")
        if result[0] == "DRSA":
            print("WEATHER: Low drifting sand.")
        if result[0] == "DRDU":
            print("WEATHER: Low drifting dust.")
        if result[0] == "DU":
            print("WEATHER: Dust.")
        if result[0] == "BLSN":
            print("WEATHER: Blowing snow.")
        if result[0] == "BLDU":
            print("WEATHER: Blowing dust.")
        if result[0] == "SQ":
            print("WEATHER: Squall.")
        if result[0] == "IC":
            print("WEATHER: Ice crystals.")
        if result[0] == "TS":
            print("WEATHER: Thunderstorm.")
        if result[0] == "VCTS":
            print("WEATHER: Thunderstorm in vicinity.")
        if result[0] == "VA":
            print("WEATHER: Volcanic ash.")
