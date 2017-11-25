# -*- coding: utf-8 -*-
from os import listdir
import io

"""
Function receives an path to a folder.
Returns a matrix of strings, the first
column being the categorie of the product
and  the second the title and price.
"""
def getText ( path ):
    matrix = [["".encode('utf-8') for i in range(2)] for j in range(10)]
    for file_name in listdir( path ):
        with open (path + '/' + file_name, "r") as myfile:
            raw_html = myfile.read()
        row = 0;
        while (matrix[row][0] != file_name[0:15] and matrix[row][0] != ""):
            row += 1;
        raw_html = raw_html.decode('iso-8859-1')
        raw_html = raw_html.encode('utf-8')
        if (matrix[row][0] == ""):
            matrix[row][0] = file_name[0:15]
            matrix[row][1] = raw_html
        else:
            matrix[row][1] += "\n" + raw_html
    return matrix
