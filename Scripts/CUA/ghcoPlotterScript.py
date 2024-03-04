# Use https://www.w3schools.com/python/trypython.asp?filename=demo_ml_scatterplot

import sys
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

dataIndex=0
x_tar, y_tar = (427.037523, 242.468668)


data = [
[
[427.023116, 242.486123, 87.799816],
[427.058843, 242.363137, 87.79959],
[427.094911, 242.252488, 87.799683],
[427.163401, 242.151638, 87.799637],
[427.240195, 242.061879, 87.846096],
[427.331875, 241.983792, 87.851075],
[427.438311, 241.927763, 87.804846],
[427.549237, 241.889624, 87.820797],
[427.6653, 241.869905, 87.831066],
[427.785548, 241.872739, 87.843389]
],

]

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


center = fitCircle(data[dataIndex])
xc_1, yc_1 = center

x = []
y = []

for i in data[dataIndex]:
    x.append(i[0])
    y.append(i[1])

fig, ax = plt.subplots(1,1, figsize=(7,5))


ax.plot(x, y, '*', label="Data")
ax.plot(xc_1,yc_1,'o', label="Fit")
ax.plot(x_tar, y_tar, 'd', label='Target')

plt.annotate("Fitted Center", (xc_1, yc_1))
plt.annotate("Target Center", (x_tar, y_tar))

plt.legend()
# print(plt.xlim())
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Gantry Head Camera Offset (GHCO)")


#plt.ylim(yc_1, y_tar)
#plt.xlim(xc_1, x_tar)
#plt.autoscale(False)


stringX_="diff_x=%.2f µm" % ((x_tar-xc_1)*10**3)
stringY_="diff_y=%.2f µm" % ((y_tar-yc_1)*10**3)
if dataIndex==0 or dataIndex==1:
    ## 1st and 2nd (0 & 1)
    plt.text(x=xc_1-(xc_1*0.0007), y=yc_1+(yc_1*0.0007), s=stringX_)
    plt.text(x=xc_1-(xc_1*0.0007), y=yc_1+(yc_1*0.0005), s=stringY_)

if dataIndex==2:
    ### 3rd (2)
    plt.text(x=xc_1-(xc_1*(26.5*(10**-6))), y=yc_1+(yc_1*(2.8*(10**-5))), s=stringX_)
    plt.text(x=xc_1-(xc_1*(26.5*(10**-6))), y=yc_1+(yc_1*(2.3*(10**-5))), s=stringY_)

if dataIndex==3 or dataIndex==4:
    ### 4th & 5th (3 & 4)
    plt.text(x=xc_1-(xc_1*(16.5*(10**-6))), y=yc_1+(yc_1*(3.5*(10**-5))), s=stringX_)
    plt.text(x=xc_1-(xc_1*(16.5*(10**-6))), y=yc_1+(yc_1*(3.0*(10**-5))), s=stringY_)

if dataIndex==5:
    ### 6th (5)
    plt.text(x=xc_1-(xc_1*(16.5*(10**-6))), y=yc_1+(yc_1*(3.0*(10**-5))), s=stringX_)
    plt.text(x=xc_1-(xc_1*(16.5*(10**-6))), y=yc_1+(yc_1*(2.5*(10**-5))), s=stringY_)

if dataIndex==6:
    ### 7th (6)
    plt.text(x=xc_1-(xc_1*(26.5*(10**-6))), y=yc_1+(yc_1*(2.8*(10**-5))), s=stringX_)
    plt.text(x=xc_1-(xc_1*(26.5*(10**-6))), y=yc_1+(yc_1*(2.3*(10**-5))), s=stringY_)

if dataIndex==7:
    ### 8th (8)
    plt.text(x=xc_1-(xc_1*(20.5*(10**-6))), y=yc_1+(yc_1*(3.5*(10**-5))), s=stringX_)
    plt.text(x=xc_1-(xc_1*(20.5*(10**-6))), y=yc_1+(yc_1*(3.0*(10**-5))), s=stringY_)

if dataIndex==8 and dataIndex==9:
    ### 8th (8)
    plt.text(x=xc_1-(xc_1*(20.5*(10**-6))), y=yc_1+(yc_1*(3.5*(10**-5))), s=stringX_)
    plt.text(x=xc_1-(xc_1*(20.5*(10**-6))), y=yc_1+(yc_1*(3.0*(10**-5))), s=stringY_)


#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()