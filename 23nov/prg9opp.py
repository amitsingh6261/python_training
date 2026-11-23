class product:
    def setdata(self,a,b,c,d):
        self.code=a
        self.name=b
        self.qty=c
        self.price=d
    def display(self):
        print("code=",self.code)
        print("name=",self.name)
        print("qty=",self.qty)
        print("price",self.price)
        self.total=self.qty*self.price
        print("total price=",self.total)

obj1=product()
obj1.setdata(111,"printer",2,2223232)
obj1.display()
print("==========================")
obj2=product()
obj2.setdata(112,"cd",5,3232)
obj2.display()