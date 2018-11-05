from pymongo import MongoClient
from matplotlib import pyplot

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)
db = client.get_database()
customers = db["customers"]
customers_list = customers.find()
ref_dict = {}

for p in customers_list:
    if p["ref"] not in ref_dict:
        ref_dict[p["ref"]] = 1
    else:
        ref_dict[p["ref"]] += 1
print(ref_dict)
ref_list = ref_dict.keys()
ref_count = ref_dict.values()
pyplot.pie(ref_count, labels=ref_list, autopct="%.1f%%", shadow=True, explode=[0, 0.1, 0])
pyplot.axis("equal")
pyplot.title("References")
pyplot.show()

client.close()