from tkinter import *
import subprocess
import psutil
import pyshark

connection_status = 0
security_status = 0


root = Tk()

def script():
    global connection_status
    global security_status
    capture = pyshark.FileCapture('pack.pcap')
    lenght = -1
    pkt = ''
    for packet in capture:
        if 'Long Term Key' in str(packet):
            pkt = (str(packet).split())
            break
    if len(pkt) != 0:
        lenght = len(pkt[pkt.index('Key:') + 1])
    for packet in capture:
        if 'Connect Complete' in str(packet):
            conenction_status = 1
            break
    if lenght == 32:
        security_status = 1
def Start_Button():
    advertisment_label.config(foreground='#000000')
    Butoon_to_Reload.pack(side=BOTTOM, pady=10)
    subprocess.Popen("sudo tshark -i bluetooth0 -a duration:60 -w pack.pcap", shell=True)
    Butoon_to_Reload.pack(side=BOTTOM, pady=10)
    security_label.config(text='Безопасность соединения:\n')

def Reload_Button():
    for proc in psutil.process_iter():
        if 'tshark' in proc.name():
            proc.kill()
    script()
    if security_status == 1 and connection_status == 1:
        sec = 'Безопасно'
    elif connection_status == 1:
        sec = 'Соединение отсутствует'
    else:
        sec = 'Небезопасно'
    advertisment_label.config(foreground='#B3E5FC')
    security_label.config(text='Безопасность соединения:\n' + sec)
    Butoon_to_Reload.pack_forget()
    pcap = open('pack.pcap', 'r+')
    pcap.truncate(0)
    pcap.close()

root['bg'] = '#B3E5FC'
root.title('BLE-ecnryption-key')
root.geometry("600x600")

Button_to_Start = Button(root, text='Нажмите, чтобы начать', font=90, bg='#004C99', fg='#FFFFFF', command=Start_Button)
Button_to_Start.pack(side=BOTTOM, pady=40)
Butoon_to_Reload = Button(root, text='Обновить', font=90, bg='#004C99', fg='#FFFFFF', command=Reload_Button)


advertisment_label = Label(root, text='Подключитесь к устройству в течение 1 минуты', font=70, background='#B3E5FC', foreground='#B3E5FC')
advertisment_label.pack(pady=(50, 0))
security_label = Label(root, text='Cтатус соединения:\n-', font=70, background='#B3E5FC')
security_label.pack(pady=(10, 0))


root.mainloop()
