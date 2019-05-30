import serial

ser = serial.Serial('/dev/ttyACM0',9600,timeout=None)   # '/dev/ttyUSB0'の部分は自分の環境に合わせて変更する

while True:
    bytes_data = ser.readline()
    str_data = bytes_data.decode("UTF-8")
    print(str_data, end="")

ser.close()
