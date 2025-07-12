##################################
### Created: July 12, 2025
### Author: Devin Hunt
### Program: Student.py
### Description: creates the Student class as a child class of Course
### Inputs: Course.py
### Packages: None 
### Output: None
### References: Pulled some new functions and knowledge from reading: 
###             Ernesti, J., & Kaiser, P. (2022). Python 3: The comprehensive guide. Rheinwerk Publishing.
##################################

import os
import csv
from GPA import *

class Student:

    # initialization of student object
    def __init__(self, studentId, firstName, lastName):
        self.studentId = studentId
        self.firstName = firstName
        self.lastName = lastName

    def getFileRef(self):
        # create a fileRef that creates the file name to use for saving GPA data
        fileRef = "-".join([self.studentId, self.firstName, self.lastName]) + ".csv"

        return fileRef

    # creates a new csv file reference to add GPAs to later
    def addStudent(self):
        # create outfile name based on student id and full name
        # store in program subdirectory called data
        outfile = "./data/" + self.getFileRef()
        headerRow = (["dept", "courseNum", "courseName", "credits", "semester", "grade"])

        #open file to write
        # x is used instead of w so we don't overwrite existing files and clear out the data
        with open(outfile, "x", newline = '') as f_csv:
            #create first row with column names in CSV format
            writer = csv.writer(f_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(headerRow[0:])

        return True

    def getCourses(self):
        infile = "./data/" + self.getFileRef()
        # initialize a list to store course information in. 
        # This will be a list of GPA objects, one for each record in the CSV file
        studentCourses = []
        
        with open(infile, 'r', newline='') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            # read in each row of the csv file and save to a GPA object
            for row in csv_reader:
                # create a GPAA object based on row data from the csv file
                GPAdata = GPA(*row)
                # append the object to the studentCourses list. This allows us to use class properties for GPA
                studentCourses.append(GPAdata)

        # return all but the header row
        return studentCourses[1:]           

    def totalSummary(self):
        
        # cumulative credits and qual points for the entire transcript
        totalCredits = int(0)
        totalQualPoints = float(0)
        
        # loop through all courses and add up the total credits and qual points
        for course in self.getCourses():
            totalQualPoints += course.getQualityPoints()
            totalCredits += int(course.credits)
        
        #calculate total GPA as total qual points / total credits
        totalGPA = totalQualPoints / totalCredits

        # output the summary line for the transcript
        stringOutput = "Total Credits: {}   Overall Quality Points: {:.1f}   Overall GPA: {:.3f}".format(totalCredits, totalQualPoints, totalGPA)
        print(stringOutput)

        return None

    def semesterSummary(self):

        # get a list of all courses for the student
        courses = self.getCourses()
        #determine maximum course name length to format output
        maxLen = max(len(courses[i].courseName) for i in range(len(courses)))

        # create set of all semesters in the file. A set is chosen to allow for collection of unique values in the file
        semesters = set([courses[i].semester for i in range(len(courses))]) 

        # loop through the unique semesters identified above
        for semester in semesters:
            # create variables to count up total credits and quality points for the semester
            semesterCredits = int(0)
            semesterQualPoints = float(0)
            # loop through the courses and determine if it is part of the semester
            for course in self.getCourses():

                # if course is in the semester then add credits and qual points to total
                if course.semester == semester:
                    semesterCredits += int(course.credits)
                    semesterQualPoints += course.getQualityPoints()
                    
                    # output the course description details and print to console
                    courseString = "{} {:<3} {} {:<{}} {} credits {:<2} {:>5.2f} qual pts.".format(course.semester, course.dept, course.courseNum, course.courseName, maxLen, course.credits, course.grade, course.getQualityPoints())
                    print(courseString)

            # calculate the semester GPA at end of loop and print it to console       
            semesterGPA = semesterQualPoints/semesterCredits
            print("Semester GPA: {:.3f}\n".format(semesterGPA))
        
        return None
           
        
    # default printing using the super class output and adding additional variables
    def __str__(self):
        return f" {self.studentId} {self.firstName} {self.lastName}"

