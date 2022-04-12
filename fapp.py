from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrapy


app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

@app.route("/")
def home():
    
    mars = mongo.db.mars.find_one()

    return render_template("repress.html", mars=mars)

@app.route("/scrape")
def scrape():

    # Run the scrape function
    mars = mongo.db.mars
    mars_data = scrapy.scrape_all()
    mars.update({}, mars_data, upsert=True)




if __name__ == "__main__":
    app.run(debug=True)