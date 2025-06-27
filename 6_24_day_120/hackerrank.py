def merge_the_tools(string, k):
    # your code goes here
    result = []
    list1 = []
    check = True
    while check:
        for i in range(len(string) + 1):
            # print(i)
            if i < k:
                list1.append(string[i])
            else:
                # for j in range(len(list1)):
                # if list1[j+1]==list1[j+2]:
                #     list1.pop(j+1)
                # elif len(list1)==3:
                #     if list1[j]==list1[j+2]:
                #         list1.pop(j+2)
                #     elif list1[j] == list1[j+1]:
                #         list1.pop(j)
                #     else:
                #         pass

                # else:
                #     if list1[j] == list1[j+1]:
                #         list1.pop(j)
                #     else:
                #         pass

                set1 = set(list1)
                # print(set1)
                list1 = list(set1)

                result.append(''.join(list1))
                # print(result)
                # print(list1)
                if len(string) < k + 1:
                    for i in result:
                        print(i)
                    check = False
                else:
                    string = string[k:]
                list1 = []

                break


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)