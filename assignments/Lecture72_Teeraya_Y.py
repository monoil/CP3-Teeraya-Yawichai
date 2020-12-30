menuList = []


def showBill():
    total = 0
    print("---- My Food ----")
    for i in range(len(menuList)):
        print(menuList[i][0], menuList[i][1])
        total += menuList[i][1]
    print("Total: %d THB" % total)


while True:
    menuName = input("Menu: ")
    if menuName.casefold() == "exit":
        break
    else:
        menuPrice = int(input("Price: "))
        menuList.append([menuName, menuPrice])

showBill()

