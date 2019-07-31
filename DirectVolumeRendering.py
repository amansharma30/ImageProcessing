import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np


dataSet=np.fromfile("volume.raw",dtype=np.int16)
xyzdatadataSet = np.reshape(dataSet, (421,512,512))
print ((xyzdatadataSet))

xy0data= xyzdatadataSet[0,:,:]
xydata= xyzdatadataSet[420,:,:]
print ('===============')



plt.figure(1)
xdata = np.ndarray(shape=(421,512))
for i in range(0,512):
    xdata = xdata + xyzdatadataSet[:,i,:]

print(xdata[:,511])
xdata= ((xdata - np.min(xdata))/ (np.max(xdata)- np.min(xdata) )) * 255
#print(xdata)
plt.imshow(xdata,cmap = 'bone',origin='upper')  #,interpolation='bicubic'

plt.show()