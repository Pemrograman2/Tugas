# https://realpython.com/python-matplotlib-guide/
# https://towardsdatascience.com/matplotlib-tutorial-learn-basics-of-pythons-powerful-plotting-library-b5d1b8f67596

# In[1]: https://www.edureka.co/blog/python-matplotlib-tutorial/
from matplotlib import pyplot as bebas
  
#Plotting to our canvas
  

x=[1,2,3]
y=[4,5,1]
bebas.plot(x,y)
  
#Showing what we plotted
  
bebas.show()



# In[2]:
from matplotlib import pyplot as plt
 
x = [5,2,7]
y = [2,16,4]
plt.plot(x,y)
plt.title('Info')
plt.ylabel('Ini Y Lho')
plt.xlabel('Ini X lho')
plt.show()


# In[3]: 2 data satu graph

from matplotlib import pyplot as plt
from matplotlib import style
 
style.use('ggplot')
x = [5,8,10]
y = [12,16,6]
x2 = [6,9,11]
y2 = [6,15,7]
plt.plot(x,y,'g',label='data pertama', linewidth=1)
plt.plot(x2,y2,'c',label='data kedua',linewidth=1)
plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.legend()
#plt.grid(True,color='b')
plt.show()

# In[4]: bar

from matplotlib import pyplot as plt
 
plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20],
label="BMW",color='m',width=.5)
plt.bar([.75,1.75,2.75,3.75,4.75],[80,20,20,50,60],
label="Audi", color='r',width=.5)
plt.legend()
plt.xlabel('Days')
plt.ylabel('Distance (kms)')
plt.title('Information')
plt.show()

# In[5]: histogram


import matplotlib.pyplot as plt
population_age = [11,22,16,9,10,15,22,55,62,45,21,22,34,42,42,4,2,102,95,85,55,110,120,70,65,55,111,115,80,75,65,54,44,43,42,48]
bins = [0,10,20,30,40,50,60,70,80,90,100]
plt.hist(population_age, bins, histtype='bar', rwidth=.9)
plt.xlabel('age groups')
plt.ylabel('Number of people')
plt.title('Histogram')
plt.show()

# In[6]: Scatter

import matplotlib.pyplot as plt
x = [1,1.5,2,2.5,3,3.5,3.6]
y = [7.5,8,8.5,9,9.5,10,10.5]
 
x1=[8,8.5,9,9.5,10,10.5,11]
y1=[3,3.5,3.7,4,4.5,5,5.2]
 
plt.scatter(x,y, label='high income low saving',color='r')
plt.scatter(x1,y1,label='low income high savings',color='b')
plt.xlabel('simpanan dalam ratusan')
plt.ylabel('pendapatan dalam ribuan')
plt.title('Scatter Plot')
plt.legend()
plt.show()

# In[7]: area plot

import matplotlib.pyplot as plt
days = [1,2,3,4,5]
  
sleeping =[7,8,6,11,7]
eating = [2,3,4,3,2]
working =[7,8,7,2,2]
playing = [8,5,7,8,13]
  
plt.plot([],[],color='m', label='Sleeping', linewidth=5)
plt.plot([],[],color='c', label='Eating', linewidth=5)
plt.plot([],[],color='r', label='Working', linewidth=5)
plt.plot([],[],color='k', label='Playing', linewidth=5)
  
plt.stackplot(days, sleeping,eating,working,playing, colors=['m','c','r','k'])
  
plt.xlabel('x')
plt.ylabel('y')
plt.title('Stack Plot')
plt.legend()
plt.show()


# In[8]: Pie Chart

import matplotlib.pyplot as plt
 
days = [1,2,3,4,5]
 
sleeping =[7,8,6,11,7]
eating = [2,3,4,3,2]
working =[7,8,7,2,2]
playing = [8,5,7,8,13]
slices = [7,2,2,13]
activities = ['sleeping','eating','working','playing']
cols = ['c','m','r','b']
 
plt.pie(slices,
  labels=activities,
  colors=cols,
  startangle=90,
  shadow= True,
  explode=(0,0.1,0,0),
  autopct='%1.1f%%')
 
plt.title('Pie Plot')
plt.show()


# In[9]: Multiple Plot

import numpy as np
import matplotlib.pyplot as plt
 
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)
plt.subplot(331)#tinggi,lebar,urutan
plt.plot(t1, f(t1), 'bo', t2, f(t2))
plt.subplot(335)
plt.plot(t2, np.cos(2*np.pi*t2))
plt.subplot(339)
plt.plot(t2, np.cos(2*np.pi*t2))
plt.savefig("kodok.png")

# In[10]:


# In[11]:


# In[12]:


# In[13]:


# In[14]:
