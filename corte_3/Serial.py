import serial
import time

puerto=serial.Serial('COM4', baudrate=96000, timeout=1)
while 1:
    dato=input('dato a enviar: ')
    puerto.whrite(dato.encode('utf-8'))
    time.sleep(0.5)
    line=puerto.readline().decode('ascii')
    if str('line').rstrip('\r\n')=='Dato incorrecto ':
        print('Error rn los datos')
        break
    print(str(line).rstrip('\r\n'))