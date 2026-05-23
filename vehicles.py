class Vehicle:
    def __init__(self, make, model, year, weight):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight

    def start_engine(self):
        print("Engine started.")


class Car(Vehicle):
    def __init__(self, make, model, year, weight, num_doors, num_passengers):
        super().__init__(make, model, year, weight)
        self.num_doors = num_doors
        self.num_passengers = num_passengers

    def start_engine(self):
        print("The car's engine is starting...")

    def drive(self):
        print("Driving the car.")


class Truck(Vehicle):
    def __init__(self, make, model, year, weight, cargo_capacity, towing_capacity):
        super().__init__(make, model, year, weight)
        self.cargo_capacity = cargo_capacity
        self.towing_capacity = towing_capacity

    def start_engine(self):
        print("The truck's engine is starting...")

    def haul(self):
        print("Hauling cargo with the truck.")


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, weight, num_wheels, has_sidecar):
        super().__init__(make, model, year, weight)
        self.num_wheels = num_wheels
        self.has_sidecar = has_sidecar

    def start_engine(self):
        print("The motorcycle's engine is starting...")

    def ride(self):
        print("Riding the motorcycle.")


car = Car("BMW", "5 Series", 2023, 1735, 4, 5)
truck = Truck("Chevrolet", "Silverado", 2022, 2300, 900, 4500)
motorcycle = Motorcycle("Yamaha", "MT-07", 2022, 184, 2, False)

car.start_engine()
car.drive()

truck.start_engine()
truck.haul()

motorcycle.start_engine()
motorcycle.ride()

all_vehicles = [car, truck, motorcycle]
print("Polymorphism:")
for item in all_vehicles:
    item.start_engine()
