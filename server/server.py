from http.server import BaseHTTPRequestHandler, HTTPServer
import math
import random
	
import os


database = {}
percentiles = {}

names = ["n_tokens_title", "n_tokens_content", "num_hrefs", "num_self_hrefs", "num_imgs", "num_videos", "average_token_length",
         "channel", "self_reference_min_shares", "self_reference_max_shares",
         "self_reference_avg_shares", "weekday", "shares"]

names2 = ["n_tokens_title", "n_tokens_content", "num_hrefs", "num_self_hrefs", "num_imgs", "num_videos", "average_token_length",
         "channel", "self_reference_min_shares", "self_reference_max_shares",
         "self_reference_avg_shares", "weekday"]

names3 = ["n_tokens_content", "num_imgs" ,"channel", "weekday"]
names4 = ["n_tokens_content", "num_imgs" ,"channel", "weekday", "shares"]



#Classification code

#load the file into a dictonary
def create_dict(name):
    file = open(name, "r")
    dataset = {}
    for i in range(len(dataset)):
        dataset[names[i]] = []

    primeraLinea = True
    for line in file:
        i = 0
        if primeraLinea == False:
            line = line.split(",")
            for obj in line:
                if dataset.__contains__(names[i]):
                    list = dataset.get(names[i])
                    list.append(obj)
                    dataset[names[i]] = list
                    
                else:
                    list = []
                    list.append(obj)    
                    dataset[names[i]] = list
                i += 1
        primeraLinea = False
    file.close()
    return dataset

names_used = set()
dataset = create_dict("../Data/current_data.csv")
DIV = 4.72

def entropy_decision(dataset, name, value):
    shares = dataset.get(name)
    total = len(shares)
    vector = []
    used = set()
    for i in range(len(shares)):
        if value == None:
            if shares[i] in used:
                for j in range(len(vector)):
                    if vector[j][0] == shares[i]:
                        aux = (shares[i], vector[j][1]+1)
                        vector.remove(vector[j])
                        vector.append(aux)
                        break
            else:
                vector.append((shares[i], 1))
                used.add(shares[i])
        else:
            if shares[i] == value:
                if shares[i] in used:
                    for j in range(len(vector)):
                        if vector[j][0] == shares[i]:
                            aux = (shares[i], vector[j][1]+1)
                            vector.remove(vector[j])
                            vector.append(aux)
                            break
                else:
                    vector.append((shares[i], 1))
                    used.add(shares[i])
    
    first = True
    for t in vector:
        if first:
            entropy = -(t[1]/total) * math.log2(t[1]/total)
            first = False
        else:
            entropy -= (t[1]/total) * math.log2(t[1]/total)
    return entropy
    
def compute_entropy(row, dataset, name, value):
    shares = dataset.get(name)
    total = len(shares)
    vector = dataset.get(names[row])
    used = set()
    tuples = []
    cont = 0
    entropy = 0
    
    for i in range(total):
        a = random.uniform(0, 100)
        if value == None:
            if a < 100: 
                if (vector[i],shares[i]) not in used:
                    cont += 1
                    used.add((vector[i],shares[i]))
                    tuples.append(((vector[i],shares[i]),1))
                    
                else:
                    for t in tuples:
                        if t[0] == (vector[i],shares[i]):
                            cont += 1
                            tuples.append((t[0], t[1]+1))
                            tuples.remove(t)
                            break
        else:
            if vector[i] == value:
                if a < 1: 
                    if (vector[i],shares[i]) not in used:
                        cont += 1
                        used.add((vector[i],shares[i]))
                        tuples.append(((vector[i],shares[i]),1))
                        
                    else:
                        for t in tuples:
                            if t[0] == (vector[i],shares[i]):
                                cont += 1
                                tuples.append((t[0], t[1]+1))
                                tuples.remove(t)
                                break
            
    first = True
    for i in range(len(tuples)):
        for j in range(i+1, len(tuples)):
            if tuples[i][0][0] == tuples[j][0][0]:
                if first:
                    sum = tuples[i][1]+tuples[j][1]
                    entropy = (sum/total) * (-tuples[i][1]/sum * math.log2(tuples[i][1]/sum) - tuples[j][1]/sum * math.log2(tuples[j][1]/sum))
                    first = False
                else:
                    sum = tuples[i][1]+tuples[j][1]
                    entropy += (sum/total) * (-tuples[i][1]/sum * math.log2(tuples[i][1]/sum) - tuples[j][1]/sum * math.log2(tuples[j][1]/sum))                
    return entropy

