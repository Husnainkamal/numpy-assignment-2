#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np


# In[2]:


def function1():print("china")
def function1():print("pakistan")
function1()


# In[3]:



l1=(1,2,3)
print(sum(l1))
print(np.sum(l1))


# In[4]:



l1=np.arange(1,30000)
l1+5


# In[5]:



function1=np.arange(1,13)
print(function1)
print('deminsion',l1.ndim)
print('datatype',l1.dtype)


# In[6]:



function1=np.arange(1,13).reshape((6,-1))
print (function1)


# In[24]:



function2 = np.arange(10,37,dtype=np.float).reshape((3,3,3))
print(function2)


# In[32]:



    #extract those numbers from given array. those are must exist in 5,7 Table
    #example [35,70,105,..]
    a = np.arange(1,1000+1).reshape((10,100))
    print(a)
    print(a[a % 5 == 0])
     #wrtie your code here
    


# In[12]:


#task4

    #Swap columns 1 and 2 in the array arr.
   
arr = np.arange(9).reshape(3,3)
print(arr)
  
return #wrtie your code here
    """Expected Output:
          array([[1, 0, 2],
                [4, 3, 5],
                [7, 6, 8]])
                


# In[23]:


z=np.arange(1,21)
print(z)
z=np.zeros((4,5))
z


# In[32]:


#task6

    # Create a null vector of size 10 but the fifth and eighth value which is 10,20 respectively
   
arr =np.zeros(10) #wrtie your code here
  
print(arr)
print(" fifth and eighth value which is 10,20")
arr[5] = 10
arr[8]=20
print(arr)
   


# In[45]:


#task7

    #  Create an array of zeros with the same shape and type as X. Dont use reshape method

x = np.zeros(4, dtype=np.int64)

print(x)
x.dtype
   


# In[68]:


# Create a new array of 2x5 uints, filled with 6.
x = np.full((2,6), 6)
x


# In[60]:



    # Create an array of 2, 4, 6, 8, ..., 100.
    
a=np.arange(1,101) # write your code here
  
print(a)


# In[63]:



arr = np.array([[3,3,3],[4,4,4],[5,5,5]])
brr = np.array([1,2,3])
subt =brr-arr # write your code here 
 
print(subt)


# In[77]:


#Replace all odd numbers in arr with -1 without changing arr.
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr)
np.where(arr%3==0, -1, arr) 


# In[ ]:




