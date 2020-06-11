from datetime import *
import json
import os
import math
import socket
from threading import *


def func_ip1():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("255.255.255.255", 1))
    ip = s.getsockname()[0]
    s.close()
    return ip

def func_ip():
    #You need to enter your own Hamachi IPv4 address in the " "
    return "25.148.3.99"


def server(ip):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((ip, 5001))
    sock.listen(50)
    print("Server has been started.")
    while True:
        conn, info = sock.accept()
        Thread(target=send, args=(conn, info)).start()


def write_log(message, log_file_name):
    with open(log_file_name, "a") as log:
        log.write(message)


def send(conn, clientInfo):
    try:
        while True:
            data = conn.recv(4096)
            if data:
                fileName = "server_files/" + json.loads(data.decode())["filename"]
                with open(fileName, "rb") as f:
                    conn.send(f.read(os.path.getsize(fileName)))
                    write_log(str(datetime.now()) + "," + clientInfo[0] + "," + fileName + "\n", "server_success.log")
                    break
            else:
                break
    except:
        write_log(str(datetime.now()) + ", Error has been occured.", "server_fail.log")
    finally:
        conn.close()


def divide_into_chunks(file,directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    c = os.path.getsize(file)
    CHUNK_SIZE = math.ceil(math.ceil(c) / 5)
    cnt = 1
    with open(file, 'rb') as infile:
        divided_file = infile.read(int(CHUNK_SIZE))
        while divided_file:
            name = directory + "/" + file + "_" + str(cnt)
            with open(name, 'wb+') as div:
                div.write(divided_file)
            cnt += 1
            divided_file = infile.read(int(CHUNK_SIZE))
    print(file + " divided into 5 chunks each chunk is " + str(CHUNK_SIZE) + " bytes")


if __name__ == '__main__':
    file = input("Enter file path : ")
    divide_into_chunks(file,"server_files")
    server(func_ip())
