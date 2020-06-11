import datetime
import json
import platform
from socket import *

d = {}


try:
    f = open("users.txt", "a")
    f.close()
    print("Program Started At : " + str(datetime.datetime.now()))
    s = socket(AF_INET, SOCK_DGRAM)
    s.connect(("255.255.255.255", 77))
    ip = s.getsockname()[0].split(".")
    my_ip = s.getsockname()[0]
    s.close()
    test = ip[0] + "." + ip[1] + "." + ip[2] + ".255"
    print(test)
    sock = socket(AF_INET, SOCK_DGRAM)
    # The comment code below is normal LAN sharing
    #sock.bind((test if platform.system() != 'Windows' else my_ip, 5000))
    # You need to change "25.148.3.99" with your Hamachi IPv4 address in the code below
    sock.bind(("25.148.3.99", 5000))
    while 1:
        msg, addr = sock.recvfrom(4096)
        print("Received a packet at : " + str(datetime.datetime.now()))
        recv_ip, _ = addr
        if recv_ip != my_ip or 1:
            dat = json.loads(str(msg.decode()))
            try:
                for file in dat["files"]:
                    d[file] = recv_ip
                for key in d:
                    print("Received Username - " + dat["username"])
                with open("users.txt", "w") as f:
                    f.write(json.dumps(d))
                    print("users.txt has been updated")
            except:
                print("Error occured. Probably JSON format or value is wrong.")
except KeyboardInterrupt:
    print("Exitting")
