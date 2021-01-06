class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added to " + self.name + " " + self.lastName + "'s cart")


customer1 = Customer()
customer1.name = "Teeraya"
customer1.lastName = "Y"
customer1.addCart()

customer2 = Customer()
customer2.name = "Thanesuan"
customer2.lastName = "N"
customer2.addCart()

customer3 = Customer()
customer3.name = "Thananya"
customer3.lastName = "P"
customer3.addCart()

customer4 = Customer()
customer4.name = "Pannipa"
customer4.lastName = "K"
customer4.addCart()
