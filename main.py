import extractInfo
import getText

path = "/home/lclpsoz/Dropbox/prog/PYTHON/KABUM/Saved Tabs"
matrix = getText.getText( path )
matrix_info = extractInfo.extractInfo( matrix )

k = 0;
f = open('out.txt', 'w')
f.write("")
f.close
f = open('out.txt', 'a')
while (matrix_info[k][0] != ""):
    f.write(matrix_info[k][0].encode('utf-8') + "|" + matrix_info[k][1].encode('utf-8') + "|" + matrix_info[k][2].encode('utf-8') + '\n')
    k+=1
f.close
