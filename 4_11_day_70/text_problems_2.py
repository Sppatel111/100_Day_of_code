# Count Vowels - Enter a string and the program counts the number of vowels in the text.
# For added complexity have it report a sum of each vowel found.


# vowels='aeiou'
#
# s=input("enter the string:")
# count=0
# for i in s:
#     print(i)
#     if i in vowels:
#         print(f"vowels :{i}")
#         count+=1
#
#
# print(f"the number of vowels in the text is {count}")


# Check if Palindrome - Checks if the string entered by the user is a palindrome.
# That is that it reads the same forwards as backwards like “racecar”


# s=input("enter the string:")
#
# print(len(s))
# print(s[len(s)::-1])
#
# if s == s[len(s)::-1]:
#     print(" it is palindrome.")
# else:
#     print("it is not palindrome string. ")

# Count Words in a String - Counts the number of individual words in a string.
# For added complexity read these strings in from a text file and generate a summary.

with open("text.txt",'r') as f:
    text=f.read()
    print(text)
    words=text.split()

print(f" the words length is {len(words) }")
print(f" total unique words count is {len(set(words))}")
print(f"unique words are:{set(words)}")



