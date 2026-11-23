class product:
    def setdata(self):
        self.code=121
        self.name="printer"
        self.qty=4
        self.price=22222
    def display(self):
        print("code=",self.code)
        print("name=",self.name)
        print("qty=",self.qty)
        print("price",self.price)
        self.total=self.qty*self.price
        print("total price=",self.total)

obj=product()
obj.setdata()
obj.display()