list1 = [0, 0, 0, 0, 0, 0]
front = 0
rear = 0


def deque(a, b):
    global list1, front, rear, size, i

    print(front)
    print(rear)
    print(list1)
    if (front == 0 and rear == size - 1) or (front == rear + 1):
        print('yes')
        i = 6
        return i

    else:

        if a == 'append':
            list1[rear] = int(b)
            rear += 1


        elif a == 'appendleft':
            if front == 0:
                print(list1)
                list1[size - 1] = int(b)
                print(list1)
                front = size - 1
            else:
                list1[front - 1] = int(b)

        elif a == 'pop':
            print('pop')
            if rear != 0:
                print(rear)
                list1.pop(rear)
                print(list1)
            else:
                list1.pop(front)

        elif a == 'popleft':
            list1.pop(front)
            if front == size:
                front = 0
            else:
                front += 1
        else:
            pass


size = int(input())
# print(size)
i = 0
while i < size:
    x = input().split(' ')
    print(x)
    deque(x[0],  x[1] if len(x) > 1 else 0)
    i += 1

print(list1)