# text content->
# binary content->text formet, resume,image, oudio,vedio
# crad opration perform by file hendaling
#creat()/open()
# write()/read()
# close()
# 1.open():-
# syntex:-    open ('filename withextention ,mode' )
# mode
# x(creat)
# w(write)
# r(read)
# a(append)

# # f=open('n1.txt','x')#creat mode
# f=open('n5.txt','x')
# print(f.name)
# print(f.mode)
# print(f.readable())
# print(f.writable())
# print(f.encoding)
# print(f.closed)

# f=open('n6.txt','w')
# print(f.name)
# print(f.mode)
# print(f.readable())
# print(f.writable())
# print(f.encoding)
# print(f.closed)

# f=open('n7.txt','r')#read mode(default mode)
# print(f.name)
# print(f.mode)
# print(f.readable())
# print(f.writable())
# print(f.encoding)
# print(f.closed)

# f=open('n8.txt','a')#apppent mode previse last
# print(f.name)
# print(f.mode)
# print(f.readable())
# print(f.writable())
# print(f.encoding)
# print(f.closed)


# f=open('g8.txt','w+')
# print(f.name)
# print(f.mode)
# print(f.readable())
# print(f.writable())
# print(f.encoding)
# print(f.closed)

# f=open('g2.txt','w+')
# print(f.name)
# print(f.mode)
# print(f.readable())
# print(f.writable())
# print(f.encoding)
# print(f.closed)

# f=open('g3.txt','w+')#read mode
# print(f.tell())
# print(f.name)
# print(f.mode)
# print(f.readable())
# print(f.writable())
# print(f.encoding)
# print(f.closed)

# f=open('g4.txt','a+')#apppent mode previse last
# print(f.name)
# print(f.mode)
# print(f.readable())
# print(f.writable())
# print(f.encoding)
# print(f.closed)

#   ---------------------------------erres contant in w mode file if we open it---------------------------------------
#x+,w+,a+,r+ all are true in readable and writeable mode

# single string ko ek file pe likhane ke liye use karte hai
#---------------------------write------------------------
# f1=open('n6.text','a+')
# data='this is python class\n'
# f1.write(data)
# f1.close()

# #------------------------writeline--------------------------------
# f1=open('n6.text','a+')
# print(f1.tell())
# data=['java\n','python\n']
# # d1='priya\n, hello\n'
# # f1.write(d1)
# f1.writelines(data)
#------------------------------read------------------------------
#read()->read all data
# read(n)->read n bit of data
# readline()->read single line of data
# readlines()->read all line of data

# f=open('n6.txt')no mode given it is read mode
# f=open('n8.txt','r+')
# print(f.tell())
# data=f.read(10)
# # data=f.read()
# data=f.read(5)
# # data=f.readline()
# # data=f.readlines()
# print(data)
# f.close()

# for deleting file:-
# import os
# os.remove('n5.txt')
#------------------------cursure movement--------------------------------------------------------------------
#tell():->  to tell current position of cursure
# f=open('x1.txt','x+')
# print(f.tell())
# f=open('x1.txt','r+')
# print(f.tell())#0
# data=f.read(10)#0
# print(data)#helow i am
# print(f.tell())#10
#seek:->to move our cursure to requid position
# seek('how many bit are move','from where')
# where:0->starting position
#     1->current position
#     2->last position
# f=open('x1.txt','rb+')
# # print(f.tell())
# # data=f.read(10)#0
# # print(data)
# # print(f.tell())
# # f.seek(-5,1)
# # print(f.tell())
# # f.read(10)
# # print(f.tell())
# data=f.read(25)
# f.seek(20)
# print(f.tell())#20
# f.seek(-1,1)
# print(f.tell())#20-19position
# f.seek(-5,2)
# print(f.tell())#37position
class a():
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
    def ci(self):
        return 2*3.14*self.radius
a1=a(5)
print(a1.area())
print(a1.ci())


