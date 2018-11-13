import time

from scapy.all import rdpcap, UDP, send, IP, RandShort

# product_path = "/Users/wongxinjie/Downloads/radius.pcap"
product_path = "/Users/wongxinjie/Downloads/udp.pcap"
local_path = "/Users/wongxinjie/Downloads/local.pcap"


def extract_payload(pacp_path):
    pcap = rdpcap(pacp_path)

    packet = pcap[510]
    packet.show()
    yield packet[UDP].payload
    # sessions = pcap.sessions()
    # for session in sessions:
    #     for packet in sessions[session]:
    #         if packet[UDP].sport != 1812 and packet[UDP].sport != 1813:
    #             yield packet[UDP].payload


def replay():
    packet = IP(dst="127.0.0.1", chksum=0) / UDP(dport=1812, sport=RandShort(), chksum=0)
    for payload in extract_payload(product_path):
        packet[UDP].payload = payload
        del packet[IP].chksum
        del packet[UDP].chksum
        packet.show2()
        send(packet, iface="lo0")
        time.sleep(1)


replay()
