# User management section
username = "teeraya"
password = "12345678"

# Login section
print("== Chino Coffee Bean ===")
print("Please Login")
inUsername = input("Username: ")
inPassword = input("Password: ")

# Login successfully
if username == inUsername and password == inPassword:
    print("==================================================")
    print("          Welcome to Chino Coffee Bean            ")
    print("==================================================")
    print(" Product No.  Description                  Price  ")
    print(" 1            Chiang Dao Special           100.-  ")
    print(" 2            Chiang Dao Medium Dark       110.-  ")
    print(" 3            Doi Chang Organic Medium     190.-  ")
    print(" 4            Doi Chang Special            250.-  ")
    print("To order an item, please enter product number     ")
    print("==================================================")

    selectedProduct = int(input("Product number: "))
    if selectedProduct == 1:
        print("Chiang Dao Special")
        Qty   = int(input("How many items do you want: "))
        total = Qty * 100
        print("Total price: ", total, "Baht")
    elif selectedProduct == 2:
        print("Chiang Dao Medium Dark")
        Qty   = int(input("How many items do you want: "))
        total = Qty * 110
        print("Total price: ", total, "Baht")
    elif selectedProduct == 3:
        print("Doi Chang Organic Medium")
        Qty   = int(input("How many items do you want: "))
        total = Qty * 190
        print("Total price: ", total, "Baht")
    elif selectedProduct == 4:
        print("Doi Chang Special")
        Qty   = int(input("How many items do you want: "))
        total = Qty * 250
        print("Total price: ", total, "Baht")
    else:
        print("Sorry. We don't have that product number.")
# Login fail
elif username == inUsername:
    print("Wrong password !!!")
else:
    print("User is not found !!!")
