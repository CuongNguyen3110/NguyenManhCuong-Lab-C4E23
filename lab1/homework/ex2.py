from pymongo import MongoClient
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)
db = client.get_database()
posts = db["posts"]
new_post = {
    "Title": "C4E",
    "Author": "Nguyen Manh Cuong",
    "Content": "Hi vong minh se yeu thich code va hoan thanh tot khoa hoc",
}
posts.insert_one(new_post)
client.close()