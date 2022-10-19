# Get the modulus
m = int(input("m: "))
# Get the user's number
n = int(input("n: "))

# reference function: https://www.geeksforgeeks.org/
def extendedGCD(a, b):
    if a == 0:
        return b,0,1
             
    gcd,x1,y1 = extendedGCD(b%a, a)

    x = y1 - (b//a) * x1
    y = x1
     
    return gcd,x,y

results = extendedGCD(n, m)
inverse = results[1]
if inverse < 0:
    inverse = m + inverse

print("Inverse of", n, ":", inverse)