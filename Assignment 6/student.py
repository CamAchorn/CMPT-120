# oo scary
'''
Instructions:
We're now experts at classes, right?
Yeah?
mkay so do me a favor
Create the class student
every student has these traits:
name
student id (you can pick this number arbitrarily)
year (f/s/j/s)
major
gpa
create a function to see if the student is eligible for the honors program
to be eligible they need to have a gpa above 3.5
return true if they can and false if they cant, and print it out
create a function because this college is a wacky one- every day they generate a student id and if the student id matches a student, that student gets free food that day.
1. generate a random number the length of however long you choose to make the id number
2. compare if the random number matches your student's id
3. if it matches print out "winner! student (name) gets free lunch!"
4. if not, print "Loser!"
(disclosure: obviously there's a very small chance of your generated number matching the student id number. I just want to see that you're generating and comparing properly)
'''
import random

class student:
    def __init__(self, name, stuID, year, major, gpa):
        self.name = name
        self.stuID = stuID
        self.year = year
        self.major = major
        self.gpa = gpa

    def honors(self):
        if self.gpa > 3.5:
            return ("you may enter honors program")
        else:
            return ("you may not enter honors program")

    def studentID(self):
        num = 200400 + random.randint(1, 11)
        if num == self.stuID:
            return "winner! student " + (self.name) + " gets free lunch!"
        else:
            return "Loser!"


def main():
    student1 = student("Gretta", 200401, "freshman", "communications", 3.6)
    student2 = student("Ted", 200405, "senior", "business", 3.2)
    student3 = student("Sally", 200409, "sophomore", "computer science", 4.0)

    print(student1.studentID(), student1.honors())
    print(student2.studentID(), student2.honors())
    print(student3.studentID(), student3.honors())
# create three students and check if they get free lunch and if they qualify for honors


main()