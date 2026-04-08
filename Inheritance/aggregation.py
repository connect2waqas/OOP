"""Aggregation"""
class Customer:
    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address  = address
    
    def print_address(self):
        return f"Name: {self.name} | city: {self.address.city} | postal_code: {self.address.get_postal_code} | street: {self.address.get_street}"
    
    def edit_profile(self,new_name, new_city, new_postal, new_street):
        self.name = new_name
        self.address.update_location(new_city,new_postal,new_street)

class Address:
    def __init__(self, city, postal_code, street):
        self.__city = city
        self.__postal_code = postal_code
        self.__street = street
    def get_address(self):
        print(f"Address is: {self.__city} {self.__postal_code} {self.__street}")
    @property
    def city(self):
        return self.__city
    @property
    def get_postal_code(self):
        return self.__postal_code
    @property
    def get_street(self):
       return self.__street
    def update_location(self, new_city, new_postal, new_street):
        self.__city = new_city
        self.__postal_code = new_postal
        self.__street = new_street


add_1 = Address("Peshaware",18300,"landay")
cust = Customer("waqas","male",add_1)
print(f"Before: {cust.print_address()}")
cust.edit_profile("Ilyas","Islamabad", 44000, "Blue Area")
print(f"After: {cust.print_address()}")