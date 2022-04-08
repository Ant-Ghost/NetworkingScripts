import socket, sys
sys.path.append("../../")
from NameServerLookUp.lookup import getIPFromName
import NameServerLookUp.myRegex as myReg


def scanPort(ipaddress, port):
    '''
    Tries to connect to individual port
    '''
    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect((ipaddress, port))
        print(f"[+] Port {port} is open")
    except:
        print(f"[-] Port {port} is closed")

def mainFunc():
    addr = input("[+] Enter target: ")
    converted_addr, code = getIPFromName(addr)
    if code == 1:
        #Accepting a range of port
        lowerLimit, upperLimit = input("[+] Enter Range of Port (p1 p2): ").split()
        
        for port in range(int(lowerLimit), int(upperLimit)+1):
            scanPort(converted_addr, port)
    else:
        print("[-] Invalid Target (Please Enter domain name or IP address)")


if __name__== "__main__":
    mainFunc()