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

age = []
salary = []
purchased = []
with open( 'SocialNetworkAds.csv' , newline='' ) as csvfile :
    #
    myreader = csv.reader( csvfile , delimiter=',' , quotechar='"' )
    #
    # header
    #
    for row in myreader :
    #
        print( row )
    #
        break
    #
    #
    # data
    #
    for row in myreader :
    #
        age1 = row[0]
    #
        salary1 = row[1]
        purchase = row[2]
        age.append(float(age1))
        salary.append(float(salary1))
        purchased.append(float(purchase))
    #
        #print( age , salary )
    #
    #
    #

age0 = []
age1 = []
est0 = []
est1 = []
for i in range(0,len(age)):
    if purchased[i]:
        age1.append(age[i])
        est1.append(salary[i])
    else:
        age0.append(age[i])
        est0.append(salary[i])
meanage0 = sum(age0)/len(age0)
meanage1 = sum(age1)/len(age1)
meansalary0 = sum(est0)/len(est0)
meansalary1 = sum(est1)/len(est1)

sdage0 = statistics.pstdev(age0)
sdage1 = statistics.pstdev(age1)
sdest0 = statistics.pstdev(est0)
sdest1 = statistics.pstdev(est1)


total = len(age0) + len(age1) + len(est0) + len(est1)
p0 = (len(age0) + len(est0))/total
p1 = (len(age1) + len(est1))/total

#print(meanage0, meanage1, meansalary0, meansalary1, sdage0, sdage1, sdest0, sdest1)
plt.title("Bayes Age + Salary")

def f(sd, mean, x):
    return 1/(sd*math.sqrt(2*math.pi))*math.exp(-(x-mean)**2/(2*sd**2))

for i in range(0, len(age)):
    #T0
    px1_0 = f(sdage0, meanage0, age[i])
    px2_0 = f(sdest0, meansalary0, salary[i])
    T0 = px1_0 * px2_0 * p0
    #T1
    px1_1 = f(sdage1, meanage1, age[i])
    px2_1 = f(sdest1, meansalary1, salary[i])
    T1 = px1_1 * px2_1 * p1

    p0_x1x2 = T0/(T0+T1)
    p1_x1x2 = T1/(T0+T1)
    if p0_x1x2 > p1_x1x2:
        plt.scatter(age[i], salary[i], color='blue', facecolors='none', edgecolors='b', label="no default")
    else:
        plt.scatter(age[i], salary[i], color='red', marker="x", label="yes default")

# fig, ax = plt.subplots()
# ax.legend(["purchased", "not purchased"])

plt.ylabel('Est $')
plt.xlabel('Age');
plt.show()

