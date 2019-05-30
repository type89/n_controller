import serial
import matplotlib.pyplot as plt
import datetime

ser = serial.Serial('/dev/ttyACM0',9600,timeout=None)   # '/dev/ttyUSB0'の部分は自分の環境に合わせて変更する


now_time = []
distance = []

i = 0
while i < 10:
    now = datetime.datetime.now()
    now_hms = "{0:%H:%M:%S}".format(now)
    now_time.append(now_hms)
    print(str(now_time[i]))

    bytes_data = ser.readline()
    str_data = bytes_data.decode("UTF-8")
    distance.append(str_data.rstrip(' \n'))
    print(str(distance[i]))

    i+=1
    #print(str(now_time[i]) +temperature[i], end="")

ser.close()

plt.title('Type89 finder')
plt.plot(now_time, distance)
plt.xlabel('time')
plt.ylabel('distance（cm）')
#plt.xlim(Xの最小値, Xの最大値)
#plt.ylim(0, 25)
plt.show()
