try:
    a = int(input("enter a number: "))
    c = 1/a
    print(c)
except ValueError as e:
    print("please enter a valid number")
    print(e)    
except ZeroDivisionError as e:
    print("make sure you are not dividing by zero")
    print(e)    
print("thank you")   