import requests
from cs50 import SQL
from flask import Flask, redirect, render_template, request

db = SQL("sqlite:///cities.db")

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/", methods=["GET", "POST"])
def index():
    weather = {}
    l = []
    if request.method == "POST":
        city_name = request.form.get("city")
        url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=449423f2a0e7b1d347686f203416e8f6"
        w = requests.get(url.format(city_name)).json() # Requesting weather data for the city
        d = request.form.get("delete")
        if d:
            db.execute("DELETE FROM names WHERE city=?", d) # Deleting city from the database
            return redirect("/")
        if not city_name:
            return render_template("apology.html", msg="Please enter a city!") # Returning apology if the input field is empty
        else:
            city_name = city_name.upper()
            duplicate = db.execute("SELECT * FROM names WHERE city=?", city_name)
            if not duplicate:
                if w["cod"] == 200:
                    db.execute("INSERT INTO names(city) VALUES(?)", city_name) # Inserting the city into the database
                    return redirect("/")
                else:
                    return render_template("apology.html", msg="Invalid city!") # Returning apology if the city does not exist
            else:
                return render_template("apology.html", msg="City already added!") # Returning apology if the city is already added
    all_cities = db.execute("SELECT * FROM names")
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=449423f2a0e7b1d347686f203416e8f6"
    for cities in all_cities: # Looping over each city in the database and adding the information to l
        w = requests.get(url.format(cities["city"])).json()
        weather = {
            "main" : w["weather"][0]["main"],
            "temp" : w["main"]["temp"],
            "icon" : w["weather"][0]["icon"],
            "city" : cities["city"]
            }
        l.append(weather)
    return render_template("weather.html",l=l)



