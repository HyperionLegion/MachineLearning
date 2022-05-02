import math
#Bayes
#prob of output=0 given input x1=x1 and x2=x2
#prob o output=1 given inputx1=x1 and x2=x2
#take the prob that is bigger, instead of just 1 number with a threshold, 2 numbers

#Prob of A given B = Prob of A and B / Prob of B (naive bayes rule)
#prob of A and B = Prob of B * Prob of (A given B) = Prob of A * Prob of ( B given A)

#Prob of A given B = Prob of A * Prob of B given A / (Prob of A * Prob of B given A + Prob of not A * Prob of B given not A)
#denom = prob of B and A + prob of B and not A (total probability)
#not A = output = 1
#A output = 0

#Prob of B given A, prob of B given not A, prob of x1, x2 given output = 0, prob of x1, x2 given output = 1
#function = 1/(standard dev * sqrt(2pi)) * exp(-(x-mean)^2/(2*standard dev^2))
#P of x1, x2 = P of x1 * P of x2, means independent events

#prob of output =0 given x1, x2) = Prob(output=0) * Prob(x1, x2 | output =0) / (Prob output=0)*P(x1, x2 | output = 0) + P(output=1)*P(x1, x2 | output = 1)
#Prob of output=1 given x1, x2 = same thing but outpu=1 in numerator ^^^
#Prob of output =0 = pi_0 = n_0/n
#prob of output = 1 = pi_1 = n_1/n
#n = n0 +n1 = 400?
#P(x1, x2 | output = 1) = P(x1 | output=1) * P(x2 | output=1) ASSUMPTION, independent from naive
#P of x1 | output = 1 = f_1(x_1)
#P of x_2 | output = 1 = f_2(x_2)
#p0 * f_0(x_1) * f_0(x_2) / pi_0*f_0(x_1)*f_0(x_2) + pi_1*f_1(x_1)*f_2(x_2)
import csv
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d
import statistics
from scipy.stats import norm
from matplotlib.axes import Axes
from sklearn import svm
import statistics


x = []
y = []
z = []
with open( 'data.csv' , newline='' ) as csvfile :
    #
    myreader = csv.reader( csvfile , delimiter=',' , quotechar='"' )
    #
    # header
    #
    # for row in myreader :
    # #
    #     print( row )
    # #
    #     break
    #
    #
    # data
    #
    for row in myreader :
    #
        x1 = row[0]
    #
        y1 = row[1]
        z1 = row[2]
        purchase = row[2]
        x.append(float(x1))
        y.append(float(y1))
        z.append(float(z1))
    #
        #print( age , salary )
    #
    #
    #
def distancePointLine(a, b, c, x, y):
    return abs((a * x + b * y + c) / math.sqrt(a * a + b * b))

xavg = sum(x)/len(x)
yavg = sum(y)/len(y)

xsd = statistics.pstdev(x)
ysd = statistics.pstdev(y)

X = [[x[i]/xavg, y[i]/yavg] for i in range(len(x))]
Y = [z[i] for i in range(len(z))]
#
import numpy as np
#
from sklearn import decomposition
#
X = np . array( X )
#   
pca = decomposition . PCA( n_components = 2 )
#
pca . fit( X )
#
print( pca . components_               )
print( pca . explained_variance_       )
print( pca . explained_variance_ratio_ )

line1dx = pca.components_[0][0]
line1dy = pca.components_[0][1]
line2dx = pca.components_[1][0]
line2dy = pca.components_[1][1]
#y = mx
fig, ax = plt.subplots()
for i in range(len(x)):
    #first score x
    # if (line2dy/line2dx)*(x[i]-xavg) > (y[i]-yavg):
    #     ax.scatter(distancePointLine(line2dy/line2dx, -1, 0, x[i], y[i]), (x[i]-xavg), color='C0')
    # else:
    #     ax.scatter(-distancePointLine(line2dy/line2dx, -1, 0, x[i], y[i]), (x[i]-xavg), color='C0')
    #first score y
    # if (line2dy/line2dx)*(x[i]-xavg) > (y[i]-yavg):
    #     ax.scatter(distancePointLine(line2dy/line2dx, -1, 0, x[i], y[i]), (y[i]-yavg), color='C0')
    # else:
    #     ax.scatter(-distancePointLine(line2dy/line2dx, -1, 0, x[i], y[i]), (y[i]-yavg), color='C0')
    #second score x
    #ax.scatter(distancePointLine(line2dy/line2dx, -1, 0, x[i], y[i]), (x[i]-xavg)/xsd, color='C0')
    # if (line1dy/line1dx)*(x[i]-xavg) > (y[i]-yavg):
    #     ax.scatter(distancePointLine(line1dy/line1dx, -1, 0, x[i], y[i]), (x[i]-xavg), color='C0')
    # else:
    #     ax.scatter(-distancePointLine(line1dy/line1dx, -1, 0, x[i], y[i]), (x[i]-xavg), color='C0')
    #second score y
    #ax.scatter(distancePointLine(line2dy/line2dx, -1, 0, x[i], y[i]), (y[i]-yavg)/ysd, color='C0')
    if (line1dy/line1dx)*(x[i]-xavg) > (y[i]-yavg):
        ax.scatter(distancePointLine(line1dy/line1dx, -1, 0, x[i], y[i]), (y[i]-yavg), color='C0')
    else:
        ax.scatter(-distancePointLine(line1dy/line1dx, -1, 0, x[i], y[i]), (y[i]-yavg), color='C0')

# ax.set_xlim(-3, 3)
# ax.set_ylim(-2, 4) 

plt.ylabel('y')
plt.xlabel('second score');
plt.show()
