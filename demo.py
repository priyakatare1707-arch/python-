    # number = int(input("enter a num :"))
    # if number >= 0:
    #     print ("positive")

    #     else:
    #         print("negetive")

    # print("helow world")
    # print('priya')
    # print('priya')
    # add in disnary we use-> update
    # marks={}
    # x=int(input("enter phy:"))
    # marks.update({"phy":x})
    # x=int(input("enter math:"))
    # marks.update({"math":x})
    # x=int(input("enter sin:"))
    # marks.update({"sin":x})
    # print(marks)

    # looop-> while/for--------------------
    # itration=>loop ka chaker lgana
    # itrator=> jish variable ki halpe se chakere lgaya


    # i=1            #print 1 to 100       
    # while i<=100:
    #     print(i)
    #     i+=1

    # i=100                   #print 100 to 1    
    # while i>=1:
    #     print(i)
    #     i-=1

    # n=int(input("enter a number"))         #multiple of n no.
    # i=1
    # while i<=10:
    #     print(n*i)
    #     i+=1



    # i=1                          # squ of 1 to 10    
    # while i<=10:
    #     print(i*i)
    #     i+=1

    # num=[1,4,9,16,25,36,49,64,81,100]
    # idx=0
    # while idx<len(num):
    #     print(num[idx])
    #     idx+=1

    # heros=['supermen','ironmen','aqamen','batmen','thor']                          # print the elment of list
    # i=0
    # while i<=len(heros):
    #         print(heros[i])
    #         i += 1


    # num=(1,4,9,16,25,36,49,64,81,100)                                   #    search number in tuple using loop
    # x=36
    # i=0
    # while i<len(num):
    #    if(num[i]==x):
    #     print("found at i:",i)
    #     i += 1
                                                                            
    #break->teminate loop while incounter------------------------
    #countinue->terminat exacution in the current itration ------------------------------
#     i = 0
# while i < 5:
#     if i == 3:
#         i += 1
#         continue
#     print(i)
#     i += 1

# --------------------------------------for if condition---------------------------------
# x=int(input("enter a value"))
# if x>10 :
#    print("grater")
# print("thank you")

# x=int(input("enter a value"))  run only true condition
# y=int(input("enter a value"))
# if x>=0  :
#     if y>=0 :
#        print(x+y)
# print("thank for visit")

# -------------------------------if else----------------------------------------------------------
# n=int(input("enter a number"))
# if n%2==0 :
#     print(f'given number{n} is even')
# else :
#     print(f'given number{n} is odd')  
#-------------------elif(self completed)-------------------------------------------
# x=int(input("enter a value"))
# if x>0 :
#     print(f' given number {x} is positive ')
# elif x<0 :
#      print("negetive")
# else :
#     print("zero")



# ----------------------indexing->always positive indexing(order of element in a ordered collection)-----------------------------------
# space->ascii value store 32 
# s= 'this' 'is' 'python'
# print(s.index('y'))
# s='THIS IS PYTHON'
# print(s.index('Y'))
# print(s.index('P',9)) #it give substring not found
# print(s.index('P',5,4)) 
# l=[10,20,'python','java']
# print(l.index('java'))
# -------------------------slice[start:stop:step/direction]--------------------------------------------------------------
# print(l[::])
# s='python'
# print(s[::-1])

# x=input("enter a number")
# print(x[::-1])
# print(x[::-2])
# s=(input("enter a number"))
# print(s[::-1])
# print(s[::-2])
# l=[10,20,30,40,50]
# print(l[1:2:5])
# print(l[2:-3:5])  #it give empity
# print(l[-1::-3])
# print(l[1:4:-1])#empity

#-----------------------------------------range(start,stop,jump/step) index collection--------------------------------------
#range(stop)
# x=range(10)
# print(x)
# print(list(x))
# x=range(-4,5,2)
# print(list(x))
# x=range(4,4)
# print(list(x))#empty
# x=range(1,10,-1)#empty
# print(list(x))
#-----------------------------------type casting(change one datatype to another datatype)------------------------------------
#charactor not change in int,float
# x=10.5
# y=int(x)
# print(y)
# z=float(y)
# print(z)
# a=complex(z)
# print(a)
# b=str(a)
# print(b)
# l=[10,20,30]
# t=tuple(l)
# print(t)
# l1=list(t)
# print(l1)
# st=set(l1)
# print(st)
# fs=frozenset(st)
# print(fs)
#-----------------------------------------print(sep='',end='/n')/n terminet new it is argument----------------------
# print("hellow",end=' ')
# print("world")
# print(10,20,30,sep=',')

