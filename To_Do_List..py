#!/usr/bin/env python
# coding: utf-8

# In[3]:


To_Do_list=[]
flag = True #flag is used in commands to modify their execution.

while flag:
    User_Input = input("Enter start to execute To_Do_list: ")
    if User_Input == "start":
        Append_tasks = input("Enter task that suits you: ")
        To_Do_list.append(Append_tasks)
        print(To_Do_list)
    
    User_Input2 = input("Enter delete to remove a task from the list: ")
    if User_Input2 == "delete":
        Delete_tasks = input("Enter task that you like you remove: ")
        To_Do_list.remove(Delete_tasks)
        print(To_Do_list)
    
    User_Input3 = input("Enter finish to close the list: ")
    if User_Input3 == "finish":
        flag = False # Here flag is stated false which means at this stage the modification is finished so the list will close.
    else:
        print("Your input is not acceptible")


# In[ ]:





# In[ ]:




