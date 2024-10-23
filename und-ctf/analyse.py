from scapy.all import rdpcap

# Read the packet capture file
pcap_file_path = "block_in_the_wall.pcap"
packets = rdpcap(pcap_file_path)

# Display summary of packets
packets.summary()

