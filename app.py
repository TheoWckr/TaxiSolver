import gym
import numpy as np  # 1. Load Environment and Q-table structure

env = gym.make('Taxi-v3')

Q = np.zeros([env.observation_space.n, env.action_space.n])
# env.obeservation.n, env.action_space.n gives number of states and action in env loaded
# 2. Parameters of Q-leanring
eta = 0.95
gma = 0.8
epis = 5000
rev_list = []  # rewards per episode calculate
win = False
count = 0
moove = 0
result = 0
# 3. Q-learning Algorithm
for i in range(epis):
    # Reset environment
    s = env.reset()
    rAll = 0
    d = False
    j = 0
    # The Q-Table learning algorithm
    moove = 0
    while j < 1000:
        j += 1
        moove +=1
        # Choose action from Q table
        a = np.argmax(Q[s, :] + np.random.randn(1, env.action_space.n) * (1. / (i + 1)))
        # Get new state & reward from environment
        s1, r, d, _ = env.step(a)
        # Update Q-Table with new knowledge
        Q[s, a] = Q[s, a] + eta * (r + gma * np.max(Q[s1, :]) - Q[s, a])
        rAll += r
        s = s1
        print()
        if d == True  :
            print('Won')
            count += 1
            if( moove > 19):
                result = i
            break

    rev_list.append(rAll)
    env.render()
print ('Count',count)
print ('Mooves',moove)
print ('result',result)
print("Reward Sum on all episodes " + str(sum(rev_list)/epis))
print("Final Values Q-Table")
print(Q)
while True:
    key = input('Mouvement : ')

    # if the 'ESC' key is pressed, Quit
    if key == 27:
        quit()
    if key == 'z':
        print("up")
    elif key == 's':
        print ("down")
    elif key == 'q':
        print ("left")
    elif key == 'd':
        print ("right")
    # 255 is what the console returns when there is no key press...
    elif key != 255:
        print(key)

