class Piece:
	def __init__(self, name, location, image,color):
		self.name = name
		self.location = location
		self.image = image
		self.color = color
	def set_name(self, name):
		self.name = name

	def set_location(self, location):
		self.location = location

	def get_name(self):
		return self.name

	def get_location(self):
		return self.location

	def get_image(self):
		return self.image

	def set_image(self, image):
		self.image = image
	def get_color(self):
		return self.color

	def set_color(self, color):
		self.color = color



class Board:
	playable = []
	captured = []
	moves = []
	squares = []

	def __init__(self, playable):
		self.playable = playable

	def find_moves(self, piece):
		next = [(0,0)]
		if piece.get_name() == 'pawn':
			next = [(piece.get_location()[0], piece.get_location()[1] - 1)]
			for i in self.playable:
				if i.get_location() == next:
					next = [(1000,1000)]
		return next


