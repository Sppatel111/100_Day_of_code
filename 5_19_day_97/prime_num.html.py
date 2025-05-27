num=int(input('enter number'))

def prime_number(num):
    is_not = False
    if num == 0 or num ==1:
        is_not=True
        return is_not
    if num > 1:
        for i in range(2,num):
            print(f'outside{i}')
            if (num % i) == 0:
                print(f'inside{i}')
                is_not=True
                return is_not

if prime_number(num):
    print("Not prime number")
else:
    print('prime number')



