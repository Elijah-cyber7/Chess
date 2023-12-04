import pieces
##TPWGAHPENFQCTF6
class Bot:
	def __init__(self, board,color):
		self.color = color
		self.game = board
		self.move_count = 0
		self.moves = []
		self.attacks = []

	point_dict = {
					"queen": 9,
		            "pawn": 1,
		            "knight": 3,
		            "rook": 5,
		            "bishop": 3,
		            "kjng": 20
	}
	lost_list = []
	attackable = []
	def search():
		if self.move_count < 10:
			self.moves = self.game.valid_moves(self.color)