def find_bigger(vector):
    max = 0
    obj = None
    for i in range(len(vector)):
        if vector[i][1] > max:
            max = vector[i][0]
            obj = vector[i]
    return max, obj

def find_values(name):
    ve = dataset.get(name)
    val = []
    for vo in ve:
        if vo not in val:
            val.append(vo)
    return val

def main(name, value):
    decision_entropy = entropy_decision(dataset, name, value)
    #print("Entropy of Decision: {}" .format(decision_entropy))
    v = []
    for i in range(len(dataset)-1):
        if names[i] not in names_used:
            entropy = compute_entropy(i, dataset, name, value)
            #print("Value: {} Entropy: {}" .format(i+1, entropy))
            val = decision_entropy - entropy
            v.append((i, val))
    return v

def initialLoop(name, article, deep, vector, num):
    deep += 1
    vector = main(name, None)
    bigger, obj = find_bigger(vector)
    names_used.add(names[bigger])
    a = find_values(names[bigger])
    tam = len(a)

    for i in range(tam):
        if article[bigger] == a[i]:
            r = loop(names[bigger], a[i], article, deep, vector, num)
    return r

def loop(name, value, article, deep, vector, num):
    deep += 1
    num += vector[0][1]
#     if vector[0][1] == 0:
#         print("Unpopular")
#         return "Unpopular"
    if deep == len(dataset):
        print(num)
        if num > DIV:
            print("Unpopular")
            names_used.clear()
            return "Unpopular"
        else:   
            print("Popular")
            names_used.clear()
            return("Popular")

    vector = main(name, value)
    bigger,obj = find_bigger(vector)
    names_used.add(names[bigger])
    a = find_values(names[bigger])
    tam = len(a)
    for j in range(tam):
        if article[bigger] == a[j]:
            r = loop(names[bigger], a[j], article, deep, vector, num)
    return r

#start the classification (init is the entry point for starting the prediction and getting the result back)
def init(article):
    vec = main("shares", None)
    number = 0
    deep = 0
    prediction = initialLoop("shares", article, deep, vec, number)
    names_used.clear()
    return prediction

#end classification


#returns the percentiles of the attributes in the used dataset
#this function is needed to convert the input from the user to the discretized values
def build_percentile():
	percentiles = {}

	percentiles["n_tokens_title"] = [9.0,12.0]
	percentiles["n_tokens_content"] = [246.0,716.0]
	percentiles["num_hrefs"] = [4.0,14.0]
	percentiles["num_self_hrefs"] = [1.0,4.0]
	percentiles["num_imgs"] = [1.0,4.0]
	percentiles["num_videos"] = [0.0,4.0]
	percentiles["average_token_length"] = [4.4784,4.85483870968]
	percentiles["self_reference_min_shares"] = [639.0,2600.0]
	percentiles["self_reference_max_shares"] = [1100.0,8000.0]
	percentiles["self_reference_avg_shares"] = [981.0,5200.0]

	return percentiles

#analyzes the request string for the parameters and returns them as
#dictonary where the parameter names are used as keys
def get_parameters(parameter, parameter_names):
	global percentiles
	argument_values = {}
	size = len(parameter)
	for a in parameter_names:
		print(a)
		value = ''
		i = parameter.find(a)
		if i != -1:
			i += len(a) +1
			while(i < size and parameter[i] != '?'):
				value += parameter[i]
				i += 1
			print(value)
			if a == "weekday" or a == "channel":
				argument_values[a] = value
			else:
				number = float(value)
				if number < percentiles[a][0]:
					argument_values[a] = "Few"
				elif number > percentiles[a][1]:
					argument_values[a] = "Many"
				else:
					argument_values[a] = "Normal"
		else:
			print("could not find name: " + a)
	return argument_values


