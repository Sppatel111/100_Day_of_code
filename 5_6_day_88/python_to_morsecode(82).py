# morse code dictionary
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


def morse(x):
    text = ''
    for i in x:
        # print(i)
        if i in MORSE_CODE_DICT:
            text += MORSE_CODE_DICT[i]
            text += ' '
            # print(text)
    return text


def encode():
    global list1

    take = input("enter the string to converts:").upper().split()
    list1 =[len(i)for i in take]
    morse1 = ''
    # print(take)
    for i in take:
        morse1 += morse(i)
        morse1 += '  '
    # print(list1)
    return morse1


def decode(y):
    # print(y.split())
    d=''
    for i in y.split():
        # print(i)
        for k,v in MORSE_CODE_DICT.items():
            if i == v:
                d+=k
    # with space
    final=''
    x=0
    for index in list1:
        final += d[x:x+index] + ' '
        x= x+ index
    # print(final)
    return final


active = True
global string
print(" Do you want to do encoding or decoding with respect to string to morse and morse to string??")
while active:
    type = input(" Type ['E' Encoding] or ['D' decoding ] or ['N' exit]: ").upper()
    if type == 'N':
        active = False
    elif type == 'E':
        string = encode()
        print(f' Morse code:\n{string}')
    elif type == 'D':
        # print(string)
        s=decode(string)
        print(f'String:\n{s}')
    else:
        print(' Incorrect input!!')

#https://timmyomahony.com/