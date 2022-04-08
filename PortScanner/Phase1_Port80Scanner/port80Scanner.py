import socket

ipAddress = input("[+] Enter IP address : ");
port = 80

try:
    sock = socket.socket()
    sock.connect((ipAddress, port))
    print("[+] Port 80 is open")
except:
    print("[-] Unable to connect to port 80")