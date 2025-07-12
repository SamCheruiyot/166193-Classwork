#write a python program that achieves the same as qst 3 by using recursion10
y=int(input("Y: "))
x=int(input("X: "))

def countdown(x,y):
    print(y)

    if x==y:
        return
    else:
        countdown(x,y-1)
countdown(x,y)