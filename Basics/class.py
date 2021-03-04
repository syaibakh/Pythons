class Student():
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
    
    def major(self):
        print('Computer Science')

john = Student('John Doe', 'Male', 21)

print(john.name)
print(john.gender)
print(john.age)
print(john.major)