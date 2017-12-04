class Amplifier:
	def __init__(self, description):
		self._description = description
		self._tuner = None
		self._dvd_player = None
		self._cd_player = None

	def on(self):
		print (self._description + " on")
	
	def off(self):
		print (self._description + " off")
	
	def set_stereo_sound(self):
		print (self._description + " stereo mode on")
	
	def set_surround_sound(self):
		print(self._description + " surround on " "(5 speakers, 1 subwoofer) ")
	
	def set_volume(self, level):
		print (self._description + " setting volume to " + str(level))
	
	def	set_tuner(self, tuner):
		print (self._description + " setting tuner to " + tuner)
		self._tuner = tuner

	def set_dvd(self, dvd):
		print (self._description + " setting DVD player to " + str(dvd))
		self._dvd_player = dvd

	def set_cd(self, cd):
		print (self._description + " setting Cd player to " + cd)
		self._cd_player =  cd

	def __str__(self):
		return self._description	