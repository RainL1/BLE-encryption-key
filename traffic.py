import os

os.system('tshark -i bluetooth1 -a duration:60 -w pack.pcap')
