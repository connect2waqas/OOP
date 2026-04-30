class Hammer:
    def use(self):
        print("Using Hammer...")

class Screwdriver:
    def use(self):
        print("Using Screwdriver...")
    
class Drill:
    def use(self):
        print("Using Drill...")

machines = [Hammer(), Screwdriver(), Drill()]

def using_machine(machine):
    machine.use()

for machine in machines:
    using_machine(machine)