menuList  = {"ข้าวหมกไก่": 45, "ข้าวมันไก่": 40, "ข้าวมันไก่ผสม": 50, "ข้าวมันไก่พิเศษ": 45}
orderList = []


def showBill():
    total = 0
    print("---- My Food ----")
    for i in range(len(orderList)):
        print(orderList[i][0], orderList[i][1])
        total += orderList[i][1]
    print("Total: %d" % total)


while True:
    menuName = input("Menu: ")
    if menuName.casefold() == "exit":
        break
    elif menuName in menuList:
        orderList.append([menuName,menuList[menuName]])
    else:
        print("Menu is not found!!")

showBill()

