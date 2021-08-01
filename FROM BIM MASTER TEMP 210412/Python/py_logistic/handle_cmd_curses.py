# -*- coding: utf-8 -*-
"""Module hỗ trợ các lệnh về Terminal / Shell cho chươngtrinh2]]

"""
import os
import pynput
from pynput.keyboard import Listener
import keyboard
import curses

#--------------------------------------------------------------#
# DANH SÁCH CHỌN BẰNG MŨI TÊN
#--------------------------------------------------------------#

#--------------------------------------------------------------#
def listen_keypress(key_value):
    while True:
        if keyboard.read_key() == key_value:
            # print(f"You pressed {key_value}")
            break
#--------------------------------------------------------------#        
# keyboard.on_press_key("r", lambda _:print("You pressed r"))

#--------------------------------------------------------------#
def character(stdscr):
    classes = ["The sneaky thief", "The smarty wizard", "The proletariat"]
    attributes = {}
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    attributes['normal'] = curses.color_pair(1)

    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
    attributes['highlighted'] = curses.color_pair(2)

    c = 0  # last character read
    option = 0  # the current option that is marked
    while c != 10:  # Enter in ascii
        stdscr.erase()
        stdscr.addstr("What is your class?\n", curses.A_UNDERLINE)
        for i in range(len(classes)):
            if i == option:
                attr = attributes['highlighted']
            else:
                attr = attributes['normal']
            stdscr.addstr("{0}. ".format(i + 1))
            stdscr.addstr(classes[i] + '\n', attr)
        c = stdscr.getch()
        if c == curses.KEY_UP and option > 0:
            option -= 1
        elif c == curses.KEY_DOWN and option < len(classes) - 1:
            option += 1

    stdscr.addstr("You chose {0}".format(classes[option]))
    stdscr.getch()
#--------------------------------------------------------------#
def menu():
    print()
#--------------------------------------------------------------#
def print_menu(stdscr, selected_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    for idx, row in enumerate(menu):
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()
#--------------------------------------------------------------#
def print_center(stdscr, text):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    x = w//2 - len(text)//2
    y = h//2
    stdscr.addstr(y, x, text)
    stdscr.refresh()
#--------------------------------------------------------------#
def main_curse(stdscr):
    # turn off cursor blinking
    curses.curs_set(0)

    # color scheme for selected row
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_YELLOW)

    # specify the current selected row
    current_row = 0

    # print the menu
    print_menu(stdscr, current_row)

    while True:
        key = stdscr.getch()
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu)-1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            print_center(stdscr, "You selected '{}'".format(menu[current_row]))
            stdscr.getch()
            # if user selected last row, exit the program
            if current_row == len(menu)-1:
                break

        print_menu(stdscr, current_row)

# GLOBAL VAR
key_  = 0
key_name = ''


def main_curse_2(stdscr,menu):   
    curses.noecho()
    stdscr.keypad(True) # IMPORTANT
    global key_, key_name
    # curses.start_color()
    # curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_YELLOW)    #   Change the definition of a color-pair.     
    # curses.curs_set(2)  #   Set the cursor state. visibility can be set to 0, 1, or 2, for invisible, normal, or very visible.
    # stdscr.clear()   
    # stdscr.addstr(f"Your menu{menu}")
    while True:        
        try:
            key_ = stdscr.get_wch()# Get character (keyboard)     
            stdscr.addstr(f"\nYou pressed key number {key_}")
            # key_name = curses.keyname(key_)#.decode('ascii')
            # stdscr.addstr(f"Key name {key_name}")   
            if key_ == curses.KEY_UP:
                stdscr.addstr("\nYou pressed Up key!")   
            if key_ == curses.KEY_DOWN:
                stdscr.addstr("\nYou pressed Down key!")   
            if key_ == 10:
                # stdscr.clear()
                stdscr.addstr(f"\nYou chose {key_name}")
                # break
            if key_ == 'q' or key_ == 'Q':
                # quit()
                break
            stdscr.refresh() # Update the display immediately (sync actual screen with previous drawing/deleting methods).
        except:
            pass
    
    # promp = f"Next actions {key_name}"
    # stdscr.addstr(promp)
    # while True:   
    #     stdscr.addstr(promp)
    #     if key_ == 81 or key_ == 113:
    #         quit()
from curses.textpad import Textbox, rectangle

def main_text_pad(stdscr):
    stdscr.addstr(0, 0, "Enter IM message: (hit Ctrl-G to send)")
    editwin = curses.newwin(5,30, 2,1)
    rectangle(stdscr, 1,0, 1+5+1, 1+30+1)
    stdscr.refresh()
    box = Textbox(editwin)
    # Let the user edit until Ctrl-G is struck.
    box.edit()
    # Get resulting contents
    message = box.gather()

#--------------------------------------------------------------#

#  TEST

#--------------------------------------------------------------#

try:    
    # stdscr = curses.initscr() # Initialize the library. Return a window object which represents the whole screen.

    menu = ['Home', 'Play', 'Scoreboard', 'Exit']         
    curses.wrapper(main_curse_2,menu)

    # curses.wrapper(main_text_pad(stdscr))

  
    
    # main_curse(stdscr)    
    # character(curses.initscr())
    # menu()
    # listen_keypress('up')
    # listen_keypress('down')    
    # print('123')
    # listen_keypress('up')
    # print('456',end='\r')
    # listen_keypress('down')
    # print('abc')
    # listen_keypress('left')
    # print('def',end='\r')
except KeyboardInterrupt:
    quit()