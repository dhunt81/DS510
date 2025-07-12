##################################
### Created: July 12, 2025
### Author: Devin Hunt
### Program: DS510 GPA.py
### Description: creates the GPA class as a child class of Course
### Inputs: Course.py
### Packages: None 
### Output: None
### References: 
##################################
import Course
import os

class GPA(Course):

    # Create class dictionary to map letter grade to numeric grade
    # creates here so it can be initiated once for the class instead of each time getQualityPoints is called
    points = {"A":4.00, "A-":3.67, "B+":3.33, "B":3.00, "B-":2.67, "C+":2.33, "C":2.00, \
        "C-":1.67, "D+":1.33, "D":1.00, "D-":0.67, "F":0}

    # initialization of the class object extending from super class
    def __init__(self, dept, courseNum, courseName, credits, semester, grade):
        super().__init__(dept, courseNum, courseName, credits)
        self.semester = semester
        self.grade = grade

    def getQualityPoints(self):
        # Calculate quality points by multiplying total course credits by numeric grade from above
        # Using the previously initialized grade and credits to calculate the qualiyt points and return
        qualPoints = int(self.credits) * points[self.grade]
        return qualPoints

    def assignToStudent(self, student):
        # append course details to a student file
        outfile = "./data/" + student.getFileRef()
        data = ([self.dept, self.courseNum, self.courseName, self.credits, self.semester, self.grade])

        #open file to write
        if os.path.exists(outfile):
            with open(outfile, "a", newline = '') as f_csv:
                #append data row from course
                writer = csv.writer(f_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                writer.writerow(data[0:])
            response = True
        else:
            print("ERROR: Student file does not exist. Create student file with .addStudent().")
            response = False

        return response

    # default printing using the super class output and adding additional variables
    def __str__(self):
        return super().__str__() + f" {self.semester} {self.grade}"

