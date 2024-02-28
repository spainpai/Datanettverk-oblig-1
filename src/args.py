import argparse
import re
import sys

port = 8088         # defining variables to start with 
ip = "10.0.0.2"

server = False     # defining booleans to start with
client = False

# Code taken from https://github.com/safiqul/2410/blob/main/argparse-and-oop/optional-arg.py
parser = argparse.ArgumentParser(description="positional arguments", epilog="end of help")

regex = re.compile(r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$') # regex to check if ip is formatted correctly src: https://www.w3schools.com/python/python_regex.asp

parser.add_argument('-s' , '--server', action='store_true', help="enable the server mode")
parser.add_argument('-c' , '--client', action='store_true', help="enable the client mode")
parser.add_argument('-p', '--port', type=int, required=False,help="allows to select port number on which the server will listen; the port must be an integer and in the range [1024, 65535], default: 8088.") # https://stackoverflow.com/questions/25295487/python-argparse-value-range-help-message-appearance
parser.add_argument('-i', '--ip', type=str, required=False, help="allows to select the ip address of the server's interface where the client should connect. Use a default value if it's not provided. It must be in the dotted decimal notation format, e.g. 10.0.0.2 and each block should be in the range of [0,255].")

args = parser.parse_args() # src: https://docs.python.org/3/howto/argparse.html

def server():
    global ip   # import global values src: https://stackoverflow.com/questions/10814452/how-can-i-access-global-variable-inside-class-in-python
    global port
    if args.port != None and port_check(args.port) == True: # if input port is not null and check passes, set port
        port = args.port
    elif port != None and port_check == False:          # if port is not null and port check fails, error
        print("Invalid port. Choose a range between [1024 - 65535]")
        sys.exit(1)
    if args.ip != None and regex.match(args.ip) == True : # if input ip is not null and it is correctly formatted, set ip
        ip = args.ip
    elif ip != None and regex.match(args.ip) == False :  # if ip is not null and formatting is wrong, error
        print("Invalid IP. Format it in the pattern of {1-3}.{1-3}.{1-3}.{1-3}")
        sys.exit(1)
    print(f"The server is running with IP address = {ip} and port address = {port}") 

def client():
    print(f"The client is running with IP address = {ip} and port address = {port}")

def port_check(port):           # port check that retuns true if within range
    if port in range(1024, 65535):
        return True
    else:
        return False

if args.server == True and args.client == True:         # if you try to do both 
    print("You cannot use both at the same time")

elif args.server == False and args.client == False:     # if you try to do none
    print("You should either run in server or client mode")

elif args.server == True:   # -s 
    server()

elif args.client == True:     # -c
    client()