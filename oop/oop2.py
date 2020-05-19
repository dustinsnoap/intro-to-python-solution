# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheel defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle:
    def __init__(self, num_wheels=4):
        self.num_wheels = num_wheels

    def drive(self):
        return("vrooom")


# Subclass Motorcycle from Vehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

class Motorcycle(GroundVehicle):
    def __init__(self):
        super().__init__(2)

    def drive(self):
        return("BRAAAP!!")

vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vechicles list and call drive() on each.
for v in vehicles:
    print(v.drive())

