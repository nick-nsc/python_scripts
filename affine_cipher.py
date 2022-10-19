alpha = "abcdefghijklmnopqrstuvwxyz"
cipher = "LKCEILZGXVBHHEHXLWHXLWXKYXKJWEVTKEBWRYTK"
plain = ""

# use multiplicative_inverse.py to determine the inverse of a
a_inv = 17
b = 9

score = 0
counter = 0
for a in alpha:
    counter = 0
    for c in cipher:
        if a == c.lower():
            counter += 1
    score += (counter * (counter-1))

coincidence = score / (len(cipher) * (len(cipher)-1))

print("Index of coincidence:", coincidence)

c_int = 0
plain_int = 0
for c in cipher:
    c_int = ord(c.lower())-97
    plain_int = ((c_int - b) * a_inv) % 26
    plain += chr(plain_int + 97)

print("Plain text:", plain)