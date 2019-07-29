import socket
import datetime

def s_port(ip_adress):

    for port in range(1,1025):
        sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        sock.settimeout(0.5)
        res = sock.connect_ex((ip_adress , port))
        if res == 0:
            print("port{}:     Open".format(port))
            sock.close()
    else:
        print("port{}:     Closed".format(port))
