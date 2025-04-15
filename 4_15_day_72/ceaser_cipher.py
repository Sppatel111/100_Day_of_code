import string
k=3
cipher=[]

dict1={k:v for k,v in zip(string.ascii_uppercase,range(26))}
print(dict1)

def encryption(plain_text,k):
    for i in plain_text:
        x=(dict1[i] - k) % 26
        x1=[key for key, val in dict1.items() if x == val]
        cipher.append(x1[0])

    print(cipher)
    return ''.join(cipher)

plain=[]
def decryption(cipher,k):
    for i in cipher:
        x=(dict1[i] + k) % 26
        x1 = [key for key, val in dict1.items() if x == val]
        plain.append(x1[0])

    print(plain)
    return ''.join(plain)

plain_text=input("enter the text:").upper()
e=encryption(plain_text,k)
print(e)
d=decryption(e,k)
print(d)
