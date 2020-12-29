def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return True
    else:
        return False


def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")


def menuSelect():
    userSelected = int(input(">>"))
    return userSelected


def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result


def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculator(price1 + price2)


while not login():
    login()

showMenu()
menu = menuSelect()

if menu == 1:
    print("=== Vat Calculation Program ===")
    price = int(input("Please enter product price: "))
    print("Price include VAT = ", vatCalculator(price))
elif menu == 2:
    print("=== Price Calculator Program ===")
    print("Total price of products = ", priceCalculator())
else:
    print("You have select unavailable program !!!")