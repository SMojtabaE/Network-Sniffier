from time import sleep
from scapy.all import *


def menu():
    while True:
        print("Welcom,What do you want??\n\n\n")        
        print("          1) Sniff everything!\n")       # 10 spaces-
        print("          2) Sniff a protocol!\n\n\n")

        inp = int(input("(0 to Exit) : "))
        if inp == 1:
            sniff_all()
        elif inp == 2:
            print("which one?\n\n\n")
            print("    1) TCP\n")  # 4 spaces
            print("    2) UDP\n")
            print("    3) ICMP\n")
            protocol = int(input(" : "))
            sniff_protocol(protocol)
        elif inp == 0:
            quit()
        else:
            print("Ops, enter the right numbers :D")
