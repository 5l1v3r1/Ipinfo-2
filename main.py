import argparse
import tracer

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
parser.add_argument('-i' , help = "Put  IP address")
args = parser.parse_args()
ip_adress = args.i

try:

    tracer.tr_ip(ip_adress)
except IndexError:
    print("NO RECORDS AVAILABLE")

except AttributeError:
    print("BAD INPUT! refer to main.py -h ")
