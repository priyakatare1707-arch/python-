# n=int(input('enter a num'))
# if n>1:
#       print(f'given num{n} is +ve')

# n=int(input('entera num'))
# if n>=1:
#     print(f'given num{n} is +ve')
# else:
#     print(f'given num{n} is -ve or zero')

#------------------------if elif-----------(block may be executed)---------------------------------------------
# n=int(input('entera num'))
# if n>=1:
#     print(f'given num{n} is +ve')
# elif n==0:
#      print(f'given num{n} is -ve or zero')


#----------------------if elif else(block must be executed)--------------------------------------------------------
# n=int(input('entera num'))
# if n>=1:
#     print(f'given num{n} is +ve')
# elif n==0:
#      print(f'given num{n} is  zero')
# else:
#     print(f'given num{n} is -ve ')
#---------------------------------------age of child,adult,odd in limit-------------------------------------------------
# age=int(input('enter your age'))
# if 0<age<17:
#     print("child")
# elif 17<age<60:
#     print("adult")
# elif 59<age<100:
#     print("odd")
# else:
#     print('invelid')
#----------------------------------averege and gread ------------------------------------------------------
# h=int(input('enter a marks'))
# if 0 < h < 100:
#     e=int(input('enter a marks'))
#     if 0<e<100:
#         m=int(input('enter a marks'))
#         if 0 < e < 100:
#             avg = ((h + e + m) / 3)
#             if 0 < avg <= 34:
#                 print('fail')
#             elif 35 < avg <  44:
#                 print ('3rd divition')


#             elif 45 < avg < 59:
#                 print ('2rd divition')

#             else:
#                 print('1st divition')

#         else:
#             print=(f'invelid')
   
#     else:
#         print=(f'invelid')
# else:
#     print (f'given mark{h}is invelid')
#-------------------------------------------pelindrom---------------------------------------------------------------------
# n=input ('enter row')
# v=(n[::-1])

# if n == v:
#     print('palindrom')
# else:
#     print('not palindrom')

#------------------------------------------loop to avoid repeatetion of same block------------------------------------------------

# syntex ->for i in iterable
# s=str(input(' a value'))
# for i in s:
#       print(i)

# l=[1,2,3,4]
# for i in l:
#       print(i)

# l=[1,2,3,4]
# for i in l:
#       print(i+5)

# t=(1,2,3,'python') 
# for i in t:
#       print(i)   

# t={'x':1,'y':2,'z':'python'} # give keys x,y,z
# for i in t:
#       print(i)   

# d={'x':1,'y':2,'z':'python'}
# for i in d:
#       print(i,'=',d[i])      

 
# s=input('enter your name') 
# s=s.lower()
# v,c=0,0
# for i in s:
#       if i in ('a','e','o','i','u'):
#          v=v+1
#       elif i=='':
#             pass
#       else:
#             c=c+1
# print('v=',v) 


# s=input('enter any string:')
# s=s.replace(' ','')
# # print(s)
# if s.isalpha():
#       print('alphabet')
# else:
#       print('not alpha')

# s=input('enter any string:')
# s=s.replace(' ','')
# v=c=0
# if s.isalpha():
#       s=s.lower()
#       for i in s:
#             if i in ('a','e','o','i','u'):
#                   v=v+1
           
#             else:
#                c=c+1
#       print('v=',v)
#       print('c',c) 
# else:

#       print('please inter alphabet')

#-------------------------------for n natural number-----------------------

# n=int(input('enter value'))
# for i in range(1,n+1):
#     print(i,end=' ,')



# n=int(input('enter value'))#------------------------------for n natural number in horizontal--------------------

# for i in range(1,n+1):
#       if i<n:
#             print(i,end=' ,')
#       else:
#             print(i)

#--------------------sum of natural number-------------------

# n=int(input('enter value'))
# sum=0
# for i in range(1,n+1):

#       sum=sum+i
#       if i<n:
#             print(i,end=' ,')

#       else:
#             print(i,end=' =')
# print(sum) 
#------------------------------two ka table-------------------------------------------------------------   
# n=int(input('enter value'))
# for i in range(1,n+1):
#   print(i*2)
# #-----------------------two ka tabble in horizontal--------------------------------------------------------
# n=int(input('enter value'))
# for i in range(1,n+1):
#     if i<n:
#         print(i,end=' ')
#     else:
#         print(i*2)

#----------------------------------------------sum of even-------------------------------------
# n=int(input('enter value'))#horizontal
# sum=0
# for i in range(1,n+1):
#       sum=sum+2*i
#       if i<n:
#           print(i*2,end='+')
#       else:
#             print(i*2,end='=')
# print(sum)


#----------------------------------------------sum of n odd num-----------------------------
# n=int(input('enter value'))
# sum=0
# for i in range(1,n+1):
#       sum=sum+(2*i-1)
#       if i<n:
#           print((i*2-1),end='+')
#       else:
#             print((i*2-1),end='=')
# print(sum)