#---------------------input give str in runtime-------------------------------------------
# x=input('enter a value')
# print(type(x),x)

# x=eval(input('enter a value'))
# print(type(x),x)
#------------------------logical-------------------------------------------------------
# x='python'
# y='java'
# print(x and y)#python return last value
# z=''
# print(x and z)
# # x=''
# # print(bool(''))
# x='a'
# print(bool('x'))
# s1=''
# s2=''
# print(s1 and s2)#space bcoz
# s1,s2='','python'
# print(s1 and s2)
# s1,s2='python',''
# print(s1 and s2)
# s1,s2='python','java'
# print(s1 and s2)
# s1,s2='python','java'
# print(s1 or s2)
# s1,s2='','python'
# print(s1 or s2)
# s1,s2='python',''
# print(s1 or s2)
# s1=''
# s2=''
# print(s1 or s2)
# x=''
# print(bool(''))
# x='a'
# print(not(bool('x')))
#which boolean value in string return false->empty
#which boolean value in integer return false->zero
# s='aeiouAEIOU'
# s1='p'
# print(s1 in s)
# s1='ae'
# print(s1 in s)
# s3='ea'#sequance metter
# print(s1 in s)
# s1= 'python'
# s2='java'
# print(s1 is s2)#in memory adress
# print(s1 == s2)#on value
# l=[10,20,'python','java']#it is hetrogeeous
# print(max(l))
# print(min(l))
# print(some(l))
# l=['python','java','phy']
# print(max(l))
# print(min(l))
#--------------------------function-----------------------
# print(some(l))#numeric value is nessesary some
#len(),type,id do not depent upon data type
# print(len(l))
# print(id(l))
# print(type(l))
#---------------------------list methode-------------------------------
# append()#add single element in last position
# copy()#create new element with same element
# clear()#clear all element in list
# index()#findout order/location of any element
# count()#findout freq of any element
# pop()#remove index targeted element(bydefoult it remove -1 index element)
# remove()#remove targeted element
# extend()#add multiple element at last position also it recoment collection
# insert()#add element in targeted element
# sort()#arrenge in assending order
# reverse()#reverse all element
#--------------------------immutable always creat new string-------------------------
# l=[2,4,6,2,'python']
# n=eval(input('enter a num'))
# print(l.append(n))
# print(l)
# n=eval(input('enter a num'))
# print(l.extend(n))
# print(l)
# n=eval(input('enter a num'))
# l.insert(0,n)
# print(l)
# l.clear()
# print(l,id(l))
# l.pop()
# print(l)
# l.pop(2)
# print(l.pop())

# print(l)
# l.remove(4)
# print(l)
# print(l.index('python'))
# print(l.count(2))
# l=[10,40,30]
# l.sort(reverse=True)
# l.reverse()
# print(l)
# x=10
# print(x,type(x),id(x))
# print(max(x))
# print(min(x)
# print(len(x))


# s='python programming'
# print(s.swapcase())
# print(s)#reason->string nature is immutable->bcoz object is different, addressis changed
# print(s.upper())
# print(s.lower())
# print(s.capitalize())
# print(s.title())
# print(s.index('y'))
# print(s.index('Y'))#SUBSTRING NOT FOUND
# index tells the position of any element
# print(s.find('s'))
# # print(s.count('p'))
# s1='python'
# s2='java'
# s3='php'

# s4=' '.join((s1,s2,s3))#we are giving list , bcoz join takes only one argument
# print(s4)
# a1='python'
# a2=10
# # a3=''.join['python',10]
# s='This is python class'
# # l=s.split()#by default it will split by space, how many times->till the time we have space
# # print(l)
# l=s.split('s')
# print(l)

# l=s.split('s',2)
# print(l)
# x='10'
# print(x.isdigit())#it will be useful in loops
# x1,x2='python','java'
# print(x1+x2)# + -> referred as concatenation
# # print(x1-x2)# - -> will give error
# print(x1*5)
# print(x1+x2,sep=',')#it will be s singl element so separator will not work
# print('a'>'A')#true
# print('Python'>'java')
# print('Python'>'Pava')
