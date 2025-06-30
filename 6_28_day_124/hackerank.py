# n = int(input())
# list1 = []
# count = {}
# for i in range(n):
#     c = input()
#     list1.append(c)
#
#     if c in count:
#         count[c] += 1
#     else:
#         count[c] = 1
#
# print(len(count))
# for k, v in count.items():
#     print(f'{v} ', end='')

# list1=[0,0,0,0,0]
# # list1.append(12)
# list1.insert(0,23)
# print(list1)

from collections import deque

# Initialize an empty deque
d = deque()

# Read the number of operations
n = int(input())

# Process each operation
for _ in range(n):
    operation = input().split()
    command = operation[0]

    if command == 'append':
        d.append(int(operation[1]))
    elif command == 'appendleft':
        d.appendleft(int(operation[1]))
    elif command == 'pop':
        if d:  # Check if deque is not empty
            d.pop()
    elif command == 'popleft':
        if d:  # Check if deque is not empty
            d.popleft()

# Print the space-separated elements of the deque
print(' '.join(map(str, d)))


