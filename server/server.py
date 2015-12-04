from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import os

database = []

def readFile(filename):
	f = open(filename, 'r')
	database = []
	for line in f:
		itemset = []
		tmp = ""
		for s in line:
			if not(s == ' '):
				tmp += s
			else:
				itemset.append(tmp)
				tmp = ""
		database.append(itemset)
	return database

def handle_query(self, parameter):
	self.send_response(200)
	self.send_header('Content-type', 'text-html')
	self.end_headers()

	return_value = "The Overview for the database"
	
	return_value = "<table border=1><tr><th>URL</th><th>Time Delta</th><th>n_tokens_title</th><th>n_tokens_content</th><th>num_hrefs</th><th>num_self_hrefs</th><th>num_images</th><th>num_videos</th><th>self_reference_average_shares</th><th>monday</th><th>tuesday</th><th>wednesday</th><th>thursday</th><th>friday</th><th>saturday</th><th>sunday</th><th>class</th></tr></table>"
	print return_value
	self.wfile.write(return_value)
	return


def handle_request(self, parameter):
		self.send_response(200)
		self.send_header('Content-type', 'text-html')
		self.end_headers()

		size = len(parameter)
		arguments = ["n_tokens_title=","n_tokens_content=","num_hrefs=","num_self_hrefs=","num_imgs=","num_videos=","average_token_length=","channel=","self_reference_min_shares=","self_reference_max_shares=","self_reference_avg_shares=","weekday="]
		#arguments = ["day=", "title=","publishing=", "channel=", "email="]
		argument_values = {}
		for a in arguments:
			value = ''
			i = parameter.find(a)
			i += len(a)
			while(i < size and parameter[i] != '?'):
				value += parameter[i]
				i += 1
			argument_values[a] = value

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
				if request == '/predict':
					handle_request(self, parameter)
				elif request == '/query':
					handle_query(self, parameter)

				return


		except IOError:
			print "Was not able to open " + self.path
			self.send_error('404', "File was not available or could not be found")

	
def run():
	print "Starting the Script"
	print "Load Data"
	database = readFile("../Data/prepro_data.csv")
	server_address = ("127.0.0.1", 2000)
	httpd = HTTPServer(server_address, myHTTPServerRequestHandler)
	print "Started the Server"

	httpd.serve_forever()

if __name__ == '__main__':
	run()
