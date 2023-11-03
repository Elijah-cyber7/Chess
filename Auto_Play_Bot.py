import pieces

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
		            "king": 20
	}
	lost_list = []
	attackable = []
	def move(self, board):

	def opening(self,board,movecount):

		moves = lambda x: tuple(x) if x == 'move' else None
		self.moves = list(map(moves, self.game.get_moves().keys()))




