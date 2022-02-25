import csv
import math
from matplotlib.axes import Axes
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import random
data = []
student = []
nonstudent = []
#(array 0: default (bool), 1: student (bool) 2: balance (number), 3: income (number))
with open( 'Default.csv' , newline='' ) as csvfile :
    myreader = csv.reader( csvfile , delimiter=',' , quotechar='"' )
    for row in myreader :
        print( row )
        break

    for row in myreader :
        data.append((row[0]=="Yes", row[1]=="Yes", float(row[2]), float(row[3])))
        if row[1] == "Yes":
            student.append((row[0]=="Yes", row[1]=="Yes", float(row[2]), float(row[3])))
        else:
            nonstudent.append((row[0]=="Yes", row[1]=="Yes", float(row[2]), float(row[3])))
    
random.shuffle(data)
random.shuffle(student)
random.shuffle(nonstudent)
print(len(data))
print(len(student))
print(len(nonstudent))
# fig, ax = plt.subplots()
labels = ['yes default', 'no default']
#students and nonstudents
# plt.title("students and non-students")
# defaults = 0
# nondefaults = 0
# i = 0
# while defaults < 100:
#     if data[i][0] == True: #defaulted
#         plt.scatter(data[i][2], data[i][3], color='red', marker="x", label="yes default")
#         defaults +=1
#     i+=1
# i=0
# while nondefaults < 100:
#     if data[i][0] == False : # not defaulted
#         plt.scatter(data[i][2], data[i][3], color='blue', facecolors='none', edgecolors='b', label="no default")
#         nondefaults +=1
#     i+=1

#students
# plt.title("students only")
# defaults = 0
# nondefaults = 0
# i = 0
# while defaults < 100:
#     if student[i][0] == True: #defaulted
#         plt.scatter(student[i][2], student[i][3], color='red', marker="x", label="yes default")
#         defaults +=1
#     i+=1
# i=0
# while nondefaults < 100:
#     if student[i][0] == False : # not defaulted
#         plt.scatter(student[i][2], student[i][3], color='blue', facecolors='none', edgecolors='b', label="no default")
#         nondefaults +=1
#     i+=1

#nonstudents
# plt.title("non-students only")
# defaults = 0
# nondefaults = 0
# i = 0
# while defaults < 100:
#     if nonstudent[i][0] == True: #defaulted
#         ax.scatter(nonstudent[i][2], nonstudent[i][3], color='red', marker="x", label=labels[0])
#         defaults +=1
#     i+=1
# i=0
# while nondefaults < 100:
#     if nonstudent[i][0] == False : # not defaulted
#         ax.scatter(nonstudent[i][2], nonstudent[i][3], color='blue', facecolors='none', edgecolors='b', label=labels[1])
#         nondefaults +=1
#     i+=1

# handles, labels1 = ax.get_legend_handles_labels()

# # ax.legend(["yes default", "no default"])
# ax.legend(handles=[handles[0],handles[-1]])
# ax.grid(True)
# ax.set_xlim([0,3000])
# ax.set_ylim([0,90000])
# plt.xlabel("balance")
# plt.ylabel("income")
# plt.show()

#lab02

#need new iterative, newtons method to determine b0, b1 instead of previous lab's method
numerator = 0
denominator = 0
xn = 0
yn = 0
count = 0
for i in student:
    xn += i[2]
    count += 1
xn = xn / count
for i in student:
    if i[0]:
        yn+=1
print(yn)
yn = yn / count
for i in range(0,len(student)):
    numerator += (student[i][2]-xn)*(student[i][0]-yn)
    denominator += (student[i][2]-xn)**2
b1 = numerator/denominator
b0 = yn - b1*xn
#print(b0, b1)

#max error occurs:
b0 = -11.2259
b1 = 0.005599

student_balances = []
student_defaults = []
for i in student:
    student_balances.append(i[2])
    student_defaults.append(i[0])
def formula(X, Y, b0, b1):
    error = 0
    for i in range(0,len(X)):
        error += (Y[i]*(b0+b1*X[i])-math.log(1+math.exp(b0+b1*X[i])))
    return error
    #sum of Y*log(P)+(1-Y)*log(1-P) = Y*(b0+b1*x)-log(1+e^(b0+b1*x))

err = formula(student_balances, student_defaults, b0, b1)
print(err)

#plot for lab2
def errorFunc(student_balances, student_defaults, b0, b1):
    b0 = b0.tolist()
    b1 = b1.tolist()
    errors = []
    for a in range(len(b0)):
        errorList = []
        for b in range(len(b0[a])):
            errorList.append(formula(student_balances, student_defaults, b0[a][b], b1[a][b]))
        errors.append(errorList)
    return np.array(errors)

b0 = np.arange(-15.0, -5.0, 0.5)
b1 = np.arange(0.001,.01,0.009/10)
b0, b1 = np.meshgrid(b0, b1)
#print(b0)
#print(b0, b1)
z = errorFunc(student_balances, student_defaults, b0, b1)
# b0residStanError, b1residStanError = residualStandardError(b0, b1, tvData, salesData, xn) #resid stand error
# print(b0residStanError)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(b0, b1, z) #surface plot
ax.set_zlim3d(-2000, -200)
ax.scatter( -11.2259 , 0.005599, formula(student_balances, student_defaults, -11.2259, 0.005599) , color = '#ff0000' )
plt.show()