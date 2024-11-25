import random as r
class Student:
    def __init__(self,ชื่อ,ชื่อเล่น,คะแนนสอบ):
        self.name = ชื่อ
        self.nickname = ชื่อเล่น
        self.score = คะแนนสอบ
    def score0(self):
        self.score = r.randint(1,10) 
    def grade(self):
        if self.score >= 5:
            print("คุณสอบผ่าน")
        else:
             print("คุณสอบตก")
std1 = Student(ชื่อ="ณภัทรพงศ์ จิตพิชัย",ชื่อเล่น="คิว",คะแนนสอบ=0)
std1.score0()
print(std1.name,std1.nickname,std1.score)
std1.grade()
print("-------------------------------------------------------------------------")
std2 = Student(ชื่อ="ศรีสุเทพ หนูทอง",ชื่อเล่น="ออมสิน",คะแนนสอบ=0)
std2.score0()
print(std2.name,std2.nickname,std2.score)
std2.grade()
print("-------------------------------------------------------------------------")
std3 = Student(ชื่อ="ภุเบศ ดีหนู",ชื่อเล่น="หนู",คะแนนสอบ=0)
std3.score0()
print(std3.name,std3.nickname,std3.score)
std3.grade()
print("-------------------------------------------------------------------------")
std4 = Student(ชื่อ="ณัฐพงศ์ ศรีเทพย์",ชื่อเล่น="นาย",คะแนนสอบ=0)
std4.score0()
print(std4.name,std4.nickname,std4.score)
std4.grade()
print("-------------------------------------------------------------------------")
std5 = Student(ชื่อ="พงศกร กาญจนณรงค์",ชื่อเล่น="น้ำเพชร",คะแนนสอบ=0)
std5.score0()
print(std5.name,std5.nickname,std5.score)
std5.grade()
print("-------------------------------------------------------------------------")

