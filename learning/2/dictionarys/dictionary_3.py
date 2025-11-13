print()
import json
# Dictionarys is almost the same as JSON (JavaScript Object Notation)
# JSON is used to store data 

# ---------------------

# open() = a function which can open up a file/data
# example: file = open("folder/filename")


file_name: str = "learning/2/dictionarys/example.json" 

# with() = a statement which opens a resource and guarantee that the resource will be closed when the with block completes, regardless of how the block completes.
# Encoding represents how to convert data or info into a specific format
with open(file_name, encoding="utf-8") as file:
    
    # load() method - takes json-data, puts the data in a dictionary and loads it
    data: dict = json.load(file)
    
for person in data["people"]:
    print(person)