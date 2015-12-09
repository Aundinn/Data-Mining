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
        aux_vec.append(vec_split[24])
        a = vec_split[25].rstrip('\n')
        aux_vec.append(a)
        matrix.append(aux_vec)
        
    f = open ("test.txt", "w")
    for i in range(1, len(matrix)):
		
		new_line = []
		new_matrix = []
		num_popular = 0
		num_unpopular = 0
		
		#The program is checking if the value of the attribute is 1.0 to then put in the newly created column the name of corresponding data channel
		if float(matrix[i][7]) == 1.0:
			matrix[i].append("Lifestyle")
			string = ""
			for r in matrix[i]:
				string = string + r + ","
			f.write(string.rstrip(","))
			f.write("\n")
		elif float(matrix[i][8]) == 1.0:
			matrix[i].append("Entertainment")
			string = ""
			for r in matrix[i]:
				string = string + r + ","
			f.write(string.rstrip(","))
			f.write("\n")
		elif float(matrix[i][9]) == 1.0:
			matrix[i].append("Business")
			string = ""
			for r in matrix[i]:
				string = string + r + ","
			f.write(string.rstrip(","))
			f.write("\n")
		elif float(matrix[i][10]):
			matrix[i].append("Social Media")
			string = ""
			for r in matrix[i]:
				string = string + r + ","
			f.write(string.rstrip(","))
			f.write("\n")
		elif float(matrix[i][11]):
			matrix[i].append("Tech")
			string = ""
			for r in matrix[i]:
				string = string + r + ","
			f.write(string.rstrip(","))
			f.write("\n")
		elif float(matrix[i][12]) == 1.0:
			matrix[i].append("World")
			string = ""
			for r in matrix[i]:
				string = string + r + ","
			f.write(string.rstrip(","))
			f.write("\n")

    
    f.close()
    file.close()    
    
generate_file(sys.argv[1])
