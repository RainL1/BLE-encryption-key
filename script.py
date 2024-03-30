import pyshark

cap = pyshark.FileCapture('pack.pcap')

lenght = -1


for packet in cap:
	if 'Long Term Key' in str(packet):
		pkt = (str(packet).split())
		lenght = len(pkt[-1])
a = open('sec.txt', 'r+')
a.truncate(0)
if lenght == 32:	
	a.write('1')
elif lenght != -1:
	a.write('0')
else:
	a.write('2')
a.close()