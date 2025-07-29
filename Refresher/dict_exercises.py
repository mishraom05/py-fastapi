# Dictionary
my_vehicle = {
        "model": "Ford",
        "make": "Explorer",
        "year": 2018,
        "mileage": 40000
    }
# Create a for loop to print all keys and values
for x,y in my_vehicle.items():
    print(f"Key is: {x}, Value is: {y}")

# Create a new variable vehicle2, which is a copy of my_vehicle
vehicle2 = my_vehicle.copy()

# Add a new key 'number_of_tires' to the vehicle2 variable that is equal to 4
vehicle2["number_of_tires"] = 4
print(vehicle2) 

# Delete the mileage key and value from vehicle2
vehicle2.pop("mileage")
print(f"After popping mileage: {vehicle2}")

# Print just the keys from vehicle2
for x in vehicle2:
    print(f"Key : {x}")

# Original dictionary
print(f"My Dictionary : {my_vehicle}")