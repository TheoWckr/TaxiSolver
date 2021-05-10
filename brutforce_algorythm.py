import math
import random

import gym

env = gym.make('Taxi-v3')

epis = 1
turn = 0
allR = 0
for i in range(epis):
    wait = True
    r = 0
    while(wait) :
        s = env.reset()
        next_move = random.randint(0,5)

        s1, r, d, _ = env.step(next_move)
        if d == True:
            print('Won')
            wait = False;
        turn += 1
        allR += r
    print("End")
    print(turn)
    print(allR)

