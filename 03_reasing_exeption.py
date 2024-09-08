def increament(num):
    try:
        return int(num) + 1 
    except:
        raise ValueError("This is not good")
    
a = increament(98)
print(a)
