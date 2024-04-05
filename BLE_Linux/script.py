import pyshark

capture = pyshark.FileCapture('pack.pcap')

lenght = -1

pkt = ''
def len_key():
	global lenght
	global pkt
	for packet in capture:
		if 'Long Term Key' in str(packet):
			pkt = (str(packet).split())
			break
	if len(pkt) != 0:
			lenght = len(pkt[pkt.index('Key:')+1])
def conn():
	global capture
	b = open('conn.txt', 'r+')
	b.truncate(0)
	for packet in capture:
		if 'Connect Complete' in str(packet):
			b.write('1')
			break
	b = open('conn.txt', 'r+')
	if str(b.read()) != '1':
		b.write('0')

len_key()
conn()

a = open('sec.txt', 'r+')
a.truncate(0)
if lenght == 32:	
	a.write('1')
elif lenght != -1:
	a.write('0')
else:
	a.write('2')
a.close()