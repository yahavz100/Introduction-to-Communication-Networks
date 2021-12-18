# Dvir Asaf
# Yahav Zarfati

import socket
import sys

# Check user input is valid, if not exit
if len(sys.argv) < 4:
	sys.exit()
# Check user input if port is not a number
if not sys.argv[1].isnumeric():
	sys.exit()

# Get user input from CMD into arguments
port = int(sys.argv[1])
ip = sys.argv[2]
fileName = sys.argv[3]

# Check if given ip is valid, if not exit
try:
	socket.inet_aton(ip)
except:
	sys.exit()

# Define IPv4 UDP socket, and buffer size
socket1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket1.settimeout(10)	# Define timeout timer to 10s
buffSize: int = 90

# Open given file and traverse each line in it
pFile = open(fileName, 'r')
lines = pFile.read(buffSize)

counter: int = 0

# Iterate file, send file in chunks of buffer size
while lines:
	try:
		message = str(counter) + lines
		socket1.sendto(message.encode(encoding = 'utf-8'), (ip, port))
		data, addr = socket1.recvfrom(buffSize)

		# Check if data corrupted
		if data == lines.encode(encoding = 'utf-8'):
			counter += 1
			lines = pFile.read(buffSize)
		else:
			continue

	# Check if data lost
	except socket.timeout:
		continue

# Close resources
socket1.close()
pFile.close()
