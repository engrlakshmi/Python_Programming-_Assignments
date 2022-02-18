#!/usr/bin/env python
# coding: utf-8

# In[14]:


#Write a Python Program to Check if a Number is Positive, Negative or Zero?
a=int(input(" Enter the number:"))
if a>0 :
    print(" The number is positive", a)
elif a<0:
        print(" The number is negative", a)
elif a==0:
        print(" The number is zero", a)
else :
        print(" The number is not Positive, Negative or Zero", a)
    


# In[21]:


#Write a Python Program to Check if a Number is Odd or Even?
a=int(input(" Enter the number:"))
if a%2==0 :
    print(" The number is even :", a)
else :
    print(" The number is odd :", a)


# In[13]:


#Write a Python Program to Check Leap Year?
a=int(input(" Enter the Year:"))
if a%4==0 and a%400==0:
        print(" Leap year")
else:
        print(" Not a Leap year")


# In[45]:


#Write a Python Program to Check Prime Number?
a=int(input(" Enter the number:"))
if a>1:
    for i in range(2,a) :
                if a%i==0 :
                    print(" The number is not prime",a)
                    break
                else:
                    print(" The number is prime",a)
                    break
                 
                    
            
    


# In[2]:


#Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?
a=1
b=10000
c=int(input(" Enter the number:"))
print("The prime numbers are :", end ='')
for c in range (a,b+1):
    if c>1 :
        for i in range (2,c):
            if c%i==0 :
                break
        else:
            print(c)
                
                    
                


# In[55]:





# In[ ]:





# In[ ]:




