import csv
from matplotlib.axes import Axes
import matplotlib.pyplot as plt
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
fig, ax = plt.subplots()
labels = ['yes default', 'no default']
#students and nonstudents
#plt.title("students and non-students")
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
#plt.title("students only")
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
plt.title("non-students only")
defaults = 0
nondefaults = 0
i = 0
while defaults < 100:
    if nonstudent[i][0] == True: #defaulted
        ax.scatter(nonstudent[i][2], nonstudent[i][3], color='red', marker="x", label=labels[0])
        defaults +=1
    i+=1
i=0
while nondefaults < 100:
    if nonstudent[i][0] == False : # not defaulted
        ax.scatter(nonstudent[i][2], nonstudent[i][3], color='blue', facecolors='none', edgecolors='b', label=labels[1])
        nondefaults +=1
    i+=1

#ax.legend(["yes default", "no default"])
ax.grid(True)
plt.xlabel("balance")
plt.ylabel("income")
plt.show()