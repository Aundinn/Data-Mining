from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import os

database = {}
percentiles = {}

names = ["n_tokens_title", "n_tokens_content", "num_hrefs", "num_self_hrefs", "num_imgs", "num_videos", "average_token_length",
         "channel", "self_reference_min_shares", "self_reference_max_shares",
         "self_reference_avg_shares", "weekday", "shares"]

names2 = ["n_tokens_title", "n_tokens_content", "num_hrefs", "num_self_hrefs", "num_imgs", "num_videos", "average_token_length",
         "channel", "self_reference_min_shares", "self_reference_max_shares",
         "self_reference_avg_shares", "weekday"]

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

def get_parameters(parameter):
	global names2
	global percentiles
	argument_values = {}
	size = len(parameter)
	for a in names2:
		print a
		value = ''
		i = parameter.find(a)
		if i != -1:
			i += len(a) +1
			while(i < size and parameter[i] != '?'):
				value += parameter[i]
				i += 1
			print value
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
			print "could not find name: " + a 
	return argument_values



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
    return dataset

def handle_query(self, argument_values):
	global database
	global names2
	self.send_response(200)
	self.send_header('Content-type', 'text-html')
	self.end_headers()
	return_value = "The Overview for the database"
	
	return_value = "<table><tr>"
	for name in names:
		return_value += "<th>" + name+ "</th>"

	print "Expect the database"
	return_value += "</tr>"

	n = len(database[names2[0]])
	for i in xrange(n):
		in_range = True
		value = "<tr>"
		for name in names2:
			value += "<th>" + str(database[name][i]) + "</th>"
	
			if name == "channel" or name=="weekday":
			#if True:
				if database[name][i] != argument_values[name]:
					print name + " " + str(database[name][i]) + ": " + str(argument_values[name])
					in_range = False
		if in_range:
			value += "</tr>"
			return_value += value
			print "inRange"
		#else:
		#	print "not in Range"

	return_value += "</table>"

	self.wfile.write(return_value)
	return


def handle_request(self, argument_values):
		self.send_response(200)
		self.send_header('Content-type', 'text-html')
		self.end_headers()


		return_value = "The values are: " + str(argument_values)
		print return_value
		self.wfile.write(return_value)
		print "send_value"
		return


class myHTTPServerRequestHandler(BaseHTTPRequestHandler):

	def do_POST(self):
		self.send_response(200)
		self.send_header('Content-type', 'text-html')
		return_value = "Post"
		print return_value
		self.wfile.write(return_value)
		return



	def do_GET(self):
		print self
		print self.path
		root = "../Interface/"
		try: 
			if self.path.endswith('.html') or self.path.endswith('.js') or self.path.endswith('.png') or self.path.endswith('.css'):
				f = open(root + self.path)

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

				print request
				print parameter
				arguments = get_parameters(parameter)
				if request == '/predict':
					handle_request(self, arguments)
				elif request == '/query':
					handle_query(self, arguments)

				return


		except IOError:
			print "Was not able to open " + self.path
			self.send_error('404', "File was not available or could not be found")

	
def run():
	global database	
	global percentiles
	print "Starting the Script"
	print "Load Data"
	database = create_dict("../Data/current_data.csv")
	print database["self_reference_avg_shares"]
	percentiles = build_percentile()
	server_address = ("127.0.0.1", 2000)
	httpd = HTTPServer(server_address, myHTTPServerRequestHandler)
	print "Started the Server"

	httpd.serve_forever()

if __name__ == '__main__':
	run()
