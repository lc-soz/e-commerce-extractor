from os import listdir
import unicodecsv as csv
import numpy, sys, time, shutil

def backup_data ( file_path, backup_path):
    shutil.copyfile(file_path + "/data.csv", backup_path + "/data-bckp-" + str(int(time.time())))

"""
Function receives an matrix of strings, the
first column is the categorie of that product,
the second the product name and the third it price
and a string, a path to a csv file to add this values
or to start a new table and the name of the header, in
case a csv file already exists.
"""
def csvManip ( matrix_info, path, header ):

    already_exists = False
    for file_name in listdir( path ):
        if (file_name == "data.csv"):
            already_exists = True
    if (not(already_exists)):
        matrix_info[0][2] = header
        with open(path + "/data.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerows(matrix_info)
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

        with open(path + "/data-tmp.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerows(matrix_info)
        cycles = 0
        with open(path + "/data-tmp-" + str(cycles) + ".csv", "w") as f:
            writer = csv.writer(f)
            writer.writerows(matrix_csv)

        real_dif = 1
        while (cycles < 3 and real_dif > 0):
            print "\n"*5
            cycles += 1
            print str(cycles) + "o CYCLE"
            if (cycles > 1):
                for x in prods_inc:
                    print x[0] + "\t" + x[1] + "\t" + x[2]

            k = 0
            dif = 0
            real_dif = 0
            for (i, j) in zip(matrix_csv, matrix_info):
                k += 1
                #sys.stdout.write('.')
                if (i[1] != "" and i[1] == j[1]):
                    i[new_col] = j[2]
                if (i[1] != ""):
                    dif+=1
                    is_present = False
                    for l in matrix_csv:
                        if (l[1] == j[1]):
                            is_present = True
                            l[new_col] = j[2]
                    if (not(is_present)):
                        real_dif+=1
                        print
                        print k
                        print "PRICES ARE EQUAL? " + str(i[new_col-1] == j[2])
                        l = 0;
                        while (i[1][l] == j[1][l]):
                            l += 1
                        print ("OLD: \t" + i[1] + "\t" + i[new_col-1])
                        print ("NEW: \t" + j[1] + "\t" + j[2])
                        print " "*(l+8) + "^"
                        if (i[new_col-1] == j[2]):
                            i[1] = j[1]
                            """
                        answer = raw_input("Substitute name? (y/n) ")
                        if (answer == "y"):
                            print "Yes!"
                            i[1] = j[1]
                            """
                        if (cycles > 1):
                            answer = raw_input("There's a known equal product? (y/n) ")
                            if (answer == 'y'):
                                subs_row = input("Product ROW:")
                                matrix_csv[subs_row][1] = j[1]
                                matrix_csv[subs_row][new_col] = j[2]
                            else:
                                answer = raw_input("Add as a new line? (y/n) ")
                                if (answer == 'y'):
                                    matrix_csv[last_row][0] = j[0]
                                    matrix_csv[last_row][1] = j[1]
                                    matrix_csv[last_row][3] = j[2]
                                    last_row+=1

            m = last_row
            while (matrix_info[m][0] != ""):
                for l in matrix_csv:
                    if (l[1] == matrix_info[m][1]):
                        is_present = True
                        l[new_col] = matrix_info[m][2]
                m+=1

            prods_inc = [["ROW", "NAME", "PRICE"]]
            x = 0
            while (matrix_csv[x][0] !=  ""):
                if (matrix_csv[x][0] != "" and matrix_csv[x][new_col] == ""):
                    prods_inc.append([str(x), matrix_csv[x][1], matrix_csv[x][new_col-1]])
                x+=1

            print str(dif) + " " + str(real_dif)
            with open(path + "/data-tmp-" + str(cycles) + ".csv", "w") as f:
                writer = csv.writer(f)
                writer.writerows(matrix_csv)

    matrix_info.sort(key=lambda x:(x[0] == "", x[0], x[1]))
    with open(path + "/data.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(matrix_csv)
