import math
import random

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
game = Board()
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


# empty list to hold game information
def init_pices():  # factory funtion to create piece objects and the board
    for x in range(len(white_pieces)):
        if white_pieces[x] == 'pawn':

            game.add_Piece(
                Pawn(white_pieces[x], white_locations[x], pygame.image.load(white_dict[white_pieces[x]]), 'white',
                     game))

            game.add_Piece(
                Pawn(black_pieces[x], black_locations[x], pygame.image.load(black_dict[black_pieces[x]]), 'black',
                     game))
        elif white_pieces[x] == 'rook':

            game.add_Piece(
                Rook(white_pieces[x], white_locations[x], pygame.image.load(white_dict[white_pieces[x]]), 'white',
                     game))

            game.add_Piece(
                Rook(black_pieces[x], black_locations[x], pygame.image.load(black_dict[black_pieces[x]]), 'black',
                     game))

        elif white_pieces[x] == 'bishop':

            game.add_Piece(
                Bishop(white_pieces[x], white_locations[x], pygame.image.load(white_dict[white_pieces[x]]), 'white',
                       game))

            game.add_Piece(
                Bishop(black_pieces[x], black_locations[x], pygame.image.load(black_dict[black_pieces[x]]), 'black',
                       game))
        elif white_pieces[x] == 'knight':

            game.add_Piece(
                Knight(white_pieces[x], white_locations[x], pygame.image.load(white_dict[white_pieces[x]]), 'white',
                       game))

            game.add_Piece(
                Knight(black_pieces[x], black_locations[x], pygame.image.load(black_dict[black_pieces[x]]), 'black',
                       game))
        elif white_pieces[x] == 'queen':

            game.add_Piece(
                Queen(white_pieces[x], white_locations[x], pygame.image.load(white_dict[white_pieces[x]]), 'white',
                      game))

            game.add_Piece(
                Queen(black_pieces[x], black_locations[x], pygame.image.load(black_dict[black_pieces[x]]), 'black',
                      game))
        elif white_pieces[x] == 'king':

            game.add_Piece(
                King(white_pieces[x], white_locations[x], pygame.image.load(white_dict[white_pieces[x]]), 'white',
                     game))

            game.add_Piece(
                King(black_pieces[x], black_locations[x], pygame.image.load(black_dict[black_pieces[x]]), 'black',
                     game))


def draw_board():  # drawing the background of the board
    for i in range(32):
        col = (i % 4)
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, 'light gray', [600 - (col * 200), row * 100, 100, 100])
        else:
            pygame.draw.rect(screen, 'light gray', [700 - (col * 200), row * 100, 100, 100])


init_pices()

locations = game.get_locations()


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


def draw_path(someList):
    if someList == -10: print('Thats Game!')
    elif -10 not in someList:
        for l in someList: pygame.draw.circle(screen, 'red', [(l[0] * 100) + 50, (l[1] * 100) + 50], 5, 0)

def auto_play(move_list):
    if len(move_list) <= 1 : return 0
    magic = random.randint(0,len(game.get_locations())-1)
    keys = list(game.get_locations().keys())
    moves = list(game.valid_moves(game.locations.get(keys[magic])).keys())
    mag = random.randint(0,len(moves)-1)
    print(game.moves)
    game.move(keys[magic])
    game.move(moves[mag])
    return auto_play(list(game.get_moves(game.get_turn()).keys()))



while run:
    timer.tick(fps)
    screen.fill('dark gray')
    draw_board()
    draw_pieces()
    locations = Board.locations
    draw_path(game.move(coordinates))
    pygame.draw.rect(screen, 'red',
                     [coordinates[0] * 100 + 1, coordinates[1] * 100 + 1, 100, 100],
                     2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x_coord = event.pos[0] // 100
            y_coord = event.pos[1] // 100
            coordinates = (x_coord, y_coord)
           # auto_play(list(game.get_moves(game.get_turn()).keys()))
            #print(coordinates)

    pygame.display.flip()
pygame.quit()
