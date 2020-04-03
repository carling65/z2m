import rtmidi2
import time
import configparser
import ast

class MidiFootController():
	def __init__(self,input_device_name="Zoom G Series",output_device_name="loopMIDI Port"):
		config_ini = configparser.ConfigParser()
		config_ini.read('config.ini')
		self.input_device_name = config_ini['DEFAULT']['INPUT_DEVICE_NAME']
		self.output_device_name= config_ini['DEFAULT']['OUTPUT_DEVICE_NAME']
		self.switch_state = [0,0,0,0,0,0]
		self.start_sysex = ast.literal_eval(config_ini['DEFAULT']['START_SYSEX'])
		self.status_byte = ast.literal_eval(config_ini['DEFAULT']['STATUS_BYTE'])
		
	def startup(self):
		"""
			send starting Sysex message
			Zoom G3		:	F0 52 00 5A 50 F7
			Zoom G3X	:	F0 52 00 59 50 F7
		"""
		
		output_port = self.connect_output_port(self.input_device_name)
		output_port.send_sysex(self.start_sysex[0],self.start_sysex[1],self.start_sysex[2],self.start_sysex[3])
	
	def connect_input_port(self,input_device):
		midi_in = rtmidi2.MidiIn()
		input_port = self.connecting(midi_in,input_device)
		return input_port
	
	def connect_output_port(self,output_device):
		midi_out = rtmidi2.MidiOut()
		output_port = self.connecting(midi_out,output_device)
		return output_port
	
	def connecting(self,midi_io,device_name):
		try:
			index = midi_io.ports_matching(device_name+"*")[0]
			io_port = midi_io.open_port(index)
		except IndexError:
			raise(IOError("Input/Output port not found."))
		return io_port
	
	def change_state(self,x,y):
		self.switch_state[x] = y
	
	def turn_on(self,array):
		now_state = [array[6],array[19],array[33],array[47],array[60],array[74]]
		now_state = [1 if i == 19 else 0 for i in now_state]
		array_detected_change_position = [i - j for i,j in zip(now_state,self.switch_state)]
		pedal_num = array_detected_change_position.index(1)
		self.change_state(pedal_num,1)
		return pedal_num
	
	def turn_off(self,array):
		id_signal = array[5]
		self.change_state(id_signal,0)
		return id_signal
	
	def send_midi(self,port,num):
		hex = 0x00 if num == 0 else 0x01 if num == 1 else 0x02 if num == 2 else 0x03 if num == 3 else 0x04 if num == 4 else 0x05 if num == 5 else 0x09
		port.send_raw(self.status_byte,hex)
	
	def state_of_waiting_input(self):
		input_port = self.connect_input_port(self.input_device_name)
		output_port = self.connect_output_port(self.output_device_name)
		input_port.ignore_types(midi_sysex=False)
		print("If you want to end this program, please press Ctrl-C.")
		try:
			while 1 :
				time.sleep(0.01)
				message = input_port.get_message()
				if message:
					if len(message) == 110:
						pedal_num = self.turn_on(message)
						self.send_midi(output_port,pedal_num)
					elif len(message) == 10:
						pedal_num = self.turn_off(message)
						self.send_midi(output_port,pedal_num)
					else:
						continue
					print(self.switch_state)
				else:
					continue
		except KeyboardInterrupt:
			input_port.close_port()
			output_port.close_port()
			print("quit")


if __name__=="__main__":
	print("Please use after set all fx as T Scream and turn all foot switch off ")
	mfc = MidiFootController()
	mfc.startup()
	mfc.state_of_waiting_input()
