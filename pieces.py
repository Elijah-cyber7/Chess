
class Board:
	squares = []

	def __init__(self, playable):
		self.playable = playable
		self.under_attack = []
		self.captured = []
		self.moves = []
		self.locations = {}  # list of moves in the game so you can record and hopefully feed to computer

	def get_moves(self):
		return self.moves

	def set_moves(self, moves):
		self.moves = moves

	def get_underAttack(self):  # getter for list of pieces under attack
		return self.under_attack

	def set_underAttack(self, attacked):  # setter for the list of under attack
		self.under_attack = attacked


class Piece:
	piece_list = {}

	def __init__(self, name, location, image, color):
		self.name = name
		self.location = tuple(location)
		self.image = image
		self.color = color
		self.moves = []
		self.color_factor = 1 + ((self.color == 'black') * -2)
		self.piece_list.update({self.location: self})

	def set_name(self, name):
		self.name = name

	def clean(self, lis):
		mo = []
		for i in lis:
			if not i == ():
				if i[0] <= 7 and i[1] <= 7 and i[0] >= 0 and i[1] >= 0 and i not in self.get_locations_B():
					mo.append(tuple(i))
		return mo

	def set_location(self, location):
		self.piece_list.pop(self.location)
		self.location = location
		self.piece_list.update({self.location: self})

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

	def set_moves(self, moves):
		self.moves = moves  # adding a list to store valid moves so we can then find of the valid moves which ones are attacks

	def get_locations(self):
		return self.piece_list.keys()

	def get_locations_B(self):
		uhh = lambda x: tuple(x) if self.piece_list.get(x).get_color() == self.color else None
		return list(map(uhh, self.piece_list.keys()))

	def add(self, x, y):
		return tuple(map(sum, zip(x, y)))

	def __exit__(self, exc_type, exc_val, exc_tb):
		del self


class Pawn(Piece):
	def get_moves(self):
		self.moves.clear()
		self.moves.append((self.location[0] - self.color_factor, self.location[1] + self.color_factor))
		self.moves.append((self.location[0] + self.color_factor, self.location[1] + self.color_factor))
		self.moves.append((self.location[0], self.location[1] + self.color_factor))
		return self.clean(self.moves)


class Rook(Piece):
	def get_moves(self):
		self.moves.clear()
		z = lambda x, y: self.add(x, y) if not self.add(x, y) in self.get_locations() and not self.add(x,y) == () else ()
		i = 0
		e, f, g, h, can_move = True, True, True, True, True
		while can_move and i < 8:
			num = i * self.color_factor
			tup_1 = (num, num)
			if e:
				self.moves.append(z(self.location, (tup_1[0], 0)))
			if not z(self.location, (tup_1[0] * -1, 0)): f = False
			if f:
				self.moves.append(z(self.location, (tup_1[0] * -1, 0)))

			if not z(self.location, (0, tup_1[0] * -1)): g = False
			if g:
				self.moves.append(z(self.location, (0, tup_1[0] * -1)))
			if not z(self.location, (0, tup_1[0])): h = False
			if h:
				self.moves.append(z(self.location, (0, tup_1[0])))

			i += 1
		return self.clean(self.moves)


class Bishop(Piece):
	def __init(self, name, location, image, color):
		super().__init__(name, location, image, color)

	def get_moves(self):
		self.moves.clear()
		z = lambda x, y: self.add(x, y) if not self.add(x, y) in self.get_locations() and not self.add(x, y) == () else ()
		i = 0
		a, b, c, d, can_move = True, True, True, True, True
		while can_move and i < 8:
			num = i * self.color_factor
			tup_1 = (num, num)
			if not a and b and c and d:
				can_move = False
			if not z(self.location, tup_1) == (): a = False
			if a:
				self.moves.append(z(self.location, tup_1))

			if not z(self.location, (tup_1[0] * -1, tup_1[1] * -1)) == (): b = False
			if b:
				self.moves.append(z(self.location, (tup_1[0] * -1, tup_1[1] * -1)))

			if not z(self.location, (tup_1[0], tup_1[1] * -1)): c = False
			if c:
				self.moves.append(z(self.location, (tup_1[0], tup_1[1] * -1)))

			if not z(self.location, (tup_1[0] * -1, tup_1[1])): d = False
			if d:
				self.moves.append(z(self.location, (tup_1[0] * -1, tup_1[1])))
			i += 1
		return self.clean(self.moves)


class King(Piece):
	pass


class Queen(Piece):
	def __init(self, name, location, image, color):
		super().__init__(name, location, image, color)

	def get_moves(self):
		self.moves.clear()
		z = lambda x, y: self.add(x, y) if not self.add(x, y) in self.get_locations() and not self.add(x, y) == () else ()
		i = 0
		a, b, c, d, e, f, g, h, can_move = True, True, True, True, True, True, True, True, True
		while can_move and i < 8:
			num = i * self.color_factor
			tup_1 = (num, num)
			if not a and b and c and d:
				can_move = False
			if not z(self.location, tup_1) == (): a = False
			if a:
				self.moves.append(z(self.location, tup_1))

			if not z(self.location, (tup_1[0] * -1, tup_1[1] * -1)) == (): b = False
			if b:
				self.moves.append(z(self.location, (tup_1[0] * -1, tup_1[1] * -1)))

			if not z(self.location, (tup_1[0], tup_1[1] * -1)): c = False
			if c:
				self.moves.append(z(self.location, (tup_1[0], tup_1[1] * -1)))

			if not z(self.location, (tup_1[0] * -1, tup_1[1])): d = False
			if d:
				self.moves.append(z(self.location, (tup_1[0] * -1, tup_1[1])))
			if not z(self.location, (tup_1[0], 0)): e = False
			if e:
				self.moves.append(z(self.location, (tup_1[0], 0)))
			if not z(self.location, (tup_1[0] * -1, 0)): f = False
			if f:
				self.moves.append(z(self.location, (tup_1[0] * -1, 0)))

			if not z(self.location, (0, tup_1[0] * -1)): g = False
			if g:
				self.moves.append(z(self.location, (0, tup_1[0] * -1)))
			if not z(self.location, (0, tup_1[0])): h = False
			if h:
				self.moves.append(z(self.location, (0, tup_1[0])))

			i += 1
		return self.clean(self.moves)


class Knight(Piece):
	def get_moves(self):
		self.moves.clear()
		self.moves.append((self.location[0] + 2, self.location[1] + 1))
		self.moves.append((self.location[0] - 2, self.location[1] - 1))
		self.moves.append((self.location[0] - 2, self.location[1] + 1))
		self.moves.append((self.location[0] + 2, self.location[1] - 1))
		# i wonder if there is an algorithmic way to do this, it seems like a fun mind challange
		self.moves.append((self.location[0] + 1, self.location[1] + 2))
		self.moves.append((self.location[0] - 1, self.location[1] - 2))
		self.moves.append((self.location[0] - 1, self.location[1] + 2))
		self.moves.append((self.location[0] + 1, self.location[1] - 2))
		print(self.clean(self.moves))
		return self.clean(self.moves)
