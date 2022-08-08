#! /usr/bin/python3
# coding=utf-8

"""
An example script to connect to Google using socket programming in Python
"""
from alive_progress import alive_bar
import socket
import sys
import time

def port_scanner(target, port_range):
    open_ports = []
    try:
        target_ip = socket.gethostbyname(target)
        print(f"Target IP: {target_ip}")
    except socket.gaierror:
        print('Hostname could not be resolved. Exiting.')
        sys.exit()
    except:
        print(f"There was an error resolving the host.")
        sys.exit()

    try:
        for port in range(1, port_range):
            try:
                # AF_INET => IPv4
                # SOCK_STREAM => Connection-oriented TCP protocol
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                # print(f"[+] Socket successfully created for port {port}")
            except socket.error as error:
                print(f"[-] Socket creation failed with error: {error}")
                sys.exit()

            try:
                result = sock.connect_ex((target_ip, port))
            except ConnectionRefusedError:
                print(f"[-] Error establishing connection: Connection Refused.")

            if result == 0:
                # print(f"The socket has successfully connected to Google")
                print(f"[+] Port {port} OPEN")
                open_ports.append(port)
            else:
                # print(f"[-] Port {port} CLOSED, connect_ex return: {result}")
                pass

            yield


    except KeyboardInterrupt:
        print("You pressed Ctrl+C")
        print("Exiting...")
        sys.exit()

    print(f"--- Scan completed in {time.time() - start_time} seconds. ---")

    print(f"========== Open Ports at {target}: ==========")
    for port in open_ports:
        print(f"Port: {port}")

if __name__ == "__main__":
    target = input("Enter a remote host to scan (scanme.nmap.org): ")
    port_range = 101 # 0,1,2,3,....,80

    start_time = time.time()

    with alive_bar(port_range -1) as bar:
        for i in port_scanner(target, port_range):
            time.sleep(0.1)
            bar.text("Scan Progress")
            bar.title("Custom Karol's Port Scanner ")
            bar()




