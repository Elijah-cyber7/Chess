class Board:
    squares = []
    locations = {}
    piece_moves = {}
    moves = []
    test_locations = {}
    move_dict = {0: 'a',
                 1: 'b',
                 2: 'c',
                 3: 'd',
                 4: 'e',
                 5: 'f',
                 6: 'g',
                 7: 'h',
                 }
    def __init__(self):
        self.under_attack = []
        self.captured = []
        self.moves = Board.moves
        self.turn = 2
        self.Last = Piece
        self.next = {} # list of moves in the game so you can record and hopefully feed to computer
    def get_locations(self):
        return self.locations
    def get_moves(self, color):
        self.piece_moves.clear()
        for i in self.locations.values():
            if not i.get_color() == color: # get all the opposite colors moves
                self.piece_moves.update(i.get_moves()) # add them to one big dictionary of moves to attack or regular moves i.e (0,0): 'attack' or (0,1) : 'move'
        print(list(self.piece_moves.keys()))
        return self.piece_moves


    def get_underAttack(self, color):  # getter for list of pieces under attack
        self.under_attack.clear()
        mvs = self.get_moves(color) # grab all the opponents moves
        for i in mvs.keys(): # get all the pieces with moves probably want to make sure the moves are valid beforehand to account for pinned pieces
            if i in self.locations: # if the move is an attack then we add the move and the piece it is attacking to our under_attack list
                self.under_attack.append(self.locations.get(i).get_name())
        return self.under_attack

    def valid_moves(self,some_piece):
        valid = {}
        next = some_piece.get_moves()
        for i in next.keys():
            if not self.locations.get(i): # we can temporarily pop the piece to moves location out of the board locations list and insert a move and then retest the enemy's attacks to see if they can still attack our king
                self.locations.pop(some_piece.get_location()) # pick up our current piece
                self.locations.update({i: some_piece}) # see what it looks like in one of its moves
                new_attacks = self.get_underAttack(some_piece.get_color()) # reevaluate the board

                if 'king' not in new_attacks:
                    valid.update({i: next.get(i)})
                    self.locations.pop(i)
                    self.locations.update({some_piece.get_location(): some_piece}) # reset the piece we were going to move

                else:
                    self.locations.pop(i)
                    self.locations.update({some_piece.get_location(): some_piece})  # reset the piece we were going to move
            else:
                temp = self.locations.get(i)
                self.locations.pop(some_piece.get_location())
                self.locations.pop(i)
                self.locations.update({i: some_piece})
                new_attacks = self.get_underAttack(some_piece.get_color())  # reevaluate the board
                if 'king' not in new_attacks:
                    valid.update({i: next.get(i)})
                    self.locations.update({i: temp})
                    self.locations.update({some_piece.get_location(): some_piece}) # reset the piece we were going to move
                else:
                    self.locations.update({i: temp})
                    self.locations.update({some_piece.get_location(): some_piece})  # reset the piece we were going to move
        return valid

    def get_all_valid_moves(self,color):
        #self.piece_moves.clear()
        ii = 0
        for i in list(self.locations.values()):
            if i.get_color() == color:
                if self.valid_moves(i).keys(): ii +=1
        return ii

    def get_turn(self):
        if self.turn % 2: return 'black'
        else: return 'white'
    def set_turn(self):
        self.turn +=1
    def add_Piece(self,Piece):
        self.locations.update({Piece.get_location(): Piece})
    def move(self, coordinates):

        cur_piece = self.locations.get(coordinates) if coordinates in self.locations.keys() and self.locations.get(
            coordinates).get_color() == self.get_turn() else None # we want to get the piece that is currently selected so we check to see if it is an actual piece and if its that pieces color's turn to move
        if cur_piece and not self.get_all_valid_moves(cur_piece.get_color()):
            return -10
        if coordinates in self.next.keys():
            if self.Last.get_name() == 'pawn':
                if self.next.get(coordinates) == 'en':
                    print("WE HERE")
                    self.Last.google_en_passant(coordinates)
                    self.Last.set_location(coordinates)
                    self.moves.append(str(self.Last.get_notation()) + str(Board.move_dict.get(coordinates[0])) + str(coordinates[1]))
                    self.next.clear()
                    self.set_turn()
                elif self.next.get(coordinates) == 'enn':
                    self.Last.set_en(False)
                    self.locations.pop(self.Last.get_piece())
                    self.Last.set_location(coordinates)
                    self.next.clear()
                    self.set_turn()
                else:
                    self.Last.set_en(False)
                    self.Last.set_location(coordinates)
                    self.moves.append(str(self.Last.get_notation()) + str(Board.move_dict.get(coordinates[0])) + str(coordinates[1]))
                    self.next.clear()
                    self.set_turn()
            else:
                self.Last.set_location(coordinates)
                self.moves.append(str(self.Last.get_notation()) + str(Board.move_dict.get(coordinates[0])) + str(coordinates[1]))
                self.next.clear()
                self.set_turn()
            return []

        elif coordinates in self.next.keys() and not cur_piece.get_location() == coordinates:
            self.locations.pop(cur_piece.get_location)
            self.Last.set_location(coordinates)
            self.moves.append(str(cur_piece.get_notation()) +'x'+ str(Board.move_dict.get(coordinates[0])) + str(coordinates[1]))
            self.next.clear()
            self.set_turn()
            return []
        elif cur_piece:
            self.next = self.valid_moves(cur_piece)
            if self.Last: del self.Last
            self.Last = cur_piece
            return list(self.valid_moves(cur_piece).keys())

        return []

