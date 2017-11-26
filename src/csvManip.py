from os import listdir
import unicodecsv as csv
import numpy
import sys

"""
Function receives an matrix of strings, the
first column is the categorie of that product,
the second the product name and the third it price
and a string, a path to a csv file to add this values
or to start a new table.
"""
def csvManip ( matrix_info, path ):
    already_exists = True;
    for file_name in listdir( path ):
        if (file_name == "data.csv"):
            already_exists = True;

    if (not(already_exists)):
        with open(path + "/data.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerows(matrix_info)
    else:
        with open(path + "/data.csv", "r") as f:
            reader = csv.reader(f, delimiter=',')
            matrix_csv = list(reader)

    k = 0
    dif = 0
    real_dif = 0
    for (i, j) in zip(matrix_csv, matrix_info):
        k += 1
        #sys.stdout.write('.')
        if (i[1] != "" and i[1] != j[1]):
            dif+=1
            is_present = False
            for l in matrix_csv:
                if (l[1] == j[1]):
                    is_present = True
            if (not(is_present)):
                real_dif+=1
                print
                print (k)
                print ("\t" + i[1])
                print ("\t" + j[1])
    print str(dif) + " " + str(real_dif)
