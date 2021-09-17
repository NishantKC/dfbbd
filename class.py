class Cars:
    def __init__(self,model,color,company,speed):
        self.model=model
        self.color=color
        self.company=company
        self.speed=speed
    def start(self): 
        print("car has started")
    def accelerate(self,value):
        print("acceration is ",value)

car1=Cars("F1","red","Ferrari",300)
print(car1.company)  
car1.start() 
car1.accelerate(500)