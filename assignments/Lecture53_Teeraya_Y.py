# VAT Calculation Program
# Function definition
def vat_calculation(price):
    return price*107/100


# main function
print("=== VAT Calculation Program === ")
price = int(input("Enter price: "))
print("Price (VAT included):", vat_calculation(price))