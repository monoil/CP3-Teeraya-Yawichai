username = "admin"
password = "1234"

inUsername = input("Please enter username: ")
inPassword = input("Please enter password: ")

while not(inUsername == username and inPassword == password):
    print("Username or password is incorrect!!")
    inUsername = input("Please enter username: ")
    inPassword = input("Please enter password: ")
print("Login Successfully")
