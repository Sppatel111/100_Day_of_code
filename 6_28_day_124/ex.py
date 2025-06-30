# Enter your code here. Read input from STDIN. Print output to STDOUT
list1 = []
front = 0
rear = 0


def deque(a, b):
    global list1, front, rear, size, i

    # print(front)
    # print(rear)
    # print(list1)
    if (front == 0 and rear == size) or (front == rear + 1):
        # print('yes')
        i = 6
        return list1

    else:
        if a == 'append':
            if rear == 0:
                rear += 1
                list1.append(int(b))
            else:
                if rear < size:
                    list1.append(int(b))
                    rear += 1

        elif a == 'appendleft':
            if front == 0:
                list1.insert(0, int(b))
                front += 1
            else:
                list1.insert(front - 1, int(b))
                front -= 1

        elif a == 'pop':
            if rear > 0:
                list1.pop()
                rear -= 1

        elif a == 'popleft':
            if front > 0:
                list1.pop(0)
                front -= 1
        else:
            pass


size = int(input())
# print(size)
i = 0
while i < size:
    x = input().split(' ')
    # print(x)
    deque(x[0], x[1] if len(x) > 1 else 0)
    i += 1

# print(list1)

for i in list1:
    print(f'{i} ', end='')

