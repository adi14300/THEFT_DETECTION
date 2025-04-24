import serial

def get_location():
    try:
        gps = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=1)
        data = gps.readline()
        if b'GPGGA' in data:
            line = data.decode('utf-8').split(',')
            return (line[2], line[4])  # latitude, longitude
    except:
        return ("Unavailable", "Unavailable")
