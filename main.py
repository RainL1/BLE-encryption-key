from tkinter import *
import signal
import subprocess
import os
root = Tk()

def inf():
    att_label.config(foreground='#000000')
    subprocess.Popen(['python', 'traffic.py'])
    button1.pack(side=BOTTOM, pady=10)

def inc():
    subprocess.Popen(['python', 'script.py'])
    c = open('sec.txt', 'r')
    s = c.readline()
    if s == '1':
        sec = 'Безопасно'
    elif s == '2':
        sec = 'Соединение отсутствует'
    else:
        sec = 'Небезопасно'
    att_label.config(foreground='#B3E5FC')
    sec_label.config(text='Безопасность соединения:\n' + sec)
    h = open('conn.txt', 'r+')
    a = h.read()
    os.kill(int(a), signal.SIGKILL)
    button1.pack_forget()

root['bg'] = '#B3E5FC'
root.title('BLE-ecnryption-key')
root.geometry("600x600")

button = Button(root, text='Нажмите, чтобы начать', font=90, bg='#004C99', fg='#FFFFFF', command=inf)
button.pack(side=BOTTOM, pady=40)
button1 = Button(root, text='Обновить', font=90, bg='#004C99', fg='#FFFFFF', command=inc)


att_label = Label(root, text='Подключитесь к устройству в течение 1 минуты', font=70, background='#B3E5FC', foreground='#B3E5FC')
att_label.pack(pady=(50, 0))
sec_label = Label(root, text='Cтатус соединения:\n-', font=70, background='#B3E5FC')
sec_label.pack(pady=(10, 0))

root.mainloop()
