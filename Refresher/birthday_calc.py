def bday_calc(days):
    return days/7

if __name__ == "__main__":
    day = input("How many days until birthday:")
    times = bday_calc(int(day))
    print(f"Weeks until birthday {times}")
    