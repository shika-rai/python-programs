class rect:
    def set_dim(self,a,b):
        self.a=a
        self.b=b
    def area(self):
        return self.a*self.b
nums=[]
d=int(input("Enter the number of rectangles:"))
for i in range(d):
    r=rect()
    a=int(input("Enter the length:"))
    b=int(input("Enter the breadth:"))
    r.set_dim(a,b)
    nums.append(r)
index=1
for i in nums:
    print("Area of rectangle {} is {}".format(index,i.area()))
    index=index+1