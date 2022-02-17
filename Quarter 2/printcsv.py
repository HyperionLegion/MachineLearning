import csv
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d
import math
#
def lab03(tvData, salesData, x, n):
    indexes = [k for k in range(0,n)]
    maxIndex = 0
    for i in indexes:
        if (abs(tvData[i]-x) > abs(tvData[maxIndex] -x)):
            maxIndex = i
    for i in range (0, len(tvData)):
        if i not in indexes:
            if (abs(tvData[i]-x) < abs(tvData[maxIndex] -x)):
                indexes.remove(maxIndex)
                indexes.append(i)
                maxIndex = indexes[0]
                for j in indexes:
                    if (abs(tvData[j]-x) > abs(tvData[maxIndex] -x)):
                        maxIndex = j
    averagey = 0
    for i in indexes:
        averagey += salesData[i]
    averagey = averagey/len(indexes)
    return averagey
def SEb02(RSE, xn, tvData):
    denom = 0
    for i in tvData:
        denom += (i-xn)**2
    return RSE*(1/len(tvData) + (xn**2)/denom)
def SEb12(RSE, xn, tvData):
    denom = 0
    for i in tvData:
        denom += (i-xn)**2
    return RSE/denom
def formula(x, b0, b1):
    return b0 + b1*x
def residualStandardError(b0, b1, tvData, salesData, xn):
    b0 = b0.tolist()
    b1 = b1.tolist()
    b0stanError = []
    b1stanError = []
    for a in range(len(b0)):
        b0errorList = []
        b1errorList = []
        for b in range(len(b0[a])):
            error = 0
            for i in range(0,len(tvData)):
                error += (salesData[i] - formula(tvData[i], b0[a][b], b1[a][b]))**2
            b0errorList.append(SEb02(error/(len(tvData)-2), xn, tvData))
            b1errorList.append(SEb12(error/(len(tvData)-2), xn, tvData))
        b0stanError.append(b0errorList)
        b1stanError.append(b1errorList)
    return b0stanError, b1stanError

def errorFunc(b0, b1, tvData, salesData):
    b0 = b0.tolist()
    b1 = b1.tolist()
    errors = []
    for a in range(len(b0)):
        errorList = []
        for b in range(len(b0[a])):
            error = 0
            for i in range(0,len(tvData)):
                error += (salesData[i] - formula(tvData[i], b0[a][b], b1[a][b]))**2
            errorList.append(error)
        errors.append(errorList)
    return np.array(errors)

tvData = []
salesData = []
with open( 'Datasaurus_data.csv' , newline='' ) as csvfile :
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
        tv = row[0]
    #
        sales = row[1]
        tvData.append(float(tv))
        salesData.append(float(sales))
    #
        print( tv , sales )
    #
    #
    #
numerator = 0
denominator = 0
xn = 0
yn = 0
count = 0
for i in tvData:
    xn += i
    count += 1
xn = xn / count
for i in salesData:
    yn += i
yn = yn / count
for i in range(0,len(tvData)):
    numerator += (tvData[i]-xn)*(salesData[i]-yn)
    denominator += (tvData[i]-xn)**2
b1 = numerator/denominator
b0 = yn - b1*xn
#print(b0, b1)
error = 0
for i in range(0,len(tvData)):
    error += (salesData[i]-formula(tvData[i],b0,b1))**2
print(b0-2*SEb02(error/(len(tvData)-2), xn, tvData)**0.5, b0+2*SEb02(error/(len(tvData)-2), xn, tvData)**0.5)
print(b1-2*SEb12(error/(len(tvData)-2), xn, tvData)**0.5, b1+2*SEb12(error/(len(tvData)-2), xn, tvData)**0.5)
print(SEb02(error/(len(tvData)-2), xn, tvData))
print(SEb12(error/(len(tvData)-2), xn, tvData))
print(error)
print(lab03(tvData, salesData, 13.2, 1))
x = np.array(range(int(min(tvData)), int(max(tvData))))
#print(x)
y = formula(x, b0, b1)
#plt.plot(x, y)
#plt.scatter(tvData, salesData)
#plt.show()
b0 = np.arange(5.0,9.0,0.4/100)
b1 = np.arange(0.03,.07,0.04/101)
b0, b1 = np.meshgrid(b0, b1)
#print(b0)
z = errorFunc(b0, b1, tvData, salesData)
# b0residStanError, b1residStanError = residualStandardError(b0, b1, tvData, salesData, xn) #resid stand error
# print(b0residStanError)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(b0, b1, z) #surface plot

lab03x = np.arange(min(tvData), max(tvData), 1)
lab03x = lab03x.tolist()
lab03y = []
for i in lab03x:
    lab03y.append(lab03(tvData, salesData, i, 5))
#    plt.scatter(i, lab03(tvData, salesData, i, 5), color='#ff0000') #make this 2d
#ax.view_init(60, 35) #view angle
ax.scatter( 7.0325935491277 , 0.04753664, 2102.53 , color = '#ff0000' )
#plt.contour( b0 , b1 , z )
plt.show()
print( 'done' )

# b0upper = b0 +2*sqrt(b0residStanError)
# b0lower = b0 -2*sqrt(b0residStanError)
# b1upper = b1 +2*sqrt(b1residStanError)
# b1lower = b1 -2*sqrt(b1residStanError)

#https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contour.html
#y hat = f hat of x0 = average the associated y of the k-nearest x from the observations