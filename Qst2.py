#write a python program to count down numbers from n to 1 using recurrsion
n=int(input("Enter a number: "))
def countdown(n):
    print(n)
    if n==1:
     return
    else:
         countdown(n-1)
countdown(n)
