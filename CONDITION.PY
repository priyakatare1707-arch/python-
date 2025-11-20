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

#------------------------------pattarn-----------------------------------------------
# n=5         
# for i in range(1,6):
#  print('* '*i)
#* 
#* *
#* * *
#* * * *
#* * * * *
# n=int(input ('enter row'))  
# for i in range(1,n+1):
#     print(' '*(n-i)+'*'*i)
#     *
#    **
#   ***
#  ****
# n=int(input ('enter row'))  
# for i in range(1,n+1):
#     print(' '*(n-i)+'* '*i)

#    * 
#   * *
#  * * *
# * * * *
#* * * * *
# n=int(input ('enter row'))
# for i in range(1,n+1):
#     print('*'*i)
#    *
#    **
#    ***
#    ****
#    *****
# n=int(input ('enter row'))
# for i in range(n):
#     print(''*i+'*'*(n-i))

# *****
# ****
# ***
# **
# *
# n=int(input ('enter row'))
# for i in range(n):
#     print('*'*(n-i))
# * * * * * 
# * * * *
# * * *
# * *
# *
# n=int(input ('enter row'))
# for i in range(n):
#     print(' '*i+'* '*(n-i))

# *****
#  ****
#   ***
#    **
#     *
# n=int(input ('enter row'))
# for i in range(n):
#     print(' '*i+'* '*(n-i))

# * * * * * 
#  * * * *
#   * * *
#    * *
#     *

# n=int(input ('enter row'))
# for i in range(1,n+1):
#     print(''*i+'*'*i)

# for i in range(n-1,0,-1):
#     print(' '*(n-i)+'* '*i) 

#    * 
#   * *
#  * * *
# * * * *
#* * * * *
# * * * *
#  * * *
#   * *
#    *

# n=int(input ('enter row'))
# for i in range(1,n+1):
#     print('* '*i)
# for i in range(1,n+1):
#     print(''*i+'* '*(n-i))

#   * 
#   * *
#   * * *
#   * * * *
#   * * * * *
#   * * * *
#   * * *
#   * *
#   *  


# n = int(input("Enter number of rows: "))
# for i in range(1, n+1):
#     # print spaces first, then stars
#     print('  ' * (n - i) + '* ' * i)
#     # Decreasing stars, right-aligneb
# for i in range(n-1, 0, -1):
#     print('  ' * (n - i) + '* ' * i)
#        * 
#      * *
#    * * *
#  * * * *
#* * * * *
#  * * * *
#    * * *
#      * *
#        *
# n=int(input ('enter row'))
# for i in range(n):
#     print('* '*(n-i))
# # n=int(input ('enter row'))
# for i in range(1,n+1):
#     print('* '*i)
#     * * * * *
#     * * * *
#     * * *
#     * *
#     *
#     * *
#     * * *
#     * * * *
#     * * * * *
# n = int(input("Enter number of rows: "))
# # Decreasing stars, right-aligned
# for i in range(n, 0, -1):
#     print('  ' * (n - i) + '* ' * i)
# # Increasing stars, right-aligned
# for i in range(2, n + 1):
#     print('  ' * (n - i) + '* ' * i)
#* * * * * 
#  * * * *
#    * * *
#      * *
#        *
#      * *
#    * * *
#  * * * *
#* * * * *
# n=int(input('enter a num'))
# for i in range(n):
#     for j in ( i,n):
#         print('',end=' ')
#     for j in range(i+1):
#         print('* ',end=' ')
#     print()

# n=int(input('enter a value'))
# for i in range(n):#----------------i how much time it run--------------------
#     for j in range(1,n+1):#------------------j print-------------------------
#         print(j,end='')
#     print()

#1234
#1234
#1234
#1234

# n=int(input('enter a value'))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()

#1
#12
#123
#1234
#12345

# n=int(input('enter a value'))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j*2,end='')
#     print()

#2
#24
#246
#2468
#246810

# n=int(input('enter a value'))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j*2-1,end=' ')
#     print()

#1
#13
#135
#13579


# n = 4   # number of rows
# num = 1

# for i in range(1, n+1):
#     for j in range(i):
#         print(num, end=" ")
#         num += 1
#     print()
# 1
# 2 3
# 4 5 6
# 7 8 9 10

# n = 4   # number of rows
# num = 1

# for i in range(1, n+1):
#     for j in range(i):    # j number of column
#         print(num*2, end=" ")
#         num += 1
#     print()  
#2 
#4 6
#8 10 12
#14 16 18 20

# n = 4
# num = 1
# for i in range(1, n+1):
#     print(" "*(n-i), end="")   # left spaces
#     for j in range(i):
#         print(num, end=" ")
#         num += 1
#     print()
#         1
#        1  2
#       1  2  3
#      1  2  3  4
#     1  2  3  4  5

