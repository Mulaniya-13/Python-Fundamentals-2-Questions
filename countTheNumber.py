def count(n):
    count=0
    while n >0:
        count += 1
        n = n // 10
    return count


n = int(input("Enter number : "))
print("Number of digits in the number is:", count(n))