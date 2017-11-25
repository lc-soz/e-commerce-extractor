from os import listdir
import unicodecsv as csv

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
