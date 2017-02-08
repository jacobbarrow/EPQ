from Tkinter import *

import tkFont
from random import randint
import generals, neuralnetwork

tile_colours = {1:'red', 0:'blue', -1:'white', -2:'#ccc', -3:'#555', -4:'#000', 2:'green'}


class Gui(Frame):
    def __init__(self, root, username):

        b_width = 1000
        b_cells = 25

        self.username = username

        self.root = root

        self.cell_wraps = [[-3 for x in range(b_cells)] for y in range(b_cells)]
        self.cells = [[0 for x in range(b_cells)] for y in range(b_cells)]


        self.root.resizable(width=False, height=False)
        self.root.geometry('1300x{0}'.format(b_width))
        default_font = tkFont.nametofont("TkDefaultFont")
        default_font.configure(size=18)

        self.root.option_add("*Font", default_font)


        board_wrap = Frame(self.root, bg="#fff", width=b_width, height=b_width)
        board_wrap.pack(side=LEFT)

        board = Frame(board_wrap, bg="red", width=b_width, height=b_width)
        board.pack(fill=BOTH)
        for y in range(b_cells):
            for x in range(b_cells):

                w = b_width/b_cells

                self.cell_wraps[y][x] = Frame(board, bg=tile_colours[-2], width=w, height=w, pady=10)
                self.cell_wraps[y][x].grid(row=x, column=y)
                self.cells[y][x] = Label(self.cell_wraps[y][x], text='?')
                self.cell_wraps[y][x].pack_propagate(False)
                self.cells[y][x].pack()

        config_wrap = Frame(self.root, bg="#ccc", height=b_width, width=300)
        config_wrap.pack(side=LEFT, expand=1)

        scoreboard = Frame(config_wrap, width=300)
        scoreboard.grid(row=0, column=0)

        self.sb = {}

        self.sb['turn_label'] = Label(scoreboard, text='Turn:')
        self.sb['turn_label'].grid(row=0, column=0)
        self.sb['turn_count'] = Label(scoreboard, text='0')
        self.sb['turn_count'].grid(row=0, column=1)
        self.sb['turn_actual'] = Label(scoreboard, text='(0)')
        self.sb['turn_actual'].grid(row=0, column=2)

        self.sb['own_name'] = Label(scoreboard, text=self.username)
        self.sb['own_name'].grid(row=1, column=0)
        self.sb['own_stars'] = Label(scoreboard, text='?')
        self.sb['own_stars'].grid(row=1, column=2)
        self.sb['own_army'] = Label(scoreboard, text='?')
        self.sb['own_army'].grid(row=1, column=3)

        self.sb['enemy_name'] = Label(scoreboard, text='Enemy...')
        self.sb['enemy_name'].grid(row=2, column=0)
        self.sb['enemy_stars'] = Label(scoreboard, text='?')
        self.sb['enemy_stars'].grid(row=2, column=2)
        self.sb['enemy_army'] = Label(scoreboard, text='?')
        self.sb['enemy_army'].grid(row=2, column=3)


        new_game_button = Button(config_wrap, text="New Game")
        new_game_button.bind("<Button 1>", self.game_loop)
        new_game_button.grid(row=1, column=0)

        self.root.update()

    def update_board(self, data):

        self.sb['turn_count'].config(text=str(int(data['turn']/2)))
        self.sb['turn_actual'].config(text='({0})'.format(data['turn']))
        self.sb['own_army'].config(text='({0})'.format(data['armies'][0]))
        self.sb['enemy_army'].config(text='({0})'.format(data['armies'][1]))
        self.sb['turn_actual'].config(text='({0})'.format(data['turn']))

        for y, row in enumerate(data['tile_grid']):
            for x, tile in enumerate(row):
                self.cell_wraps[y][x].config(bg=tile_colours[tile])
                self.cells[y][x].config(text=(str(data['army_grid'][y][x])))
        self.root.update()

    def game_loop(self, event):

        self.g = generals.Generals('generalsot', self.username, '1v1')
        while True:
            print 'Waiting for game to start'
            update = self.g.get_update()

            if update:
                try:
                    pi = update['player_index']
                except KeyError:
                    break

                for city in update['cities']:
                    update['tile_grid'][city[0]][city[1]] = 2

                next_move = neuralnetwork.get_next_move(update['tile_grid'],\
                                                        update['army_grid'],\
                                                        update['armies'])

                print next_move

                self.update_board(update)

        print ('Game Over!')

root = Tk()