# #-------------------------------------------even sum in range--------------------------------------------
# n=int(input('enter value'))#------there is a problem if i give odd it didnot give (=)--------------
# sum=0
# for i in range(2,n+1,2):
#     sum=sum+i
#     if i<n:
#       print(i,end="+")
#     else:
#         print(i,end="=")
        
# print(sum)

# n=int(input('enter value'))# it give (=)
# sum=0

# last_even = n if n%2==0 else n-1

# for i in range(2, n+1, 2):
#     sum += i
#     if i < last_even:
#         print(i, end="+")
#     else:
#         print(i, end="=")

# print(sum)

#--------------------------------------odd sum in range-------------------------------------------------------------

# n=int(input('enter value'))# it give (=)
# sum=0

# last_odd = n if n%2!=0 else n-1

# for i in range(1, n+1, 2):
#     sum += i
#     if i < last_odd:
#         print(i, end="+")
#     else:
#         print(i, end="=")

# print(sum)
#-------------------------------------------------------prime number-----------------------------------




# start = int(input("Enter start value: "))
# end = int(input("Enter end value: "))

# print("Prime numbers in range:", end=" ")
# for num in range(start, end+1):
#     if num > 1:
#         is_prime = True
#         for i in range(2, num):
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             print(num, end=" ")
#-----------------------------------------pelemdrom----------------------------------------------
# n=input('enter value')
# if n==n[::-1]:
#   print(pelindrom)
# else:
#     print(not pelindrom)
#------------------------------reverse without slice---------------------------------------------------
# s='python'
# s1=''
# for i in s:
#   s1= i+s1 
#print(s1)
#------------------------factor--------------------------------------------------------------
# n=int(input('enter value'))
# i,l=2,[]
# while i<n:
#     if n%i==0:
#         l.append(i)
#     i=i+1
# print(l)
#--------------------------------------factorial--------------------------------------------------------
# n=int(input('enter value'))#horizontal
# mul=1
# for i in range(1,n+1):
#       mul*=i
#       if i<n:
#           print(i,end='*')
#       else:
#             print(i,end='=')
# print(mul)

# n=int(input('enter value'))
# temp=n
# sum=0
# while temp>0:
#       digit=temp%10
#       sum+=digit
#       temp=temp//10
# print(sum)



# temp=n
# rev=0
# while n!=0:
#     digit=n%10
#     rev=rev*10+digit
#     n=n//10
# if temp == rev:
#     print("Palindrome number")
# else:
#     print("Not palindrome")
#---------------------------------------armstong------------------------------------------
# n=int(input('enter value'))
# m=p=n
# td=sum=0
# while n>0:
#     td=td+1
#     n=n//10
# while m>0:
#     ld=m%10
#     sum += ld**td
#     m=m//10
# if p== sum:
#     print('armstong')
# else:
#     print('not armsdtong')

#--------------------------------------while loop------------------------------------
# n=int(input('enter a num'))
# i=1
# while i<n:
#     print(i,end='')
#     i +=1
#-----------------------------------lenth of input-------------------------------------------
# n=int(input('enter a num'))
# td=0
# while n>0:
#     td=td+1
#     n=n//10
# print("total digit",td)
#---------------------------------for loop is use for collection of caractor---------------------------


#-------------------------------------transfer statment-----------------------------------------
# n=int(input('enter a num'))
# i=1
# while i<n:
#     if i==5:
#         print('hellow')
#         i +=1
#         continue#--------------skip before itaretion for current stetment(it skip only continue statment amd continue for more)
#     else:
#         print(i)
#     i+=1

# n=int(input('enter a num'))# it make infinit loop because it does not increase (i+=1)so the condition when setisfy  it skip the below step and because of no inc. of num it start with five again it not change start with five)
# i=1
# while i<=n:
#     if i==5:
       
#        continue
#     else:
#         print(i)
#         i+=1

# n=int(input('enter a num'))
# i=1
# while i<=n:
#     if i==5:
#        print('okk')
#        break#-------after break teminet loop no execution after that---------
#     else:
#         print(i)
#     i +=1
#indentetion error space se ati hai 
#------------------------------------------------pass-----------------------------------------------------------------------------
# print('hellow')
# x=10
# if x%2==0:
#     pass
# print()  

# n=int(input('enter a num'))
# i=1
# while i<n:
#     if i==5:
#         pass# it not give error pass it and  not print
#     else:
#         print(i)
#     i+=1



# def print1_to_10():#-------------------------it give zero return turminet after 0------------------
#         li=[]
#         for i in range(11):
#             li.append(i)
#         return li
# # num=int(input('enter a num'))
# answer=print1_to_10 ()
# print(answer)

#--------------------------------------------------fibonachi------------------------------------------------------------------
# fi=0
# se=1
# print(fi,se,end=" ")
# n=int(input('enter a num'))
# for i in range(n-2):

#         next=fi+se
#         fi=se
#         se=next
#         print(next)

