from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<station>/<date>")
def about(station, date):
    file = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(file, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df["    DATE"] == date]["   TG"].squeeze()/10

    return {"Date":date, "Station Id":station, "Temperature":temperature}


if __name__ == "__main__":
    app.run(debug=True)