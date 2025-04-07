# Coin Flip Simulation - Write some code that simulates flipping a single coin however
# many times the user decides.
# The code should record the outcomes and count the number of tails and heads.


import random
tails=0
heads=0
coin_flips=['H','T']

flips=int(input(" How many time do you want flip coin??:"))
result=[]
for i in range(1,flips+1):
    print(f"{i}:",end='')
    result.append(random.choice(coin_flips))
    print(result[-1])

for i in result:
    if i == 'T':
        tails+=1
    else:
        heads+=1


print(f"total {flips} times coin flips by user. and outcome of result {result} tails comes {tails} times and heads are {heads} times. ")



