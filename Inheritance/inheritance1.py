class ModelConfig:

    def __init__(self, learning_rate, epoches):
        self.__learning_rate = learning_rate
        self.__epoches = epoches
    @property
    def learning_rate(self):
        return self.__learning_rate
    
class BaseModel:
    def __init__(self, model_name, config_obj):
        self.__model_name = model_name
        self.config_obj = config_obj
    
    def describe(self):
        print(f"Model_name : {self.__model_name} learning rate {self.config_obj.learning_rate}")
    
    


    @property
    def model_name(self):
        return self.__model_name

class CCNetwork(BaseModel):
    def __init__(self, model_name, config_obj, num_layers):
        super().__init__(model_name, config_obj)
        self.num_layers = num_layers
    
    def train(self):
        print(f"Training {self.model_name} with {self.num_layers} layers using {self.config_obj.learning_rate}...")
    

model = ModelConfig(0.001, 50)
cnn = CCNetwork("VisionNet", model, 10)


cnn.train()
cnn.describe()