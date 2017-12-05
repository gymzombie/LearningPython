import ipaddress

ip=['10.10.10.456', '10.10.10.10', '192.168.1.4', "snails", "4", "e000::", "127.0.0.1", "224.0.0.1", "169.48.214.143"]

for arg in ip:
    try:
        ipaddress.ip_address(arg)
        print(arg + " is a valid IP Address")
    except :
        print (arg + " is not a valid IP address.")
