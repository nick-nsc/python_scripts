number = int(input("Type the positive integer you want to calculate the factorial of: "))

fac = 1

while number > 0:
    fac = fac*number
    number = number-1

print(fac)
