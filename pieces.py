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
        self.starting_square = location
        self.image = image
        self.color = color
        self.moves = {}
        self.attacks = []
        self.color_factor = 1 + ((self.color == 'black') * -2)
        self.piece_list.update({self.location: self})

    def set_name(self, name):
        self.name = name

    def clean(self, lis):
        print(lis)
        mo = []
        for i in lis:
            if not i == ():
                if i[0] <= 7 and i[1] <= 7 and i[0] >= 0 and i[1] >= 0 and i not in self.get_locations_B():
                    mo.append(tuple(i))
            else:
                continue
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
        return list(self.piece_list.keys())

    def get_locations_B(self):
        uhh = lambda x: tuple(x) if self.piece_list.get(x).get_color() == self.color else None
        return list(map(uhh, self.piece_list.keys()))
    def get_enemy_locations(self):
        uhh = lambda x: tuple(x) if not self.piece_list.get(x).get_color() == self.color else None
        return list(map(uhh, self.piece_list.keys()))
    def add(self, x, y):
        print(tuple(((x[0] + y[0]), (x[1] + y[1]))))
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
    def __init__(self, name, location, image, color):
        super().__init__(name, location, image, color)
        self.onStart = True
        self.en = False
    def google_en_passant(self,x):
        targets = [self.add(x,(1,0)), self.add(x,(-1,0))]
        for trg in targets:
            piece =  self.piece_list.get(tuple(trg))
            if trg in self.get_locations() and piece.get_name() == 'pawn':
                piece.moves.update({tuple(self.add(x,(0,self.color_factor*-1))): 'attack'})
                piece.set_en(True)
                print("EN PASSANT")
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
        if not self.en: self.moves.clear()
        maybe_en_passant = self.add(self.location,tuple((0,self.color_factor*2)))
        if self.location == self.starting_square:
            if self.check(self.add(self.location, tuple((0,self.color_factor)))):
                self.check(maybe_en_passant)
                self.google_en_passant(maybe_en_passant)

        else:
            self.check(self.add(self.location, tuple((0,self.color_factor))))
        self.check_attacks()
        return self.clean(self.moves)
    def set_en(self, e):
        self.en = e


class Rook(Piece):
    def get_moves(self):
        print("called")
        self.moves.clear()
        i = 1
        e, f, g, h, can_move = True, True, True, True, True
        while can_move and i < 8:
            num = i * self.color_factor
            if not (e or f or g or h):
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
        while can_move and i < 8:
            num = i * self.color_factor
            tup_1 = (num, num)
            if not a and b and c and d:
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
