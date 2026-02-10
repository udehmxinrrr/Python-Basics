class employee:
    def __init__(self, fullname,position,status,age):     #"Self" is the keyword identifying an object
        self.fullname=fullname
        self.position=position
        self.status=status
        self.age=age

    def work(self):
        print(self.fullname,"is working")

employee1=employee("Ken Mwenda", "MD", "Married", 54)
print(employee1.fullname,employee1.position,employee1.status,employee1.age)
employee1.work()
print()
employee2=employee("Jean Kamau", "Programs Manager", "Single",24)
print(employee2.fullname,employee2.position,employee2.status,employee2.age)
employee2.work()
print()
employee3=employee("Mark Joe", "Lecturer", "Single", 45)
print(employee3.fullname,employee3.position,employee3.status,employee3.age)
employee3.work()
print()