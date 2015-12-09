import math
import sys

def percentile(data, percentile):
    size = len(data)
    return sorted(data)[int(math.ceil((size * percentile) / 100)) - 1]

def generate_file(name):
    file = open(name, "r")
    matrix = []   
    
    for line in file:
        vec_split = line.split(",")
        aux_vec = []
        aux_vec.append(vec_split[0])
        aux_vec.append(vec_split[1])
        aux_vec.append(vec_split[2])
        aux_vec.append(vec_split[3])
        aux_vec.append(vec_split[4])
        aux_vec.append(vec_split[5])
        aux_vec.append(vec_split[6])
        aux_vec.append(vec_split[7])
        aux_vec.append(vec_split[8])
        aux_vec.append(vec_split[9])
        aux_vec.append(vec_split[10])
        aux_vec.append(vec_split[11])
        aux_vec.append(vec_split[12])
        aux_vec.append(vec_split[13])
        aux_vec.append(vec_split[14])
        aux_vec.append(vec_split[15])
        aux_vec.append(vec_split[16])
        aux_vec.append(vec_split[17])
        aux_vec.append(vec_split[18])
        aux_vec.append(vec_split[19])
        aux_vec.append(vec_split[20])
        aux_vec.append(vec_split[21])
        aux_vec.append(vec_split[22])
        aux_vec.append(vec_split[23])
        a = vec_split[24].rstrip('\n')
        aux_vec.append(a)
        matrix.append(aux_vec)
        
    list = [0,1,2,3,4,5,6,13,14,15]   #List of the columns on which the algorithm will make a change
    for j in list:
		max = 0
		min = 99999   
		sum = 0 
		vec =  []
		for i in range(1, len(matrix)):
		    if float(matrix[i][j]) < min:
		        min = float(matrix[i][j])
		    if float(matrix[i][j]) > max:
		        max = float(matrix[i][j])
		    vec.append(float(matrix[i][j]))
		
		perc = percentile(vec, 25)
		print("Percentile 25: ", perc)
		
		perc2 = percentile(vec, 75)
		print("Percentile 75: ", perc2)
		
		new_matrix = []
		num_popular = 0
		num_unpopular = 0
		f = open ("test.txt", "w")
		
		#Below 25 will be "Few", above will be "Many" and in between will be "Normal"
		for i in range(1, len(matrix)):
		    if float(matrix[i][j]) < perc:
		        new_line = matrix[i]
		        new_line[j] = 'Few'
		    elif float(matrix[i][j]) > perc and float(matrix[i][j]) < perc2:
		        new_line = matrix[i]
		        new_line[j] = 'Normal'
		    else:
		        new_line = matrix[i]
		        new_line[j] = 'Many'
		    string = ""
		    for r in new_line:
		        string = string + r + ","
		    f.write(string.rstrip(","))
		    f.write("\n")
    
    f.close()
    file.close()    
    
generate_file(sys.argv[1])
