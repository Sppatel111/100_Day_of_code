# import matplotlib
#
# print(matplotlib.__version__)

import matplotlib.pyplot as plt
import numpy as np

#line graph
# xpoints=np.array([1,8])
# ypoints=np.array([3,10])
#
# plt.plot(xpoints,ypoints)
# plt.show()

# without line
# xpoints=np.array([1,8])
# ypoints=np.array([3,10])
#
# plt.plot(xpoints,ypoints,'o')
# plt.show()

#multiple points
# xpoints=np.array([1,2,6,8])
# ypoints=np.array([3,8,1,10])
#
# plt.plot(xpoints,ypoints)
# plt.show()


# default x axes
# ypoints=np.array([3,8,1,10])
# plt.plot(ypoints)
# plt.show()


##### marker
# ypoints=np.array([3,8,1,10])
# plt.plot(ypoints,marker='o')
# plt.show()

#marker size
# ypoints=np.array([3,8,1,10])
# plt.plot(ypoints,marker='o',ms=20)
# plt.show()

#marker edge color
# ypoints=np.array([3,8,1,10])
# plt.plot(ypoints,marker='o',ms=20, mec='r')
# plt.show()

# marker face color
# ypoints=np.array([3,8,1,10])
# plt.plot(ypoints,marker='o',ms=20, mfc='r')
# plt.show()

# doted lines
# xpoints=np.array([3,8,1,10])
# plt.plot(xpoints,'o:')
# plt.show()

#color
# xpoints=np.array([3,8,1,10])
# plt.plot(xpoints,'o:c')
# plt.show()

#linestyle or ls (:,--,-.)(dotted,dashed,dashdot)
# x=np.array([1,2,3,4,5])
# y=np.array([3,8,1,11,6])
# plt.plot(x,y,'o',linestyle='dashed')
# plt.show()

#linewidth or lw
# y=np.array([3,8,1,6])
# plt.plot(y,lw=20)
# plt.show()

#multipal line
# x1=np.array([1,5,3,8])
# y1=np.array([1,9,5,11])
# x2=np.array([4,6,12,1])
# y2=np.array([3,8,11,2])
# plt.plot(x1,y1,x2,y2)
#
# plt.show()

####label,title, font
# x=np.array([1,2,3,4,5])
# y=np.array([3,8,1,11,6])
#
# font1={'family':'serif','color':'blue', 'size':20}
# font2={'family':'serif','color':'darkred', 'size':15}
#
# plt.title('Sports Data',fontdict=font1)
# plt.xlabel('Average pulse', fontdict=font2)
# plt.ylabel('calorie burnage', fontdict=font2)
#
# plt.plot(x,y)
# plt.show()

#position title
# x=np.array([1,2,3,4,5])
# y=np.array([3,8,1,11,6])
#
# font1={'family':'serif','color':'blue', 'size':20}
# font2={'family':'serif','color':'darkred', 'size':15}
#
# plt.title('Sports Data',fontdict=font1,loc='left')
# plt.xlabel('Average pulse', fontdict=font2)
# plt.ylabel('calorie burnage', fontdict=font2)
#
# plt.plot(x,y)
# plt.show()

######grid
# y=np.array([3,6,1,8,23,56])
# plt.title('Sports Data2')
# plt.xlabel('Average pulse')
# plt.ylabel('calorie burnage')
# plt.plot(y)
# plt.grid()
# plt.show()

#for specific gride line x or y
# y=np.array([3,6,1,8,23,56])
# plt.title('Sports Data2')
# plt.xlabel('Average pulse')
# plt.ylabel('calorie burnage')
# plt.plot(y)
# plt.grid(axis='y')
# plt.show()

#line property for the grid
# y=np.array([3,6,1,8,23,56])
# plt.title('Sports Data2')
# plt.xlabel('Average pulse')
# plt.ylabel('calorie burnage')
# plt.plot(y)
# plt.grid(color='green',linestyle='--',linewidth=0.5)
# plt.show()


## Matplotlib subplot

# vertical  1 row 2 column

# x=np.array([1,2,3,4,5])
# y=np.array([3,8,1,11,6])
# plt.subplot(1,2,1)
# plt.plot(x,y)
#
# x=np.array([2,4,2,7,11])
# y=np.array([3,8,1,11,6])
# plt.subplot(1,2,2)
# plt.plot(x,y)
#
# plt.show()

# horizontal 2 rows 1 column

# x=np.array([1,2,3,4,5])
# y=np.array([3,8,1,11,6])
# plt.subplot(2,1,1)
# plt.plot(x,y)
# plt.title('Sales',loc='left')
#
# x=np.array([2,4,2,7,11])
# y=np.array([3,8,1,11,6])
# plt.subplot(2,1,2)
# plt.plot(x,y)
# plt.title('Income',loc='left')
# plt.suptitle('My shop')
#
# plt.show()


#Scatter plot
# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# plt.scatter(x,y)
#
# x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
# y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
# plt.scatter(x,y)
# plt.show()

# color map
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors=np.array([1,45,67,34,78,67,68,45,90,100,55,66,89])
plt.scatter(x,y,c=colors, cmap='viridis')
plt.show()

