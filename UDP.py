import socket

targetHost = "127.0.0.1"
targetPort = 9997

# Create a socket object (UDP)
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send some data
client.sendto(b"AAABBBCCC", (targetHost, targetPort))

# Receive some data
data, addr = client.recvfrom(4096)

print(data.decode())

client.close()