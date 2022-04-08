import socket

def scanPort(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect((ipaddress, port))
        print(f"[+] Port {port} is open")
    except:
        print(f"[-] Port {port} is closed")


ipaddr = input("[+] Enter IP addresss :");

for i in range(75, 85):
    scanPort(ipaddr, i)