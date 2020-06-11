import json
import time
from os import listdir
from os.path import isfile, join
from socket import *
import datetime

try:
    print("Program Started At : " + str(datetime.datetime.now()))
    count = 0
    d = {}
    x = input("Username : ")
    file_path = "server_files/"
    d["username"] = x
    d["files"] = [f for f in listdir(file_path) if isfile(join(file_path, f))]
    s = socket(AF_INET, SOCK_DGRAM)
    s.connect(("255.255.255.255", 77))
    ip = s.getsockname()[0].split(".")
    print(ip[0] + "." + ip[1] + "." + ip[2] + ".255")
    s.close()
    a = socket(AF_INET, SOCK_DGRAM)
    a.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    a.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    while 1:
        count += 1
        d["files"] = [f for f in listdir(file_path) if isfile(join(file_path, f))]
        print("Announce sending " + str(count) + " times")
        # The comment code below is normal LAN sharing
        #a.sendto(json.dumps(d).encode(), (ip[0] + "." + ip[1] + "." + ip[2] + ".255", 5000))
        # Below code is for Hamachi
        a.sendto(json.dumps(d).encode(), ("25.255.255.255", 5000))
        print("Announce sent at : " + str(datetime.datetime.now()))
        time.sleep(60)
except KeyboardInterrupt:
    print("Exitting.")
