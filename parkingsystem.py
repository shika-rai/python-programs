class ParkingSystem(object):

    def __init__(self, big, medium, small):
      self.big=big
      self.medium=medium
      self.small=small

    def addCar(self, carType):
        if(carType==1):
            if(self.big>0):
                self.big=self.big-1
                return True
        elif(carType==2):
            if(self.medium>0):
                self.medium=self.medium-1    
                return True
        else:
            if(self.small>0):
                self.small=self.small-1
                return True
        return False                    
        


