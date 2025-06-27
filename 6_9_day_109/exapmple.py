
s = input()

s1=s.split(' ')
list1=[]
for i in range(len(s1)):
    if s1[i].isalnum():
        print('True')
        break
    else:
        if len(list1) < 2:
            if s1[i].isdigit():
                list1.append('True')
            elif s1[i].isalpha():
                list1.append('True')
        else:
            print('True')
            break
        continue

# if s.isalnum():
#     print('True1')
for i in range(len(s)):
    if s[i].isalpha():
        print('True2')
        break
    else:
        if i < len(s) - 1:
            continue
        else:
            print('False')
            break
for i in range(len(s)):
    if s[i].isdigit():
        print('True3')
        break
    else:
        if i < len(s) - 1:
            continue
        else:
            print('False')
            break
for i in range(len(s)):
    if s[i].islower():
        print('True4')
        break
    else:
        if i < len(s) - 1:
            continue
        else:
            print('False')
            break
for i in range(len(s)):
    if s[i].isupper():
        print('True5')
        break
    else:
        if i < len(s) - 1:
            continue
        else:
            print('False')
            break

# s="#$%@^&*kjnk svskjnbui h 4oi3hheuh /dfh uidshvhdsuihv suihc 0hrem89m4c02mw4xo;,wh fwhncoishmxlxfkjsahnxu83v 08 n8OHOIHIOMOICWHOFCMHEOFMCOEJMC0J09C 03J J3L;JMFC3JM3JC3'JIOO9MMJ099U N090N9 OOHOLNHNLLKNLKNKNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333000000000000000000000000000000000000000000000000000000000000000000000000000"
# # s=s.replace(' ','')
# s1=s.split(' ')
# print(s1)
# print(s)
# print(s.isalnum())