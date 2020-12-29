num = int(input("Please enter number of row: "))
result = ""
for x in range(num):
    for y in range(num-x-1):
        result += " "
    for z in range(x*2+1):
        result += "*"
    print(result)
    result = ""
