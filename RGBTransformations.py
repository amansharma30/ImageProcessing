import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

arr= []
f= open("i170b2h0_t0.txt","r")
rows = f.readlines()
for row in rows:

    arr.append(row.strip().split(','))


dataset = np.asarray(arr)
dataset = dataset.reshape(500,500)

dataset= np.char.replace(dataset,'"','')
dataset = dataset.astype('double')
dataset = np.flip(dataset,0)

#print(dataset.size)



mean = np.mean(dataset)
variance_sum = 0.0
for x in range(0,len(dataset)):
    for y in range(0,len(dataset)):
        variance_sum += (dataset[x][y] - mean) ** 2
variance = variance_sum / dataset.size
print(np.max(dataset),' ',
np.min(dataset),' ',
mean,' ',variance )


# profile line
plt.figure(1)
plt.title('Profile-line')
plt.yscale('log')

maxi = 0
for i in range(0,500):   #rows
    for j in range(0,500):  #columns
        if maxi< dataset[i][j]:
            maxi =dataset[i][j]
            rowIndex = i
            columnIndex = j

#print(rowIndex,' ',columnIndex)
plt.plot(dataset[rowIndex])


# histogram of this 2D data set

plt.figure(2)
plt.title('HISTOGRAM')
plt.yscale('log')
plt.xscale('log')

dataset = np.log(dataset)+1
xaxis, yaxis = np.unique(dataset,return_counts=True)

plt.plot(xaxis,yaxis)

# scalling Transformation [0-255]


plt.figure(3)
plt.title('Re-Scaling  Transformation')
plt.grid(b=True, which='major', color='#666666', linestyle='-')


linear= np.ndarray(shape=(500,500))

for i in range(0,500):
    for j in range(0,500):

        linear[i][j] = (dataset[i][j] ** 1/2) /255

plt.imshow(linear)
# histogram equalization b2

plt.figure(4)
plt.subplot(222)
plt.title('Histo EQ b2, Wave-length: 25µm')
#plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.xlabel('RA')


# PDF b2
pdfYaxis= yaxis/dataset.size
plt.plot(xaxis,pdfYaxis)
#print('pdfYaxis',pdfYaxis)


# CDF b2
cdfYaxis = []
count=0                                                                          
while count < pdfYaxis.size:
    if(count == 0 ):
        cdfYaxis.append(pdfYaxis[count])
        count += 1
    else:
        cdfYaxis.append(pdfYaxis[count] + cdfYaxis[count - 1])
        count += 1

for i in range(0,len(cdfYaxis)):
    cdfYaxis[i] = cdfYaxis[i] * 255

for i in range(0,len(pdfYaxis)):
    dataset = np.where(dataset == xaxis[i], cdfYaxis[i], dataset)
plt.imshow(dataset,cmap='gray')



# working on b1 file
b1= []
f= open("i170b1h0_t0.txt","r")
rows = f.readlines()
for row in rows:

    b1.append(row.strip().split(','))


datasetb1 = np.asarray(b1)
datasetb1 = datasetb1.reshape(500,500)

datasetb1= np.char.replace(datasetb1,'"','')
datasetb1 = datasetb1.astype('double')
datasetb1 = np.flip(datasetb1,0)
datasetb1 = np.log(datasetb1)+1
xaxis, yaxis = np.unique(datasetb1,return_counts=True)

# histogram equalization b1

#plt.figure(5)
plt.subplot(221)
plt.title('Histo EQ b1, Wave-length: 12µm')
#plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.xlabel('RA')



# PDF b1
pdfYaxis= yaxis/datasetb1.size
plt.plot(xaxis,pdfYaxis)
#print('pdfYaxis',len(pdfYaxis))


# CDF b1
cdfYaxis = []
count=0
while count < pdfYaxis.size:
    if(count == 0 ):
        cdfYaxis.append(pdfYaxis[count])
        count += 1
    else:
        cdfYaxis.append(pdfYaxis[count] + cdfYaxis[count - 1])
        count += 1


