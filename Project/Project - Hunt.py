
import os
os.chdir('c:\\Users\\devin\\OneDrive\\Documents\\positron\\DS510\\Project')

from Course import Course
from GPA import *
from Student import *

jd111 = Student("111", "John", "Doe")
jdcourses = jd111.getCourses()

jdcourses[0].getQualityPoints()


