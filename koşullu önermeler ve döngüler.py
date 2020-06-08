#!/usr/bin/env python
# coding: utf-8

# ## koşullu ifadeler ve döngüler

# # 1. santigrat ve fahrenayt dönüşümü

# In[6]:


x = input("F or C ?:").upper()

while not (x == "F" or x == "C"):
    if x != "F" or x != "C":
        print("Yanlis değer girdiniz")
        x = input("F or C ?:").upper()

y = int(input("sicaklık ölçüsünü giriniz"))

if x == "F":
    C = (5/9) *(y-32)
    print(y," fahrenayt sıcaklığı için hesaplanan  {:.1f} santigrat derecedir".format(C))
else :
    F = (9/5)*y + 32
    print(y," santigrat sıcaklığı için hesaplanan  {:.1f} fahrenayt derecedir".format(F))


# # 2 kelimenin tersi

# In[7]:


z = input( "lütfen tersine çevirmek istediğiniz bir isim giriniz:")

t = " "

#print ( "z nin tersi :", z[::-1])
for i in range(len(z)-1,-1,-1):
    t += z[i]
    
print(t)


    


    


# # 3 fibonacci

# In[1]:


s1 = 1
s2 = 1
f = [s1,s2]
while s2 <= 50:
    s1,s2 = s2,s1+s2
    f.append(s2)
f
    
    
    


# # 4 çarpım tablosu

# In[3]:


q=int(input("bir rakam giriniz "))
i=1
while i < 11:
    print (q, " * ", i , " = " ,q*i )
    i += 1
    


# # 5 list comprehension

# In[5]:


p = [x**3 if x%2==0 else x**2 for x in range(1,20)]
p


# In[ ]:




