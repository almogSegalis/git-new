# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from datetime import date

def fileMaker(name, visit):
    fileName = name + ".txt"
    f = open(fileName, "w")
    f.write(str(date.today) + "\n")
    f.write("name of the patient: " + name + "\n")
    f.write("reason for visit: " + visit + "\n")
    f.close()

patientName = input("enter patient name")
visitRes = input('enter reason for visit:')

fileMaker(patientName, visitRes)
