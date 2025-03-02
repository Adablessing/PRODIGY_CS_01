from scapy.all import sniff, IP, TCP, UDP, Ether, Raw

# Function to process each captured packet
def packet_callback(packet):
    if packet.haslayer(IP):
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto

        print(f"Source IP: {ip_src} -> Destination IP: {ip_dst}")

        if packet.haslayer(TCP):
            tcp_sport = packet[TCP].sport
            tcp_dport = packet[TCP].dport
            print(f"Protocol: TCP, Source Port: {tcp_sport}, Destination Port: {tcp_dport}")

        elif packet.haslayer(UDP):
            udp_sport = packet[UDP].sport
            udp_dport = packet[UDP].dport
            print(f"Protocol: UDP, Source Port: {udp_sport}, Destination Port: {udp_dport}")

        if packet.haslayer(Raw):
            payload = packet[Raw].load
            print(f"Payload: {payload}")

        print("-" * 40)

# Start sniffing packets
print("Starting packet sniffer...")
sniff(prn=packet_callback, store=False)
