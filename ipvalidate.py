
import socket
import ipaddress

ip=['10.10.10.456', '10.10.10.10', '192.168.1.4', "snails", "4", "e000::"]

for arg in ip:
    try:
        socket.inet_aton(arg)           # test if the IP is a valid ipv4
        print(arg + " is a valid IP v4 Address")
    except socket.error:
        try:
            socket.inet_pton(socket.AF_INET6, arg)      # Test if it's a valid IPv6 address
            print(arg + " is a valid IP v6 Address")
        except socket.error:
            print(arg + " is NOT a valid IP Address")


print("\nTrying secondary method:\n")

for arg in ip:
    try:
        ipaddress.ip_address(arg)
        print(arg + " is a valid IP v4 Address")
    except :
        print (arg + " is not a valid IP address.")
