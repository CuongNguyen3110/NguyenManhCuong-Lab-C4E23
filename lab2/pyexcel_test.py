import pyexcel
from collections import OrderedDict


#2 Prepare data
dictionaries = [
    OrderedDict({
        "Name": "Cuong",
        "Age": 23,
        "Job": "abc"
    }),
    OrderedDict({
        "Name": "Luong",
        "Age": 25,
        "Job": "abc"
    })
]

# List comprehension

#3 Save file
pyexcel.save_as(records=dictionaries, dest_file_name="Name.xlsx")