class area:
    def seta(self):
        self.a=5.5
        return(self.a)
    def setb(self):
            self.b=3.5
            return(self.b)
class circle:
    def display(self):
        self.r=area.seta(self)
        self.x=3.14*self.r*self.r
        print("area of circle=",self.x)

class ractangle(area):
     def demo(self):
          self.l=area.seta(self)
          self.b=area.setb(self)
          print(self.l*self.b)

obj=circle()
obj.display()
        
obj1=ractangle()
obj1.demo()