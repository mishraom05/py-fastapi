# Create a function that takes in 3 parameters(firstname, lastname, age) and
# returns a dictionary based on those values

def dict_func(firstname, lastname, age):
    my_dict = {
    'firstname': firstname,
    'lastname': lastname,
    'age': age
    }
    return my_dict

if __name__ == '__main__':
    firstname=input("Enter first name:")
    lastname=input("Enter last name:")
    age=int(input("Enter age:"))

    dict=dict_func(firstname=firstname, lastname=lastname, age=age)
    for x,y in dict.items():
        print(f"Key: {x} Value: {y}")
    print(dict)