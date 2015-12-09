import math
import sys

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
        
    f = open ("test.txt", "w")
    for i in range(1, len(matrix)):
		
		new_line = []
		new_matrix = []
		num_popular = 0
		num_unpopular = 0
		
		#The program is checking if the value of the attribute is 1.0 to then put in the newly created column the name of corresponding weekday
		if float(matrix[i][17]) == 1.0:
			matrix[i].append("Tuesday")
			string = ""
			for r in matrix[i]:
				string = string + r + ","
			f.write(string.rstrip(","))
			f.write("\n")
		elif float(matrix[i][18]) == 1.0:
			matrix[i].append("Wednesday")
			string = ""
			for r in matrix[i]:
				string = string + r + ","
			f.write(string.rstrip(","))
			f.write("\n")
		elif float(matrix[i][19]) == 1.0:
			matrix[i].append("Thursday")
			string = ""
			for r in matrix[i]:
				string = string + r + ","
			f.write(string.rstrip(","))
			f.write("\n")
		elif float(matrix[i][20]):
			matrix[i].append("Friday")
			string = ""
			for r in matrix[i]:
				string = string + r + ","
			f.write(string.rstrip(","))
			f.write("\n")
		elif float(matrix[i][21]):
			matrix[i].append("Saturday")
			string = ""
			for r in matrix[i]:
				string = string + r + ","
			f.write(string.rstrip(","))
			f.write("\n")
		elif float(matrix[i][22]) == 1.0:
			matrix[i].append("Sunday")
			string = ""
			for r in matrix[i]:
				string = string + r + ","
			f.write(string.rstrip(","))
			f.write("\n")
		elif float(matrix[i][16]) == 1.0:
			matrix[i].append("Monday")
			string = ""
			for r in matrix[i]:
				string = string + r + ","
			f.write(string.rstrip(","))
			f.write("\n")

    
    f.close()
    file.close()    
    
generate_file(sys.argv[1])
