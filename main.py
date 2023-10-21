from Game import Game

from settings import *

if __name__ == '__main__':
    window_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
    bg = BACKGROUND
    maGame = Game(window_size, bg)
    maGame.run()