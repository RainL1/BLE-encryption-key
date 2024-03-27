import os

os.system('tshark -i bluetooth1 -a duration:20 -w traffic.pcap')
