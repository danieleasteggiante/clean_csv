import csv

file_con_elementi_da_eliminare = []
file_che_mantiene_tutti_i_record = []
duplicate = []

def delete_empty(file):
    tmp_arr = []
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                row_tmp=[]
                for el in row:
                    row_tmp.append(el.strip())
                if len(row_tmp[2]) > 5: 
                    if ";" in row_tmp[2]:
                        row_tmp[2] = row_tmp[2].split(';')[0]
                    tmp_arr.append(row_tmp)
                    line_count += 1
    return tmp_arr

def search_and_remove_duplicate(fileA, fileB):
    for elA in fileA:
        for elB in fileB:
            if elA == elB:
                print(elA)
                fileA.remove(elA)
    with open('fileA_con_eliminazioni.csv', "w") as f:
        f.write("ID;NOME;EMAIL\n")
        for el in fileA:
            f.write(el[0] + ";" + el[1] + ";" + el[2] + "\n")
    
    f.close()


file_con_elementi_da_eliminare = delete_empty('fileA.csv')
file_che_mantiene_tutti_i_record = delete_empty('fileB.csv')

search_and_remove_duplicate(file_con_elementi_da_eliminare, file_che_mantiene_tutti_i_record)