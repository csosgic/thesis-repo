import socket
import struct

# Create a raw socket to capture packets
s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))

while True:
    # Receive the packet data
    packet = s.recvfrom(65565)
    
    # Unpack the Ethernet frame
    ethernet_header = packet[0][0:14]
    eth_hdr = struct.unpack("!6s6sH", ethernet_header)
    
    print(ethernet_header)
    print(eth_hdr)
    # Check if the packet is an IP packet
    if eth_hdr[2] == 0x0800:
        # Extract the IP header
        ip_header = packet[0][14:34]
        ip_hdr = struct.unpack("!BBHHHBBH4s4s", ip_header)
        
        # Parse the IP header fields
        ip_version = ip_hdr[0] >> 4
        ip_header_length = (ip_hdr[0] & 0xF) * 4
        ip_ttl = ip_hdr[5]
        ip_protocol = ip_hdr[6]
        src_ip = socket.inet_ntoa(ip_hdr[8])
        dst_ip = socket.inet_ntoa(ip_hdr[9])
        
        # Extract the payload based on the protocol
        if ip_protocol == 1:  # ICMP
            icmp_header = packet[0][34:42]
            icmp_type, icmp_code, icmp_checksum = struct.unpack("!BBH", icmp_header)
            print(f"ICMP Packet: Type={icmp_type}, Code={icmp_code}, Checksum={icmp_checksum}")
        elif ip_protocol == 6:  # TCP
            tcp_header = packet[0][34:54]
            tcp_hdr = struct.unpack("!HHLLBBHHH", tcp_header)
            src_port = tcp_hdr[0]
            dst_port = tcp_hdr[1]
            print(f"TCP Packet: Source={src_ip}:{src_port}, Destination={dst_ip}:{dst_port}")
        elif ip_protocol == 17:  # UDP
            udp_header = packet[0][34:42]
            udp_hdr = struct.unpack("!HHHH", udp_header)
            src_port = udp_hdr[0]
            dst_port = udp_hdr[1]
            print(f"UDP Packet: Source Port={src_port}, Destination Port={dst_port}")
    else:
        print(eth_hdr)
        break