# n=int(input('enter a num'))
# fi=0
# se=1
# for i in range(n):
#         print(fi,end=' ')
#         fi,se=se,fi+se
#--------------------------------------prime num-------------------------------------------------------------------------

# n=int(input('enter a num'))
# count=0
# for i in range(1,n+1):
#         if n%i ==0:
#                 count+=1#->store the value of divisible
# if count==2:
#         print('prime')
# else:
#         print('not prime')

# i = 1 → divisible → count = 1

# i = 2 → not divisible → count = 1

# i = 3 → not divisible → count = 1

# i = 4 → not divisible → count = 1

# i = 5 → not divisible → count = 1

# i = 6 → not divisible → count = 1

# i = 7 → divisible → count = 2

# Since count == 2 → prime ->prime divie 1and itself
# num=7
# ans=True
# for i in range(2,num):
#         if num%i==0:
#                 print('not prime')
#                 ans=False
#                 break
# if ans==True:
#       print('prime')
#------------------arrenge in dect format------------------------------------------------------------------
# i/p :- l = [1, 1, 1, 2, 3, 4, 3, 4, 2, 5, 6, 5, 7]
# o/p :- {1: 3, 2: 2, 3: 2, 4: 2, 5: 2, 6: 1, 7: 1}
# l=[1,1,1,2,3,4,3,5,5,9,9,]
# output_dict={}
# for i in l:
#         if i in output_dict:
#                 output_dict[i]+=1
#         else:
#                 output_dict[i]=1
# print(output_dict)

# i/p :- [2,0,3,0,1,0,5]
# o/p :- [2,3,1,5,0,0,0]
# l = [2,0,3,0,1,0,5] 
# l1=[]
# for i in l:
#    if i !=0:
#       l1.append(i)
# zero_count = l.count(0)
# for _ in range(zero_count):
#     l1.append(0)    
# print(l1)


# l = [2,0,3,0,1,0,5] 
# l1=[]
# for i in l:
#    if i !=0:
#       l1.append(i)
# n=len(l)-len(l1)
# for _ in range(n):
#     l1.append(0)    
# print(l1)

# i/p :- [2,1,3,8,4,8,5]
# o/p :- [2,8,4,8,1,3,5]
# l=[2,1,3,8,4,8,5]
# l1=[]
# for i in l:
#    if i%2==0:
#       l1.append(i)
# for i in l:
#    if i%2!=0:
#       l1.append(i)

# print(l1)
#----------------------------- WAP to check given number is either perfect number or not.----------------------------------------------------------
# n=int(input("Enter any no:"))
# sum = 0
# for i in range(1,n):
#    if n%i==0:
#         sum=sum+i
#         if i<n:
#           print((i),end='+')
#         else:
#             print((i),end='=')
# print (sum)
# if n==sum:
#     print(f'given number {n} is perfect number')
# else:
#      print(f'given number {n} is not a perfect number')
#-----------------------------------------------------max num in list--------------------------------------------
# l = [2,4,9,3,5]
# max = l[0]
# for i in l:
#         if i>max:
#             max=i 
# print('max value:',max)
# #-----------------------------------------------------min num in list--------------------------------------------
# l = [2,4,9,3,5]
# min = l[0]
# for i in l:
#         if i<min:
#             min=i
# print('max value:',min)

#--------------------------------asending order-------------------------------------------------------------
# l = [64, 34, 25, 12, 22, 11, 90, 5]
# l.sort()
# print(l)
# l = [64, 34, 25, 12, 22, 11, 90, 5]
# for i in range(len(l)):
#     for j in range(len(l)-1-i):#l[j] → current element at index j,l[j+1] → next element at index j+1
#         if l[j] > l[j+1]:  #Compare l[0]=64 and l[1]=34→ 64> 34 → swap
#             l[j], l[j+1] = l[j+1], l[j]
# print("Ascending:", l)

# range(len(l)-1-i) = range(8-1-0) = range(7)
# So j will take values: 0, 1, 2, 3, 4, 5, 6

# Inner loop compares l[j] and l[j+1]

# First comparison
# j = 0

# l[j] = l[0] = 64 

# l[j+1] = l[1] = 34

# Condition: if l[j] > l[j+1] → if 64 > 34 → True → swap
# #------------------------------------desending order--------------------------------------------------------------
# l = [64, 34, 25, 12, 22, 11, 90, 5]
# l.sort(reverse=True)
# print(l)

# l = [64, 34, 25, 12, 22, 11, 90, 5]
# for i in range(len(l)):
#     for j in range(len(l)-1-i):
#         if l[j] <l[j+1]:  
#             l[j], l[j+1] = l[j+1], l[j]
# print("Ascending:", l)
# -----------------------------------------------new topic----------------------------------------- 
l = [64, 34, 25, 12, 22, 11, 90, 5]
for i in range(len(l)):
    for j in range(len(l)-1-i):
        if l[j] <l[j+1]:  
            l[j], l[j+1] = l[j+1], l[j]
print("Ascending:", l)