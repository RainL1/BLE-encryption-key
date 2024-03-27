import pyshark

cap = pyshark.FileCapture('traffic.pcap')

lenght = -1


for packet in cap:
	if 'Long Term Key' in str(packet):
		pkt = (str(packet).split())
		lenght = len(pkt[-2])
if lenght == 32:
	print(1)
else:
	print(0)
