# Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time

host = sys.argv[1]
textport = sys.argv[2]
n = sys.argv[3]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = (host, port)

#   s.sendall(n.encode('utf-8'))
for x in range(int(n)):
    message = "message" + str(x + 1)
    s.sendto(message.encode('utf-8'), server_address)
    
    echo, address = s.recvfrom(port)
    checkEcho = str(message)
    
    if checkEcho in str(echo.decode("utf-8")):
        print("Echo received: ")
        print(echo.decode("utf-8"))        
    else:
        print("All alone.")
s.shutdown(1)
