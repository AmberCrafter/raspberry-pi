import serial
import datetime
# import time
import threading

def serail_read(self):
    ''' serial reading'''
    # ser = serial.Serial('/dev/ttyUSB0',38400,timeout=1)
    ser = serial.Serial(**config)
    th = threading.currentThread()
    while getattr(th,'do_run',True):
        data = ser.readline()
        try:
            data = data.decode('ascii')
            txt = '{time},{data}'.format(time=datetime.datetime.now(),data=data)
        except:
            txt = '[WARNING] {time},{data}'.format(time=datetime.datetime.now(),data=data)
        txt = txt.replace('\r','')
        if not ('\n' in txt): txt+='\n'
        f = open('./data/log.txt','a+')
        f.write(txt)
        f.close()


def main():
    serial_dict=dict(
        port='/dev/ttyUSB0',
        baudrate=38400,
        timeout=5
    )
    th = threading.Thread(target=serail_read, args=(serial_dict,))
    # th.do_run=True
    th.start()
    while 1:
        try:
            txt = input()
            if txt=='q':
                raise KeyboardInterrupt
        except KeyboardInterrupt:
            th.do_run=False
            th.join()

if __name__ == "__main__":
    main()
