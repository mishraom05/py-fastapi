# - Create a variable grade holding an integer between 0 - 100
# - Code if, elif, else statements to print the letter grade of the number grade variable
# Grades:
# A = 90 - 100
# B = 80 - 89
# C = 70-79
# D = 60 - 69
# F = 0 - 59

def calc_grade(grade):
    if grade >= 90 and grade <= 100:
        return 'A'
    elif grade >= 80 and grade <= 89:
        return 'B'    
    elif grade >= 70 and grade <= 79:
        return 'C'
    elif grade >= 60 and grade <= 69:
        return 'D'
    else:
        if grade > 100:
            return 'Total score cannot be greater than 100!'
        else:
            return 'F'

if __name__ == '__main__':
    print("Welcome to Grade Evaluator! Starting ......")
    cont='Y'
    while cont not in ['N','n']:
        calc=calc_grade(int(input("Enter score of user:")))
        print(f"Grade is {calc}")
        cont = input("Do you want to continue?(Select N/n to cancel.)=>")
    print("Thank you for using Grade Evaluator!")