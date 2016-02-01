import mraa
import time

from multiprocessing import Queue,Process

import move_avge

class sensor(Process):
	def __init__(self, q):
		Process.__init__(self)
		self.q = q

		self.u=mraa.Uart(0)
		self.u.setBaudRate(9600)
		self.u.setMode(8, mraa.UART_PARITY_NONE, 1)
		self.u.setFlowcontrol(False, False)

		self.cfpm1_0_avg = move_avge.avge(60)		
		self.cfpm2_5_avg = move_avge.avge(60)		
		self.cfpm10_avg = move_avge.avge(60)		
		self.pm1_0_avg = move_avge.avge(10)		
		self.pm2_5_avg = move_avge.avge(10)		
		self.pm10_avg = move_avge.avge(10)		


	def data_log(self, dstr):
		bytedata = bytearray(dstr)
		CF_PM1_0 = bytedata[4]*256 + bytedata[5]
		CF_PM2_5 = bytedata[6]*256 + bytedata[7]
		CF_PM10 = bytedata[8]*256 + bytedata[9]
		PM1_0 = bytedata[10]*256 + bytedata[11]
		PM2_5 = bytedata[12]*256 + bytedata[13]
		PM10 = bytedata[14]*256 + bytedata[15]
	
		self.cfpm1_0_avg.add(CF_PM1_0)
		self.cfpm2_5_avg.add(CF_PM2_5)
		self.cfpm10_avg.add(CF_PM10)
		self.pm1_0_avg.add(PM1_0)
		self.pm2_5_avg.add(PM2_5)
		self.pm10_avg.add(PM10)

	def get_data(self):
		CF_PM1_0 = self.cfpm1_0_avg.get()
		CF_PM2_5 = self.cfpm2_5_avg.get()
		CF_PM10 = self.cfpm10_avg.get()
		PM1_0 = self.pm1_0_avg.get()
		PM2_5 = self.pm2_5_avg.get()
		PM10 = self.pm10_avg.get()

		ret = {	'CFPM1.0': CF_PM1_0,
			'CFPM2.5': CF_PM2_5,
			'CFPM10': CF_PM10,
			'PM1.0': PM1_0,
			'PM2.5': PM2_5,
			'PM10': PM10
			}

		return ret

	def run(self):
		count = 0

		while True:
			if self.u.dataAvailable():
				time.sleep(0.05)
				getstr = self.u.readStr(24)

				if len(getstr) == 24:
					self.data_log(getstr)

					if count == 0:
						g = self.get_data()
						self.q.put(g)
					count = (count+1)%10
					


if __name__ == '__main__':

	q = Queue()
	p = sensor(q)
	p.start()


	while True:
		print('air: '+ str(q.get()))

