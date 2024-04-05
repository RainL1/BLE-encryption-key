from tkinter import *
import signal
import subprocess
import os

root = Tk()

def inf():
    att_label.config(foreground='#000000')
    subprocess.Popen(['python', 'traffic.py'])
    subprocess.Popen(['python', 'wait.py'])
    button1.pack(side=BOTTOM, pady=10)
    sec_label.config(text='Безопасность соединения:\n')

def inc():
    h = open('conn.txt', 'r+')
    a = h.read()
    timer = open('timer.txt', 'r+')
    if str(timer.read()) != '1':
        os.kill(int(a), signal.SIGKILL)
    subprocess.Popen(['python', 'script.py'])
    s = open('sec.txt', 'r').readline()
    c = open('conn.txt', 'r+').readline()
    if s == '1':
        sec = 'Безопасно'
    elif c == '0':
        sec = 'Соединение отсутствует'
    else:
        sec = 'Небезопасно'
    att_label.config(foreground='#B3E5FC')
    sec_label.config(text='Безопасность соединения:\n' + sec)
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
