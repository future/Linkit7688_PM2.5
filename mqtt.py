import paho.mqtt.publish as publish

class mqtt:
	def __init__(self):
		self.host = 'MQTT.broker.server'
		self.port = 1883
		self.topic = 'YOUR/TOPIC'

	def pub(self, data):
		try:
			publish.single(self.topic, data, hostname=self.host, port = self.port)
		except:
			print('Send Error !')

		


