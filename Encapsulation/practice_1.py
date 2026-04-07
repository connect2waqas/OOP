class Dataset:
    
    def __init__(self,source_name,record_count):
        self.__source_name = source_name
        self.__record_count = record_count
    @property
    def getter(self):
        return f"source: {self.__source_name} | record_count: {self.__record_count}"
    @getter.setter
    def update_record_count(self, new_count):
        if new_count < 0:
            print("count cannot be negitive")
        else:
            self.__record_count = new_count
            print("Record is updated..")

medical_data = Dataset("Hospital_A",500)
medical_data.update_record_count = 1000
print(medical_data.getter)