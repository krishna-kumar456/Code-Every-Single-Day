import socket
import subprocess
import sys
from datetime import datetime


subprocess.call('clear', shell=True)



remoteServer = input('Please enter IP to scan')
remoteServerIP = socket.gethostbyname(remoteServer)



print("=" * 60)
print("=" * 60)


t1 = datetime.now()


try:
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Port {}:     Open".format(port))

        else:    
            print('meh..')
            
        sock.close()

        

except socket.gaierror:
    print('Hostname could not be resolved.')
    sys.exit()

t2 = datetime.now

total = t2 - t1

print('Scanning complete in:', total)