for i in range(0,len(cdfYaxis)):
    cdfYaxis[i] = cdfYaxis[i] * 255

for i in range(0,len(pdfYaxis)):
    datasetb1 = np.where(datasetb1 == xaxis[i], cdfYaxis[i], datasetb1)
plt.imshow(datasetb1,cmap='gray')




b3= []
f= open("i170b3h0_t0.txt","r")
rows = f.readlines()
for row in rows:

    b3.append(row.strip().split(','))


datasetb3 = np.asarray(b3)
datasetb3 = datasetb3.reshape(500,500)

datasetb3= np.char.replace(datasetb3,'"','')
datasetb3 = datasetb3.astype('double')
datasetb3 = np.flip(datasetb3,0)
datasetb3 = np.log(datasetb3+1 - np.min(datasetb3))    # transformation to deal with the negative floating point numbers
xaxis, yaxis = np.unique(datasetb3,return_counts=True)


#plt.figure(6)
plt.subplot(223)
plt.title('Histo EQ b3, Wave-length: 60µm')
#plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.xlabel('RA')



# PDF
pdfYaxis= yaxis/datasetb3.size
plt.plot(xaxis,pdfYaxis)
#print('pdfYaxis',len(pdfYaxis))


# CDF
cdfYaxis = []
count=0
while count < pdfYaxis.size:
    if(count == 0 ):
        cdfYaxis.append(pdfYaxis[count])
        count += 1
    else:
        cdfYaxis.append(pdfYaxis[count] + cdfYaxis[count - 1])
        count += 1



for i in range(0,len(cdfYaxis)):
    cdfYaxis[i] = cdfYaxis[i] * 255




for i in range(0,len(pdfYaxis)):
    datasetb3 = np.where(datasetb3 == xaxis[i], cdfYaxis[i], datasetb3)
plt.imshow(datasetb3,cmap='gray')





b4 = []
f= open("i170b4h0_t0.txt","r")
rows = f.readlines()
for row in rows:

    b4.append(row.strip().split(','))


datasetb4 = np.asarray(b4)
datasetb4 = datasetb4.reshape(500,500)

datasetb4= np.char.replace(datasetb4,'"','')
datasetb4 = datasetb4.astype('double')
datasetb4 = np.flip(datasetb4,0)
datasetb4 = np.log(datasetb4)+1
xaxis, yaxis = np.unique(datasetb4,return_counts=True)


#plt.figure(7)
plt.subplot(224)
plt.title('Histo EQ b4, Wave-length: 100µm')
#plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.xlabel('RA')


# PDF
pdfYaxis= yaxis/datasetb4.size
plt.plot(xaxis,pdfYaxis)
#print('pdfYaxis',len(pdfYaxis))


# CDF
cdfYaxis = []
count=0
while count < pdfYaxis.size:
    if(count == 0 ):
        cdfYaxis.append(pdfYaxis[count])
        count += 1
    else:
        cdfYaxis.append(pdfYaxis[count] + cdfYaxis[count - 1])
        count += 1


for i in range(0,len(cdfYaxis)):
    cdfYaxis[i] = cdfYaxis[i] * 255




for i in range(0,len(pdfYaxis)):
    datasetb4 = np.where(datasetb4 == xaxis[i], cdfYaxis[i], datasetb4)

plt.imshow(datasetb4,cmap='gray')



# Combine the histo-equalized data set to an RGB-image (b4=r, b3=g, b1=b)


plt.figure(8)
plt.title('RGB')

RGBdata = []
for i in  range(0,500):
    for j in range(0,500):
        for k in range(0,3):
            if k == 0:
                RGBdata.append(((datasetb4[i][j])))
            if k == 1:
                RGBdata.append((datasetb3[i][j]))
            if k == 2:
                RGBdata.append((datasetb1[i][j]))


RGBdata = (np.asarray(RGBdata))
RGBdata = RGBdata.reshape(500,500,3)
RGBdata = (RGBdata/255)
print(np.max(RGBdata))

plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.imshow((RGBdata))
plt.show()