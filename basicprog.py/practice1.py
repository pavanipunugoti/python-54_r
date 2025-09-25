
"""Single Inheritance..
class Employee:
    def work(self):
        print("Employee works 9 to 5")
class Manager(Employee):
    def Manage(self):
        print("Manager Manages team")
m=Manager()
m.work()
m.Manage()


class Family:
    def Mom(self):
        print(" Hii I am Bharathi...I am mom of pavani")
class Sis(Family):
    def Sasi(self):
        print("Hii I am Sasi..I am sis of Pavani")
f=Sis()
f.Mom()
f.Sasi()

"""

"""Multiple...Inheritance
class Father:
    def skills(pav):
        print("Gardring Work And Carpenter") 
class Mother:
    def skills(pav):
        print("Cooking and CAring")
class Child(Father,Mother):
    def child(pav):
        Father.skills(pav)
        Mother.skills(pav)
        print("Learning New Skills")
c=Child() 
c.child()
c.skills()
"""



""" Multilevel Inheritance
class Grand:
    def __init__(self):
        print("Grnd father Is the Gf")
class Father(Grand):
    def __init__(self):
        super().__init__()
        print("Father Is fAtehr")
class Son(Father):
    def __init__(self):
        super().__init__()
        print("son Is sOn")
s=Son()

class Grnd():
    def Ps(self):
        print("Grand Fatehr")
class Father(Grnd):
    def Ps2(self):
        print("fatehr")
class Child(Father):
    def Ps3(self):
        Grnd.Ps(self)
        Father.Ps2(self)
        print("this is mee")
s=Child()
s.Ps3()
"""