#jiske argument me hum function dete hai that is higher order arrgument
# iterable-> collection
# l1=[1,2,3,4]
# l2=[5,6,7,8]
# l3=[3,2,4,1]
# def add(x,y,z):
#     return x+y+z
# res=map( add,l1,l2,l3)
# print(res)#-->map object
# print(list(res))

# l1=[1,2,3,4,5]
# l2=[5,6,7,8]
# l3=[3,2,4]
# def add(x,y,z):
#     return x+y+z
# res=map( add,l1,l2,l3)
# print(res)#-->map object
# print(list(res))#------total number of input equal to total number of output--------------------------------------------
    
#----------------------------------square of element-------------------------------------------------------------
# l1=[1,2,3,4,5]
# def squar(n):
#     return n**2
# res=map(squar,l1)
# print(tuple(res))

#----------------------------------squareroot of element-------------------------------------------------------------
# l1=[1,2,3,4,5]
# def squar(n):
#     return n**0.5
# res=map(squar,l1)
# print(tuple(res))
#---------------------------------------------filter----------------------------------------------------------------------
# l1=[1,2,3,4,5]#grater num
# def greater3(n):
#     if n>=3:
#         return n 
# res= filter(greater3,l1)
# print(list(res)) 

# l1=[1,2,3,4,5]#small num
# def greater3(n):
#     if n<=3:
#         return n 
# res= filter(greater3,l1)
# print(list(res))

# l1=[1,2,3,4,5]# even num
# def greater3(n):
#     if n%2==0:
#         return n 
# res= filter(greater3,l1)
# print(list(res)) 

# l1=[1,2,3,4,5]# odd num
# def greater3(n):
#     if n%2!=0:
#         return n 
# res= filter(greater3,l1)
# print(list(res))