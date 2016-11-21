class Animal (object):
    pass

class Dog(Animal):

    def __init__(self,name):
        self.name =name

class Cat (Animal):
    def __init__(self,name):
        self.name = name

class Person(object)        :

    def __init__(self,name):
        self.name = name

        self.pet = None

        self.address = "Nowhere"

    def print_address(self):
        print "Printing address from the Person Class" , self.address

    #def print_name():
    #    print super.name

class Employee(Person)        :

    def __init__(self,name,salary):

        super(Employee,self).__init__(name)

        self.salary = salary


    def print_name_2(self):
        print "Printing name from the Employee Class" , self.name


class Fish(object):
    pass

class Salmon(Fish):
    pass

class Halibut(Fish):
    pass


rover = Dog("Rover")

satan = Cat("Satan")

mary = Person("Mary")

mary.pet = satan

des = Employee("Des",1250)

#print des.name
#print des.salary

#print dir(des)
#print type(des)

#print des.__dict__

des.print_address()

des.print_name_2()
