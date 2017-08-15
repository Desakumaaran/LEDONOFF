
import platform,re, os, shutil, signal, sys, _thread as thread, time, urllib, socketserver as SocketServer

import requests
import RPi.GPIO as GPIO
import time

LedPin = 11    # pin11

GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
GPIO.output(LedPin, GPIO.HIGH) # Set LedPin high(+3.3V) to turn on led

if "-iot" not in sys.argv:
	print("\nIOT : Execution Protocol (Linux Version 1.0)");
	print("\nCommand Line Options :")
	print("    -iot    : Connect to the server and start IOT Actions.")
	#print("    -cache    : Use IO Files in Current Directory instead of downloading them.")
	print()
	sys.exit(0);
    
# Initialize Var
HOST, PORT = "192.168.1.5", 8723



def LedOnfunc(led,Actions):
    
		# Connect to Database
		print("LED:",led)
		print("ACTION:",Actions)
        while True:
        GPIO.output(LedPin, GPIO.HIGH)  # led on
        time.sleep(1)
        GPIO.output(LedPin, GPIO.LOW) # led off
        time.sleep(1)
        
def destroy():
  GPIO.output(LedPin, GPIO.LOW)   # led off
  GPIO.cleanup()                  # Release resource
		
	

class MyTCPHandler(SocketServer.StreamRequestHandler):

	def handle(self):
		# self.rfile is a file-like object created by the handler;
		# we can now use e.g. readline() instead of raw recv() calls
		#self.data = self.rfile.readline()
		#print(self.data)
		#self.data = self.request.recv(1024)
		self.data = self.request.recv(1024)
		#print(self.data)
		self.data = self.data.decode('utf-8')
		#print(self.data)
		tempstr=self.data.strip()
		#tempstr=self.data
		#print(tempstr)
		list1=tempstr.split('~')
		#print(list1)
		LedOnfunc(int(list1[0]),int(list1[1]))
		#self.wfile.write(bytes(finaloutput,'UTF-8'))
		#print("output successfully wrote on clinet")
		#Likewise, self.wfile is a file-like object used to write back
		
	


if __name__ == "__main__":
    # Create the server, binding to localhost on port 8723
	server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
	server.request_queue_size = 100
	#print('Queue Size : ', server.request_queue_size)
    # Activate the server; this will keep running until you
    # inrrupt the program with Ctrl-C
	print("Waiting for Inputs... ")
	try:
		server.serve_forever()
	except KeyboardInterrupt as e:
		print(" Keyboard Interrupt Detected.\n")
        destroy()
	except Exception as e:
		print("Exception : "+str(e)+"\n")
	# Release lock
	try:
		lock.close();
		os.unlink("lock.txt");
	except: pass
	print("Released lock on Execution Protocol.\n")

	# Terminate
	print("IOT : Execution Protocol Terminated.\n");
