import pygame
from pieces import *

pygame.init()
WIDTH = 1000
HEIGHT = 900

coordinates = (10, 10)
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
def init_pices():  # factory funtion to create piece objects and the board
    for x in range(len(white_pieces)):
        if white_pieces[x] == 'pawn':

            Pawn(white_pieces[x], white_locations[x], pygame.image.load(white_dict[white_pieces[x]]), 'white')

            Pawn(black_pieces[x], black_locations[x], pygame.image.load(black_dict[black_pieces[x]]), 'black')
        elif white_pieces[x] == 'rook':

            Rook(white_pieces[x], white_locations[x], pygame.image.load(white_dict[white_pieces[x]]), 'white')

            Rook(black_pieces[x], black_locations[x], pygame.image.load(black_dict[black_pieces[x]]), 'black')

        elif white_pieces[x] == 'bishop':

            Bishop(white_pieces[x], white_locations[x], pygame.image.load(white_dict[white_pieces[x]]), 'white')

            Bishop(black_pieces[x], black_locations[x], pygame.image.load(black_dict[black_pieces[x]]), 'black')
        elif white_pieces[x] == 'knight':

            Knight(white_pieces[x], white_locations[x], pygame.image.load(white_dict[white_pieces[x]]), 'white')

            Knight(black_pieces[x], black_locations[x], pygame.image.load(black_dict[black_pieces[x]]), 'black')
        elif white_pieces[x] == 'queen':

            Queen(white_pieces[x], white_locations[x], pygame.image.load(white_dict[white_pieces[x]]), 'white')

            Queen(black_pieces[x], black_locations[x], pygame.image.load(black_dict[black_pieces[x]]), 'black')
        elif white_pieces[x] == 'king':

            King(white_pieces[x], white_locations[x], pygame.image.load(white_dict[white_pieces[x]]), 'white')

            King(black_pieces[x], black_locations[x], pygame.image.load(black_dict[black_pieces[x]]), 'black')


def draw_board():  # drawing the background of the board
    for i in range(32):
        col = (i % 4)
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, 'light gray', [600 - (col * 200), row * 100, 100, 100])
        else:
            pygame.draw.rect(screen, 'light gray', [700 - (col * 200), row * 100, 100, 100])


init_pices()
next = []
Last = Piece
locations = Piece.piece_list


def transform_pieces():  # function meant to just scale the images to usable size
    for i in locations.values():
        if i.get_name() == 'pawn':
            i.set_image(pygame.transform.scale(i.get_image(), (65, 65)))
        else:
            i.set_image(pygame.transform.scale(i.get_image(), (80, 80)))


transform_pieces()


def draw_pieces():  # function to constantly draw pieces on the board
    for j in locations.values():
        # next = game.find_moves(j)
        if j.get_name() == 'pawn':
            screen.blit(j.get_image(), (j.get_location()[0] * 100 + 20, j.get_location()[1] * 100 + 20))
        else:
            screen.blit(j.get_image(), (j.get_location()[0] * 100 + 10, j.get_location()[1] * 100 + 10))


def event_handler(coordinates):
    global next
    global Last

    cur_piece = locations.get(coordinates) if coordinates in locations.keys() else None
    pygame.draw.rect(screen, 'red',
                     [coordinates[0] * 100 + 1, coordinates[1] * 100 + 1, 100, 100],
                     2)
    if coordinates in next:
        if Last.get_name() == 'pawn' and Last.get_moves().get(coordinates) == 'en':
            Last.set_en(False)
            locations.pop(Last.get_piece())
            Last.set_location(coordinates)
            next.clear()
        else:
            Last.set_location(coordinates)
            next.clear()

    elif coordinates in next and not cur_piece.get_location() == coordinates:
        print(cur_piece)
        locations. pop(cur_piece.get_location)
        Last.set_location(coordinates)
        next.clear()

    elif cur_piece:
        next = list(cur_piece.get_moves().keys())
        del Last
        Last = cur_piece
        draw_path(cur_piece.get_moves().keys())


def draw_path(someList):
    # print(someList)
    for l in someList: pygame.draw.circle(screen, 'red', [(l[0] * 100) + 50, (l[1] * 100) + 50], 5, 0)


while run:
    timer.tick(fps)
    screen.fill('dark gray')
    locations = Piece.piece_list
    draw_board()
    draw_pieces()
    event_handler(coordinates)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x_coord = event.pos[0] // 100
            y_coord = event.pos[1] // 100
            coordinates = (x_coord, y_coord)
            print(coordinates)

    pygame.display.flip()
pygame.quit()
