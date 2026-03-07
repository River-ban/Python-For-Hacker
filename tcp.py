import socket

targetHost = "www.google.com"
targetPort = 80

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the client
client.connect((targetHost, targetPort))

# Send some data
request = "GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"
client.send(request.encode())

# Receive some data
response = client.recv(4096)

print(response.decode())

client.close()
