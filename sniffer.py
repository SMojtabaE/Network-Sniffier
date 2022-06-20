from time import sleep
from scapy.all import *


def UDP(pck):
    pass

def TCP(pck):
    print("This packet using TCP Protocol...\n")
    print(pck.summary())
    print(f"\nSport:{pck['TCP'].sport}  dport:{pck['TCP'].dport}  sequensN:{pck['TCP'].seq}\n")
    print(f"ACK:{pck['TCP'].ack}  Flag:{pck['TCP'].flags}  Len:{pck['TCP'].len}  CheckSum:{pck['TCP'].chksum}")

def ICMP(pck):
    pass



def sniff_all():
    count =int(input("\n\n\nEnter number of packets you want : "))
    pck = sniff(count=count)
    print(pck)
    inp = input("want the detales?(y/n)")
    if inp == "y":
        print(pck.show())
        numberOFpck = int(input("which one do you want to see ? "))

        if "UDP" in pck[numberOFpck]:
            UDP(pck[numberOFpck])
        elif "TCP" in pck[numberOFpck]:
            TCP(pck[numberOFpck])
        elif "ICMP" in pck[numberOFpck]:
            ICMP(pck[numberOFpck])
        else:
            print("tha package is not TCP or UDP or ICMP...")
            print("\nopening package...")
            sleep(2)
            print(pck[numberOFpck].show())
            input()

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
