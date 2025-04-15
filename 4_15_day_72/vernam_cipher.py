text = input("enter the plain text:")
key = input("enter the key:")

cipher_text=[]
def vernam_e(text, key):
    text = text.upper().replace(" ", "")
    key = key.upper().replace(" ", "")
    for p, k in zip(text, key):
        x = ord(p) ^ ord(k)
        print(x)
        cipher_text.append(chr(x))
    print(cipher_text)
    return ''.join(cipher_text)
plain_text=[]
def vernam_d(cipher_text,key):
    cipher_text = cipher_text.upper().replace(" ", "")
    key = key.upper().replace(" ", "")
    for p, k in zip(cipher_text, key):
        x = ord(p) ^ ord(k)
        plain_text.append(chr(x))
    print(plain_text)
    return ''.join(plain_text)


e=vernam_e(text, key)
print(e)
d=vernam_d(e,key)
print(d)