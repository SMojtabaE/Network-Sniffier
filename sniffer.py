from time import sleep
from scapy.all import *

#TODO""
# 1-complete show_udp and show icmp
# 2- make and complite the protocol type
# """

def show_UDP(pck):
    print("This packet using UDP Protocol...\n")
    print("summary of packet : \n")
    print(pck.summary())
    print(f"\nSport:{pck['UDP'].sport}  dport:{pck['UDP'].dport}\n")
    print(f"Len:{pck['UDP'].len}  CheckSum:{pck['UDP'].chksum}")
    input()

def show_TCP(pck):
    print("This packet using TCP Protocol...\n")
    print("summary of packet : \n")
    print(pck.summary())
    print(f"\nSport:{pck['TCP'].sport}  dport:{pck['TCP'].dport}  sequensN:{pck['TCP'].seq}\n")
    print(f"ACK:{pck['TCP'].ack}  Flag:{pck['TCP'].flags}  Len:{pck['IP'].len}  CheckSum:{pck['TCP'].chksum}")
    input()

def show_ICMP(pck):
    print("This packet using ICMP Protocol...\n")
    print("summary of packet : \n")
    print(pck.summary())
    print(f"\nType:{pck['ICMP'].type}  code:{pck['ICMP'].code}\n")
    print(f"CheckSum:{pck['ICMP'].chksum}")
    input()


def sniff_all():
    count =int(input("\n\n\nEnter number of packets you want : "))
    pck = sniff(count=count)
    print(pck)
    inp = input("want the detales?(y/n)")
    if inp == "y":
        while True:
            print(pck.show())
            numberOFpck = input("which one do you want to see (q to back) ? ")
            if numberOFpck == "q":
                break
            elif int(numberOFpck) not in range(count):
                print("enter corroct number from the list!!!")
                sleep(2)
            elif "UDP" in pck[int(numberOFpck)]:
                show_UDP(pck[int(numberOFpck)])
            elif "TCP" in pck[int(numberOFpck)]:
                show_TCP(pck[int(numberOFpck)])
            elif "ICMP" in pck[int(numberOFpck)]:
                show_ICMP(pck[int(numberOFpck)])
            else:
                print("tha package is not TCP or UDP or ICMP...")
                print("\nopening package...")
                sleep(1)
                print(pck[int(numberOFpck)].show())
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



menu()
