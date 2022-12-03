class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee:
    def __init__(self, name, idNumber, department):
        self.name = name
        self.idNumber = idNumber
        self.department = department


class Cake:
    def __init__(self, flavor, frosting):
        self.flavor = flavor
        self.frosting = frosting

# can you fill out the rest of this for me? im dumb
# the cake needs to have the cake flavor and cake frosting stored

class Cat:
    def __init__(self, name, age, fur_length):
        self.name = name
        self.age = age
        self.fur_length = fur_length

    def breedGuess(self):
        if self.fur_length == "long":
            return ("Domestic Longhair")
        else:
            return ("Domestic Shorthair")


class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def drivetrainType(self):
        if 1769 < self.year < 1980 :
            return ("manual?")
        elif self.year > 1979:
            return ("automatic?")
        else:
            return ("no car sorry!")
    # create your own function! what do you want it to do?


def main():
    # fill this one out with a dog's name and age.. can be your dog, friend's dog, etc.
    dog1 = Dog("joe", "11")
    print(dog1.name, dog1.age)

    # and what about a new employee
    em1 = Employee("craig", 777, "janitor")
    # how would we print out each of the variables from newEmployee?
    print(em1.name, em1.idNumber, em1.department)

    # now create and print out a cake you make

    # and now create another cake and print it out

    # create a cat!
    cat1 = Cat("Yummi", 200, "long")
    cat2 = Cat("lion", 1, "short")
    # create another cat!

    # What would we put here to print out the result of breedGuess for cat1?
    print(cat1.breedGuess())
    print(cat2.name)
    # create a car!
    car1 = Car("Mustang", 1967, "red")

    # Now print out the function you made for car :)
    print(car1.drivetrainType())

main()