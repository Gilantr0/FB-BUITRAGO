#!/usr/bin/env python3
import socket

def get_remote_machine_info():
    remote_host = input("Enter the name of the website whose IP address you want to know: ")
    try:
        print(f"IP address: {socket.gethostbyname(remote_host)}")
    except socket.error as err_msg:
        print(f"{remote_host}: {err_msg}")

if __name__ == '__main__':
    get_remote_machine_info()
