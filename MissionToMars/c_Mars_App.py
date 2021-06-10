## Dependencies
import pymongo
from b_Mars_Scrape import scrape

## Initialize PyMongo (MongoDB)
# conn = 'mongodb://localhost:27017'
# client = pymongo.MongoClient(conn)

## Define database and collection
# db = client.commerce_db
# collection = db.items


print(scrape())