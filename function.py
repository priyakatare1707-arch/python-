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



# def decore(fun):
#     def inner(x,y):#x=10 y=50 div 0.sumthing it give 0 remove decial value
#         print(x//y)#---
#     return inner

# @ decore
# def even(x,y):
    
#         print(x*y)
# x=int(input('enter a num'))
# y=int(input('enter a num'))
# even(x,y)

#add -->sub
#mul-->div
#---------------------------------------------opps-----------------------------------------------------------------------------
# class stud:
#     x=10
#     y=20
# obj=stud#--------------->internal constructor
# obj1=stud()#--------------->external constructor(initial informetion-->constructor)
# print(id(obj),id(obj1))
# #-------------------------------------(constructor)special tyoe if method that we dosent want to call(we can call extarnal)
# #how many constractor you made in class--->n number
# class stud:
#     def__init__(self):#----that can hold current class ka current object
#         print('constructor calls')
#         print(id(self))
#     def__init__(self):#----that can hold current object information
#         print('hellow')
# obj=stud#--------------->internal constructor
# obj1=stud()#--------------->external constructor(initial informetion-->constructor)
# print(id(obj))
# obj1__init__()




# class stud:
#     school = 'hss'
#     school_city = 'bhopal'

#     def detail(self):
#         print('from stud class')

# obj = stud()
# print(obj.school, stud.school)
# print(obj.school, stud.school_city)
# obj.detail()
# --------------------------------------------jiska parameter self hai vo instance method hai

# class stud:
#     def __init__(self,name,age,grad):
#         self_n=name
#         self_a=age
#         self_g=grad
# obj = stud('priya',23,'b.tech')

# class stud:
#     def __init__(self,name,age,grad):
#         self.n=name
#         self.a=age
#         self.g=grad
#     def display(self):
#         print(self.n,self.a,self.g)
# obj = stud('priya',23,'b.tech')
# obj.display()
#
#-------------------------------------------------variable-------------------------------------------------------------
# instance variable-->object dependent veriable(if changing object change variable)
#decaleration
#--------------------inside class
# 1.inside conductor
# 2.inside instance method
#outside class
#calling
#-------------------inside class
# 1.inside conductor
# 2.inside instance method
#outside class



# class stud:
#     def __init__(self,name,contact):
#         self.n=name  
#         self.c=contact #     decaleration
#         print(self.n,self.c)# calling inside constructor
#     def add_new(self,roll_no):
#         self.r=roll_no  #  decaleration
#     def display (self):  #  calling inside instance method
#         print(self.c,self.n,self.r,self.email)
# obj=stud('priya',123)
# obj.add_new(101)  # declearection inside instance method
# obj.email='priya@gmail.com'  #  declearection outside of class
# obj.display()
# print(obj.c,obj.n,obj.r,obj.email)  # calling outside of class                     
# #class variable-->object dependent class(object notdepending on  veriable)
# #--------------------------------------- instance of class is called object
# print(obj.n)
# obj2=stud('rahul',145)
# print(obj2)
#oops,class,localvariable,
# instence method

#------------------------------------class method-----------------------------------------------------------------------------------

# class stud:
#     grad='10th'
#     def __init__(self,name,roll_no):
#         self.n=name
#         self.r=roll_no
#     @classmethod
#     def update(cls,new):
#         cls.grad=new
# obj1=stud('priya',1234)
# print(stud().grad)
# obj1update('11th')
# print(stud.grad)

# class stud:
#     grad='10th'
#     def __init__(self,name,roll_no):
#         self.n=name
#         self.r=roll_no
#     @classmethod             #------------------update-------------------------------------
#     def update(cls,new):
#         cls.grad=new
#     @classmethod
#     def add_new(cls,add):
#         cls.code=add
# obj=stud('priya',1234)

# obj.add_new(123)
# print(stud.code)
#-------------------------------------------------static method---------------------------------------------------------------
# class stud:
#     def __init__(self,roll_no):
#         self.n=roll_no
#     @staticmethod
#     def greet(name):
#         print(f'welcome{name} to my web page')

# obj=stud('priya')
# x=obj.n 
# obj.greet(x)
# class object self variable method

# properties:-
# :for data protection
# adstraction
# incapsulation
# :for code reuseable
# inheritance
# polymorphism

# :in abstraction
# 1.abstract class
# 2.abstract method
# 3.concret method

# :encapsulation->access specifier/method(it is not supported in python)
# 1.public
# 2.protected
# 3.private

# :inheritance
# 1.type
# 2.method overritding
# 3.mro
# 4.super()

