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
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        print(f"[+] Port {port} is open")
    except:
        pass


def scanTarget(target):
    """
    For now it only scan 1st 100 ports
    """
    print(f"\n\n[o_0 Scanning ] : {target}")
    converted_addr, code = getIPFromName(target)
    if code ==1: 
        for i in range(1, 101):
            scanPort(converted_addr, port=i)
    else:
        print("[-] Invalid domain name or IPv4 address")


def mainFunc():
    targets = input("[+] Enter Target/s (seperate targets by ',' ): ")
    if "," in targets:
        for target in targets.split(","):
            scanTarget(target.strip(" "))
    else:
        scanTarget(targets)


if __name__== "__main__":
    mainFunc()