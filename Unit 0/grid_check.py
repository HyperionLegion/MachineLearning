import sys
w = int(sys.argv[1])
h = int(sys.argv[2])

grid = [[0.0 for x in range(w)] for y in range(h)]
v = [[0.0 for x in range(w)] for y in range(h)]

#(y, x) and [y, x] format where y is height and x is width
#grid y increases as it goes down and grid x increases as it goes left

WIN_STATE = [(1, 3)]
LOSE_STATE = [(2, 3)]
BARRIERS = [(1,1)]

for i in WIN_STATE:
    grid[i[0]][i[1]] = 1.0
for i in LOSE_STATE:
    grid[i[0]][i[1]] = -1.0

for x in range(h):
    for y in range(w):
        print(v[x][y], end=" ")
    print()

def one_step():
    for i in range(w):
        for j in range(h):
            if (j,i) not in BARRIERS:
                oldv = v[j][i]
                sum = 0
                if i+1 < w and (j, i+1) not in BARRIERS:
                    sum += (grid[j][i+1]+0.9*oldv)
                if i-1 >= 0 and (j, i-1) not in BARRIERS:
                    sum += (grid[j][i-1]+0.9*oldv)
                if j+1 < h and (j+1, i) not in BARRIERS:
                    sum += (grid[j+1][i]+0.9*oldv)
                if j-1 >= 0 and (j-1, i) not in BARRIERS:
                    sum += (grid[j-1][i]+0.9*oldv)
                v[j][i] =  sum

one_step()
print("updated v")
for x in range(h):
    for y in range(w):
        print(v[x][y], end=" ")
    print()

def reset():
    old_v = []
    for j in range(h):
        for k in range(w):
            old_v[j][k] = v[j][k]
            v[j][k] = 0.0
    #v = sum of R' + gamma * V')
    #v[j][k] = sum of (0.0 or 1.0 or -1.0) + 0.9*old_v[y][x] for neighbors

#init policy
p = []
for j in range(h):
    p.append([])
    for k in range(w):
        p[-1].append([0.25, 0.25, 0.25, 0.25])
        # 0 - up
        # 1 - down
        # 2 - left
        # 3 - right