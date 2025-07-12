#write a python program that uses a while loop to count down numbers within a range.
# The user sh'd be able to input the start and end

end=int(input("Enter end: "))
start=int(input("Enter start: "))


def countdown(start,end):
    while (end>=start):
        print(end)
        if start==end:
            break
        end=end-1

countdown(start,end)


