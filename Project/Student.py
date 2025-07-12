##################################
### Created: July 12, 2025
### Author: Devin Hunt
### Program: Student.py
### Description: creates the Student class as a child class of Course
### Inputs: Course.py
### Packages: None 
### Output: None
### References: 
##################################

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
                GPAdata = GPA(row[0], row[1], row[2], row[3], row[4], row[5])
                # append the object to the studentCourses list. This allows us to use class properties for GPA
                studentCourses.append(GPAdata)

        # return all but the header row
        return studentCourses[1:]           


    # default printing using the super class output and adding additional variables
    def __str__(self):
        return f" {self.studentId} {self.firstName} {self.lastName}"

