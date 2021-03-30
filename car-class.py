class Car(object):
    def __init__(self,plate,model,color,speed):
        self.plate = plate
        self.model = model
        self.color = color
        self.speed = speed

    def getPlate(self):
        return self.plate
    
    def changeColor(self,color):
        self.color = color

    def getColor(self):
        return self.color

    def getSpeed(self):
        return self.speed

    
car1 = Car("xyz123","Maruti800","red",40)
car2 = Car("abc123","TeslaModelX","blue",150)

print(car1.getPlate())
car1.changeColor("blue")
print(car1.getColor())

print(car2.getPlate())
car2.changeColor("red")
print(car2.getColor())