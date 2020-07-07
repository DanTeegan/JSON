# import json
# create a class Exchange_rates
# With required attributes
# fetch the data from exchange_rates.json
# display the data
# display the type of data
# display exchange rates with specific currencies
# Method to return the exchange rates
# Give the full path of the location if not saved within the same folder

import json

# Here we are creating the class Exchange_rates
# class Exchange_rates:
#     # Here we are initialising
#     def __init__(self):
#         # Here we are opening the .json file as "r" meaning read. We alias using exchange_files
#         with open("exchange_rates.json", "r") as exchange_files:
#              # Here we are creating a variable of data to load the json file
#             data = json.load((exchange_files))
#             for e in data:
#                 if e == "rates":
#                     print(data["rates"])
#                     currency = input("What currency would you like?: ")
#                     print(data["rates"][currency])
#
# e = Exchange_rates
# e.__init__(Exchange_rates)
# e.__init__()

# import json
import json

# create a class exchange_rates
class Exchange_rates:

    # with required attributes(none)
    def __init__(self):
        pass

    # fetch data from exchange_rates.json
    def fetch_data(self):
        with open("exchange_rates.json", "r") as jsonfile:
            dataset = json.load(jsonfile)
            # display the data
            print(dataset)
            # display the type of data
            print(type(dataset))

    # method to return the exchange rates
    def fetch_exchange_rates(self):
        with open("exchange_rates.json", "r") as jsonfile:
            dataset = json.load(jsonfile)
            # For loop to get all exchange rates
            for key in dataset:
                if key == "rates":
                    print(dataset["rates"])
            currency = input("What currency would you like the exchange rate of, please see list.\n")
            # display exchange rates with specific currencies
            print(dataset["rates"][currency])


obj1 = Exchange_rates()
obj1.fetch_data()
obj1.fetch_exchange_rates()



