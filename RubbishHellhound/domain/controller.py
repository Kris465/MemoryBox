class Controller:
    
    def __init__(self, task):
        self.task = task
        
    def run(self):
        print(self.task)