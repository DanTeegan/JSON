
# Here we are importing the Json file
import json

# Encoding from the dictionary and writing Json file
car_data = {"name": "Tesla", "engine": "electric"} # Dictionary

# This will print the dictionary
print(car_data)

# This will print the data type of the dictionary
print(type(car_data))

car_data_json_string = json.dumps(car_data) # Changing python dictionary to a Json string

# The data type is now changed from a dictionary to a string
print(type(car_data_json_string))

# Lets create a Json file with writing permission "w" stands for write
with open("new_json_file.json", "w") as jsonfile:
# Enter the name of the file, Permission type

# Encoding and creating into a Json file

    json.dump(car_data, jsonfile) # Json.dump takes 2 args
    # Car_data is the first one. It is the dictionary Second is the file object. In this case it is jsonfile

with open("new_json_file.json") as jsonfile: # Decoding
    # Reading from the file we just created

    car = json.load(jsonfile) # Storing data from file to car variable
    print(type(car)) # Checking the type of data again
    print(car["name"]) # To get the values stored in the key called name
    print(car["engine"]) # To get the value of second key pair value

# We have DECODED our file new_json.json that we created earlier
# We have used dumps(), dump() and load() methods