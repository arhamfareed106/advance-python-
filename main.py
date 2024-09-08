# //////////////////////////Exeption handling ////////////////


while True:
    print ("press q to quit")

    a = input("enter your number: ")
    if a == 'q':
        break
    try:
        a = int(a)
        if a > 6:
            print("you entered a number greater than 6")
    except Exception as e:
        print(f"you did not enter a number{e}")

print("thank you for playing this game")