# n = 4
# num = 1
# for i in range(1, n+1):
#     print(" "*(n-i), end="")   # left spaces
#     for j in range(i):
#         print(num*2, end=" ")
#         num += 1
#     print()
#      2 
#     4 6
#   8 10 12
# 14 16 18 20
# x='A'
# print(ord(x)+1)
# print(chr(ord(x)+1))
# print(chr(ord('A')+1))
# n=input('enter a char')

# n=int(input('enter a char'))
# ch=(input('enter a char'))
# for i in range(n):
#     print(ch)
#     ch=chr(ord(ch)+1)
# print()
# #a
# #b
# #c
# #d
# #e

# n=int(input('enter a char'))
# ch='a'
# for i in range(n):
#     for j in range(n):
#         print(ch,end=' ')
#     ch=chr(ord(ch)+1)
#     print()  
# #a a a a a 
# #b b b b b
# #c c c c c
# #d d d d d
# #e e e e e

# n=int(input('enter a char'))
#    ch='a' 
# for i in range(1,n+1):
   
#     for j in range(i):
#         print(ch,end=' ')
#     ch=chr(ord(ch)+1)
#     print()  

#a 
#b b
#c c c
#d d d d
#e e e e e
# n = int(input("enter a number: "))

# for i in range(1, n+1):
#     ch = 'A'           # start from A every row
    
#     for j in range(i):
#         print(ch, end=' ')
#         ch = chr(ord(ch) + 1)
#     print()
# #A 
# #A B
# #A B C
# #A B C D
# #A B C D E

# n = int(input("enter a number: "))

# for i in range(1, n+1):
#     ch = 'A'           # start from A every row
    
#     for j in range(i):
#         print(ch, end=' ')
#         ch = chr(ord(ch) + 2)
#     print()
#A 
#A C
#A C E
#A C E G
#A C E G I
# n = int(input("enter a number: "))
# num='a'
# for i in range(1, n+1):
    
#     for j in range(i):
#         print(num, end=' ')
#         num=chr(ord(num)+1)
       
#     print()

#a 
#b c
#d e f
#g h i j
#k l m n o
# n = int(input("enter a number: "))
# num='a'
# for i in range(1, n+1):
#     print(" "*(n-i), end="")
#     for j in range(i):
#         print(num, end=' ')
#         num=chr(ord(num)+1)
       
#     print()
#    a 
#   b c
#  d e f
# g h i j
#k l m n o

# n = int(input("enter a number: "))

# for i in range(1, n+1):
#     ch = 'A'           # start from A every row
#     print(" "*(n-i), end="")
#     for j in range(i):
#         print(ch, end=' ')
#         ch = chr(ord(ch) + 1)
#     print()
#      A 
#     A B
#    A B C
#   A B C D
#  A B C D 

# n=5
# i=1
# while i<=n:
#     j=1
#     ch='a'
#     while j<=i:
#        print(ch,end='')
#        ch=chr(ord(ch)+1)
#        j=j+1
#     i=i+1
#     print( )
# a
# ab
# abc
# abcd
# abcde

# n=5
# i=1
# p='a'
# while i<=n:
#     j=1    
#     while j<=i:       
#        print(p,end='')
#        p=chr(ord(p)+1)
#        j=j+1     
#     i=i+1
#     print( )
# a
# bc
# def
# ghij
# klmno
# n=5
# i=1
# while i<=n:
#     j=1
#     ch='a'
#     while j<=n:
#        print(ch,end='')
#        ch=chr(ord(ch)+1)
#        j=j+1
#     i=i+1
#     print( )

#  a a a a a 
# #b b b b b
# #c c c c c
# #d d d d d
# #e e e e e
# n=int(input('enter a num'))
# for _ in range(1,n+1):
#     for i in range(1,n+1):
#         print(i,end=' ')
#     print()

# n=int(input('enter a num'))
# for _ in range(1,n+1):
#     for i in range(1,_+1):
#         print(i,end=' ')
#     print()
#--------------------------------even num triangle------------------------------------
# n=int(input('enter a num'))
# for _ in range(1,n+1):
#     for i in range(1,_+1):
#         print(i*2,end=' ')
#     print()
#--------------------------------odd num triangle------------------------------------
# n=int(input('enter a num'))
# for _ in range(1,n+1):
#     for i in range(1,_+1):
#         print(i*2-1,end=' ')
#     print()

# n=int(input('enter a num'))
# y=1
# for i in range(1,n+1):
#    print(' '*(n-i),end=' ')
#    for i in range(1,i+1):
#         print(y,end=' ')
#         y+=1
#    print()
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
        # i+=1

# n=int(input('enter a num'))
# i=1
# while i<=n:
#     if i==5:
#        print('okk')
#        break#-------------------after break teminet loop no execution after that---------
#     else:
#         print(i)
#     i +=1
#-------------------------------------------indentetion error space se ati hai ---------------------------------------------
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

#----------------------function (remove the reapetation of loop)----------------------------------------------
