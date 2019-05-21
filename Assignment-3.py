#!/usr/bin/env python
# coding: utf-8

# <h3>Q no 1:  Write a python program to find number of occurrences of given number in a list with out using built-in methods</h3>
# <h4>**1 generate a list of some random num which is repeated again and again</h4>
# <h4>**2 take user input any number</h4>
# <h4>**3 find the number of occurrences of that num in your list</h4>
# <h4>**4 print some message to user with that result</h4>

# In[1]:


Random_num=[1,4,4,2,1,4,1,3]
User_Input=int(input("Enter Whole Number :"))
Occurence=0


# In[2]:


for i in Random_num:
    if(User_Input == i):
        Occurence+= 1
print ("Occurence",Occurence)


# <h3>Q no 2:   ["www.zframez.com", "www.wikipedia.org", "www.asp.net", "www.abcd.in"]
# <br/><br/><br/><br/><br/>
# Write a python program to print website suffixes (com , org , net ,in) from this list
# 
# Hint : Use split() method to perform this task
# </h3>
# 

# In[3]:


list= ["WWW.zframez.com","WWW.wikipedia.org","WWW.abcd.in"]


# In[4]:


for name in list:
    Suffix= name.split(".")
    print(Suffix[-1])


# <h3> Q no 3 : Write a program which can compute the factorial of a given numbers.</h3>
# <br/>
# <br/>
# <h4>**1 first take user input any number</h4>
# <h4>**2 calculate factorial of that input and then print the result to user</h4>

# In[5]:


Value = int(input("Enter the Value: "))
Loop_Value = Value - 1


# In[6]:


if(Value == 0):
    New_Value = 1

elif(Value < 0):
    New_Value = print("Enter a positive value")
    

else:
    for i in range(Loop_Value, 0 , -1):
        New_Value = Value * i
        Value = New_Value


# In[8]:


print(New_Value)


# In[ ]:





# <h3>Q 4 (a) :  If you could invite anyone, living or deceased, to dinner, who
# would you invite? Make a list that includes at least three people you’d like to
# invite to dinner. Then use your list to print a message to each person, inviting
# them to dinner.</h3>

# In[9]:


Invites=[]

for i in range(3):
    print("Guest No:",i + 1)
    
    Invites.append(input("Enter name of Invites :"))


# In[10]:


for i in Invites:
    print("Hi!",i,"I Am Inviting You For Dinner Tonight At My Home.")


# In[11]:


Not_Arriving=input("Enter the person who will not arrive :")
print(Not_Arriving,"Is unable to arrive for dinner")


# <h3>Q 4 (b) : You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.<br/></br><br/>
# •	 Start with your program from Q 4 (a). Add a print statement at the
# end of your program stating the name of the guest who can’t make it.<br/></br><br/>
# •	 Modify your list, replacing the name of the guest who can’t make it with
# the name of the new person you are inviting.<br/></br><br/>
# •	 Print a second set of invitation messages, one for each person who is still
# in your list.<br/></br><br/></h3>

# In[12]:


for i in range (0,len(Invites)):
    
    if (Invites[i] == Not_Arriving):
        
        Invites[i]=input("New Guest :")
    


# In[13]:


for i in Invites:
    print("Hi!",i,"I am Inviting you For Dinner Tonight At My Home.")


# In[ ]:





# <h3>Q 4 (c) : You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.<br/></br><br/>
# •	 Start with your program from Q 4 (a) and (b) Add a print
# statement to the end of your program informing people that you found a
# bigger dinner table.<br/></br><br/>
# •	 Use insert() to add one new guest to the beginning of your list.<br/></br><br/>
# •	 Use insert() to add one new guest to the middle of your list.<br/></br><br/>
# •	 Use append() to add one new guest to the end of your list.<br/></br><br/>
# •	 Print a new set of invitation messages, one for each person in your list.<br/></br><br/></h3>

# In[14]:


Guest=input("Add one more Guest :")
if Guest:
    Invites.insert(0,Guest)

Guest=input("Add one more Guest :")
if Guest:
    Invites.insert(2,Guest)

Guest=input("Add one more Guest :")
if Guest:
    Invites.append(Guest)


# In[15]:


print(Invites)


# In[16]:


for i in Invites:
    print("Hi!",i,"I Am Inviting you For Dinner Tonight At My Home.")


# <h5> Q 5 : Here you have some data in variable below, your task is to make a list of specific word Surah then print the list and length of list</h5>
# 

# In[17]:


Data="Sura I Who Believe In The UnSeen, Sura Are SteadFast In Prayer, And Spend Sura Out Of What We Have Provided For Them;"
Data=Data.split(" ")
New_List=[]

for i in Data:
    if(i == "Sura"):
        New_List.append("Sura")


# In[18]:


print(New_List)
print("No: of times Sura Appears :" ,len(New_List))


#  <h3>Q no 6 : You have some name of cities in list named cities, Your task is to check whether Karachi is present in this list or not, if present print the index where the value Karachi is present</h3>

# In[19]:


Index="Not Present"
Cities=["Islamabad","Lahore","Karachi","Multan","Rawalpindi","Faislabad"]

for i in range(0,len(Cities)):
    if (Cities[i] == "Karachi"):
       
        Index=i
    


# In[20]:


print(Index)


# In[ ]:




