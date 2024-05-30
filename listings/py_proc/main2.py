from scapy.all import *

def handle_packet(packet):
    if packet.haslayer(TCP):
        src_addr = packet[IP].src
        dst_addr = packet[IP].dst
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport
        protocol = packet[IP].proto
        l7_proto = packet[TCP].dport #wrong
        in_bytes = len(packet)
        in_pkts = 1 # wrong
        out_bytes = 0
        out_pkts = 0
        tcp_flags = packet[TCP].flags # wrong
        client_tcp_flags = packet[TCP].flags # wrong
        server_tcp_flags = packet[TCP].flags # wrong
        flow_duration = 0
        duration_in = 0
        duration_out = 0
        min_ttl = packet[IP].ttl
        max_ttl = packet[IP].ttl
        longest_flow_pkt = 0
        shortest_flow_pkt = 0
        min_ip_pkt_len = 0
        max_ip_pkt_len = 0
        src_to_dst_second_bytes = 0
        dst_to_src_second_bytes = 0
        retransmitted_in_bytes = 0
        retransmitted_in_pkts = 0
        retransmitted_out_bytes = 0
        retransmitted_out_pkts = 0
        src_to_dst_avg_throughput = 0
        dst_to_src_avg_throughput = 0
        num_pkts_up_to_128_bytes = 0
        num_pkts_128_to_256_bytes = 0
        num_pkts_256_to_512_bytes = 0
        num_pkts_512_to_1024_bytes = 0
        num_pkts_1024_to_1514_bytes = 0
        tcp_win_max_in = 0
        tcp_win_max_out = 0
        icmp_type = 0
        icmp_ipv4_type = 0
        dns_query_id = 0
        dns_query_type = 0
        dns_ttl_answer = 0
        ftp_command_ret_code = 0
        label = 0

        print(f"Source IP: {src_addr}, Destination IP: {dst_addr}")
        print(f"Source Port: {src_port}, Destination Port: {dst_port}")
        print(f"Protocol: {protocol}, L7 Protocol: {l7_proto}")
        print(f"In Bytes: {in_bytes}, In Packets: {in_pkts}")
        print(f"Out Bytes: {out_bytes}, Out Packets: {out_pkts}")
        print(f"TCP Flags: {tcp_flags}, Client TCP Flags: {client_tcp_flags}, Server TCP Flags: {server_tcp_flags}")
        print(f"Flow Duration: {flow_duration}, Duration In: {duration_in}, Duration Out: {duration_out}")
        print(f"Min TTL: {min_ttl}, Max TTL: {max_ttl}")
        print(f"Longest Flow Packet: {longest_flow_pkt}, Shortest Flow Packet: {shortest_flow_pkt}")
        print(f"Min IP Packet Length: {min_ip_pkt_len}, Max IP Packet Length: {max_ip_pkt_len}")
        print(f"Source to Destination Second Bytes: {src_to_dst_second_bytes}, Destination to Source Second Bytes: {dst_to_src_second_bytes}")
        print(f"Retransmitted In Bytes: {retransmitted_in_bytes}, Retransmitted In Packets: {retransmitted_in_pkts}")
        print(f"Retransmitted Out Bytes: {retransmitted_out_bytes}, Retransmitted Out Packets: {retransmitted_out_pkts}")
        print(f"Source to Destination Average Throughput: {src_to_dst_avg_throughput}, Destination to Source Average Throughput: {dst_to_src_avg_throughput}")
        print(f"Number of Packets Up to 128 Bytes: {num_pkts_up_to_128_bytes}, Number of Packets 128 to 256 Bytes: {num_pkts_128_to_256_bytes}")
        print(f"Number of Packets 256 to 512 Bytes: {num_pkts_256_to_512_bytes}, Number of Packets 512 to 1024 Bytes: {num_pkts_512_to_1024_bytes}")
        print(f"Number of Packets 1024 to 1514 Bytes: {num_pkts_1024_to_1514_bytes}")
        print(f"TCP Window Max In: {tcp_win_max_in}, TCP Window Max Out: {tcp_win_max_out}")
        print(f"ICMP Type: {icmp_type}, ICMP IPv4 Type: {icmp_ipv4_type}")
        print(f"DNS Query ID: {dns_query_id}, DNS Query Type: {dns_query_type}, DNS TTL Answer: {dns_ttl_answer}")
        print(f"FTP Command Return Code: {ftp_command_ret_code}, Label: {label}")


        print("\n#########################################\n")

def main():
    sniff(prn=handle_packet, store=0)

if __name__ == "__main__":
    main()
