class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def full_name(self):
        return f'{self.surname} {self.name}'

    def is_adult(self):
        if self.age>=18:
            return True
        else:
            return False

p1 = Person('Jimi', 'Beast', 55)
print(p1.full_name())
print(p1.is_adult())
