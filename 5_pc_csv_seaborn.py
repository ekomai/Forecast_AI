# url csv to csv_NEW

import numpy as np
import pandas as pd
import csv

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


    url="https://www.tepco.co.jp/forecast/html/images/area-2020.csv"
    df = pd.read_csv(url, skiprows=[0, 1], encoding="shift-jis")

    df.columns = ["DATE", "TIME", "demand", "nuclear", "fossil", "hydro", "geothermal", "biomass", "solar", "solar_rdx", "wind", "wind_rdx", "pump", "grid", "total"]

    df.to_csv("csv_in_progress/juyo-2020_NEW.csv", index=False, columns=["TIME", "demand", "fossil", "hydro", "solar", "wind"])

    sl = pd.read_csv("csv_in_progress/juyo-2020_NEW.csv")

    sns.pairplot(data=sl, hue="TIME")

    plt.savefig("static/PC/pair_PC.png")
    plt.close()

    templateData = {
     'title' : ' ',
     'filename' : 'pair_PC.png'
     }

    return render_template('graph.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8080, debug=True)
