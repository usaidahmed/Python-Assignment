#!/usr/bin/env python
# coding: utf-8

# # The ABC company has hired you as an intern on the coding team that creates e-commerce applications.  
# You must write a script that asks the user for a value. The value must be used as a whole number in a calculation, even if the user enters a decimal value. 
# 
# You need to write the code to meet the requirements.

# In[1]:


Items=float(input("Enter no of itmes present in the shopping cart:"))
print(Items)


# In[2]:


print ("Thank You for Shopping",int(Items),"Items From ABC Have a Good Day!")


# # You are creating a Python program that shows a congratulation message to employees on their service anniversary.
# You need to calculate the number of years of service and print a congratulatory message. You should take the inputs from the users where necessary

# In[3]:


Employed_Year=int(input("Enter in which year you have started your Job ?: "))


# In[4]:


Retirement_Year=int(input("Enter in which you will Retire ?: "))


# In[5]:


print("Congratulations! For serving",Retirement_Year-Employed_Year,"valuable years in our company")


# # Write a Python program to convert temperatures  from fahrenheit to celsius, 
# #step 1: take "fahrenheit Temperature" from user in integer data type
# #step 2: apply formula that is       (  C = (5/9) * (fahrenheit_temperature - 32)  )
# #step 3: print step 2. 

# In[6]:


Farenheight_Temperature=int(input("Enter Temperature in Farenheight:"))


# In[7]:


Celcius_Temperature=((5/9)*(Farenheight_Temperature-32))


# In[8]:


print ("Temperature in Celcius is",int(Celcius_Temperature),"Centigrade")


# <h3>assign a vlue to grade by checking the following conditions:: </h3>
# <h3>if % is greater then and equal to 90 and less then 100 grade is A+ </h3>
# <h3>if % is greater then and equal to 80 and less then 90 grade is A </h3>
# <h3>if % is greater then and equal to 70 and less then 80 grade is B </h3>
# <h3>if % is greater then and equal to 60 and less then 70 grade is C </h3>
# <h3>if % is less than 60 grade is FAIL </h3>
# 

# In[9]:


Maths=65
Physics=76
Urdu=55
Islamiat=45
Pakistan_Studies=60


# In[10]:


Obtained_Marks=(Maths+Physics+Urdu+Islamiat+Pakistan_Studies)
print("Obtained_Marks=",Obtained_Marks)


Total_Marks=500
Percentage=(Obtained_Marks/Total_Marks)*100
print("Percentage=",Percentage,"%")


# In[11]:


if Percentage >= 90 and Percentage < 100:
    Grade="A+"
if Percentage >= 80 and Percentage < 90:
    Grade="A"
if Percentage >= 70 and Percentage < 80:
    Grade="B"
if Percentage >= 60 and Percentage < 70:
    Grade="C"
if Percentage < 60:
    Grade="F"


# <h3>Print grade percentage and obtained marks</h3>

# In[12]:


print("Grade=" ,Grade, "Percentage=",Percentage,"%", "Obtained_Marks=", Obtained_Marks)


# In[ ]:





# In[ ]:




