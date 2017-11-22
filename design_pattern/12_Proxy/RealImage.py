from Image import Image

class RealImage(Image):
	def __init__(self,FILENAME):
		self.filename = FILENAME
		self.loadImageFromDisk()

	def loadImageFromDisk(self):
		print("Loading	", self.filename)

	def displayImage(self):
		print("Displaying	", self.filename)