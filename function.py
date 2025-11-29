#----------------------function (remove the repeatation of loop)----------------------------------------------
# def function name(parameter):}->reguired variable in function body(optional)
#         fun-body
#         return(optional)
# ---------------------------------------------------------------------------------------
#  fun_name(argument)->value agains parameter(optional)
#----------------------------------without argument without return------------------------------
# def x ():
#         print('hellow')
#         
# x()
# p=int(input('enter a num'))
# q=int(input('enter a num'))
# def add(x,y):
#      print(x+y) #7 is print 
     
# res=add(p,q)
# print(res)# -----it print none bcs it has by defoult return none--------------
#-----------------------with argument with return-------------------------
# p=int(input('enter a num'))
# q=int(input('enter a num'))
# def add(x,y):
#      z=x+y #7 is print 
#      return z
# res=add(p,q)
# print(res)


# print(print('hellow'))#--->it is inbuild fun we need return
#---------------------------with argument without  return--------------------------
# def add(x,y):
#      print(x+y) #7 is print 
# p=int(input('enter a num'))
# q=int(input('enter a num'))
# # add(p,q)
# print(add(p,q))
#-------------------------without argument without  return-----------------------
# def give_number():
#     return 10

# x = give_number()
# print(x)

# def add(x,y):
#      return 
# p=int(input('enter a num'))
# q=int(input('enter a num'))
# add(p,q)
# print(add(p,q))
# #return value depend on function
#---------------------------------------------------key ward argument----------------------------------------------------------------
# def fan_name(x,y,z):
#     print(z)
#     print(y)
#     print(x)
# p=int(input('enter a num'))
# q=int(input('enter a num'))
# r=int(input('enter a num'))
# fan_name(z=p,y=q,x=r)
#-------------------------------------------------default key ward argument---------------------------------
# def fan_name(x=0,y=0,z=0):
#     print(z)
#     print(y)
#     print(x)
# p=int(input('enter a num'))
# q=int(input('enter a num'))
# r=int(input('enter a num'))
# fan_name()
# fan_name(z=p)
# fan_name(z=p,x=r)
#---------------------------------------------------------vaeiable length key ward argument---------------------------------------------
# def fan_name(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
   
# fan_name(x=10,y=20,z=30,p=2,q=5)

# def fan_name(**kwargs):#--->paking
#     print(kwargs)
#     print(type(kwargs))
   
# fan_name(**eval(input("enter any dic:")))#--->unpaking
#     print(kwargs)

# def fan_name(**kwargs):
#     for i in kwargs.keys():
#        print(i)
#     for i in kwargs.values():
#         print(i)
#     for i,j in kwargs.items():
#         print('key=',i,'value=',j)
# fan_name(**eval(input("enter any dic:")))

# key= x value= 10
# key= y value= 30


# def fan_name(x,y=0,*z,p,**q):
#     print(x)
#     print(y)
#     print(z)
#     print(p)
#     print(q)
# fan_name(10,20,30,40,50,p=5,r=2,s=1,t=3)

# def fan_name(x,y=0,*z,p,**q):
#     print(x)
#     print(y)
#     print(z)
#     print(p)
#     print(q)
# fan_name(10,p=5,20,30,40,50,r=2,s=1,t=3)

# def natural_num(n):
#     sum=0
#     for i in range(1,n+1):
#         sum+=i
#     print(sum)   
# n=int(input('enter a num'))
# natural_num(n)

# def natural_num(n):
    
#     for i in range(1,n+1):
#         if i%2==0:
#            print(i)   
# n=int(input('enter a num'))
# natural_num(n)

# def natural_num(n):
#     count=0
#     for i in range(1,n+1):
#         if n % i==0:
#             count+=1
#     if count > 2:
#         return ' Not prime'
#     else:
#         return 'prime'

# while (true):
#     print('1.add/n','2.sub/n','3.div/n','4.mul/n','5.Exit')
#     n=int(input('please enter a abave value'))
#     if n in (1,2,3,4,5):
#         if n in (1,2,3,4):
#             if n == 1:
#                 nummber=int(input('how many number you want to add:'))

#                 l=[]
#                 for i in range(1,n+1):
#                    value= int(input(f'enter{i}number'))
#                    l.append(value)
#                 sum=0
#                 for i in l:
#                    sum+=i
#                 print (f'addition of {l}is {sum}')
#         else:
#             brack
#     else:
    #-------------------------------who have no name anonemas(lambda function)--------------------------------------
#  use only for loop never while loop
# x=lambda x,y,z:2*x+y+z

# print(x(1,2,3))
#syntex
# lambda x,y :if result if condition else else_result

# x=lambda x,y :x if x>y else y
# print(x(5,10))
#------------------------------------------age condition---------------------------------------------------------
# x=lambda age:'child' if 0<age<18 else ('adult' if 18<age<60 else ('senier' if 59<age else 'invelide age'))
# age=int(input('enter age'))
# print(x(age))
 #-------------------------------------------even---------------------------------------------------   
