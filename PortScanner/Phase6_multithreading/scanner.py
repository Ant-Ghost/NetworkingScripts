import socket, sys, threading, time
from  queue import Queue
sys.path.append("../../")
from NameServerLookUp.lookup import getIPFromName
import NameServerLookUp.myRegex as myReg

class PortScanner:

    def __init__(self):
        self.ipaddress = ""
        self.queuePorts = Queue()
        self.print_lock = threading.Lock()
        self.openPorts=[]

    def scanPort(self, port):

        result = False
        try:
            sock = socket.socket()
            sock.settimeout(1)
            sock.connect((self.ipaddress, port))
            result = True
            print(f"[+] Port {port} : OPEN")
            self.openPorts.append(port)
        except:
            result = False
        finally:
            sock.close()
        return result

    def investigateOpenPorts(self):
        message = "Hi"
        for port in self.openPorts:
            print(f"[+] Trying Port {port}: ", end="")
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(10)
                sock.connect((self.ipaddress, port))
                sock.send(message.encode())
                received = sock.recv(1024).decode().strip("\n")
                print(f"[+] INFO: {received}")
            except Exception as e:
                print(f"[-] Error: {e}")
            finally:
                sock.close()

    def scanTarget(self,target):
        print(f"\n\n[o_0 Scanning] : {target}")
        self.ipaddress, code = getIPFromName(target)
        
        inputPorts = input("\n[+] Enter a port, ports(seperated by ',') or range of ports(seperated by '-'):")
        iterablePorts = []
        if "," in inputPorts:
            newPorts = inputPorts.split(",")
            iterablePorts = [ int(port.strip()) for port in newPorts ]
        elif "-" in inputPorts:
            newPorts = inputPorts.split("-")
            iterablePorts = [ i for i in range(int(newPorts[0].strip()), int(newPorts[1].strip())+1)]
        else:
            iterablePorts.append(int(inputPorts.strip()))

        if code == 1:
            
            for i in iterablePorts:
                thread = threading.Thread(target=self.scanPort, args=(i,))
                thread.daemon = True
                thread.start()
            thread.join()


            if len(self.openPorts):
                print(f"\n\n[+] Open ports identified : {self.openPorts}\n\n")
                self.investigateOpenPorts()
        else:
            print("[-] Invalid domain name or IPv4 address")

    def mainFunc(self):
        targets = input("[+] Enter Target/s (seperate targets by ',' ): ")
        if "," in targets:
            for target in targets.split(","):
                self.scanTarget(target.strip(" "))
                time.sleep(1)
        else:
            self.scanTarget(targets)



if __name__=="__main__":
    ps = PortScanner()
    ps.mainFunc()