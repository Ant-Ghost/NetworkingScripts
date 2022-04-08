import socket, re, sys
sys.path.append("../")
import NameServerLookUp.myRegex as myReg

def getIPFromName(address, version=4):
    try:
        if version == 4:
            if not re.search(myReg.IPV4, address):
                return (socket.gethostbyname(address), 1)
            else:
                return (address, 1)
        elif version == 6:
            if not re.search(myReg.IPV6, address):
                return (socket.getaddrinfo(address, None, socket.AF_INET6)[0][4][0], 1)
            else:
                return (address, 1)
        else:
            return ("Wrong Version[6,4]", -1)
    except:
        return ("Nothing", -1)


if __name__=="__main__" :
    
    print("checking for google.com:"+getIPFromName("google.com")[0])
    print("checking for google.com:"+getIPFromName("google.com", 6)[0])
    print("checking for 142.250.192.238: "+getIPFromName("google.com")[0])
    print("checking for 1::ed:2a : "+getIPFromName("1::ed:2a", 6)[0])