menuList = []
priceList = []


def showBill():
    total = 0
    print("---- My Food ----")
    for i in range(len(menuList)):
        print(menuList[i], priceList[i])
        total += priceList[i]
    print("Total: %d THB" % total)


while True:
    menuName = input("Menu: ")
    if menuName.casefold() == "exit":
        break
    else:
        menuPrice = int(input("Price: "))
        menuList.append(menuName)
        priceList.append(menuPrice)

showBill()

