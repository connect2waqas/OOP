class SmartModel:
    
    def __init__(self, bias_score):
        self.__bias_score = bias_score
    
    def get_bias(self):
        return self.__bias_score

class DeploymentLog:
    
    def __init__(self):
        self.__status = "pending"
    
    def update_status(self, new_status):
        self.__status = new_status
    
    def view_log(self):
        print(f"current Deployment status: {self.__status}")
    
class ValidationEngine:
    def validate(self, model_obj, log_obj):
        if model_obj.get_bias() > 0.5:
            log_obj.update_status("Rejected: High bias")
        else:
            log_obj.update_status("Approved: Safe for production")

model = SmartModel(0.5)
log = DeploymentLog()
engine = ValidationEngine()
engine.validate(model,log)
log.view_log()