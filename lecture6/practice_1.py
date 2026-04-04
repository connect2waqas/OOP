class Engine:
    def __init__(self):
        self.is_running = False
    
    def start(self):
        self.is_running = True
        print("Car varms..")
    def stop(self):
        self.is_running = False
        print("Car silience..")
    def get_status(self):
        "RUNNING" if self.start() else "STOPPED"


class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.engine = Engine()
    
    def start_car(self):
        print(f"{self.make} {self.model} ignition..")
        self.engine.start()
    def stop_car(self):
        print(f"{self.make} {self.model} shutting down..")
        self.engine.stop()
    def check_status(self):
        return f"Engine status: {self.engine.get_status()}"

my_car = Car("Toyota", "Camry")
print(my_car.check_status())  
my_car.start_car()           
print(my_car.check_status())  
my_car.stop_car()            


