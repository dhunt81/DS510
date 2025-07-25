##################################
### Created: July 12, 2025
### Author: Devin Hunt
### Program: Project - Hunt.py
### Description: This program is an interactive interface that asks for user to input student ids and then 
###              allows users to enter new students, enter new course grades, and requests transcript summaries
###              to be printed to the console window.
### Inputs: Course.py, GPA.py, my_functions.py, Student.py, student csv files located in ./data
### Packages: None 
### Output: csv files located in ./data and summary text to console window
### References: Pulled some new functions and knowledge from reading: 
###             Ernesti, J., & Kaiser, P. (2022). Python 3: The comprehensive guide. Rheinwerk Publishing.
##################################

from Course import Course
from GPA import *
from Student import *
from my_functions import *


# Application Start
if __name__ == "__main__":

    viewStudent = True

    # Loop to keep viewing student files until user exits the program. Main program loop
    while viewStudent:

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
                #break loop and continue to next iteration to prompt for another student
                continue
            elif enterStudentYN == "EXIT":
                pass
            else:
                pass

        
        # Once the student object is created (either a new student or previous student) ask user what they want to do next
        # This can include entering a new course for the student or printing a transcript
        
        actionLoop = True

        # inner loop of program to keep asking what to do with current student until broken by user
        while actionLoop:
            
            enterAction = input(f"Would you like to enter a \033[4mN\033[0mew course for this student or print a \033[4mS\033[0mummary of their transcript? (N/S/Exit) ").upper()

            if enterAction == "EXIT":
                break

            # if user select to enter a new course
                
            if enterAction == "N":

                # boolean to keep entering new courses until False
                addNewCourse = True

                #Loop to keep adding courses until user requests no more to be added
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

            # Action is to print a transcript summary
            elif enterAction == "S" and int(len(student.getCourses()) > 0):
                print("\nTranscript for: {} {} {}\n".format(student.firstName, student.lastName, "(ID: " + student.studentId + ")"))
                student.semesterSummary()
                student.totalSummary()

                # This student action is done. Break loop to move to new student
                break

            # If student course file is blank then indicate there are no courses to summarize
            elif enterAction == "S" and int(len(student.getCourses()) == 0):
                print("\nTranscript for: {} {} {}\n".format(student.firstName, student.lastName, "(ID: " + student.studentId + ")"))
                print("No Courses Entered\n")

                # This student action is done. Break loop to move to new student
                break

        # Once printed ask user to view another student
        viewAnother = input("View another student? (Y/N)").upper()

        # if user wants to view another student then keep continue to next iteration of loop
        if viewAnother == "Y":
            continue

        # If no request to view more students then set while condition to false
        elif viewAnother == "N":
            viewStudent = False
    
    # text to indicate program is terminating
    print('Good Bye')



""" Test Run Output

Enter a Student ID: 111
This student exists, John Doe
Would you like to enter a New course for this student or print a Summary of their transcript? (N/S/Exit) S

Transcript for: John Doe (ID: 111)

19/FA CS  104 Quantitative MethodsA          3 credits B   9.00 qual pts.
19/FA MA  117 Discrete StructuresA           4 credits C   8.00 qual pts.
19/FA DS  512 Comptuer Science FundamentalsB 4 credits C   8.00 qual pts.
19/FA MA  105 Quantitative MethodsB          3 credits B+  9.99 qual pts.
19/FA MA  118 Discrete StructuresB           4 credits A- 14.68 qual pts.
19/FA DS  511 Comptuer Science FundamentalsA 4 credits A  16.00 qual pts.
Semester GPA: 2.985

20/FA DS  513 Comptuer Science Fundamentals  4 credits A  16.00 qual pts.
20/FA CS  119 Discrete Structures            4 credits C+  9.32 qual pts.
20/FA MA  106 Quantitative Methods           3 credits B+  9.99 qual pts.
Semester GPA: 3.210

19/SP DS  510 Comptuer Science Fundamentals  4 credits A- 14.68 qual pts.
19/SP MA  103 Quantitative Methods           3 credits B+  9.99 qual pts.
19/SP MA  116 Discrete Structures            4 credits C-  6.68 qual pts.
19/SP CS  480 Seminar                        1 credits B-  2.67 qual pts.
Semester GPA: 2.835

Total Credits: 45   Overall Quality Points: 135.0   Overall GPA: 3.000
View another student? (Y/N)Y
Enter a Student ID: 100 
This student ID doesn't exist. Would you like to add a new student? (Y/N/Exit): Y
Enter Student's First Name: Devin
Enter Student's Last Name: Hunt
Would you like to enter a New course for this student or print a Summary of their transcript? (N/S/Exit) N
Department abbreviation: BIN
Course number: 500
Course name: Bioinformatics Fundamentals
Course credits: 4
Semester course taken: 24/FA
Grade received: A
New course addedd sucessfully
Would you like to add another course for this student? (Y/N)Y
Department abbreviation: BIN
Course number: 516
Course name: Molecular and Cellulary Biology
Course credits: 4
Semester course taken: 24/FA
Grade received: A
New course addedd sucessfully
Would you like to add another course for this student? (Y/N)Y
Department abbreviation: DS
Course number: 510
Course name: Computer Science Fundamentals
Course credits: 4
Semester course taken: 25/SP
Grade received: A
New course addedd sucessfully
Would you like to add another course for this student? (Y/N)N
Would you like to enter a New course for this student or print a Summary of their transcript? (N/S/Exit) S

Transcript for: Devin Hunt (ID: 100)

24/FA BIN 500 Bioinformatics Fundamentals    4 credits A  16.00 qual pts.
24/FA BIN 516 Molecular and Cellulary Biology 4 credits A  16.00 qual pts.
Semester GPA: 4.000

25/SP DS  510 Computer Science Fundamentals  4 credits A  16.00 qual pts.
Semester GPA: 4.000

Total Credits: 12   Overall Quality Points: 48.0   Overall GPA: 4.000
View another student? (Y/N)Y
Enter a Student ID: 145
This student ID doesn't exist. Would you like to add a new student? (Y/N/Exit): Y
Enter Student's First Name: Jason
Enter Student's Last Name: Yamamura
Would you like to enter a New course for this student or print a Summary of their transcript? (N/S/Exit) S

Transcript for: Jason Yamamura (ID: 145)

No Courses Entered

View another student? (Y/N)N
Good Bye

"""

