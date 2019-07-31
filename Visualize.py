import pandas as pa
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


file= pa.read_csv("field2.irreg" , sep=' ' , skiprows=range(0, 6),
                  names = ["Xaxis", "Yaxis", "Zaxis", "dX", "dY", "dZ"])

# converting x,y, dx, dy to float
file["Xaxis"]= file["Xaxis"].astype(float)
file["Yaxis"]= file["Yaxis"].astype(float)
file["dX"]= file["dX"].astype(float)
file["dY"]= file["dY"].astype(float)
#file= file[500:4000]
#print(file)


#Plotting Graph

plt.plot([file.Xaxis,  file.Xaxis + file.dX ], [file.Yaxis, file.Yaxis + file.dY],linestyle= '-',linewidth=2,marker='>', markersize=4,alpha=0.4)

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')


# giving a title to the graph
plt.title('Colorado Data Set!\n Movement of Water Particles')
plt.show()
