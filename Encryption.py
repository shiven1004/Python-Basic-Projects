
# Encryption

def encrypt(s, x):
    r = ""
    for i in range(len(s)):
        c = s[i]

        if c.isupper():
            r += chr((ord(c) + x - 65) % 26 + 65)
        else:
            r += chr((ord(c) + x - 97) % 26 + 97)
    return r


s = str(input("Enter the code to be encrypted: "))
x = int(input("Enter the shift value: "))
print(encrypt(s, x))
