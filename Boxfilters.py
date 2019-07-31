import matplotlib.pyplot as plt
import numpy as np


dataSet=np.fromfile("slice150.raw","int16")
dataSet = np.reshape(dataSet, (512, 512))
#print((dataSet.ndim))
#print((dataSet.shape))
#print((dataSet.size))
#print((np.min(dataSet)))
#print((np.max(dataSet)))
#print(dataSet[200][200])
plt.figure(1)
plt.imshow(dataSet,cmap = 'bone')


# Profile line through the center line of this 2D data set.
middle = []
middle = dataSet[255:256]
middle = middle.ravel()


plt.figure(2)
plt.title('Profile')
plt.plot(middle)


#  mean value and the variance value of this 2D data set
num_rows, num_cols = dataSet.shape

#print(num_cols, num_rows)
addition=0
for i in range(0,num_rows):
	for j in range(0,num_cols):
		addition= addition +dataSet[i][j]
mean = addition/dataSet.size
print('mean is ',mean)

#variance
variance = 0
for i in range(0,512):
    for j in range(0,512):
        variance = variance + (( mean- dataSet[i][j]) ** 2)

variance= variance/dataSet.size
print('variance is ',variance)

# histogram of this 2D data set

plt.figure(3)
plt.title('HISTOGRAM')
xaxis, yaxis =np.unique(dataSet,return_counts=True)

plt.plot(xaxis,yaxis)



# Linear Transformation [0-255]
plt.figure(4)
plt.title('Re-Scaling Linear Transformation')
linear= np.ndarray(shape=(512,512))
min=0
max=255
for i in range(0,512):
    for j in range(0,512):

        linear[i][j] =  dataSet[i][j] /255

plt.imshow(linear,cmap='bone')
#plt.figure(11)
#plt.plot(linear)


#Rescaling Non-Linear
plt.figure(5)
plt.title('Re-Scaling Non- Linear')
nonLinear= np.ndarray(shape=(512,512))

for i in range(0,512):
    for j in range(0,512):
        nonLinear[i][j] = dataSet[i][j] ** 1/9
#plt.plot(nonLinear)
plt.imshow(nonLinear, cmap='bone')
#print(np.max(nonLinear))
#print(np.min(nonLinear))


##BOX-Filter 11*11
plt.figure(6)
plt.title('11*11 Filter')

boxFilter = np.full((11, 11), 1)
boxFilter = boxFilter/121




value = 0
newDataSet = np.ndarray(shape=(512,512))
np.copyto(newDataSet, dataSet)
for i in range(0, 512):   # rows
    for j in range(0, 512):  # columns
        # 11*11 filter
        value = 0
        for k in range(0, 11):  # rows of box-filter
            for l in range(0, 11):   # columns of box-filter
                if i + k < 512 and j + l < 512:  # i+k should not go beyond the actual size of the data-set which is 512
                    value += boxFilter[k][l] * dataSet[i+k][j+l]

        # print('value is: ', value)
        if i + k < 512 and j + l < 512 :
            # print(value,' value is ','assigned to: ',i+5,j+5)
            newDataSet[i+int(k/2)][j+int(l/2)]=value
#print('newDataSet: ',newDataSet[200][200])
plt.imshow(newDataSet, cmap="bone")




##MEDIANFilter 11*11

plt.figure(7)
plt.title('11*11 Median Filter')

newMDataSet= np.ndarray(shape=(512,512))
np.copyto(newMDataSet,dataSet)
for i in range(0,512):   #rows
    for j in range(0,512):  #columns
 # 11*11 Median filter
        value=[]
        for k in range(0,11):
            for l in range(0,11):
                if (i + k < 512 and j + l < 512):
                    #value+= boxFilter[k][l]* dataSet[i+k][j+l]
                    value.append(dataSet[i+k][j+l])


        mid=np.median(value)
        if i + k < 512 and j + l < 512 :
            #print('assigned to: ',i+1,j+1)
           # print('value[] is: ', value, 'median is:', mid)
            newMDataSet[i+ int(k/2)][j+int(l/2)] = mid

#print('newMDataSet: ', newMDataSet[200][200])
plt.imshow(newMDataSet , cmap="bone")



plt.show()
