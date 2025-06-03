import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import time
print(matplotlib.__version__)
x_point = np.array([0,6])
ypoint = np.array([0,250])
plt.plot(x_point,ypoint)
plt.show(block=False)
plt.pause(1)
plt.close()

plt.plot(x_point,ypoint,'o')
plt.show(block=False)
plt.pause(1)
plt.close()

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.show(block=False)
plt.pause(1)
plt.close()


ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints) #take default x point as 0, 1,2,3,4
plt.show(block=False)
plt.pause(1)
plt.close()

plt.plot(ypoints, marker = 'o') #line with points marked as 'o'
plt.show(block=False)
plt.pause(1)
plt.close()

plt.plot(ypoints, marker = '*') #line with points marked as '0'
plt.show(block=False)
plt.pause(1)
plt.close()

plt.plot(ypoints, 'o:r') #marker 'o', line : (dotted), colour ='r'(red)
plt.show(block=False)
plt.pause(1)
plt.close()

plt.plot(ypoints, 'o-.r') #marker 'o', line : (dotted), colour ='r'(red)
plt.show(block=False)
plt.pause(1)
plt.close()

plt.plot(ypoints, marker = 'o', ms = 20) #marker size
plt.show(block=False)
plt.pause(1)
plt.close()

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r') #Marker edge colour alias mec
plt.show(block=False)
plt.pause(1)
plt.close()

plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r') #marker face colour alias mfc
plt.show(block=False)
plt.pause(1)
plt.close()

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r', mfc = 'r')
plt.show(block=False)
plt.pause(1)
plt.close()

plt.plot(ypoints, marker = 'o', ms = 20, mec = "#40BB44", mfc = '#4CAF50')
plt.show(block=False)
plt.pause(1)
plt.close()

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'hotpink', mfc = 'hotpink')
plt.show(block=False)
plt.pause(1)
plt.close()

plt.plot(ypoints, linestyle = 'dotted') #same as plt.plot(ypoints, ls = ':')
plt.show(block=False)
plt.pause(1)
plt.close()



plt.plot(ypoints, linestyle = 'dashed')
plt.show(block=False)
plt.pause(1)
plt.close()

plt.plot(ypoints, color = 'r') #line colour
plt.show(block=False)
plt.pause(1)
plt.close()

plt.plot(ypoints, c = '#4CAF50')
plt.show(block=False)
plt.pause(1)
plt.close()

plt.plot(ypoints, c = 'hotpink')
plt.show(block=False)
plt.pause(1)
plt.close()

plt.plot(ypoints, linewidth = '20.5')
plt.show(block=False)
plt.pause(1)
plt.close()

y2 = np.array([6, 2, 7, 11])

plt.plot(ypoints) #plotting mutliple lines
plt.plot(y2)

plt.show(block=False)
plt.pause(1)
plt.close()

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.show(block=False)
plt.pause(1)
plt.close()

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.show(block=False)
plt.pause(1)
plt.close()

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.title("Sports Watch Data", fontdict = font1)
plt.xlabel("Average Pulse", fontdict = font2)
plt.ylabel("Calorie Burnage", fontdict = font2)

plt.plot(x, y)
plt.show(block=False)
plt.pause(1)
plt.close()

plt.title("Sports Watch Data", loc = 'left') #location of title to the left
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)
plt.show(block=False)
plt.pause(1)
plt.close()

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.plot(x, y)
plt.grid() #To add grid line
plt.show(block=False)
plt.pause(1)
plt.close()

plt.plot(x, y)
plt.grid(axis = 'x')  #Grid on x axis only  #till this only. continue others
plt.show(block=False)
plt.pause(1)
plt.close()