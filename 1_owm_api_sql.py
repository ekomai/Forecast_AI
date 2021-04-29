# api to json

from pprint import pprint
import urllib
import urllib.request
import json

api_key = "14a7f78f63337b00ab83a87c8869072b"
lat = "35.652832"
lon = "139.839478"
url = "https://api.openweathermap.org/data/2.5/forecast?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)
data = urllib.request.urlopen(url).read().decode()
obj = json.loads(data)

with open('json/forecast.json', 'w') as f:
    json.dump(obj, f)
pprint(obj)

# json to selected data

import json
import pprint

f = open('json/forecast.json', 'r',encoding="utf-8")
j = json.load(f)
k = j['list']
# print(k)

for Anon in k:
    dt_txt = Anon['dt_txt']
    print(dt_txt)

    m = Anon['main']
    humidity = m['humidity']
    print(humidity)

    temp = m['temp']
    print(temp)
    temp_max = m['temp_max']
    print(temp_max)
    temp_min = m['temp_max']
    print(temp_min)

    n = Anon['wind']
    speed = n['speed']
    print(speed)

# selected data to sqlite

import json
import sqlite3
import pprint

conn = sqlite3.connect('sqlite/forecast.db')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Forecast;
CREATE TABLE Forecast (TIME text, humidity integer, temp_max integer, temp_min integer, wind_speed integer);
''')

f = open('json/forecast.json', 'r',encoding="utf-8")
j = json.load(f)

k = j["list"]
for Anon in k:
    dt_txt = Anon['dt_txt']

    m = Anon['main']
    humidity = m['humidity']
    # temp = m['temp']
    temp_max = m['temp_max']
    temp_min = m['temp_max']

    n = Anon['wind']
    wind_speed = n['speed']

    cur.execute('''INSERT OR IGNORE INTO Forecast (TIME, humidity, temp_max, temp_min, wind_speed)
    VALUES ( ?, ?, ?, ?, ? )''', ( dt_txt[11:], humidity, temp_max, temp_min, wind_speed) )

    conn.commit()

conn.close()
