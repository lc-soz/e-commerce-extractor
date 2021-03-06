# coding=utf-8
from bs4 import BeautifulSoup
import numpy as np
import getText

"""
Function receives an matrix of strings,
the first column being the the categorie
of the product in that row, and the second
the product name and price. Returns a matrix
of categories, names and prices, ordered by name.
"""
def extractInfo ( matrix_strings ):

    matrix_info = [["".encode('utf-8') for i in range(3)] for j in range(4000)]
    matrix_info[0][0] = "CATEGORIES"
    matrix_info[0][1] = "TITLE"
    matrix_info[0][2] = "PRICE"
    row = 1;

    guide = [["" for i in range(2)] for j in range (8)]
    guide = [["Memória RAM - ", "RAM"],
             ["Disco Rígido (", "HD"],
             ["Placas-mãe - H", "MB"],
             ["Processadores -", "CPU"],
             ["Coolers - Hardw", "COOLERS"],
             ["Fontes - Hardwa", "PSU"],
             ["Placa de vídeo", "GPU"],
             ["SSD 2.5_ - Hard", "SSD"]]

    for i in range(8):
        test = -1;
        for j in range(8):
            if (matrix_strings[i][0] == guide[j][0]):
                test = j;
        if (test == -1):
            categorie = matrix_strings[i][0]
        else:
            categorie = guide[test][1]
        print "\t" + categorie
        data_html = BeautifulSoup(matrix_strings[i][1], 'html.parser')
        product = data_html.findAll( "div", { "class" : "listagem-box"})
        for i in product:
            j = i.find( "span", { "class" : "H-titulo"})
            k = i.find( "div", { "class" : "listagem-preco"})
            if (k == None):
                k = i.find( "div", { "class" : "listagem-precoavista"})
            matrix_info[row][0] = categorie
            matrix_info[row][1] = j.string.lstrip().rstrip()
            matrix_info[row][2] = k.string[3:]
            # print matrix_info[row][1][0:100] + "\t" + matrix_info[row][2]
            row += 1

    print "\tSORTING"
    matrix_info.sort(key=lambda x:(x[0] == "", x[0], x[1]))
    return matrix_info
