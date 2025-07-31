# Given: 
# - Create a while loop that prints all elements of the my_list variable 3 times.
# - When printing the elements, use a for loop to print the elements
# - However, if the element of the for loop is equal to Monday, continue without printing

def day_print(my_list):
    i=0
    while i < len(my_list):
        if my_list[i] == "Monday":
            i+=1
            continue
        else:
            for j in range(3):
                print(my_list[i])
        i+=1

if __name__ == "__main__":
    my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    day_print(my_list)
    