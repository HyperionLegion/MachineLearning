#gamma = 0.9, discount
#alpha = 0.2, learning how much to be affected by new experiences
#epsilon = 0.2, random action (exploration) and overtime decreases

#for each cell, 4 q values in array (up, down, left, right)

#Q(x, y, a) a = action

#example: ["", 6, 5, 3, 2, 2, 3, 2, 3, 3, 2, 2, 3, 1, 4, 3, -1] w: 6, h:5, m:3, borders: 2, 2 and 3, 2 and 3, 3, rewards: 2, 3, 1, ad 4, 3, -1
import sys
import random
w = int(sys.argv[1])
h = int(sys.argv[2])
m = int(sys.argv[3]) #exL 3/
n = int(sys.argv[4+2*m])

BARRIERS = []
WIN_STATE = []
LOSE_STATE = []
START = (4, 0)
state = START

for i in range(m):
    x = int(sys.argv[4+i*2+1])
    y = int(sys.argv[4+i*2])
    BARRIERS.append((y,x))
for i in range(n):
    x = int(sys.argv[4+2*m + i*3+2])
    y = int(sys.argv[4+2*m + i*3+1])
    reward = int(sys.argv[4+2*m + i*3+3])
    if reward==1:
        WIN_STATE.append((y, x, reward))
    else:
        LOSE_STATE.append((y, x, reward))

grid = [[0.0 for x in range(w)] for y in range(h)]

v = [[0.0 for x in range(w)] for y in range(h)]
states = []
#[right, left, down, up]

# python grid_check.py w h m(num of barriers) _barriers: barrier1x barrier1y barrier2x barrie2y ... m(num of rewards) rewards: reward1x reward1y reward1value reward2x reward2y reward2value

#(y, x) and [y, x] format where y is height and x is width
#grid y increases as it goes down and grid x increases as it goes left

# WIN_STATE = [(1, 3)]
# LOSE_STATE = [(2, 3)]


for i in WIN_STATE:
    grid[i[0]][i[1]] = 1.0
for i in LOSE_STATE:
    grid[i[0]][i[1]] = -1.0
for i in BARRIERS:
   grid[i[0]][i[1]] = -5
# for x in range(h):
#     for y in range(w):
#         if (x, y) not in BARRIERS:
#             print(round(grid[x][y],2), end=" ")
#         else:
#             print("---", end = " ")
        
#     print()

explore_rate = 0.7
def one_step(j, i):
    probs = []
    if i+1 < w and (j, i+1) not in BARRIERS: #right
        if (j, i+1, -1) in LOSE_STATE:
            probs.append(float('-inf'))
        else:
            probs.append(v[j][i+1])
    else:
        probs.append(float('-inf'))
    if i-1 >= 0 and (j, i-1) not in BARRIERS: #left
        if (j, i-1, -1) in LOSE_STATE:
            probs.append(float('-inf'))
        else:
            probs.append(v[j][i-1])
    else:
        probs.append(float('-inf'))
    if j+1 < h and (j+1, i) not in BARRIERS: #down
        if (j+1, i, -1) in LOSE_STATE:
            probs.append(float('-inf'))
        else:
            probs.append(v[j+1][i])
    else:
        probs.append(float('-inf'))
    if j-1 >= 0 and (j-1, i) not in BARRIERS: #up
        if (j-1, i, -1) in LOSE_STATE:
            probs.append(float('-inf'))
        else:
            probs.append(v[j-1][i])
    else:
        probs.append(float('-inf'))
    max_prob = max(probs)
    num = 1
    index = probs.index(max_prob)
    values = [0, 0, 0, 0]
    values[index] = 1
    for z in range(0, len(probs)):
        if index !=z and max_prob - values[z] <= 0.001:
            num +=1
    actions = []
    for z in range (0,len(probs)):
        if index==z:
            actions.append(index)
        elif max_prob  - probs[z] <= 0.001:
            actions.append(z)
        else:
            values[z] = 0

    #explore?
    if random.random() > explore_rate:
        #print('explore')
        choices = []
        if i+1 < w and (j, i+1) not in BARRIERS and 0 not in actions: #right
            choices.append( (j, i+1))
        if i-1 >= 0 and (j, i-1) not in BARRIERS and 1 not in actions: #left
            choices.append( (j, i-1))
        if j+1 < h and (j+1, i) not in BARRIERS and 2 not in actions: #down
            choices.append( (j+1, i))
        if j-1 >= 0 and (j-1, i) not in BARRIERS and 3 not in actions: #up
            choices.append( (j-1, i))
        if len(choices) > 0:
            return random.choice(choices)
        choices = []
        if i+1 < w and (j, i+1) not in BARRIERS: #right
            choices.append( (j, i+1))
        if i-1 >= 0 and (j, i-1) not in BARRIERS: #left
            choices.append( (j, i-1))
        if j+1 < h and (j+1, i) not in BARRIERS: #down
            choices.append( (j+1, i))
        if j-1 >= 0 and (j-1, i) not in BARRIERS: #up
            choices.append( (j-1, i))
        return random.choice(choices)
    else:
        #print('max')
       
        index = random.choice(actions)
        #print(index)
        if index ==0:
            return (j, i+1)
        elif index == 1:
            return (j, i-1)
        elif index == 2:
            return (j+1, i) 
        else:
            return (j-1, i)

