import socket, sys
sys.path.append("../../")
from NameServerLookUp.lookup import getIPFromName
import NameServerLookUp.myRegex as myReg

def getBanner(s):
    return s.recv(1024)


def scanPort(ipaddress, port):
    '''
    Tries to connect to individual port
    '''
    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect((ipaddress, port))
        print()
        try:
            banner = getBanner(sock).decode().strip('\n')
            print(f"[+] Port {port} is open : {banner}")
        except Exception as e:
            print(f"[+] Port {port} is open : Error : {e}")
    except:
        print("\r", end="")


def scanTarget(target):
    """
    For now it only scan 1st 100 ports
    """
    print(f"\n\n[o_0 Scanning ] : {target}")
    converted_addr, code = getIPFromName(target)
    if code ==1: 
        for i in range(1, 65536):
            print(f"[@ Scanning port {i}]", end="")
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
    # print("Scanning port 25 of router")
    # scanPort("192.168.29.1", 25)