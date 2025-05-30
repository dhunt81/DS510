"""
DS510 Assignment 1 - Part D
Author: Devin Hunt
Created: May 29, 2025
Description: Prompt user for 2 inputs and create HTML tag of first and append to second.
"""

""" Assignment Text
Write a Python program to prompt for two input strings, (1) an HTML (or XML) tag and (2) a content string.  

An HTML tag is in instruction in a web page.  It contains two parts: a start tag and an end tag.  
The only difference is that the end tag has a / in it.  The two tags surround some content.  
You don't really need to know anything else about HTML for this little program.

Thus, your code should output an HTML string with start and end tags wrapped around the content string.   
An HTML start tag is in a web page is enclosed in angle brackets <tag > and an end tag appears as </tag>
You do not have to verify the html tag as legal HTML; any word of one or more letters can stand as a 
tag which is true actually for XML.
"""

#Prompt user for input strings
tag = input("Enter an HTML or XML tag: ")
content = input("Enter a string of content: ")

# create html or xml tags from input
taggedString = "<{0}>{1}</{0}>".format(tag,content)

#print the output
print(taggedString)


""" Console Output of Testing
>>> %run "c:\\Users\\devin\\OneDrive\\Documents\\positron\\DS510\\Assignment 1\\Assignment 1D - Hunt.py"
Enter an HTML or XML tag: 
i
Enter a string of content: 
italics
<i>italics</i>
>>> %run "c:\\Users\\devin\\OneDrive\\Documents\\positron\\DS510\\Assignment 1\\Assignment 1D - Hunt.py"
Enter an HTML or XML tag: 
em
Enter a string of content: 
bolded
<em>bolded</em>
>>> %run "c:\\Users\\devin\\OneDrive\\Documents\\positron\\DS510\\Assignment 1\\Assignment 1D - Hunt.py"
Enter an HTML or XML tag: 
h1
Enter a string of content: 
Header 1 content. Such as a title.
<h1>Header 1 content. Such as a title.</h1>
>>>
"""