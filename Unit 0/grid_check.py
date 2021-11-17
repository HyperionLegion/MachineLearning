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
        print(v[x][y], end=" ")
    print()

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
                    sum += (grid[j][i+1]+0.9*oldv[j][i+1])*policies[(j,i)][0]
                if i-1 >= 0 and (j, i-1) not in BARRIERS: #left
                    sum += (grid[j][i-1]+0.9*oldv[j][i-1])*policies[(j,i)][1]
                if j+1 < h and (j+1, i) not in BARRIERS: #down
                    sum += (grid[j+1][i]+0.9*oldv[j+1][i])*policies[(j,i)][2]
                if j-1 >= 0 and (j-1, i) not in BARRIERS: #up
                    sum += (grid[j-1][i]+0.9*oldv[j-1][i])*policies[(j,i)][3]
                v[j][i] =  sum

def update_policy():
    for i in range(w):
        for j in range(h):
            if (j,i) not in BARRIERS:
                sums = 0
                probs = []
                if i+1 < w and (j, i+1) not in BARRIERS: #right
                    sums += v[j][i+1]
                    probs.append(policies[(j,i)][0])
                if i-1 >= 0 and (j, i-1) not in BARRIERS: #left
                    sums += v[j][i-1]
                    probs.append(policies[(j,i)][1])
                if j+1 < h and (j+1, i) not in BARRIERS: #down
                    sums += v[j+1][i]
                    probs.append(policies[(j,i)][2])
                if j-1 >= 0 and (j-1, i) not in BARRIERS: #up
                    sums += v[j-1][i]
                    probs.append(policies[(j,i)][0])
                count = len(probs)
                if sums!=0:
                    min_prob = min(probs)
                    if min_prob<0:
                        min_prob = min_prob * -1
                    if i+1 < w and (j, i+1) not in BARRIERS: #right
                        policies[(j,i)][0] = (min_prob+policies[j,i][0])/(sums+min_prob*count)
                    else:
                        policies[(j,i)][0] = 0.0
                    if i-1 >= 0 and (j, i-1) not in BARRIERS: #left
                        policies[(j,i)][1] = (min_prob+policies[j,i][1])/(sums+min_prob*count)
                    else:
                        policies[(j,i)][1] = 0.0
                    if j+1 < h and (j+1, i) not in BARRIERS: #down
                        policies[(j,i)][2] = (min_prob+policies[j,i][2])/(sums+min_prob*count)
                    else:
                        policies[(j,i)][2] = 0.0
                    if j-1 >= 0 and (j-1, i) not in BARRIERS: #up
                        policies[(j,i)][3] = (min_prob+policies[j,i][3])/(sums+min_prob*count)
                    else:
                        policies[(j,i)][3] = 0.0   
                    #update policy

for i in range(50):
    one_step()
    #update_policy()
print("updated v")
for x in range(h):
    for y in range(w):
        print(round(v[x][y],2), end=" ")
    print()
