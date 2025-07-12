
import os
os.chdir('c:\\Users\\devin\\OneDrive\\Documents\\positron\\DS510\\Project')

from Course import Course
from GPA import *
from Student import *
from my_functions import *


# Application Start
if __name__ == "__main__":

    # Ask user for a student ID to search if they exist already in the data files
    SID = input("Enter a Student ID: ")

    # use inputed student id and search the file structure for this SID and return the tuple(exists, SID, Fname, LName)
    studentInfo = fileExists(SID)

    if studentInfo[0]:
        # if student already exists then create student object from data file name
        print("This student exists, {fname} {lname}".format(fname=studentInfo[2], lname=studentInfo[3]))
        student = Student(studentInfo[1], studentInfo[2], studentInfo[3])
    else:
        # if student doesn't already exists, ask user if they want to create a new student
        enterStudentYN = input("This student ID doesn't exist. Would you like to add a new student? (Y/N/Exit): ").upper()

        if enterStudentYN == "Y":
            # Ask user for student information and create a new student object.
            enterFName = input("Enter Student's First Name: ")
            enterLName = input("Enter Student's Last Name: ")
            student = Student(SID, enterFName, enterLName)

            # Add the new student to the data files
            student.addStudent()
        elif enterStudentYN == "N":
            pass
        elif enterStudentYN == "EXIT":
            pass
        else:
            pass

    
    # Once the student object is created (either a new student or previous student) ask user what they want to do next
    # This can include entering a new course for the student or printing a transcript
    enterAction = input(f"Would you like to enter a \033[4mN\033[0mew course for this student or print a \033[4mS\033[0mummary of their transcript? (N/S) ").upper()

    # if user select to enter a new course
    if enterAction == "N":

        # boolean to keep entering new courses until False
        addNewCourse = True

        while addNewCourse:
            # Collect course information from user
            enterDept = input("Department abbreviation: ")
            enterNum = input("Course number: ")
            enterTitle = input("Course name: ")
            enterCredits = input("Course credits: ")
            enterSemester = input("Semester course taken: ")
            enterGrade = input("Grade received: ")

            # create the GPA object basaed on information entered
            newCourse = GPA(enterDept, enterNum, enterTitle, enterCredits, enterSemester, enterGrade)
            # assign the course to the student (appends to the csv file for the student)
            # returns if the add was successful
            added = newCourse.assignToStudent(student)

            if added:
                print("New course addedd sucessfully")
                
                # Ask user if they want to add another course and check if it is "Y". 
                addNewCourse = input("Would you like to add another course for this student? (Y/N)").upper() == "Y"
            else:
                #error handling. If new course did not get added successfully then exit the program gracefully
                print("Adding new course failed. Quiting program.")
                addNewCourse = False
                break
            

