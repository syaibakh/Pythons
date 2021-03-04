import socket

ipaddrs = '127.0.0.1' # Scanning Localhost

def portscan(port):
    try:
        socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.connect((ipaddrs, port))
        return True
    except:
        return False

print(portscan(8080))