lr = 0.2

def update_policy(j, i):
    global states
    global state
    reward = grid[j][i]
    v[j][i] = reward
    for s in reversed(states):
        #print(s)
        reward = v[s[0]][s[1]] + lr * (reward-v[s[0]][s[1]])
        v[s[0]][s[1]]= round (reward, 3)
    states = []
    state = START
while x < 100:
    if (state[0], state[1], 1) in WIN_STATE or (state[0], state[1], -1) in LOSE_STATE:
        update_policy(state[0], state[1])
        x+=1
        print(x)
        state=START
        states = []
    else:
        states.append(state)
        #print(state)
        state = one_step(state[0], state[1])

print("updated v")
for x in range(h):
    for y in range(w):
        print("{:.2f}".format(v[x][y]), end=" ")
        #print(v[x][y], end=" ")
    print()

for j in range(h):
    for i in range(w):
        #print("{:.2f}".format(v[x][y]), end=" ")
        values = []
        if i+1 < w and (j, i+1) not in BARRIERS: #right
            values.append(v[j][i+1])
        else:
            values.append(float('-inf'))
        if i-1 >= 0 and (j, i-1) not in BARRIERS: #left
            values.append(v[j][i-1])
        else:
            values.append(float('-inf'))
        if j+1 < h and (j+1, i) not in BARRIERS: #down
            values.append(v[j+1][i])
        else:
            values.append(float('-inf'))
        if j-1 >= 0 and (j-1, i) not in BARRIERS: #up
            values.append(v[j-1][i])
        else:
            values.append(float('-inf'))

        if (j, i) in BARRIERS:
            print("####", end=" ")
        elif (j,i+1,1) in WIN_STATE:
            print("---r", end=" ")
        elif (j,i-1,1) in WIN_STATE:
            print("--l-", end=" ")
        elif (j+1,i,1) in WIN_STATE:
            print("-d--", end=" ")
        elif (j-1,i,1) in WIN_STATE:
            print("u---", end=" ")
        else:
            threshold = 0.001

            string = "----"

            maximum = max(values)
            index = values.index(maximum)
            letters = {0: "r", 1: "l", 2: "d", 3: "u"}
            string = string[:index] + letters[index] + string[index+1:]
            for z in range(len(values)):
                if index !=z and maximum-values[z]<=threshold:
                    string = string[:z] + letters[z] + string[z+1:]
            secondmax = min(values)
            secondindex = values.index(secondmax)
            for a in range(len(values)):
                if values[a] != maximum:
                    if secondmax < values[a]:
                        secondmax = values[a]
                        secondindex = a
            if (j,i+1,-1) in LOSE_STATE:
                string = string[:0] + "-" + string[0+1:]
                if index==0:
                    string = string[:secondindex] + letters[secondindex] + string[secondindex+1:]
            if (j,i-1,-1) in LOSE_STATE:
                string = string[:1] + "-" + string[1+1:]
                if index==1:
                    string = string[:secondindex] + letters[secondindex] + string[secondindex+1:]
            if (j+1,i,-1) in LOSE_STATE:
                string = string[:2] + "-" + string[2+1:]
                if index ==2:
                    string = string[:secondindex] + letters[secondindex] + string[secondindex+1:]
            if (j-1,i,-1) in LOSE_STATE:
                string = string[:3] + "-" + string[3+1:]
                if index == 3:
                    string = string[:secondindex] + letters[secondindex] + string[secondindex+1:]
            print(string[::-1], end=" ")
    print()

## for barriers, udlr for policy and - in place of letters if that is not a good move
