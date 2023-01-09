import pyfiglet
import sys
import socket


banner = pyfiglet.figlet_format("port      scanner")

print("-"*80)
print(banner)
print("-"*80)

cmd_line = len(sys.argv)  # to get the values from cmd line

if cmd_line == 2:

    target = socket.gethostbyname(sys.argv[1]) 
    
else :
    print("invalid arguments")
    
    
print("scanning ip = ",target)

try:

  for port in range(10,30):
     i = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #storing our ip and port number in i
     socket.setdefaulttimeout(0.5)
     result = i.connect_ex((target,port)) #connecting  i with target ip and port
     
     if result == 0:
        print("port",port," is open")
        
     else :
        print("port",port,"is closed")
        
     i.close()
     
except KeyboardInterrupt:
     print("key board intrupted")
     sys.exit()
     
     
except socket.gaierror :
   print("cannot connect hostname")
   sys.exit()
     
except socket.error :
   print("cannot connect")
   sys.exit() 



