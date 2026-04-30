class Staff:
    def duty(self):
        print("Staff duty...")

class Doctor(Staff):
    def duty(self):
        print("Doctor duty...")
class Nurse(Staff):
    def duty(self):
        print("Nurse duty...")
    
class Receptionist(Staff):
    print("Receptionist duty")

