import json
import os
import subprocess
import socket
import datetime
import platform

files = {}


def combine_chunks(inp):
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
    with open('downloads/' + inp, 'wb') as outfile:
        for i in range(1, 6):
            with open(os.path.join("server_files",inp + "_" + str(i)), "rb") as infile:
                outfile.write(infile.read())
    for i in range(1, 6):
        if os.path.exists(inp + "_" + str(i)):
            os.remove(inp + "_" + str(i))


def main():
    while 1:
        download_success = True
        with open("users.txt", "r") as f:
            val = json.loads(f.readline())
            files.clear()
            for x in val:
                files[x[:-2]] = val[x]
            print("\n")
            for x in files:
                print("IP Address : " + files[x] + " File Name : " + x)
            inp = input("Enter File Name = ")
            for i in range(1, 6):
                flag = False
                if client(files[inp], inp + "_" + str(i)) is False:
                    for x in files:
                        if x == inp:
                            if client(files[x], inp + "_" + str(i)) is True:
                                flag = True
                                break
                else:
                    flag = True
                if flag is False:
                    download_success = False
                    write_log(str(datetime.datetime.now()) + ", Error on downloading.", "client_fail.log")
                    break
            if download_success is True:
                combine_chunks(inp)


def write_log(message, log_name):
    with open(log_name, "a") as log:
        log.write(message)


def client(ipAddress, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ipAddress, 5001))
    try:
        sock.send(json.dumps({"filename": message}).encode())
        chunk = open(os.path.join("server_files",message), "wb")
        while True:
            data = sock.recv(4096)
            chunk.write(data)
            print("Download in progress. You will know when finished or occured an error.")
            if len(data) == 0:
                write_log(str(datetime.datetime.now()) + "," + ipAddress + "," + message + "\n", "client_success.log")
                break
        return True
    except:
        write_log(str(datetime.datetime.now()) + ", Error on download from " + ipAddress + ", Filename : " + message,
                  "client_fail.log")
        return False
    finally:
        sock.close()


if __name__ == "__main__":
    main()
