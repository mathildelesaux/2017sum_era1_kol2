#
# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.


class diary(object):
    nb_stud = 0
    def __init__(self,name="unknown",surname="unknown",marks=None):
        self.name=name
        self.surname=surname
        self.marks=marks
        diary.nb_stud =+1
        
    def display(self):
        print(self.name,"-",self.surname,"-",self.marks)
        
    def nb_stud(self):
        print("There are",diary.nb_stud,"students")
        
    def average_all_student(marks):
        for i in marks : 
            average = sum(i)/len(marks)
        print(average)

stud1=diary("Martin","Maurice",12)
stud1.display()
print()
stud2=diary("Lucy","MacCafé",4)
stud2.display()
print()
stud3=diary("Yves","StLaurent",18)
stud3.display()
print()
stud1.average_all_student()
print()
