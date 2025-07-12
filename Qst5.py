
x=5
y=3

def product(x,y):
    if y==0:
        return 0
    elif(y>0):
        return product(x,y)

product(5,3)