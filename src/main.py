import extractInfo
import getText
import csvManip

path = "/home/lclpsoz/Dropbox/Pessoal/KABUM"
print "HTML TO TEXT"
matrix = getText.getText( path + "/html/17-11-24-0557" )
print "TEXT TO MATRIX"
matrix_info = extractInfo.extractInfo( matrix )
print "INTERFACE"
csvManip.csvManip ( matrix_info, path )

k = 0;
f = open('/home/lclpsoz/Dropbox/Pessoal/KABUM/out-24.txt', 'w')
f.write("")
f.close
f = open('/home/lclpsoz/Dropbox/Pessoal/KABUM/out-24.txt', 'a')
while (matrix_info[k][0] != ""):
    f.write(matrix_info[k][0].encode('utf-8') + "|" + matrix_info[k][1].encode('utf-8') + "|" + matrix_info[k][2].encode('utf-8') + '\n')
    k+=1
f.close
