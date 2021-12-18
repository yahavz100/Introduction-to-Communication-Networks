# Dvir Asaf
# Yahav Zarfati

import socket
import sys

# Check user input is valid, if not exit
if len(sys.argv) < 2:
    sys.exit()
# Check user input if port is not a number
if not sys.argv[1].isnumeric():
	sys.exit()

# Define IPv4 UDP socket, and bind socket to given port
socket1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(sys.argv[1])
socket1.bind(('', port))

counter: int = 0
prevData = ""

# Print all data received and send it back
while True:
    # Process protocol
    data, addr = socket1.recvfrom(100)
    clientCounter = int(data[:1])
    cleanData = data[1:].decode(encoding='utf-8')
    prevData = cleanData

    # If data sent was received, print new data
    if clientCounter == counter:
        print(str(cleanData), end='')
        counter += 1
        socket1.sendto(cleanData.encode(encoding='utf-8'), addr)
    else:
        socket1.sendto(prevData.encode(encoding = 'utf-8'), addr)
