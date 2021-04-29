# api to json

from pprint import pprint
import urllib
import urllib.request
import json
import sqlite3
import sqlite3 as sql
import os
import csv
from sqlite3 import Error

try:

    conn = sqlite3.connect('sqlite/forecast.db')
    cur = conn.cursor()

    cur.execute('''SELECT * FROM Forecast''')
    rows = cur.fetchall()

    for row in rows:
      print(row)

    # conn.commit()

    # Export data into CSV file
    # print("Exporting data into CSV............")

    cursor = conn.cursor()
    cursor.execute("select * from Forecast")

    with open("csv/forecast.csv", "w") as csv_file:
      csv_writer = csv.writer(csv_file, delimiter=",")
      csv_writer.writerow([i[0] for i in cursor.description])
      csv_writer.writerows(cursor)

    dirpath = os.getcwd() + "csv/forecast.csv"
    print("Data exported Successfully into {}".format(dirpath))

except Error as e:
    print(e)

# Close database connection
finally:
    conn.close()
