import os

def fileExists(studentId):
        # module to check if student file exists already by student ID
        # create list of files from directory
        student_files = os.listdir("./data")

        # use list comprehensions to extract the student ids from each file and store as list
        student_ids = [file.split("-")[0] for file in student_files]
        student_fname = [file.split("-")[1] for file in student_files]
        student_lname = [file.split("-")[2].removesuffix(".csv") for file in student_files]

        # check if student file exists in directory already and return bool value
        exists = studentId in student_ids
        if exists:
            loc = student_ids.index(studentId)
            studentFname = student_fname[loc]
            studentLname = student_lname[loc]
        else:
            studentFname = ''
            studentLname = ''

        #Create a tuple that contains the boolean exists and the student name for calling later
        returnTuple = (exists, studentId, studentFname, studentLname)

        return returnTuple
