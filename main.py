import argparse
import tracer
import socket
import sport

def skull():
    print('''
    ###        ###
 #  #####   #  #    # ######  ####
 #  #    #  #  ##   # #      #    #
 #  #    #  #  # #  # #####  #    #
 #  #####   #  #  # # #      #    #
 #  #       #  #   ## #      #    #
### #      ### #    # #       ####


    ''')
skull()
parser = argparse.ArgumentParser()
parser.add_argument('-u' , help = "Put  IP or URL address")
args = parser.parse_args()
raw_ip_adress = args.u
ip_adress = socket.gethostbyname(raw_ip_adress)
print("[+]***IN PROGRESS***[+]")

try:
    tracer.tr_ip(ip_adress)
except IndexError:
    print("NO RECORDS AVAILABLE")

print(f"Do you want to run port scan for {ip_adress}\n")
input('>? ')


try:
    sport.s_port(ip_adress)
except:
    print("lul")
