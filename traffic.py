import os

os.system('tshark -i bluetooth0 -a duration:60 -w pack.pcap')
