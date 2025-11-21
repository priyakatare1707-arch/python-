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