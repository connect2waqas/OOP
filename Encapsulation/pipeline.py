class DataPackage:
    def __init__(self, size):
        self.__size = size

    def get_size(self):
        return self.__size

class AIModel:
    
    def __init__(self):
        self.__weight_initialized = False
    
    def initialize_weights(self):
        print("System: Optimizing weight tensors..")
        self.__weight_initialized = True
    def is_ready(self):
        return self.__weight_initialized
    
class TrainingPipeline:
    def __init__(self, data, model):
        self.data = data
        self.model = model
    
    def run_train(self):
        if self.model.is_ready():
            count = self.data.get_size()
            print(f"Success: Training started with {count} samples.")
        else:
            print("Waqas: Model not ready. Initiating auto-setup...")
            self.model.initialize_weights()
            self.run_train()
data = DataPackage(5000)
model = AIModel()
pipeline = TrainingPipeline(data,model)
pipeline.run_train()