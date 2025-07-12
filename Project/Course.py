##################################
### Created: July 11, 2025
### Author: Devin Hunt
### DS510 Course.py
### Description: creates the Course class
### Inputs: None
### Packages: None 
### Output: None
### References: 
##################################

class Course:

    # initialization of class object with attributes entered
    def __init__(self, dept, courseNum, courseName, credits):
        self.dept = dept
        self.courseNum = courseNum
        self.courseName = courseName
        self.credits = credits

    # default print of the course class outputs
    def __str__(self):
        return f"{self.dept} {self.courseNum} {self.courseName} {self.credits} credits"