#is called when the request string begins with 'query' (from list articles view)
def handle_query(self, argument_values):
	global database
	global names3
	global names
	self.send_response(200)
	self.send_header('Content-type', 'text-html')
	self.end_headers()
	return_value = "The Overview for the database"
	
	return_value = "<table id='my_table'><tr>"
	for name in names:
		return_value += "<th>" + name+ "</th>"

	print("Expect the database")
	return_value += "</tr>"

	n = len(database[names3[0]])
	for i in range(0,n):
		in_range = True
		value = "<tr>"
		for name in names:
			value += "<th>" + str(database[name][i]) + "</th>"
	
			#if name == "channel" or name=="weekday":
			if name in names3:
				if database[name][i] != argument_values[name]:
					print(name + " " + str(database[name][i]) + ": " + str(argument_values[name]))
					in_range = False
		if in_range:
			value += "</tr>"
			return_value += value
			print("inRange")
		#else:
		#	print "not in Range"

	return_value += "</table>"

	self.wfile.write(bytes(return_value, "utf8"))
	return

#is called when the request string begins with 'predic' (from the Predict View)
def handle_request(self, argument_values):
		self.send_response(200)
		self.send_header('Content-type', 'text-html')
		self.end_headers()


		return_value = "The values are: " + str(argument_values)
		classification_arguments = []
		for n in names2:
			classification_arguments.append(argument_values[n])


		classification_arguments.append("Unpopular")
		print(classification_arguments)
		
		return_value = "The classification of the article is: " 
		return_value += init(classification_arguments)

		print("The returned value is: " + str(return_value))
		self.wfile.write(bytes(return_value, "utf8"))
		print("send_value")
		return





class myHTTPServerRequestHandler(BaseHTTPRequestHandler):

	def do_POST(self):
		self.send_response(200)
		self.send_header('Content-type', 'text-html')
		return_value = "Post"
		print(return_value)
		self.wfile.write(return_value)
		return



	def do_GET(self):
		global names2
		global names3
		print(self)
		print(self.path)
		root = "../Interface/"
		try: 
			if self.path.endswith('.html') or self.path.endswith('.js') or self.path.endswith('.png') or self.path.endswith('.css'):
				f = open(root + self.path, 'rb')

				self.send_response(200)
				if self.path.endswith('.html'):
					self.send_header('Content-type', 'text-html')
				elif self.path.endswith('.css'):
					self.send_header('Content-type', 'text')
				else:
					self.send_header('Content-type', 'text-html')

				self.end_headers()

				self.wfile.write(f.read())
				f.close()
				return
			else:
				path = self.path
				i = path.find('?')
				parameter = ''
				request = ''
				if i != -1:
					parameter = path[i:]
					request = path[:i]

				print(request)
				print(parameter)
				if request == '/predict':
					arguments = get_parameters(parameter, names2)
					handle_request(self, arguments)
				elif request == '/query':
					arguments = get_parameters(parameter, names3)
					handle_query(self, arguments)

				return


		except IOError:
			print("Was not able to open " + self.path)
			self.send_error('404', "File was not available or could not be found")

#initial startup for the server
#load the database
#and start the HTTP server	
def run():
	global database	
	global percentiles
	print("Starting the Script")
	print ("Load Data")
	database = create_dict("../Data/current_data.csv")
	#print(database["self_reference_avg_shares"])
	percentiles = build_percentile()
	server_address = ("127.0.0.1", 2000)
	httpd = HTTPServer(server_address, myHTTPServerRequestHandler)
	print("Started the Server")

	httpd.serve_forever()

if __name__ == '__main__':
	run()