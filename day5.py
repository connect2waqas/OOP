# Vehical Rental system
class Vehicle:
    def __init__(self, vehicale_id, brand, model):
        self.vehicale_id = vehicale_id
        self.brand = brand
        self.model= model
    def calculate_rental_cost(self,days):
        return 0
    def vehicle_info(self):
        return f"{self.brand} {self.model} (ID: {self.vehicale_id})"
class Car(Vehicle):
    def __init__(self, vehicale_id, brand, model,daily_rate):
        super().__init__(vehicale_id, brand, model)
        self.daily_rate = daily_rate
    def calculate_rental_cost(self, days):
        return self.daily_rate * days
class Motorcycle(Vehicle):
    def __init__(self, vehicale_id, brand, model, hourly_rate):
        super().__init__(vehicale_id, brand, model)
        self.hourly_rate = hourly_rate
    def calculate_rental_cost(self, days):
        hours = days * 8
        return self.hourly_rate * hours
class Truck(Vehicle):
    def __init__(self, vehicale_id, brand, model, daily_rate, price_per_km):
        super().__init__(vehicale_id, brand, model)
        self.daily_rate = daily_rate
        self.price_per_km = price_per_km
    def calculate_rental_cost(self, days,km=0):
        return (self.daily_rate * days) + (self.price_per_km * km)

fleet = [
    Car("CAR001", "Toyota", "Camry", 50),
    Motorcycle("BIKE001", "Honda", "CBR", 10),
    Truck("TRUCK001", "Ford", "F-150", 100, 2)
]

rental_days = 3

for vehicale in fleet:
    print(f"{vehicale.vehicle_info()}")
    print(f"  Type: {vehicale.__class__.__name__}")

    if isinstance(vehicale,Truck):
        cost = vehicale.calculate_rental_cost(rental_days,km=150)
        print(f"  Cost for {rental_days} days + 150 km: ${cost:.2f}")
    print()

