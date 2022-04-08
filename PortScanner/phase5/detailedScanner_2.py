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
    result = False
    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect((ipaddress, port))
        result= True
        print(" OPEN ")
        # try:
        #     banner = getBanner(sock).decode().strip('\n')
        #     print(f"[+] Port {port} is open : {banner}")
        # except Exception as e:
        #     print(f"[+] Port {port} is open : Error : {e}")
    except:
        print("\r", end="")
    finally:
        sock.close()
    return result


def investigateOpenPorts(ipaddress, ports):
    message = "Hello World"
    for port in ports:
        print(f"[+] Trying Port {port} : ", end="")
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect_ex((ipaddress, port))
            sock.send(message.encode())
            received = sock.recv(1024)
            print(f"[+] INFO : {received}")
        except Exception as e: 
            print(f"[-] Error: {e}")
        finally:
            sock.close()



def scanTarget(target):
    """
    For now it only scan 1st 100 ports
    """
    print(f"\n\n[o_0 Scanning ] : {target}")
    converted_addr, code = getIPFromName(target)
    open_ports = []
    if code ==1: 
        for i in range(1, 100):
            print(f"[@ Scanning port {i}]", end="")
            if scanPort(converted_addr, port=i):
                open_ports.append(i)
        
        print("\n\n[+] Open ports identified")
        investigateOpenPorts(converted_addr,open_ports)
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