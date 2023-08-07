class Piece:
	def __init__(self, name, location, image,color):
		self.name = name
		self.location = location
		self.image = image
		self.color = color
		self.valid_moves = []
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
	def set_valid_moves(moves):
		self.valid_moves = moves
	def get_valid_moves():
		return valid_moves # adding a list to store valid moves so we can then find of the valid moves which ones are attacks 
		



class Board:
	
	captured = []
	moves = []
	squares = []

	def __init__(self, playable):
		self.playable = playable

	def find_moves(self, piece):
		next = [(0,0)]
		if piece.get_name() == 'pawn':
			next = [(piece.get_location()[0], piece.get_location()[1] - 1)] if piece.ge_color() == 'white' else [(piece.get_location()[0], piece.get_location()[1] + 1)] # adding logic to distinguish if piece is black or white
			next.append(next[0](0) + 1, next[0](1)) # adding diagnol attack to list of next moves 
			for i in self.playable:
				if i.get_location() == next[0]: # figuring out if next move will intersect with existing piece 
					next = [(1000,1000)]
				else if i.get_location() == next[1]: # getting the attack location 
					
		return next


