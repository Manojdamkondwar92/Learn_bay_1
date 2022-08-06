#!/usr/bin/env python
# coding: utf-8

# In[2]:


## Fabonachi series
# 0,1,1,2,3,5,8.....


# In[2]:


num = int(input("Enter a number : "))

n1, n2 = 0,1
count =0
if num<=0:
    print("Enter a positive integer")

elif num ==1:
    print(f"fib value is {num} is {n1}")

else:
    print("Fibonacci sequence:")
    while count < num:
        print(n1, end = "\n ")
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count+=1
    
# print(f"fib series is : {n}")


# In[ ]:





# In[ ]:




