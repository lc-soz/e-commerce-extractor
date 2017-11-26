import extractInfo, getText, csvManip

path = "/home/lclpsoz/Dropbox/Pessoal/KABUM"
print ("HTML TO TEXT")
matrix = getText.getText( path + "/html/17-11-24-0557" )
print ("TEXT TO MATRIX")
matrix_info = extractInfo.extractInfo( matrix )
print ("INTERFACE")
csvManip.csvManip ( matrix_info, path , "17-11-24-0557")