class Piece:

    def __init__(self, name, location, image, color, board):
        self.name = name
        self.location = tuple(location)
        self.starting_square = location
        self.image = image
        self.color = color
        self.moves = {}
        self.attacks = []
        self.color_factor = 1 + ((self.color == 'black') * -2)
        self.board = board
        self.piece_list = Board.locations

    def set_name(self, name):
        self.name = name
    def get_notation(self):
        dict  = {'pawn': '',
                 'rook': 'R',
                 'king': 'K',
                 'queen': 'Q',
                 'bishop': 'B',
                 'knight': 'N',}
        return dict.get(self.get_name())
    def clean(self, lis):
        mo = {}
        for i in lis:
            if not i == () and not i == self.get_location():
                if i[0] <= 7 and i[1] <= 7 and i[0] >= 0 and i[1] >= 0 and i not in self.get_locations_B(): # make sure the location is on the board
                    mo.update({tuple(i):self.moves.get(i)})
            else:
                continue
        return mo

    def set_location(self, location):
        Board.locations.pop(self.location)
        self.location = location
        Board.locations.update({self.location: self})

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
        return list(self.piece_list.keys())

    def get_locations_B(self):
        uhh = lambda x: tuple(x) if self.piece_list.get(x).get_color() == self.color else None # get the location of friendly pieces
        return list(map(uhh, self.piece_list.keys()))
    def get_enemy_locations(self):
        uhh = lambda x: tuple(x) if not self.piece_list.get(x).get_color() == self.color else None
        return list(map(uhh, self.piece_list.keys()))
    def add(self, x, y):
        return tuple(((x[0] + y[0]), (x[1] + y[1])))

    def check(self, x):
        if x not in self.get_locations_B() and x not in self.get_enemy_locations():
            self.moves.update({tuple(x): 'move'})
            return True

        elif x in self.get_enemy_locations():
            self.moves.update({tuple(x): 'attack'})
            return False
        else:
            return False

    def __exit__(self, exc_type, exc_val, exc_tb):
        del self


