#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Print Hello Python
print ("Hello Python")


# In[1]:


# Arithmetic operation

o=input()
p=input()
if o=="sum" and p=="divide":
    print(" Perform sum operation")
    a =int(input(" Enter the value of first number"))
    b=int(input(" Enter the value of second number"))
    c=a+b
    print(" The arithmetic sum of two numbers is  " , c)
    print(" Perform division")
    a =int(input(" Enter the value of first number"))
    b=int(input(" Enter the value of second number"))
    c=a/b
    print(" The quotient is  " , c)
else :
    print(" Can not perform arithematic operation")
    


# In[2]:


# Area of Triangle
b=int(input("Enter the base of the Triangle\t" ))
h=int(input("Enter the height of the Triangle\t" ))
A = .5*b*h
print("Area of the Triangle is ", A)


# In[12]:


# Python program to swap two variables
a=int(input("Enter the first variable, a: \t" ))
b=int(input("Enter the second variable, b: \t" ))
# swap variable
a,b = b,a
print(" The new value of first variable, a : \t " , a )
print(" The new value of second variable, b : \t " , b )


# In[32]:


#Python program to generate a random number
import random
# Print random number from a list by choice
l =[1,2,3,4,5,6,7,8]
print(random.choice(l))

