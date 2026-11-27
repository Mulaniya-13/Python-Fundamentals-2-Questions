while True:
    num = input("Enter a number(or Quit to stop): ")

    if num == "Quit":
        break

    num = int(num)

    if num < 0:
        print("Negative number")
    elif num > 0:
        print("Positive Number")
    else:
        print("Zero")