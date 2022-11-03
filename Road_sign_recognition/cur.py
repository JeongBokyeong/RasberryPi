import curses

screen=curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)