x = -0.7
i = 0
def function(x):
    return pow(x, 3) + x - 1
def derivFunction(x):
    return 3*pow(x, 2) + 1
while i<10: 
    print('%3i %20.16f %20.16f'% (i, x, function(x)))
    i += 1
    x -= (function(x) / derivFunction(x))