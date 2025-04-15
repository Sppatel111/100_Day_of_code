def create_vigenere_matrix():
    matrix=[]
    for i in range(26):
        row=[(chr((j+i)% 26 + 65)) for j in range(26)]
        matrix.append(row)
        # print(matrix)
    return matrix

def encryption(text,key):
    matrix=create_vigenere_matrix()
    text=text.upper().replace(" ","")
    key=key.upper().replace(" ","")

    key_repeated= (key * (len(text)//len(key) +1))[:len(text)]

    cipher_text=[]
    for p,k in zip(text,key_repeated):
        if p.isalpha():
            row = ord(k) - 65
            col =ord(p) - 65
            cipher_text.append(matrix[row][col])
        else:
            cipher_text.append(p)
    return ''.join(cipher_text)



def decryption(cipher_text,key):
    matrix=create_vigenere_matrix()
    cipher_text = cipher_text.upper().replace(" ", "")
    key = key.upper().replace(" ", "")

    key_repeated = (key * (len(cipher_text) // len(key) + 1))[:len(cipher_text)]

    plain_text = []
    for c,k in zip(cipher_text,key_repeated):
        if c.isalpha():
            row=ord(k) - 65
            col = matrix[row].index(c)
            plain_text.append(chr(col + 65))
        else:
            plain_text.append(c)
    return ''.join(plain_text)

plain_text=input("enter the plain text")
key=input("enter key:")


encrypt=encryption(plain_text,key)
print(f"encryption:{encrypt}")

decrypt=decryption(encrypt,key)
print(f'decryption:{decrypt}')