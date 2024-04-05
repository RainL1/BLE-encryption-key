import time
time.sleep(60)
a = open('timer.txt', 'r+')
a.truncate(0)
a.write('1')
a.close()