from pymongo import MongoClient
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)
db = client.get_database
posts = db["post"]
new_post = {
    "Title": 
    "Author": "Nguyen Manh Cuong"
    "Content":
}
posts.insert_one(new_post)
client.close()