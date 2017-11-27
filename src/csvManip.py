from os import listdir
import unicodecsv as csv
import numpy, sys, time, shutil
"""
Function receives a path to a data.csv file
and a path to a backup folder. It will copy
the file to the backup_path with a time
in seconds concateneted to make it unique.
"""
def backup_data ( file_path, backup_path):
    shutil.copyfile(file_path + "/data.csv", backup_path + "/data-bckp-" + str(int(time.time())) + ".csv")

"""
Function receives a matrix, a path and a
file name. Save the matrix_to_save to the
path received with the name of the string
in file_name as a csv file.
"""
def save_matrix ( matrix_to_save, path, file_name ):
    with open(path + "/" + file_name + ".csv", "w") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(matrix_to_save)

"""
Function receives two matrix and a value
new_col. Returns both of them with the
first one with the values of the second
one in the new_col column if the second
column is equal in that row. It also
deletes used rows from matrix_info.
"""
def match_same_line ( matrix_csv, matrix_info, new_col ):
    i = 1
    while (i < len(matrix_csv) and i < len(matrix_info) and matrix_csv[i][0] != "" and matrix_info[i][0] != ""):
        if (matrix_csv[i][1] == matrix_info[i][1]):
            matrix_csv[i][new_col] = matrix_info[i][2]
            matrix_info[i][0] = "D"
        i+=1
    i = 1
    while (i < len(matrix_info)):
        if (matrix_info[i][0] == "D" or matrix_info[i][0] == ""):
            del (matrix_info[i])
        else:
            i+=1
    return matrix_csv, matrix_info

"""
Function receives two matrix and a value
new_col. Returns both of them with the
first one with the values of the second
one in the new_col column if the second
column is equal in some row, will search
the value of the second matrix in the first.
"""
def match_dif_line ( matrix_csv, matrix_info, new_col ):
    i = 1
    while (i < len(matrix_csv) and i < len(matrix_info) and matrix_info[i][0] != ""):
        for row_csv in matrix_csv:
            if (row_csv[1] == matrix_info[i][1]):
                row_csv[new_col] = matrix_info[i][2]
                matrix_info[i][0] = "D"
                break
        i+=1
    i = 1
    while (i < len(matrix_info)):
        if (matrix_info[i][0] == "D" or matrix_info[i][0] == ""):
            del (matrix_info[i])
        else:
            i+=1
    return matrix_csv, matrix_info