# x=lambda n: 'even' if n%2==0 else None# not use pass bcause it use for block work
# n=int(input('enter a num'))
# print(x(n))
#---------------------------------------square---------------------------------------------------
# x=lambda n: n**2
# n=int(input('enter a num'))
# print(x(n))

#---------------------------------------squar root-----------------------------------------------
# x=lambda n: n**0.5
# n=int(input('enter a num'))
# print(x(n))
#------------------------------collection of natural num--------------------------------------------
#output-->i
# n=10
# x=lambda n : [i for i in range(1,n+1)]
# print(x(n))
#----------------------------list of even---------------------------------------------------------------
# n=10
# x=lambda n : [i for i in range(1,n+1) if i%2==0]
# print(x(n))
#------------------------------------(map with lambda)------------------------------------------------------
# l=[1,2,3,4,5]
# print(list(map(lambda n: n**2,l)))#---------------(l itrable)---------------------

# l1=[1,2,3,4,5]
# l2=[6,7,8,9,10]
# l3=[11,12,13,14,15]
# print(list(map(lambda x,y,z : x+y+z ,l1,l2,l3)))

# l1=[1,2,3,4,5]
# l2=[6,7,8,9,10]
# l3=[11,12,13,14,15]
# print(list(map(lambda x,y,z : x-y-z ,l1,l2,l3)))

# l1=[1,2,3,4,5]
# l2=[6,7,8,9,10]
# l3=[11,12,13,14,15]
# print(list(map(lambda x,y,z : x*y*z ,l1,l2,l3)))
#---------------------squar root sum----------------------------------------
# l1=[1,2,3,4,5]
# l2=[6,7,8,9,10]
# l3=[11,12,13,14,15]
# print(list(map(lambda x,y,z : x**0.5+y**0.5+z**0.5 ,l1,l2,l3)))
#-----------------------------even by filter---------------------------
# l1=[1,2,3,4,5]
# print(list(filter(lambda x : x if x%2==0 else None,l1)))
#-----------------------------------sum by reduse------------------------------------------------
# import functools
# l1=[1,2,3,4,5]
# print((functools.reduce(lambda x,y : x+y,l1 )))#we didnot use list bcz it return single value

# def decore (fun):
#     def inner():
#         fun()
#     return inner
# def add():
#     print('hellow')
# res = decore(add)
# print(res)
# res()

# def decore (fun):
#     def inner(p,q):#p=10,q=20
#         p=p+5       #p=15,q=40
#         q=q*2
#         fun(p,q)
#     return inner
# def add(x,y):  #x=15,y=40
#     print(x+y) #55
# res = decore(add)
# print(res)
# res(10,20)
#-----------------------------------------decoretor( without changing theinternal function  modify code )-------------------------
# def decore (fun):
#     def inner(p,q):#p=10,q=20
#         p=p+5       #p=15,q=40
#         q=q*2
#         fun(p,q)
#     return inner
# @decore  # xand y ki value pass kar rha hai fun me
# def add(x,y):  #x=15,y=40
#     print(x+y) #55

# add(10,20)

# def first(fun): #--------------------------give welcome-----------------------------------
#     def inner():
#         print('welcome')
#     return inner
# @ first 
# def great():  
#     print('hellow') 
# great()
# -----------------------------even by def-------------------------------------------------
# n=10
# def even(n):
#     for i in range(1,n+1):
#         print(2*i)
# even(n)

#-------------------------------------even return odd-----------------------------------------
# def decore(fun):
#     def inner(x):
#         for i in range(1,x+1):
#              print(2*i-1)
#     return inner

# @ decore
# def even(n):
#     for i in range(1,n+1):
#         print(2*i)
# n=int(input('enter a num'))
# even(n)

# def decore(fun):
#     def inner(x,y):
#         print(x-y)
#     return inner

# @ decore
# def even(x,y):
    
#         print(x+y)
# x=int(input('enter a num'))
# y=int(input('enter a num'))
# even(x,y)

# def decore(fun):
#     def inner(x,y):
#         print(x+y)
#     return inner

# @ decore
# def even(x,y):
    
#         print(x-y)
# x=int(input('enter a num'))
# y=int(input('enter a num'))
# even(x,y)

#-------------------------use return--------------------------------------------------------
# def decore(fun):
#     def inner(x,y):
#         return(x+y)
#     return inner

# @ decore
# def even(x,y):
    
#         return(x-y)
# x=int(input('enter a num'))
# y=int(input('enter a num'))
# print(even(x,y))



def decore(fun):
    def inner(x,y):#x=10 y=50 div 0.sumthing it give 0 remove decial value
        print(x//y)#---
    return inner

@ decore
def even(x,y):
    
        print(x*y)
x=int(input('enter a num'))
y=int(input('enter a num'))
even(x,y)

#add -->sub
#mul-->div