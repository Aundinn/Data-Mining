'''
Created on 06/11/2015

@author: Aitor
'''
import math
import sys

#Calculation of the percentile
def percentile(data, percentile):
    size = len(data)
    return sorted(data)[int(math.ceil((size * percentile) / 100)) - 1]

def generate_file(name):
    file = open(name, "r")
    matrix = []
    
    #This for is to keep only the columns we want, i.e. removing the ones we don't want
    for line in file:
        vec_split = line.split(",")
        aux_vec = []
        aux_vec.append(vec_split[2])
        aux_vec.append(vec_split[3])
        aux_vec.append(vec_split[7])
        aux_vec.append(vec_split[8])
        aux_vec.append(vec_split[9])
        aux_vec.append(vec_split[10])
        aux_vec.append(vec_split[11])
        aux_vec.append(vec_split[13])
        aux_vec.append(vec_split[14])
        aux_vec.append(vec_split[15])
        aux_vec.append(vec_split[16])
        aux_vec.append(vec_split[17])
        aux_vec.append(vec_split[18])
        aux_vec.append(vec_split[28])
        aux_vec.append(vec_split[29])
        aux_vec.append(vec_split[30])
        aux_vec.append(vec_split[31])
        aux_vec.append(vec_split[32])
        aux_vec.append(vec_split[33])
        aux_vec.append(vec_split[34])
        aux_vec.append(vec_split[35])
        aux_vec.append(vec_split[36])
        aux_vec.append(vec_split[37])
        aux_vec.append(vec_split[38])
        a = vec_split[60].rstrip('\n')
        aux_vec.append(a)
        matrix.append(aux_vec)
    
    
    max = 0
    min = 99999   
    sum = 0 
    vec =  []
    for i in range(1, len(matrix)):
        if float(matrix[i][24]) < min:
            min = int(matrix[i][24])
        if float(matrix[i][24]) > max:
            max = float(matrix[i][24])
        vec.append(float(matrix[i][24]))
    
    #The percentile chosen is 50, so above is "Popular" and below is "Unpopular"
    perc = percentile(vec, 50)
    print("Max: ", int(max))
    print("Min: ", int(min))
    print("Percentile 50: ", perc)
    
    new_matrix = []
    num_popular = 0
    num_unpopular = 0
    f = open ("prepro_data.txt", "w")
    
    for i in range(1, len(matrix)):
        if float(matrix[i][24]) < perc:
            new_line = matrix[i]
            new_line[24] = 'Unpopular'
            num_unpopular += 1
        else:
            new_line = matrix[i]
            new_line[24] = 'Popular'
            num_popular += 1
        string = ""
        for r in new_line:
            string = string + r + ","
            f.write(string.rstrip(","))
        f.write(string)
        f.write("\n")
    
    print("Number of Popular: ", num_popular)
    print("Number of Unpopular: ", num_unpopular)
    f.close()
    file.close()    
    
generate_file(sys.argv[1])
