## matplotlib scatter plot
import matplotlib.pyplot as plt
import numpy as np

#size
# x=np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y=np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# sizes=np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])
#
# plt.scatter(x,y,s=sizes)
# plt.show()

#alpha
#adjust trasnsparcy of dots
# x=np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y=np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# sizes=np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])
#
# plt.scatter(x,y,s=sizes,alpha=0.5)
# plt.show()

## combine color size with alpha

# x=np.random.randint(100,size=(100))
# y=np.random.randint(100,size=(100))
# colors = np.random.randint(100, size=(100))
# sizes=10*np.random.randint(100, size=(100))
#
# plt.scatter(x,y,c=colors,alpha=0.5, s=sizes, cmap='nipy_spectral')
# plt.show()

## bar chart

# vertical by defuakl and horizontal with barh
# x=np.array(['a','b','c','d'])
# y=np.array([10,2,6,68])
#
# # plt.bar(x,y)
# plt.barh(x,y)
# plt.show()

# colors parameter
# x=np.array(['a','b','c','d'])
# y=np.array([10,2,6,68])
#
# # plt.bar(x,y,color='yellow')
# plt.bar(x,y,color='#4CAF50')
# plt.show()

# width parameter
# x=np.array(['a','b','c','d'])
# y=np.array([10,2,6,68])
#
# # plt.bar(x,y,width=0.1)
# plt.barh(x,y,height=0.1)
# plt.show()


## histogram

#mean,sd,size
# x=np.random.normal(170,10,250)
# plt.hist(x)
# plt.show()

# pie chart
#parameters=labels, startangle, explode, shadow, colors
y=np.array([35, 25, 25, 15])
mylabels=['apple','banana','mango','dates']
myexplode=[0.2,0,0,0]
mycolors=['red','blue','hotpink','#4CAF50']
plt.pie(y,labels=mylabels,startangle=90,explode=myexplode,shadow=True,colors=mycolors)
plt.legend(title='Four fruits:')
plt.show()