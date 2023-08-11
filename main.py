

import pygame
import pieces


pygame.init()
WIDTH = 1000
HEIGHT = 900

selection = ()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
timer = pygame.time.Clock()
fps = 120
run = True
# Game Variables, lists for black and white pieces and locations
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]

black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]

black_dict = {'pawn': 'images/black pawn.png',
              'rook': 'images/black rook.png',
              'knight': 'images/black knight.png',
              'bishop': 'images/black bishop.png',
              'king': 'images/black king.png',
              'queen': 'images/black queen.png'}

white_dict = {'pawn': 'images/white pawn.png',
              'rook': 'images/white rook.png',
              'knight': 'images/white knight.png',
              'bishop': 'images/white bishop.png',
              'king': 'images/white king.png',
              'queen': 'images/white queen.png'}
# dictionary to translate from grid to chess moves

move_dict = {0: 'a',
             1: 'b',
             2: 'c',
             3: 'd',
             4: 'e',
             5: 'f',
             6: 'g',
             7: 'h',
             }
# empty list to hold game information
total = []


def event_handler(coordinates):
	cur_piece = locations.get(coordinates)
	pygame.draw.rect(screen, 'red',
	                 [cur_piece.get_location()[0] * 100 + 1, cur_piece.get_location()[1] * 100 + 1, 100, 100],
	                 2)  # highlighting the sqaure to show that it is selected


def transform_pieces():  # function meant to just scale the images to usable size
	for i in total:
		if i.get_name() == 'pawn':
			i.set_image(pygame.transform.scale(i.get_image(), (65, 65)))
		else:
			i.set_image(pygame.transform.scale(i.get_image(), (80, 80)))


def draw_pieces():  # function to constantly draw pieces on the board
	for j in total:
		# next = game.find_moves(j)
		if j.get_name() == 'pawn':
			screen.blit(j.get_image(), (j.get_location()[0] * 100 + 20, j.get_location()[1] * 100 + 20))
		else:
			screen.blit(j.get_image(), (j.get_location()[0] * 100 + 10, j.get_location()[1] * 100 + 10))


#	if selection == j.get_location():
#		pygame.draw.rect(screen, 'red', [j.get_location()[0] * 100 + 1, j.get_location()[1] * 100 + 1, 100, 100], 2)
#		for l in next: pygame.draw.circle(screen, 'red', [(l[0] * 100) + 50, (l[1] * 100) + 50], 5, 0)
#	if selection in next:
#		j.set_location(selection)

def init_pices():  # factory funtion to create piece objects and the board
	for x in range(len(white_pieces)):
		if white_pieces[x] == 'pawn':
			total.append(
				pieces.Pawn(white_pieces[x], white_locations[x], pygame.image.load(white_dict[white_pieces[x]]),
				            'white'))
			total.append(
				pieces.Pawn(black_pieces[x], black_locations[x], pygame.image.load(black_dict[black_pieces[x]]),
				            'black'))
		elif white_pieces[x] == 'rook':
			total.append(
				pieces.Rook(white_pieces[x], white_locations[x], pygame.image.load(white_dict[white_pieces[x]]),
				            'white'))
			total.append(
				pieces.Rook(black_pieces[x], black_locations[x], pygame.image.load(black_dict[black_pieces[x]]),
				            'black'))

		elif white_pieces[x] == 'bishop':
			total.append(
				pieces.Bishop(white_pieces[x], white_locations[x], pygame.image.load(white_dict[white_pieces[x]]),
				              'white'))
			total.append(
				pieces.Bishop(black_pieces[x], black_locations[x], pygame.image.load(black_dict[black_pieces[x]]),
				              'black'))
		elif white_pieces[x] == 'knight':
			total.append(
				pieces.Knight(white_pieces[x], white_locations[x], pygame.image.load(white_dict[white_pieces[x]]),
				              'white'))
			total.append(
				pieces.Knight(black_pieces[x], black_locations[x], pygame.image.load(black_dict[black_pieces[x]]),
				              'black'))
		elif white_pieces[x] == 'queen':
			total.append(
				pieces.Queen(white_pieces[x], white_locations[x], pygame.image.load(white_dict[white_pieces[x]]),
				             'white'))
			total.append(
				pieces.Queen(black_pieces[x], black_locations[x], pygame.image.load(black_dict[black_pieces[x]]),
				             'black'))
		elif white_pieces[x] == 'king':
			total.append(
				pieces.King(white_pieces[x], white_locations[x], pygame.image.load(white_dict[white_pieces[x]]),
				             'white'))
			total.append(
				pieces.King(black_pieces[x], black_locations[x], pygame.image.load(black_dict[black_pieces[x]]),
				             'black'))


def draw_board():  # drawing the background of the board
	for i in range(32):
		col = (i % 4)
		row = i // 4
		if row % 2 == 0:
			pygame.draw.rect(screen, 'light gray', [600 - (col * 200), row * 100, 100, 100])
		else:
			pygame.draw.rect(screen, 'light gray', [700 - (col * 200), row * 100, 100, 100])


<<<<<<< HEAD
# else:class (Piece):
#   pass
#	pygame.draw.rect(screen, 'light gray', [900 - (col * 200), row * 100, 100, 100])
=======

>>>>>>> fa99ce1 (call to event handler)

init_pices()
transform_pieces()
game = pieces.Board(total)
isAttacked = game.get_underAttack()
locations = game.get_locations()
for i in total: print(str(i.get_name()) + str(i.get_location()))
while run:
	timer.tick(fps)
	screen.fill('dark gray')
	draw_board()
	draw_pieces()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
			x_coord = event.pos[0] // 100
			y_coord = event.pos[1] // 100
			selection = (x_coord, y_coord)
			event_handler(selection)

	pygame.display.flip()
pygame.quit()
