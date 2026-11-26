def even_Number(a,b):
    for i in range(a,b+1):
        if i % 2 == 0:
            print(i)


a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
even_Number(a,b)