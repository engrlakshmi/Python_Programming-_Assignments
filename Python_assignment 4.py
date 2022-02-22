#!/usr/bin/env python
# coding: utf-8

# # Python_Assignment 4

# In[ ]:


##1.Write a Python Program to Find the Factorial of a Number?
#Using function
def factorial(number):
    """This function can be used to find factorial of number, you can give input as integer"""
    print(" The factorial of a number :"  )
    if number == 0: 
        return 1
    else :
          return number * (number-1)
    print("\r")


# In[ ]:


factorial(30)


# In[ ]:


##2. Write a Python Program to Display the multiplication Table?
a=int(input("Enter the number"))
print("Multiplication Table of the number is :")
if a!=0:
        for i in range(0,10):
            i=i+1
            b = a*i
            print("\n",a,"x",i,"=",b)
else :
            print('can not perform multiplication')               
                    


# In[ ]:


##3. Write a Python Program to Print the Fibonacci sequence?
num1=0 # first number
num2=1 # second number
terms =int(input("terms"))  # No of terms
if terms>=1:
    print(num1,num2,end=" ")
    for i in range(2,terms):
        num3=num1+num2
        print(num3, end=" " )
        num1=num2
        num2=num3
        
else:
    print("None")
   
    
   


# In[ ]:


##4. Write a Python Program to Check Armstrong Number?
number=int(input("enter the number"))
a=number
Sum=0
order=len(str(number))
while a>0:
    reminder =a%10
    Sum =Sum + reminder**order
    a=a//10
    print(Sum)
if Sum==number:
        print("It is armstrong number",number)  
else:
        print("Not a armstrong number", number) 


# In[46]:


##5. Write a Python Program to Find Armstrong Number in an Interval?
lower =int(input("Lower range"))
upper =int(input("Upper range"))
print("The armstrong numbers are :")
for num in range (lower,upper+1):
    order=len(str(num))
    Sum=0
    c=num
    while c>0:
        reminder =c%10
        Sum =Sum + reminder**order
        c=c//10
        if num ==Sum :
            print("It is armstrong number",num)  
       
        
    


# In[15]:


##6. Write a Python Program to Find the Sum of Natural Numbers?
Sum=0
a = 1
d = 1 
def naturalnumbers(number):
    """This  function is adopted to calculate the sum of natural numbers"""
    c=number-1
    Sum = number/2 *(2*a + c*d)
    return Sum


# In[17]:


naturalnumbers(30)


# In[ ]:





# In[ ]:




