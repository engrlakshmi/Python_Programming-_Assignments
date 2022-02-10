#!/usr/bin/env python
# coding: utf-8

# In[9]:


#Python program to convert kilometers to miles
a = float(input(" Enter the value in kilometeres \t "))
b= 0.621371*a
print(" The value in miles is  : ", b, "miles")


# In[10]:


#Python program to convert Celsius to Fahrenheit
a = float(input(" Enter the value in Celsius \t "))
b =(a * 1.8) + 32
print(" The value in Fahrenheit is  : ", b, "F")


# In[16]:


#Python program to display calendar
import calendar
a= int(input("Enter the year of calendar \t:"))
b= int(input("Enter the month of the calendar \t:"))
print(calendar.month(a,b))


# In[18]:


# Python program to solve quadratic equation
import cmath
a =int(input(" Enter the value of the variable, a : \t"))
b =int(input(" Enter the value of the variable, b : \t"))
c =int(input(" Enter the value of the variable, c : \t"))
d =b*2-4*a*c
#roots of the equation
r1 = b*2/(2*a) -cmath.sqrt(d)/(2*a)
r2 = b*2/(2*a) +cmath.sqrt(d)/(2*a)
print(" The roots of the equations are: \t", r1, r2)


# In[19]:


#Python program to swap two variables without temp variable
a=int(input("Enter the first variable, a: \t" ))
b=int(input("Enter the second variable, b: \t" ))
# swap variable
a,b = b,a
print(" The new value of first variable, a : \t " , a )
print(" The new value of second variable, b : \t " , b )


# In[ ]:




