#!/usr/bin/env python
# coding: utf-8

# In[1]:


person={"firstName":"sufyan","lastName":"shaikh","age":"23","city":"hydrabad"}
for key, value in person.items():
    print(key+":"+value)
person["qualification"]="inter_mediate"
for key, value in person.items():
    print(key+":"+value)
print("              update qualification")
person["qualification"]="gratuation"
for key, value in person.items():
    print(key+":"+value)


# In[2]:


cities = {
    "karachi":{
        "country":"pakistan",
        "population" :"14.9 million",
        "fact":"six biggest city in the world",
    },
    "lahore":{
        "country":"pakistan",
        "population":"1.09 million",
        "fact":" It is the capital of the province of Punjab. It is also known as the 'City of Gardens' ",
    },
    "islamabad":{
        "country":"pakistan",
        "population":"1.28millon",
        "fact":"slamabad Capital Territory Remarkable for its 16 local universities,",
    }
}
for citykey,cityinfo in cities.items():
    print(citykey)
    for city in cityinfo:
        print(city+":"+str(cityinfo[city]))


# In[ ]:


res="a"
while res!='n':
    age=int(input("enter your age :"))
    if age>12:
        print("ticket is 15$")
    elif age>=3:
        print("ticket is 10$")
    else:
        print("ticket is free")
        res=input("are you want to take ticket a/n :")


# In[3]:


def favorite_book(title):
    print(title)
book_title="Alice in  wonderland"
if(len(book_title)!=0):
    favorite_book(book_title)
else:
    print("please populate the book title")
    


# In[ ]:


import random
count = 0
while count < 3:
    guest=int(input("enter the guess number"))
    count += 1
    rand = random.randint(1,30)
    if guess == rand:
        print("you guess correct no")
    elif guess > rand:
        print("you guess highest number")
    elif guess < rand:
        print("you guess lower number")
    print("computer is guess number :",rand)
    


# In[ ]:





# In[ ]:




