#/usr/bin/bash
if [$1 = ""] ; then
    echo "Скрипт должен быть запущен с параметром"
    exit
fi

ICAO=$1

curl -k https://tgftp.nws.noaa.gov/data/observations/metar/stations/$ICAO.TXT --output $ICAO.TXT
