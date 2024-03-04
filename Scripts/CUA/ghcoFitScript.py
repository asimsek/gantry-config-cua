# The Kasa method to fit a circle to a set of data points
# Ali Eren & Souvik, 2022
# Use https://www.jdoodle.com/python3-programming-online/
# Upload the log file and this script will take the last 10 "Fit position:" information

import re, os, sys

refPos = [0.3714394647,-102.2092046759,-17.20]
filePath = "/uploads/LOG_Calibrate_GHCO.txt"


###### Don't change anything after this
targetPos = []
x = []

foo_x=[]
foo_y=[]

ctrFitPos = -1
ctrTarget=-1
for line in reversed(list(open(filePath))):
    s = line.rstrip()
    if ">>> targetPos:" in line.rstrip() and ctrTarget==-1:
        pos = (s[s.find("{")+1:s.rfind("}")])
        foo = pos.split(",")
        for i in foo:
            targetPos.append(float(i))
        print ("targetPos: %s" % (targetPos))
        print ("refPosition: %s\n" % (refPos))
        ctrTarget+=1
    if ">>> Fit position:" in s:
        ctrFitPos+=1
        if ctrFitPos < 10:
            pos = (s[s.find("{")+1:s.rfind("}")])
            foo = pos.split(",")
            foo2 = [ float('{:.10f}'.format(float(x))) for x in foo]
            x.insert(0, foo2)
            foo_x.insert(0, x[0][0])
            foo_y.insert(0, x[0][1])
            

for i in x:
    print ("%s," % (i))

def fitCircle(x):
    sum_x = 0
    sum_xx = 0
    sum_xxx = 0
    sum_y = 0
    sum_yy = 0
    sum_yyy = 0
    sum_xy = 0
    sum_xxy = 0
    sum_xyy = 0
    N = len(x)
    for i in range(0, N):
        sum_x += x[i][0]
        sum_xx += x[i][0]*x[i][0]
        sum_xxx += x[i][0]*x[i][0]*x[i][0]
        sum_y += x[i][1]
        sum_yy += x[i][1]*x[i][1]
        sum_yyy += x[i][1]*x[i][1]*x[i][1]
        sum_xy += x[i][0]*x[i][1]
        sum_xxy += x[i][0]*x[i][0]*x[i][1]
        sum_xyy += x[i][0]*x[i][1]*x[i][1]
    alpha = 2.*(sum_x**2 - N*sum_xx)
    beta = 2.*(sum_x*sum_y - N*sum_xy)
    gamma = 2.*(sum_y**2 - N*sum_yy)
    delta = sum_xx*sum_x - N*sum_xxx + sum_x*sum_yy - N*sum_xyy
    epsilon = sum_xx*sum_y - N*sum_yyy + sum_y*sum_yy - N*sum_xxy

    A = (delta*gamma - epsilon*beta)/(alpha*gamma - beta**2)
    B = (alpha*epsilon - beta*delta)/(alpha*gamma - beta**2)

    return (A, B)



AfterFit = [fitCircle(x)[0], fitCircle(x)[1]]

print ("\nafterFit: (%.10f,%.10f) \n" % (AfterFit[0], AfterFit[1]))

diffTargetFit_x, diffTargetFit_y = (targetPos[0]-AfterFit[0])*10**3, (targetPos[1]-AfterFit[1])*10**3
print ("Difference Between Target & Fit: x=%.2f µm | y=%.2f µm\n\n" % (diffTargetFit_x, diffTargetFit_y) )


diffFromRef_x = refPos[0] - (targetPos[0] - AfterFit[0])
diffFromRef_y = refPos[1] - (targetPos[1] - AfterFit[1])

print ("Subtract:")
print ("geometry.tool_holder_offset: {%.10f,%.10f,%.2f}\n" % (diffFromRef_x,diffFromRef_y,refPos[2]))


diffFromRef_x = refPos[0] + (targetPos[0] - AfterFit[0])
diffFromRef_y = refPos[1] + (targetPos[1] - AfterFit[1])

print ("Add:")
print ("geometry.tool_holder_offset: {%.10f,%.10f,%.2f}\n" % (diffFromRef_x,diffFromRef_y,refPos[2]))



print ("x = ", foo_x)
print ("y = ", foo_y)