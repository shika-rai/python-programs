class rectangle:
    prop1="Sum of angles is 360 degree"
    prop2="Each angle is 90 degree"
    def input(self):
        l=int(input("Enter the length:"))
        b=int(input("Enter the breadth:"))
        self.l=l
        self.b=b
        
    def display(self): 
        print("AREA=",self.l*self.b)
        print("PERIMETER=",2*(self.l+self.b))
print("The rectangle properties are:")
print(rectangle.prop1)
print(rectangle.prop2)
a1=rectangle()
a1.input()
a1.display()