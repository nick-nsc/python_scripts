cipher = "WJVYMHCIBDJBWJYFXDLWLTSTLYOPRHENRPW"
keyword = "LFH"
plain = ""

c_int = 0
plain_int = 0
counter = 0
for c in cipher:
    c_int = ord(c.lower())-97
    plain_int = (c_int - (ord(keyword[counter].lower())-97)) % 26
    plain += chr(plain_int + 97)
    counter = (counter + 1) % 3

print("Plain text:", plain)