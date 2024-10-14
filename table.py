import serial,time
from matplotlib import pyplot
s=serial.Serial('/dev/ttyUSB0',38400,timeout=1)
#query instrument id
print(s.readline())

s.write(b'*IDN?\n')
print(s.readline())


def query(cmd):
	s.write((cmd+'\n').encode())
	return s.readline().strip().decode()
def write(cmd):
	s.write((cmd+'\n').encode())
	
pyplot.ion()
pyplot.show()
for a in range(1000):
	pyplot.scatter(a,float(query('MEAS:1?')))
	pyplot.pause(0.2)
#remote comment
