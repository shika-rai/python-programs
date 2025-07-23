class emp:
    tax=10
    comp="COGNIZANT"
    profit=100000
    def __init__(self,name,sal,age,per):
        self.name=name
        self.sal=sal
        self.age=age
        self.per=per
    def cal_tax(self):
        return (emp.tax/100)*self.sal
    def cal_share(self):
        return (self.per/100)*emp.profit
    
    def display(self):
        print("1.Name: ",self.name)
        print("2.Company: ",emp.comp)
        print("3.Age: ",self.age)
        print("4.Salary: ",self.sal)
        print("5.Tax: ",self.cal_tax())
        print("6.Profit share: ",self.cal_share())
a1=emp("SACHIN",40000,30,5)
a2=emp("ROHIT",35000,29,5)
a1.display()
print("------------------")
a2.display()