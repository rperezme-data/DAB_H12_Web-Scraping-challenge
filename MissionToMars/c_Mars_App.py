## Dependencies
import pymongo
from flask import Flask, render_template, redirect
from b_Mars_Scrape import scrape_mars

## FLASK SETUP
## Create Flask instance
app = Flask(__name__)

## DATABASE SETUP
## Setup Database connection (MongoDB)
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

## Define Database (MongoDB)
db = client.mars_db


## FLASK ROUTES
## Homepage (Render "index.html" template)
@app.route("/")
def index():

    ## Retrieve data from MongoDB
    mars_data = db.collection.find_one()

    ## Return template and data
    return render_template("index.html", mars_data=mars_data)

## Scrape route (Trigger scrape function)
@app.route("/scrape")
def scrape():

    ## Run scrape function
    mars_data = scrape_mars()

    ## Insert data into Database (MongoDB)
    # db.collection.insert_one(mars_data)
    
    ## Update Database (MongoDB) using update & upsert=True
    db.collection.update({}, mars_data, upsert=True)

    ## Redirect back to Homepage
    return redirect("/")


## RUN FLASK APP
if __name__ == "__main__":
    app.run(debug=True)

