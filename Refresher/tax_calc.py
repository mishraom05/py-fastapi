def tax_calc(amnt,spent):
    tax = 0.03
    return (amnt - (spent + (spent * tax)))

if __name__ == "__main__":
    tot = int(input("Enter total amount you have :"))
    spnt = int(input("Enter the amount spent :"))
    rem_amnt = tax_calc(tot,spnt)
    print(f"Remaining Amount is {rem_amnt}")
