import mraa
import time
from multiprocessing import Queue,Process


class sensor(Process):
        def __init__(self,q):
		Process.__init__(self)
		self.q = q
                self.tmp = 0
                self.sensor = mraa.I2c(0)
                self.sensor.address(0x40)
		self.Tcmd = 0xF3
		self.RHcmd = 0xF5

	def run(self):
		T = self.getT()
		RH = self.getRH()
		send_data = {
			'Tmp':T,
			'RH':RH
		}
		self.q.put(send_data)


		while True:
			send_data['Tmp'] = self.getT()
			time.sleep(5)
			send_data['RH'] = self.getRH()
			
			self.q.put(send_data)
			time.sleep(5)
			

        def getT(self):
		self.sensor.writeByte(self.Tcmd)
		time.sleep(0.1)
                d = self.sensor.read(3)
		bdata = bytearray(d)
		
		St = bdata[0]*256+bdata[1]
		T = (175.72*St/2**16)-46.85

		return T


	def getRH(self):
		self.sensor.writeByte(self.RHcmd)
		time.sleep(0.1)
		d = self.sensor.read(3)
		bdata = bytearray()
		bdata.extend(d)
		
		Srh = bdata[0]*256+bdata[1]
		RH = (125*Srh/2**16)-6

		return RH

if __name__ == '__main__':

	q = Queue()
        sen = sensor(q)
	sen.start()

	while True:
		if not q.empty():
			print(str(q.get()))
		else:	
			print('wait...')
			time.sleep(1)
		


