class product:
    def __init__(self,x ,y):  # default constructor
        self.qty=x
        self.price=y
        print("total=",(self.qty*self.price))

obj1=product(3,55555)
obj=product(5,12321)
obj=product(6,3243242)