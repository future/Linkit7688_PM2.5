import mraa
import mqtt
import time

import g3 as air_sensor
import sht2x as tmp_sensor
from multiprocessing import Queue


if __name__ == '__main__':

	air_data = ''
	tmp_data = ''

	air_q = Queue()
	tmp_q = Queue()

	air = air_sensor.sensor(air_q)
	tmp = tmp_sensor.sensor(tmp_q)

	air.start()
	tmp.start()

	pat = 'PM1.0={pm1_0},PM2.5={pm2_5},PM10={pm10},Tmp={tmp:5.3f},RH={rh}'
	tmp_data = {'Tmp':0.0, 'RH':0}

	while True:
		air_data = air_q.get()
		
		if not tmp_q.empty():
			tmp_data = tmp_q.get()

		send_str = pat.format(
		    pm1_0=air_data['CFPM1.0'],
		    pm2_5=air_data['CFPM2.5'],
		    pm10=air_data['CFPM10'],
		    tmp=tmp_data['Tmp'],
		    rh=tmp_data['RH'],
		    )

		mqtt.mqtt().pub(send_str)

