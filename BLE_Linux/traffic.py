import subprocess


process = subprocess.Popen('tshark -i bluetooth0 -a duration:20 -w pack.pcap', shell=True)
a = open('conn.txt', 'r+')
a.truncate(0)
a.write(str(process.pid))
a.close()
