#JSON Javascript Object Notation

# Person = {
#     name : "markson",
#     age : age,
#     speak : function(){
#         console.log("my name is "+ name)
#     }
# }

# TYPES of data inside a JSON file
# JSON is a key value system or a large dictionary as we knoe it in python

# - "key" : "value"
# - a string
# - a number
# - a key or an object (Json object)
# - an array
# - a boolean
# - null
# {
# "Trainer1 = {
#     "name" : "markson",
#     "age" : 25,
#     "job" : "mechanic"
#     },
# "Trainer2"
# "name" : "markson",
#     "age" : 25,
#     "job" : "mechanic"
# }
import json
car_data = {"name" : "tesla", "engine" : "electric"}

# We need two methods ins JSON:
# 1. json.dumps()
# 2. json.dump()

car_data_jason_string = json.dumps(car_data)
print(car_data_jason_string)
print(car_data)

json_file = open("json_out_alternative.json","w")

car_data_jason_string = json.dump(car_data,json_file)

# This is an alternative to the statement above

with open("json_out_alternative.json", "w")as json_file2:
    json.dump(car_data, json_file2)

with open('json_out_alternative.json') as open_json_file:
    electric_car = json.load(open_json_file)
    print(type(electric_car))
    print(electric_car['name'])
    print(electric_car['engine'])