# :polymorphism
# 1.type
# ->compile time
# ->rantime
# 2.overload

#------------------------------------------inheritance(child direct excess parent proparty)
# class parent:
#     x=10
#     def home(self):
#         print('from your parent class')
# class child(parent):
#     pass
# obj=child()
# print(obj.x)
# obj.home()

# --------------------type:-
# 1.single_level
# parent
#     |
# # child
# # 2.multiple_level
# # grantparent
#      |
# # parent
#      |
# # child
# # 3.multiple
# # parent1,parent2
#     |
# # child
# # 4.hierachical
# # parent
#      |
# # child1,child2
#hybrid
#  parent
#      |
# # child1,child2
#        |
# #subchild

# 1.single_level

# class parent:          #method overriding
#     x=10
#     def home(self):
#         print('from your parent class')
# class child(parent):
#     def home(self):
#         print('from your child class')
#         super().home()
# obj= child()
# obj.home()
# child se parent ki property udhana and class same ho to super() method use karte hai

# 2.multiple_level
# class grandparent:          #method overriding
#     x=10
#     def home(self):
#         print(' home from grand parent')
# class parent(grandparent):
#     def home(self):
#         print(' call from  parent class')
#         super().home()
# class child(parent):
#     def home(self):
#         print('home from child')
        # super().home()
# obj= child()
# obj.home()   

#  3.multiple
# class father:          #method overriding
#     x=10
#     def home(self):
#         print(' home from father')
#         mother.home(self)
# class mother:          #method overriding
#     def home(self):
#         print(' home from mother')
# class child(father,mother):    #mro->method resolution object      
#     x=10
#     def home(self):
#         print(' home from child')
#         super().home()
# obj= child()
# obj.home()   

# hybrid-inheritance(having multiple child->)
# class a:
#     def home(self):
#         print('from class a')
        
# class b(a):
#     def home(self):
#         print('from class b')
#         c.home(self)
# class c(a):
#     def home(self):
#         print('from class c')
#         super().home()
# class d(b,c):
#     pass
# obj= d()
# obj.home() 

# -----------------------------------------------abstrection(protecting data the data)--------------------------------------------
# abstract class
# abstract method
# concrete method
# from abc import ABC , abstractmethod
# class A(ABC):
#     def desboard(self):
#         print('welcome to desboard')
#     @abstractmethod
#     def login (self):
#         pass
# class B(A):
#     def login(self):
#         print('login successfully')
# obj=B()
# obj.desboard()
# obj.login()
#protect perent class with inheritance

# class hold variable and method 
#------------------------------------------------incapsulation----------------------------------------------------------------
#to wrap variable and methoid in single unit is incapsulation
#   access specification/modifier(it is in opps consept but not in python)
#public-->(x,add())access in inside outside and child class


#-----------------------------------publice variable and method( vaeiable use inside class, outsideclass and child class)---------------------------------------------------
# class a:
#     x=10
#     def show (self):
#         print("from class a")
#         # print(a.x)
# class b(a):
#     pass
# obj=b()
# print(obj.x)
# obj.show()
# print(a.x)
# print(a.show(10))

#----------------------------------------protected variable not python supported(accessable only child class not ouside)----------------------------------------------------
# class a:
#     x=10
#     def _show (self):
#         print("from class a")
#         # print(a._x)
# class b(a):
#     pass
# obj=b()
# print(obj._x)
# obj._show()
# print(a._x)
# print(a._show(10))
#-----------------------private--------------------------------------------
class a:
    x=10
    def __show (self):
        print("from class a")
        # print(a.__x)
class b(a):
    pass
obj=b()
print(obj.__x)
obj.__show()
print(a.__x)
print(a.__show(10))

# class a:
#     x=10
#     def __show (self):
#         print("from class a")
#         print(a.__x)
# class b(a):
#     pass
# obj=b()
# print(dir(a))
# # print (obj._a__x)

# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__',
#  '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', 
#  '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
#   '__static_attributes__', '__str__', '__subclasshook__', '__weakref__', '_a__show', 'x']
# name megling-->name ko change kare dusare name store karne
class a:
    __x=10
    def __show (self):
        print("from class a")
        print(a.__x)
class b(a):
    pass
obj=b()
print(dir(a))
# print (obj._a__x)



# mro method resolution object who came fist
























#  constructor it call outometicaly by making object
# current becouse over load bysame constructor
# ild value lekar bahar nikal jata hai not terminet 
# return terminet withb data
# self current object ki identity hold karta hai