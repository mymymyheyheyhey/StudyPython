# random function
import random

print(random.choice(range(1, 7))) # 주사위

# lottery
numbers = [i for i in range(1, 46)]
lottery = [] # list

for i in range(6):
    lottery.append(random.choice(numbers))

print(lottery)
