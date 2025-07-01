##################################
### Created: July 1, 2025
### Author: Devin Hunt
### DS510 Assignment 5 Part B
### Description: This program imports a CSV file, perform data manipulations, and output the file to a new CSV
### Inputs: weather.csv
### Packages: csv
### Output: out.csv
### References: some snippits of code and logic borrowed from code snippets by Loren Rhodes and Gerald Kruse
##################################

import csv

# infile = input("Input csv file name: ")
# outfile = input("Output csv file name")
infile = "weather.csv"
outfile = "weatherOutput.csv"

outfile = open(outfile, 'w', newline = '')
out_writer = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

with open(infile) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = True

    for row in csv_reader:
        if header:
            # Use row.index to find the variable value we want to place rather than attempting to find it manually
            # save it as a variable to manipulate in data rows below
            # create dictionary with the field name as key and index as value.
            csvIndex = {}
            for i in range(0,len(row)):
                csvIndex[row[i]] = i
            
            row[csvIndex["low_wind"]] = "gust_wind"
            print(row)
            header = False # no more headers
        else: #row is data
            # if gust is NA then replace with high_wind value
            if row[csvIndex["low_wind"]] == "NA":
                row[csvIndex["low_wind"]] = row[csvIndex["high_wind"]]

            # if precip is "T" replace with 0.001
            if row[csvIndex["precip"]] == "T":
                row[csvIndex["precip"]] = "0.001"

            # format precip to two decimals
            row[csvIndex["precip"]] = "{:.2f}".format(float(row[csvIndex["precip"]]))

            print(row)

        #drop first column by starting at column 1 instead of 0  
        out_writer.writerow(row[1:])

#close the files
csv_file.close()
outfile.close()
