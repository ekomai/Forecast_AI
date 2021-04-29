# csv to csv_NEW

import csv
import pandas as pd

df = pd.read_csv("csv_in_progress/forecast_data_Shikoku.csv")
df.head()
# tp.plot()

df.to_csv("csv_in_progress/forecast_data_Shikoku_NEW.csv", index=False, columns=['Name', 'Cloud Cover', 'Solar Radiation', 'Relative Humidity', 'Temperature', 'Wind Speed', 'Solar Energy'])

sl = pd.read_csv("csv_in_progress/forecast_data_Shikoku_NEW.csv")

sl.head()

# csv to seaborn

import numpy as np
import pandas as pd

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
   # sns.set(font="serif")
   sns.set_theme(context='notebook', style='darkgrid', palette='deep', font='sans-serif', font_scale=1, color_codes=True, rc=None)


   # pd.read_csv("csv/area-2020_04.csv")
   tp = pd.read_csv("csv_in_progress/forecast_data_Shikoku_NEW.csv")
   # tp.head()
   # tp.plot()

   sns.pairplot(data=tp, hue="Name",)

   plt.savefig("static/VC/pair_VC_02.png")
   plt.close()

   templateData = {
     'title' : ' ',
     'filename' : 'pair_VC_02.png'
   }

   return render_template('graph.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8080, debug=True)
