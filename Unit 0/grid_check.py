import sys
w = int(sys.argv[1])
h = int(sys.argv[2])

grid = [[0.0 for x in range(w)] for y in range(h)]
v = [[0.0 for x in range(w)] for y in range(h)]
policies = {}
#[right, left, down, up]

#(y, x) and [y, x] format where y is height and x is width
#grid y increases as it goes down and grid x increases as it goes left

WIN_STATE = [(1, 3)]
LOSE_STATE = [(2, 3)]
BARRIERS = [(2,1)]

#initialize policy
for i in range(w):
    for j in range(h):
        if (j,i) not in BARRIERS:
            policies[(j,i)] = [0.0, 0.0, 0.0, 0.0]
            count = 0
            if i+1 < w and (j, i+1) not in BARRIERS: #right
                policies[(j,i)][0] = 1.0
                count+=1
            if i-1 >= 0 and (j, i-1) not in BARRIERS: #left
                policies[(j,i)][1] = 1.0
                count+=1
            if j+1 < h and (j+1, i) not in BARRIERS: #down
                policies[(j,i)][2] = 1.0
                count+=1
            if j-1 >= 0 and (j-1, i) not in BARRIERS: #up
                policies[(j,i)][3] = 1.0
                count+=1
            if i+1 < w and (j, i+1) not in BARRIERS: #right
                policies[(j,i)][0] = 1.0/count
            if i-1 >= 0 and (j, i-1) not in BARRIERS: #left
                policies[(j,i)][1] = 1.0/count
            if j+1 < h and (j+1, i) not in BARRIERS: #down
                policies[(j,i)][2] = 1.0/count
            if j-1 >= 0 and (j-1, i) not in BARRIERS: #up
                policies[(j,i)][3] = 1.0/count

for i in WIN_STATE:
    grid[i[0]][i[1]] = 1.0
for i in LOSE_STATE:
    grid[i[0]][i[1]] = -1.0

for x in range(h):
    for y in range(w):
        print(grid[x][y], end=" ")
    print()


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
                    probs.append(v[j][i+1])
                if i-1 >= 0 and (j, i-1) not in BARRIERS: #left
                    probs.append(v[j][i-1])
                if j+1 < h and (j+1, i) not in BARRIERS: #down
                    probs.append(v[j+1][i])
                if j-1 >= 0 and (j-1, i) not in BARRIERS: #up
                    probs.append(v[j-1][i])
                count = len(probs)
                max_prob = max(probs)
                if i+1 < w and (j, i+1) not in BARRIERS: #right
                    if v[j][i+1]==max_prob:
                        policies[(j,i)][0] = learning_rate
                    else:
                        policies[(j,i)][0] = (1-learning_rate)/(count-1)
                if i-1 >= 0 and (j, i-1) not in BARRIERS: #left
                    if v[j][i-1]==max_prob:
                        policies[(j,i)][1] = learning_rate
                    else:
                        policies[(j,i)][1] = (1-learning_rate)/(count-1)
                if j+1 < h and (j+1, i) not in BARRIERS: #down
                    if v[j+1][i]==max_prob:
                        policies[(j,i)][2] = learning_rate
                    else:
                        policies[(j,i)][2] = (1-learning_rate)/(count-1)
                if j-1 >= 0 and (j-1, i) not in BARRIERS: #up
                    if v[j-1][i]==max_prob:
                        policies[(j,i)][3] = learning_rate
                    else:
                        policies[(j,i)][3] = (1-learning_rate)/(count-1)
                # min_prob = min(probs)
                # if min_prob < 0:
                #     for x in probs:
                #         sums += (x-min_prob)
                # else:
                #     for x in probs:
                #         sums += x
                # if sums!=0:
                #     pos_min_prob = min(probs)
                #     if min_prob<0:
                #         pos_min_prob = min_prob * -1
                #         sums+=1
                #     else:
                #         pos_min_prob = 0
                #     if i+1 < w and (j, i+1) not in BARRIERS: #right
                #         policies[(j,i)][0] = (pos_min_prob+policies[j,i][0])/(sums)
                #         if v[j][i+1] == min_prob:
                #             policies[(j,i)][0] = (pos_min_prob+1+policies[j,i][0])/(sums+1)
                #     else:
                #         policies[(j,i)][0] = 0.0
                #     if i-1 >= 0 and (j, i-1) not in BARRIERS: #left
                #         policies[(j,i)][1] = (pos_min_prob+policies[j,i][1])/(sums+1)
                #         if v[j][i-1] == min_prob:
                #             policies[(j,i)][1] = (pos_min_prob+1+policies[j,i][1])/(sums+1)
                #     else:
                #         policies[(j,i)][1] = 0.0
                #     if j+1 < h and (j+1, i) not in BARRIERS: #down
                #         policies[(j,i)][2] = (pos_min_prob+policies[j,i][2])/(sums+1)
                #         if v[j+1][i] == min_prob:
                #             policies[(j,i)][2] = (pos_min_prob+1+policies[j,i][2])/(sums+1)
                #     else:
                #         policies[(j,i)][2] = 0.0
                #     if j-1 >= 0 and (j-1, i) not in BARRIERS: #up
                #         policies[(j,i)][3] = (pos_min_prob+policies[j,i][3])/(sums+1)
                #         if v[j-1][i] == min_prob:
                #             policies[(j,i)][3] = (pos_min_prob+1+policies[j,i][3])/(sums+1)
                #     else:
                #         policies[(j,i)][3] = 0.0   
                #     #update policy

for i in range(50):
    one_step()
    update_policy()
print("updated v")
for x in range(h):
    for y in range(w):
        print(round(v[x][y],2), end=" ")
    print()
