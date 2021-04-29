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
   sns.set_theme(context='notebook', style='darkgrid', palette='deep', font='sans-serif', font_scale=1, color_codes=True, rc=None)

   tp = pd.read_csv("csv/forecast.csv")
   # tp.head()
   # tp.plot()
   sns.pairplot(data=tp, hue="TIME",)

   plt.savefig("static/OWM/onecall_01.png")
   plt.close()

   templateData = {
     'title' : ' ',
     'filename' : 'onecall_01.png'
   }

   return render_template('graph.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8080, debug=True)
