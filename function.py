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

def natural_num(n):
    count=0
    for i in range(1,n+1):
        if n % i==0:
            count+=1
    if count > 2:
        return ' Not prime'
    else:
        return 'prime'
           
n=int(input('enter a num'))
res=natural_num(n)
print(res)
def natural_num(n):
    count=0
    for i in range(1,n+1):
        if n % i==0:
            count+=1
    if count > 2:
        return ' Not prime'
    else:
        return 'prime'
           
n=int(input('enter a num'))
res=natural_num(n)
print(res)




