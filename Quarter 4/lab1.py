#pi0 = n0/n
#n0 = # of 0 in set
#k = 0, all ages, all est $ -> calculate average, calculate standard deviation
# = 1, all ages, all est $, P(X1 = x | Y= 0),, histogram -> bins, gaussian = 1/(standard dev * sqrt(2pi))*e^-(x-mean)^2/(2*standard dev^2)))
#overlap - histograms (# bins) (... hist density=Time)
#Bayes

import csv
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d
import statistics
from scipy.stats import norm

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

print(meanage0, meanage1, meansalary0, meansalary1, sdage0, sdage1, sdest0, sdest1)

x_axis = np.arange(min(age0), max(age0), 1)
plt.plot(x_axis, norm.pdf(x_axis, meanage0, sdage0))
plt.hist(age0, density=True, bins=20)
plt.ylabel('Proportion')
plt.xlabel('Age without purchase')
plt.show()

x_axis = np.arange(min(age1), max(age1), 1)
plt.plot(x_axis, norm.pdf(x_axis, meanage1, sdage1))
plt.hist(age1, density=True, bins=20)
plt.ylabel('Proportion')
plt.xlabel('Age with purchase')
plt.show()

x_axis = np.arange(min(est0), max(est0), 1)
plt.plot(x_axis, norm.pdf(x_axis, meansalary0, sdest0))
plt.hist(est0, density=True, bins=20)
plt.ylabel('Proportion')
plt.xlabel('Est $ without purchase');
plt.show()

x_axis = np.arange(min(est1), max(est1), 1)
plt.plot(x_axis, norm.pdf(x_axis, meansalary1, sdest1))
plt.hist(est1, density=True, bins=20)
plt.ylabel('Proportion')
plt.xlabel('Est $ with purchase');
plt.show()