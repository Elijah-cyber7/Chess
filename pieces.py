import numpy as np


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

    def set_moves(self, moves):
        self.moves = moves  # adding a list to store valid moves so we can then find of the valid moves which ones are attacks

    def get_locations(self):
        return self.piece_list.keys()

    def get_locations(self, color):
        uhh = lambda x: x if self.piece_list.get(x).get_color() == color else None
        return map(uhh, self.piece_list.keys())

    def add(self, x, y):
        return tuple(map(sum, zip(x, y)))


class Pawn(Piece):
    def get_moves(self):
        self.moves.append([self.location[0] - self.color_factor, self.location[1] + self.color_factor])
        self.moves.append([self.location[0] + self.color_factor, self.location[1] + self.color_factor])
        self.moves.append([self.location[0], self.location[1] + self.color_factor])
        return self.moves


class Rook(Piece):
    def get_moves(self):
        for i in range(0, 8):
            self.moves.append([self.location[0] + (i * self.color_factor), self.location[1]])
            self.moves.append([self.location[0] - (i * self.color_factor), self.location[1]])
        for i in range(0, 8):
            self.moves.append([self.location[0], self.location[1] + (i * self.color_factor)])
            self.moves.append([self.location[0], self.location[1] - (i * self.color_factor)])
        return self.moves


class Bishop(Piece):
    def __init(self, name, location, image, color):
        super().__init__(name, location, image, color)

    def get_moves(self):
        moves = []
        i = 0
        z = lambda x, y: self.add(x, y) if not self.add(x, y) in self.get_locations(self.color) else ()
        for i in range(8):
            num = i * self.color_factor
            tup_1 = (num, num)
            moves.append(z(self.location, tup_1))
            moves.append(z(self.location, (tup_1 * -1)))
            moves.append(z(self.location, (tup_1[0] * -1, tup_1[1])))
            moves.append(z(self.location, (tup_1[0], tup_1[1] * -1)))
        for m in moves: self.moves.append(m) if not m == () else None
        return list(self.moves)


class King(Piece):
    pass


class Queen(Piece):
    pass


class Knight(Piece):
    def get_moves(self):
        self.moves.append([self.location[0] + 2, self.location[1] + 1])
        self.moves.append([self.location[0] - 2, self.location[1] - 1])
        self.moves.append([self.location[0] - 2, self.location[1] + 1])
        self.moves.append([self.location[0] + 2, self.location[1] - 1])
        # i wonder if there is an algorithmic way to do this, it seems like a fun mind challange
        self.moves.append([self.location[0] + 1, self.location[1] + 2])
        self.moves.append([self.location[0] - 1, self.location[1] - 2])
        self.moves.append([self.location[0] - 1, self.location[1] + 2])
        self.moves.append([self.location[0] + 1, self.location[1] - 2])
        return self.moves

# we want to keep adding moves until we reach one of our pices or an opposing piece. If it is an opposing piece i want it to stop on that piece so that it is attackable
while flag:
    add to list unless intersection