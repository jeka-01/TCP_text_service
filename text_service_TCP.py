import os
import json
import sys
import socket
import optparse
 
class Server:
    def __init__(self,interface, port):
        self.interface = '127.0.0.1'
        self.port = port

    def listen(self):
        connect_listener = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        connect_listener.bind((self.host,self.port))
        connect_listener.listen(0)
        print("[+] Waiting for Incoming Connection")
        self.connection,address = connect_listener.accept()
        print("[+] Got a Connection from " + str(address))

    def send(self, data):
        json_data = json.dumps(data)
        self.cnn.send(json_data.encode())

    def receive(self):
    	jsn_data = ""
    	while True:
    		try:
    			jsn_data = jsn_data + self.connection.recv(1024).decode()
    			return jsn.loads(jsn_data)
    		except ValueError:
    			continue
          
    def change_text(self, text, dict_string):
    	words = text.split()
    	final_dict = eval(dict_string)
    	print(words)
    	for word in words:
    		if word in final_dict.keys():
    			text = text.replace(word, final_dict[word])
    	return text

    def start(self):
    	self.listen()
    	r_data = self.receive()
    	if (r_data[0] == 'encode_decode'):
    		result = self.encode_text(r_data[1], r_data[2])
    	if (r_data[0] == 'change_text'):
    		result = self.change_text(r_data[1], r_data[2])
    	
    	self.send(result)

    def encode_text(self, txt, key):
    	en_text = ""
    	for i in range(len(text)):
    		ch = text[i]
    		k = key[i%len(key)]
    		en_text += chr(ord(ch) ^ ord(k))
    	return en_text

class Client:
	def __init__(self, mode, hostname, port):
		self.mode = mode
    self.hostname = hostname
    self.port = port
    self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.sock.connect((self.host,self.port))

	def send(self, data):
		j_data = j.dumps(data)
		self.connection.send(j_data.encode())

	def receive(self):
		j_data = ""
		while True:
			try:
				j_data = j_data + self.connection.recv(1024).decode()
				return j.loads(j_data)
			except ValueError:
				continue

	def process(self, msg_file, aux_file):
		msg_text = open(msg_file, 'r').read()
		aux_text = open(aux_file, 'r').read()
		data = []
		data.append(self.mode)
		data.append(msg_text)
		data.append(aux_text)
		self.send(data)
		received_data = self.receive()
		print(received_data)



def main():
	parser = optparse.OptionParser()
	parser.add_option("-p", metavar="PORT", type= int, help="Port on which server listens")
	if sys.argv[1] == "client":
		parser.add_option("--host", dest = "host", help="Ip address of server")
		parser.add_option("--mode", dest = "mode", help="Mode which idetifies how program shoud operate")
		parser.add_option("--msg_file", dest = "msg_file", help="Path of the file which contains message")
		parser.add_option("--aux_file", dest = "aux_file", help="Key or json file according to mode")
	(options,arguments) = parser.parse_args()
	if sys.argv[1] == "client":
		client = Client(options.mode)
		client.connect(options.host, options.p)
		client.send_to_process(options.msg_file, options.aux_file)
	else:
		server = Server(options.p)
		server.run()

if __name__== "__main__":
	main()
