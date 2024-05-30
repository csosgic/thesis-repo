#from scapy.all import *
#
#def packet_callback(packet):
#
#
#    print(packet)
#    # Inspect the packet and decide whether to accept or deny it
#    if packet.haslayer(TCP) and packet[TCP].dport == 80:
#        # Accept HTTP traffic
#        return packet
#    else:
#        # Deny other traffic
#        return None
#
#
#
#
#
#def main():
#    sniff(prn=packet_callback, filter="tcp", store=0)
#
#if __name__ == "__main__":
#    main()
#
#
#
#















#
#
#
#
#from scapy.all import *
#
#def handle_packet(packet):
#    if packet.haslayer(IP) and packet.haslayer(TCP) and packet.haslayer(UDP):
#        ip_layer = packet[IP]
#        tcp_layer = packet[TCP]
#        
#        # Extract the required fields
#        duration = 0  # Not available in the given data
#        protocol_type = ip_layer.proto
#        service = tcp_layer.dport
#        flag = tcp_layer.flags
#        src_bytes = len(packet) if TCP in packet else 0
#        dst_bytes = 0  # Not available in the given data
#        land = 0  # Not available in the given data
#        wrong_fragment = 0  # Not available in the given data
#        urgent = tcp_layer.urgptr
#        hot = 0  # Not available in the given data
#        num_failed_logins = 0  # Not available in the given data
#        logged_in = 0  # Not available in the given data
#        num_compromised = 0  # Not available in the given data
#        root_shell = 0  # Not available in the given data
#        su_attempted = 0  # Not available in the given data
#        num_root = 0  # Not available in the given data
#        num_file_creations = 0  # Not available in the given data
#        num_shells = 0  # Not available in the given data
#        num_access_files = 0  # Not available in the given data
#        num_outbound_cmds = 0  # Not available in the given data
#        is_host_login = 0  # Not available in the given data
#        is_guest_login = 0  # Not available in the given data
#        count = 0  # Not available in the given data
#        srv_count = 0  # Not available in the given data
#        serror_rate = 0  # Not available in the given data
#        srv_serror_rate = 0  # Not available in the given data
#        rerror_rate = 0  # Not available in the given data
#        srv_rerror_rate = 0  # Not available in the given data
#        same_srv_rate = 0  # Not available in the given data
#        diff_srv_rate = 0  # Not available in the given data
#        srv_diff_host_rate = 0  # Not available in the given data
#        dst_host_count = 0  # Not available in the given data
#        dst_host_srv_count = 0  # Not available in the given data
#        dst_host_same_srv_rate = 0  # Not available in the given data
#        dst_host_diff_srv_rate = 0  # Not available in the given data
#        dst_host_same_src_port_rate = 0  # Not available in the given data
#        dst_host_srv_diff_host_rate = 0  # Not available in the given data
#        dst_host_serror_rate = 0  # Not available in the given data
#        dst_host_srv_serror_rate = 0  # Not available in the given data
#        dst_host_rerror_rate = 0  # Not available in the given data
#        dst_host_srv_rerror_rate = 0  # Not available in the given data
#        
#        # Print or process the extracted data as needed
#        print(f"Source IP: {ip_layer.src}, Destination IP: {ip_layer.dst}")
#        print(f"Source Port: {tcp_layer.sport}, Destination Port: {tcp_layer.dport}")
#        print(f"Protocol Type: {protocol_type}, Service: {service}")
#        print(f"Flags: {flag}, Source Bytes: {src_bytes}, Urgent: {urgent}")
#        
#        print("\n#########################################\n")
#        # Add further processing or storage of the extracted data
#
#def main():
#    sniff(prn=handle_packet, filter="tcp", store=0)
#
#if __name__ == "__main__":
#    main()
#





























#import pyshark
#
## Open a live capture
#capture = pyshark.LiveCapture(interface='eno1')
#
## Process each packet
#for packet in capture.sniff_continuously():
#    # Check if the packet has a layer 7 protocol
#    print("\n###########################################################\n")
#    print(packet)
#    print("\n###########################################################\n")
#    #if hasattr(packet, 'highest_layer'):
#    #    l7_proto = packet.highest_layer
#    #    
#    #    # Check for specific protocols
#    #    if l7_proto == 'HTTP':
#    #        http_info = packet.http
#    #        print(f"HTTP Info: {http_info}")
#    #    elif l7_proto == 'DNS':
#    #        dns_info = packet.dns
#    #        print(f"DNS Info: {dns_info}")
#    #    else:
#    #        print(f"Layer 7 Protocol: {l7_proto}")
#    #else:
#    #    print("Layer 7 protocol not found.")
#




import psutil

def monitor_network_packets():
    net_io_counters = psutil.net_io_counters()
    in_pkts = net_io_counters.packets_recv
    out_pkts = net_io_counters.packets_sent
    
    print(f"IN_PKTS: {in_pkts}")
    print(f"OUT_PKTS: {out_pkts}")

if __name__ == "__main__":
    monitor_network_packets()
