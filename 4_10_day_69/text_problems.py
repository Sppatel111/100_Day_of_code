# Fizz Buzz - Write a program that prints the numbers from 1 to 100.
# But for multiples of three print “Fizz” instead of the number and for
# the multiples of five print “Buzz”.
# For numbers which are multiples of both three and five print “FizzBuzz”.

# for i in range(1,101):
#     if i % 3 ==0:
#         print("Fizz")
#         continue
#     elif i % 5 ==0:
#         print("Buzz")
#         continue
#     elif i % 3==0 and i % 5==0:
#         print("FizzBuzz")
#         continue
#     print(i)


# Reverse a String - Enter a string and the program will reverse it and print it out.

# s=input("enter the string:")
#
# print(s[len(s)::-1])


# Pig Latin - Pig Latin is a game of alterations played on the English language game.
# To create the Pig Latin form of an English word the initial consonant sound is transposed to
# the end of the word and an ay is affixed (Ex.: "banana" would yield anana-bay). Read Wikipedia
# for more information on rules.

def pig_latin_converter(word):
    vowels = "aeiou"
    word = word.lower()

    if word[0] in vowels:
        return word + "way"
    else:
        for i in range(len(word)):
            if word[i] in vowels:
                return word[i:] + word[:i] + "ay"
        return word + "ay"

def pig_latin_sentence(sentence):
    words = sentence.split()
    print(words)
    pig_latin_words = [pig_latin_converter(word.strip('.,!?"')) for word in words]
    print(pig_latin_words)
    return ' '.join(pig_latin_words)

if __name__ == "__main__":
    user_input = input("Enter a word or sentence to convert to Pig Latin: ")
    pig_latin_output = pig_latin_sentence(user_input)
    print("Pig Latin:", pig_latin_output)
