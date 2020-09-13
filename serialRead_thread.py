#!/usr/bin/python3

import serial
import datetime
# import time
import threading
import os

# check data folder
folder = '/home/pi/ecotech/aurora3000/data'
if not os.path.isdir(folder):
    os.system("sudo mkdir {folder}".format(folder=folder))

class my_thread(threading.Thread):
    def __init__(self,config):
        threading.Thread.__init__(self)
        self.config = config
        self.switch = True

    def run(self):
        ''' serial reading'''
        global watchdog
        # ser = serial.Serial('/dev/ttyUSB0',38400,timeout=1)
        ser = serial.Serial(**self.config)
        th = threading.currentThread()
        # while getattr(th,'do_run',True):
        while self.switch==True:
            watchdog = datetime.datetime.now()
            data = ser.readline()
            try:
                data = data.decode('ascii')
                txt = '{time},{data}'.format(time=datetime.datetime.now(),data=data)
            except:
                txt = '[WARNING] {time},{data}'.format(time=datetime.datetime.now(),data=data)
            txt = txt.replace('\r','')
            if not ('\n' in txt): txt+='\n'
            f = open('/home/pi/ecotech/aurora3000/data/log_{date}.txt'.format(date=datetime.datetime.now().strftime('%Y%m%d')),'a+')
            f.write(txt)
            print(txt.replace('\n',''))
            f.close()

    def stop(self):
        self.switch = False


def main():
    # set watchdog
    global watchdog
    watchdog = datetime.datetime.now()

    serial_dict=dict(
        port='/dev/ttyUSB0',
        baudrate=38400,
        timeout=5
    )
    th=my_thread(serial_dict)
    th.start()
    while 1:
        nowtime = datetime.datetime.now()
        if (nowtime-watchdog>datetime.timedelta(seconds=30)):
            th.stop()
            th.join(2)
            th=my_thread(serial_dict)
            th.start()
            watchdog=nowtime
        try:
            txt = input("Please type 'q' to exit...:   ")
            if txt=='q':
                raise KeyboardInterrupt
        except KeyboardInterrupt:
            th.stop()
            th.join()
            break

if __name__ == "__main__":
    main()
