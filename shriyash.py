#!/usr/bin/env python
# coding: utf-8

# In[1]:


sales = [5000, 7000, 8000, 6500, 7200, 9000, 8500]
highest_sales = max(sales)
lowest_sales = min(sales)
print("Highest Sales:", highest_sales)
print("Lowest Sales:", lowest_sales)


# In[2]:


import numpy as np
sales_data = np.array([1000, 1200, 1500, 1800, 2000, 2100, 2500, 2700])
sales_data_2d = sales_data.reshape(4, 2)
print(sales_data_2d)


# In[3]:


bal = 0
i=0
while i!=4:
  print("\n1. Check Balance")
  print("2. Deposit Money")
  print("3. Withdral Money")
  print("4. Exit")
  i=int(input("\nEnter operation: "))

  if i==1:
    print("Total Balance: ", bal)
  elif i==2:
    add_amt=int(input("Enter Deposit Amount: "))
    print("Amount to be deposited: ", add_amt)
    bal+=add_amt
    print("Amount deposited successfully! \nTotal Balance: ",bal)
  elif i==3:
    with_amt=int(input("Enter Withdrawal Amount: "))
    if with_amt > bal:
      print("Insufficient Balance!")
    else:
      bal-=with_amt
      print("Amount withdrawal successfully! \nTotal Balance: ",bal)
  elif i==4:
      print("Thank you!")
      break
  else:
    print("Invalid Operation")


# In[4]:


passengers,sum=0,0;
for i in range(1,6):
  passengers = int(input(f"Enter Number of Passengers at {i}: "))
  sum+=passengers

print("Total Passengers: ", sum)


# In[5]:


attempt=3
for i in range(1,4):
  pin=int(input("Enter PIN: "))
  if pin==1234:
    attempt -= 1
    if attempt == 0:
        
      print("Granted")
  else:
    print("Denied")
    break


# In[6]:


# 6. Reverse a Number
num = int(input("Enter Number: "))
rev = 0

while num > 0:
    digit = num % 10
    rev = (rev * 10) + digit
    num //= 10

print(rev)


# In[7]:


# 7. ATM Cash Dispensing Machine
amt=int(input("Enter Amount: "))
notes_2000 = amt // 2000
amt = amt % 2000
notes_500 = amt // 500

print("Notes of 2000rs: ",notes_2000)
print("Notes of 500rs: ",notes_500)


# In[ ]:




