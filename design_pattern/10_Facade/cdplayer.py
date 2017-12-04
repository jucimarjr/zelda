class CdPlayer:
	"""docstring for CdPlayer"""
	def __init__(self, description,amplifier):
		self._description = description
		self._amplifier = amplifier
		self._current_track = None
		self._title = None


	def on(self):
		print (self._description + " on")

	def off(self):
		print (self._description + " off")

	def eject(self):
		self._title = None
		print (self._description + " eject")

	def play_title(self, title):
		self._title = title
		self._current_track = 0
		print (self._description + ' playing "' + self._title + '"')

	def play_track(self,track):
		if self._title is None:
			print(self._description + " can't play track " + self._current_track + " , no cd inserted")
		else:
			self._current_track =  track
			print (self._description + " playing track " + self._current_track)

	def stop(self):
		self._current_track = 0
		print (self._description + " stopped")

	def pause(self):
		print (self._description + 'paused "' + self._title + '"')

	def __str__(self):
		return self._description