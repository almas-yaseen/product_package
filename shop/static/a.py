class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname = lname

    def printname(self):
        print(self.firstname,self.lastname)

class Student(Person):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)


x=Student("almas","jacky")
x.printname()