"""
Function receives a matrix of strings, the
first column is the categorie of that product,
the second the product name and the third it price
and a string, a path to a csv file to add this values
or to start a new table and the name of the header, in
case a csv file already exists.
"""
def csvManip ( matrix_info, path, header ):

    # Tests if data.csv file already exists
    already_exists = False
    for file_name in listdir( path ):
        if (file_name == "data.csv"):
            already_exists = True
    # If not, create new
    if (not(already_exists)):
        matrix_info[0][2] = header
        save_matrix(matrix_info, path, "data")
    # If yes, will insert new rows and/or columns as needed
    else:
        backup_data ( path, path + "/bckp")
        with open(path + "/data.csv", "r") as f:
            reader = csv.reader(f, delimiter=',')
            matrix_csv = list(reader)

        new_col = len(matrix_csv[0])
        matrix_csv = [x + [""] for x in matrix_csv]
        matrix_csv[0][new_col] = header
        matrix_info[0][2] = header

        last_row = 0
        while (matrix_csv[last_row][0] != ""):
            last_row += 1

        save_matrix(matrix_info, path, "data-" + header)
        cycles = 0
        save_matrix(matrix_csv, path, "data-csv-" + str(cycles))

        real_dif = 1
        prices_equal_subs = "m"
        while (cycles < 3 and real_dif > 0):
            print "\n"*50
            cycles += 1
            print str(cycles) + "o CYCLE"

            k = 0
            real_dif = 0
            matrix_csv, matrix_info = match_same_line(matrix_csv, matrix_info, new_col)
            matrix_csv, matrix_info = match_dif_line(matrix_csv, matrix_info, new_col)
            print "ALL THAT IS LEFT IN INFO:"
            print "_"*181
            for row_info in matrix_info:
                print ("|{:^12s}|{:<150s}|{:^15s}|".format(row_info[0].encode('utf-8'), row_info[1].encode('utf-8'), row_info[2].encode('utf-8')))
            print "_"*181
            print "ALL THAT IS LEFT IN CSV:"
            print "_"*181
            print ("|{:^12s}|{:<150s}|{:^15s}|".format(matrix_csv[0][0].encode('utf-8'), matrix_csv[0][1].encode('utf-8'), matrix_csv[0][2].encode('utf-8')))
            for row_csv in matrix_csv:
                if (row_csv[3] == "" and row_csv[0] != ""):
                    print ("|{:^12s}|{:<150s}|{:^15s}|".format(row_csv[0].encode('utf-8'), row_csv[1].encode('utf-8'), row_csv[2].encode('utf-8')))
            print "_"*181
            for (i, j) in zip(matrix_csv, matrix_info):
                k += 1
                if (i[1] == "" or j[1] == ""):
                    break
                elif (i[1] != "TITLE"):
                    real_dif+=1
                    print
                    print k
                    if (i[new_col-1] == j[2]):
                        print "PRICES ARE EQUAL!"
                    else:
                        print "PRICES ARE DIFFERENT!"
                    l = 0;
                    while (l < len (i[1]) and l < len(j[1]) and i[1][l] == j[1][l]):
                        l += 1
                    print ("OLD: \t" + i[1] + "\t" + i[new_col-1])
                    print ("NEW: \t" + j[1] + "\t" + j[2])
                    print " "*(l+8) + "^"
                    if (i[new_col-1] == j[2]):
                        answer = "y"
                    elif (cycles > 1):
                        answer = raw_input("Substitute name? (y/n) ")
                    else:
                        answer = "n"
                    if (answer == "y"):
                        i[1] = j[1]
                    elif (cycles > 1):
                        for x in prods_inc:
                            if (x[0] == j[0]):
                                if (x[0] == "GPU"):
                                    if (x[2][19:30] == j[1][19:30]):
                                        print x[0] + "\t" + x[1] + "\t" + x[2][19:] + "\t" + x[3]
                                else:
                                    print x[0] + "\t" + x[1] + "\t" + x[2] + "\t" + x[3]
                        are_sure = "n"
                        answer = raw_input("There's a known equal product? (y/n) ")
                        while (answer == 'y' and are_sure == "n"):
                            subs_row = input("Product row:")
                            l = 0
                            while (matrix_csv[subs_row][1][l] == j[1][l]):
                                l += 1
                            print ("OLD: \t" + matrix_csv[subs_row][1] + "\t" + matrix_csv[subs_row][2])
                            print ("NEW: \t" + j[1] + "\t" + j[2])
                            print " "*(l+8) + "^"
                            are_sure = raw_input("Are you sure? (y/n)")
                            if (are_sure == "y"):
                                matrix_csv[subs_row][1] = j[1]
                                matrix_csv[subs_row][new_col] = j[2]
                                x = 0;
                                while (x < len(prods_inc)):
                                    if (prods_inc[x][1] == subs_row):
                                        del(pro_inc[x])
                                    x+=1
                            else:
                                answer = raw_input("There's a known equal product? (y/n) ")
                        if (answer == 'n'):
                            answer = raw_input("Add as a new product? (y/n) ")
                            if (answer == 'y'):
                                matrix_csv[last_row][0] = j[0]
                                matrix_csv[last_row][1] = j[1]
                                matrix_csv[last_row][3] = j[2]
                                last_row+=1

            matrix_csv, matrix_info = match_dif_line(matrix_csv, matrix_info, new_col)

            prods_inc = [["CAT" , "ROW", "NAME", "PRICE"]]
            x = 0
            while (matrix_csv[x][0] !=  ""):
                if (matrix_csv[x][0] != "" and matrix_csv[x][new_col] == ""):
                    prods_inc.append([matrix_csv[x][0], str(x), matrix_csv[x][1], matrix_csv[x][new_col-1]])
                x+=1

            print "REAL DIF: " + str(real_dif)
            save_matrix(matrix_csv, path, "data-csv-" + str(cycles))

        matrix_csv.sort(key=lambda x:(x[0] == "", x[0], x[1]))
        save_matrix(matrix_csv, path, "data")
