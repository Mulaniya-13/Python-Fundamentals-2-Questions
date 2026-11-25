salary = int(input("Enter your salary: "))

if salary < 30000:
    print("Your final tax rate is: ", salary * 5/100)
elif salary <70000:
    print("Your final tax rate is: ", salary * 15/100)
else:
    print("Your final tax rate is: ", salary * 25/100)

