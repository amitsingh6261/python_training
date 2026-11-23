x=11 #global variable
print("outside function x= ",x)

def demo():
    global y
    y=13 # local variable
    print("inside function x= ",x)
    print("inside function x= ",y)

demo()
print("outside function x= ",y)