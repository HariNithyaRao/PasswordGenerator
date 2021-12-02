import random
caps=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num=[i  for i in range(10)]
symbol=["@","#","~","&","$","/","`",".",",",":","'"]
names=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
n=int(input("enter the length of password:"))
while n<8:
    print("password should should contain atleast 8 characters")
    n=int(input("enter the length of password:"))   
def password():
     count =1
     list1=[]
     while count<=n:
         if count%4==1:
                k=str(random.choice(caps))
                list1.append(k)
         elif count%4==2:
                l=str(random.choice(num))
                list1.append(l)
         elif count%4==3:
                m=str(random.choice(symbol))
                list1.append(m)
         elif count%4==0:
                o=str(random.choice(names))
                list1.append(o)
         count+=1
     key="".join(list1)
     print(key)
     save_it=str(input("do you want to save it (yes or no)?:"))
     list_of_keys=[]
     if save_it=="yes":
         list_of_keys.append(key)
         print("your pasword has been saved")
     else:
     	print("generating another password")
     	password()
     gen_new=str(input("do you want to generate another password?(yes/no)"))
     if gen_new=="yes":
         password()
     show=str(input("do you want to view all the saved passwords?(yes/no):"))
     if show=="yes":
     	for i in range(len(list_of_keys)):
        	print(list_of_keys[i])
if n>=8:
    password()
    
