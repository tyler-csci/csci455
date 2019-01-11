import socket
import time
import sys
from thread import *
class Server:


	#Function for handling connections. This will be used to create threads
	def clientthread(self,conn,id):
		while True:
			data = conn.recv(1024)
			if not data:
				sys.stdout.write( 'No data\n')
				sys.stdout.flush()
				break
			sys.stdout.write(id)
			sys.stdout.flush()
			return data
			break
		conn.close()

	def serverthread(self,conn,id,ui):
		while True:
			input = ui
			#input = raw_input()
			input_msg = input + '\n'
			if not input:
				sys.stdout.write( 'No input\n')
				sys.stdout.flush()
				break
			#sys.stdout.write(id)
			#sys.stdout.flush()
			conn.sendall(input_msg)
			break
		conn.close()


	#now keep talking with the client

		#wait to accept a connection - blocking call
	def startServer(self):
		HOST = ''   # Symbolic name meaning all available interfaces
		PORT = 12345 # Arbitrary non-privileged port

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
		sys.stdout.write( 'Socket created\n')
		sys.stdout.flush()

		#Bind socket to local host and port
		try:
			s.bind((HOST, PORT))
		except socket.error as msg:
			sys.stdout.write( 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1] +'\n')
			sys.stdout.flush()
			sys.exit()

		sys.stdout.write( 'Socket bind complete\n')
		sys.stdout.flush()

		#Start listening on socket
		s.listen(10)
		sys.stdout.write( 'Socket now listening\n')
		sys.stdout.flush()

		return s

	def startConn(self, s):
		conn, addr = s.accept()
		id = addr[0] + ':'+str(addr[1])
		#sys.stdout.write( '\nConnected with ' +id+'\n\n')
		#sys.stdout.flush()
		#time.sleep(5)

		return conn, id


	def closeSocket(self, s):
		s.close()
