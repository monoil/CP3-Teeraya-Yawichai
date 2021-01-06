class Vehicle:
    licenseCode = ""
    serialCode = ""
    face = ""
    def turnOnAirConditioner(self):
        print("Turn On: Air")


class Car(Vehicle):
    pass

class PickUp(Vehicle):
    pass

class Van(Vehicle):
    pass


print("Car1")
car1 = Car()
car1.turnOnAirConditioner()

print("Pickup1")
pickup1 = PickUp()
pickup1.turnOnAirConditioner()

print("Van1")
van1 = Van()
van1.turnOnAirConditioner()

