# Complete the solve function below.
import os

def solve(s):
    list2 = []
    list1 = s.split(' ')
    # print(list1)
    for i in list1:
        i = i.capitalize()
        list2.append(i.capitalize())

    return ' '.join(list2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
