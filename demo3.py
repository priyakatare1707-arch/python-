#-------------------------get(returns value)---------------------------------------
# d={'x':10,'y':20,'2':30}
# print(d.get('z'))
# print(d.get('x'))
# print(d.keys())
# print(d.values())
# print(d.items())#pair of value and key
# d.pop('y')#keypair remove
# print(d.pop('y'))#it give delet vaue
# print(d.popitem())#last item pop
# print(d)
# s=[10,20,30,'python']
# d=dict.fromkeys(s)
# print(d)
# s=['name','email','contect','add']
# d=dict.fromkeys(s)
# n='priya'
# # n=input('enter')
# e='priya@gmail.com'
# c=124
# a='bhopal'
# # d['key']=updatedvalue
# # d['name']=n
# d['email']=e
# d['contect']=c
# d['add']=a
# print(d)
# #--------------update(combine two dict)-----------
# d1={'x':20,'y':30}
# d2={'z':40}
# d1.update(d2)
# print(d1)#update dict
# print(d2)#odd dict
# d1={'x':20,'y':30}
# print(d1.setdefault('x',20))
# print(d1.setdefault('z',30))
# print(d1)
#--------------------set-------------------------------
#collection of unique element
# my={10,20,30,'python','java'}#inorded by hesing 
# print(my,type(my))
# print(len(my))
# print(type(my))
# print(id(my))
# print(max(my))
# print(min(my))
# print(sum(my))
#----------------------set method------------------
#1. required more then two set
# s1,s2={1,2,3,4},{4,3}
# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1.difference(s2))
# print(s1.symmetric_difference(s2))
# s1.intersection_update(s2)
# s1.difference_update(s2)
# print(s1)
# print(s2)
# print(s1.issuperset(s2))
# print(s2.issuperset(s1))
# print(s1.issubset(s2))
# print(s2.issubset(s1))
# print(s1.isdisjoint(s2))#  when both element are same
# print(s2.isdisjoint(s1))
# s1,s2={1,2,3,4},{5,6,7,8}
# print(s1.isdisjoint(s2))# when both element  not same
# print(s2.isdisjoint(s1))

# #--------------------------------method for single set------------------------
# s={1,2,3,'python','java'}
# d=s.copy()
# print(d,id(d),id(s))
# e=s.clear()
# print(e)
#add->add in rendom position
# s.add('phy')
# print(s)
#to add multiple element
# s.update({5,6,3})
# print(s)
# print(s.pop())#remove rendom element
# print(s.remove('python'))
# print(s)
# print(s.remove('priya'))#to remove this error use discart
# print(s.discard('python'))
# print(s)
#----------------------------frozenset(frez element/not change)immutible/it is property of set
# s='python'
# s1=[10,20,'python']
# s2=[60,40,'python']
# fs1=frozenset(s)
# print(fs1,type(fs1))
# fs2=frozenset(s1)
# print(fs2,type(fs2))
# fs3=frozenset(s2)
# print(fs3,type(fs3))
# print(len(fs3))
# print(type(fs3))
# print(id(fs3))
# # print(sum(fs3))#numerice homogeneaus
# print(max(fs3))
# print(min(fs3))
#---------------------------method of frozenset--------------------------
#union,interserion,diffrence,symmetric_difference,issubset,issuperset,isdisjoint
# s1=({10,20,30,40})
# s2=({30,40,50,60})
# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1.difference(s2))
# print(s1.symmetric_difference(s2))
# print(s1.issuperset(s2))
# print(s1.issubset(s2))
# print(s1.isdisjoint(s2))
