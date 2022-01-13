
#example: ["", 6, 5, 3, 2, 2, 3, 2, 3, 3, 2, 2, 3, 1, 4, 3, -1] w: 6, h:5, m:3, borders: 2, 2 and 3, 2 and 3, 3, rewards: 2, 3, 1, ad 4, 3, -1
import sys
w = int(sys.argv[1])
h = int(sys.argv[2])
m = int(sys.argv[3]) #exL 3/
n = int(sys.argv[4+2*m])

BARRIERS = []
WIN_STATE = []
LOSE_STATE = []

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
policies = {}
#[right, left, down, up]

# python grid_check.py w h m(num of barriers) _barriers: barrier1x barrier1y barrier2x barrie2y ... m(num of rewards) rewards: reward1x reward1y reward1value reward2x reward2y reward2value

#(y, x) and [y, x] format where y is height and x is width
#grid y increases as it goes down and grid x increases as it goes left

# WIN_STATE = [(1, 3)]
# LOSE_STATE = [(2, 3)]

#initialize policy
for i in range(w):
    for j in range(h):
        if (j,i) not in BARRIERS:
            policies[(j,i)] = [0.0, 0.0, 0.0, 0.0]
            policies[(j,i)][0] = 0.25
            policies[(j,i)][1] = 0.25
            policies[(j,i)][2] = 0.25
            policies[(j,i)][3] = 0.25


for i in WIN_STATE:
    grid[i[0]][i[1]] = 1.0
for i in LOSE_STATE:
    grid[i[0]][i[1]] = -1.0
#for i in BARRIERS:
#    grid[i[0]][i[1]] = -5
# for x in range(h):
#     for y in range(w):
#         if (x, y) not in BARRIERS:
#             print(round(grid[x][y],2), end=" ")
#         else:
#             print("---", end = " ")
        
#     print()

gamma = 0.9
def one_step():
    oldv = [[0.0 for x in range(w)] for y in range(h)]
    for j in range(h):
        for k in range(w):
            oldv[j][k] = v[j][k]
    for i in range(w):
        for j in range(h):
            if (j,i) not in BARRIERS:
                sum = 0
                if i+1 < w and (j, i+1) not in BARRIERS: #right
                    sum += (grid[j][i+1]+gamma*oldv[j][i+1])*policies[(j,i)][0]
                if i-1 >= 0 and (j, i-1) not in BARRIERS: #left
                    sum += (grid[j][i-1]+gamma*oldv[j][i-1])*policies[(j,i)][1]
                if j+1 < h and (j+1, i) not in BARRIERS: #down
                    sum += (grid[j+1][i]+gamma*oldv[j+1][i])*policies[(j,i)][2]
                if j-1 >= 0 and (j-1, i) not in BARRIERS: #up
                    sum += (grid[j-1][i]+gamma*oldv[j-1][i])*policies[(j,i)][3]
                v[j][i] =  sum

learning_rate = 0.7
def update_policy():
    for i in range(w):
        for j in range(h):
            if (j,i) not in BARRIERS:
                sums = 0
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
                count = 4
                max_prob = max(probs)
                num = 1
                index = probs.index(max_prob)
                for z in range(0, len(probs)):
                    if index !=z and max_prob - probs[z] <= 0.001:
                        num +=1
                for z in range (0,len(probs)):
                    if index==z:
                        policies[(j,i)][z] = 1/num
                    elif max_prob  - probs[z] <= 0.001:
                        policies[(j,i)][z] = 1/num
                    else:
                        policies[(j,i)][z] = 0
                # if i+1 < w and (j, i+1) not in BARRIERS: #right
                #     if v[j][i+1]==max_prob:
                #         policies[(j,i)][0] = learning_rate
                #     else:
                #         policies[(j,i)][0] = (1-learning_rate)/(count-1)
                # if i-1 >= 0 and (j, i-1) not in BARRIERS: #left
                #     if v[j][i-1]==max_prob:
                #         policies[(j,i)][1] = learning_rate
                #     else:
                #         policies[(j,i)][1] = (1-learning_rate)/(count-1)
                # if j+1 < h and (j+1, i) not in BARRIERS: #down
                #     if v[j+1][i]==max_prob:
                #         policies[(j,i)][2] = learning_rate
                #     else:
                #         policies[(j,i)][2] = (1-learning_rate)/(count-1)
                # if j-1 >= 0 and (j-1, i) not in BARRIERS: #up
                #     if v[j-1][i]==max_prob:
                #         policies[(j,i)][3] = learning_rate
                #     else:
                #         policies[(j,i)][3] = (1-learning_rate)/(count-1)
                

for i in range(1):
    for j in range(4):
        one_step()
    update_policy()
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
