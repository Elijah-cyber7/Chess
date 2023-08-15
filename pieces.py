class Piece:
    def __init__(self, name, location, image, color):
        self.name = name
        self.location = location
        self.image = image
        self.color = color
        self.moves = []
        self.color_factor = 1 + ((self.color == 'black') * -2)

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
        self.moves = moves     # adding a list to store valid moves so we can then find of the valid moves which ones are attacks
    



class Board:
    squares = []
    
    def __init__(self, playable):
        self.playable = playable
        self.under_attack = []
        self.captured = []
        self.moves = []
        self.locations = {}# list of moves in the game so you can record and hopefully feed to computer

    def get_moves(self):
        return self.moves
        
    def set_moves(self, moves):
        self.moves = moves 
        
    def get_underAttack(self):  # getter for list of pieces under attack
        return self.under_attack
        
    def set_underAttack(self, attacked):  # setter for the list of under attack
        self.under_attack = attacked
        
    def get_locations(self):
        for i in self.playable: 
            self.locations.update({i.get_location(): i}) # creating a dictionary of the pieces with their locations being the key and instance being the value. 
        return self.locations
        
    def set_locations(self, locations):
        self.locations = locations 
        
    def find_moves(self, piece):
        if piece.get_name() == 'pawn':
            next = {((piece.get_location()[0], piece.get_location()[1] + 1) if piece.get_color() == 'white' else  (piece.get_location()[0], piece.get_location()[1] - 1)): 'move'}  # adding logic to distinguish if piece is black or white
            attacking = [(next[0][0] + 1, next[0][1])]  # adding diagonal attack to list of next moves

            for i in self.playable:
                if i.get_location() in next:  # figuring out if next move will intersect with existing piece
                    next = [(1000, 1000)]
                elif i.get_location() in attacking:  # getting the attack location
                    self.under_attack.append(i.get_location())  # setting this move to be an attack instead of a regular move
        else:
            next = {(0,0): 'none'}
        return next

class Pawn(Piece):
    def get_moves(self):
        self.moves.append([self.location[0] - self.color_factor, self.location[1] - self.color_factor ])
        self.moves.append([self.location[0] + self.color_factor, self.location[1] - self.color_factor])
        self.moves.append([self.location[0],self.location[1] - self.color_factor])
        return self.moves
class Rook(Piece):
    def get_moves(self):
        for i in range(0,8):
            self.moves.append([self.location[0] + (i * self.color_factor), self.location[1]])
            self.moves.append([self.location[0] - (i * self.color_factor), self.location[1]])
        for i in range(0,8):
            self.moves.append([self.location[0], self.location[1] + (i * self.color_factor)])
            self.moves.append([self.location[0], self.location[1] - (i * self.color_factor)])
        return self.moves
class Bishop(Piece):
    def get_moves(self):
        for i in range(8):
            self.moves.append([self.location[0] + (i * self.color_factor), self.location[1] + (i * self.color_factor)])
            self.moves.append([self.location[0] - (i * self.color_factor), self.location[1] - (i * self.color_factor)])
            self.moves.append([self.location[0] - (i * self.color_factor), self.location[1] + (i * self.color_factor)])
            self.moves.append([self.location[0] + (i * self.color_factor), self.location[1] - (i * self.color_factor)])


        return self.moves
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


