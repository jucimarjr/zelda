from Image import Image
from RealImage import RealImage

class ProxyImage(Image):
	def __init__(self, FILENAME):
		self.filename = FILENAME
		self.image = None

	def displayImage(self):
		if self.image is None:
			self.image = RealImage(self.filename)

		self.image.displayImage()