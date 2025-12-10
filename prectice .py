class stud:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def avg(self,s1,s2,s3):
        return (s1.mark+s2.mark+s3.mark)/3
s1=stud('priya',99)
s2=stud('riya',98)
s3=stud('iya',97)
print(s1.avg(s1,s2,s3))
# class stud:
#     def __init__(self,name,mark):
#         self.name = name
#         self.mark = mark

# s1 = stud('priya', 99)
# s2 = stud('riya', 98)
# s3 = stud('iya', 97)

# avg = (s1.mark + s2.mark + s3.mark) / 3
# print("Average =", avg)
