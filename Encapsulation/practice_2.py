class DataWarehouse:
    
    def __init__(self, records):
        self.__records = records
    
    def get_record(self):
        return self.__records
    
    def set_record(self, new_record):
        self.__records = new_record
    

class DataCleaner:

    def filter_outlier(self, warehouse_obj):
        record = warehouse_obj.get_record()
        new_record  = []
        for i in record:
            if i < 100:
                new_record.append(i)
        warehouse_obj.set_record(new_record)

class AIPipeline:
    
    def __init__(self, data_obj, clean_data_obj):
        self.data = data_obj
        self.clean_data = clean_data_obj
    def execute(self):
        print(f"Data before cleaning: {self.data.get_record()}")
        self.clean_data.filter_outlier(self.data)
        print(f"Data after cleaning:  {self.data.get_record()}")
    
data = [15, 120, 45, 300, 8, 101]
data_ware = DataWarehouse(data)
cleaner = DataCleaner()
pipeline = AIPipeline(data_ware,cleaner)
pipeline.execute()