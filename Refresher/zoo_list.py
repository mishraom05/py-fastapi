def animal_list(zoo):
    print(zoo)
    # Delete the animal at the 3rd index.
    print(zoo.pop(3))
    # Append a new animal at the end of the list
    zoo.append('croc')
    print(zoo)
    # Delete the animal at the beginning of the list.
    print(zoo.pop(0))
    # Print all the animals
    print(zoo)
    # Print only the first 3 animals
    print(zoo[0:3])

if __name__ == '__main__':
    # Create a list of 5 animals called zoo
    zoo = ['tiger', 'lion', 'wolf', 'bear', 'ostrich']
    animal_list(zoo)