class Pawn(Piece):
    def __init__(self, name, location, image, color,board):
        super().__init__(name, location, image, color,board)
        self.en = False
        self.kill = ()
    def google_en_passant(self,x):
        targets = [self.add(x,(self.color_factor*-1,0)), self.add(x,(self.color_factor,0))] # this is the place where the pice would move to attack the current piece using en passant
        for trg in targets:
            piece =  self.piece_list.get(tuple(trg))
            if trg in self.get_locations() and piece.get_name() == 'pawn': # so we just want to check that if there is a piece there that it is a pawn
                piece.moves.update({tuple(self.add(x,(0,self.color_factor*-1))): 'enn'})
                print("Added")
                piece.set_piece(x)
                piece.set_en(True)
    def check(self, x):
        if x not in self.get_locations():
            self.moves.update({tuple(x): 'move'})
            return True
        else:
            return False
    def check_attacks(self):
        attacks = [(self.location[0] - self.color_factor, self.location[1] + self.color_factor),(self.location[0] + self.color_factor, self.location[1] + self.color_factor)]
        for attack in attacks:
            if attack in self.get_enemy_locations():
                self.moves.update({attack: 'attack'})
    def get_moves(self):
        if not self.en : self.moves.clear()
        maybe_en_passant = self.add(self.location,tuple((0,self.color_factor*2)))
        if self.location == self.starting_square:
            if self.check(self.add(self.location, tuple((0,self.color_factor)))):
                if self.check(maybe_en_passant): self.moves.update({maybe_en_passant: 'en'})

        else:
            self.check(self.add(self.location, tuple((0,self.color_factor))))
        self.check_attacks()
        #self.en = False
        return self.clean(self.moves)
    def set_en(self, e):
        self.en = e
    def get_piece(self):
        return self.kill
    def set_piece(self, x):
        self.kill = x
    def clear_moves(self):
        self.moves.clear()
class Rook(Piece):
    def get_moves(self):
        self.moves.clear()
        i = 1
        e, f, g, h, can_move = True, True, True, True, True
        while can_move and i < 8:
            num = i * self.color_factor
            if not e and f and g and h:
                can_move = False
            if e: e = self.check(self.add(self.location, (num, 0)))
            if f: f = self.check(self.add(self.location, (num * -1, 0)))
            if g: g = self.check(self.add(self.location, (0, num * -1)))
            if h: h = self.check(self.add(self.location, (0, num)))
            i += 1
        return self.clean(self.moves)


class Bishop(Piece):

    def get_moves(self):
        self.moves.clear()
        i = 1
        a, b, c, d, can_move = True, True, True, True, True
        while can_move and i < 8:
            num = i * self.color_factor
            if not a and b and c and d:
                can_move = False
            if a: a = self.check(self.add(self.location, (num, num)))
            if b: b = self.check(self.add(self.location, (num * -1, num * -1)))
            if c: c = self.check(self.add(self.location, (num, num * -1)))
            if d: d = self.check(self.add(self.location, (num * -1, num)))
            i += 1
        return self.clean(self.moves)


class King(Piece):
    def get_moves(self):
        self.moves.clear()
        for i in range(-1, 2):
            for x in range(-1, 2):
                self.check(self.add(self.location, tuple((i, x))))
        return self.clean(self.moves)


class Queen(Piece):
    def __init(self, name, location, image, color):
        super().__init__(name, location, image, color)

    def get_moves(self):
        self.moves.clear()
        i = 1
        a, b, c, d, e, f, g, h, can_move = True, True, True, True, True, True, True, True, True
        while can_move and i <= 7:
            num = i * self.color_factor
            if not a and b and c and d and e and g and f and h:
                can_move = False
            if a: a = self.check(self.add(self.location, (num, num)))
            if b: b = self.check(self.add(self.location, (num * -1, num * -1)))
            if c: c = self.check(self.add(self.location, (num, num * -1)))
            if d: d = self.check(self.add(self.location, (num * -1, num)))
            if e: e = self.check(self.add(self.location, (num, 0)))
            if f: f = self.check(self.add(self.location, (num * -1, 0)))
            if g: g = self.check(self.add(self.location, (0, num * -1)))
            if h: h = self.check(self.add(self.location, (0, num)))

            i += 1
        return self.clean(self.moves)


class Knight(Piece):
    def get_moves(self):
        self.moves.clear()
        for i in range(-2, 3):
            if i == 0:
                continue
            for x in range(2):
                self.check(self.add(self.location, tuple((i, (3-abs(i))*((x%2)*2-1)))))
        return self.clean(self.moves)
