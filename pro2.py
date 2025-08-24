import random
import curses
screan=curses.initscr()
curses.curs_set(0)
screan_height,screan_width=screan.getm[]
window=curses.newwin(screan_height,screan_width,0,0)
window.keypad(1)
window.timeout(100)
snk_x=screan_width//4
snk_y=screan_height//2
snake=[[snk_y,snk_x],[snk_y,snk_x-1],[snk_y,snk_x-2]]
food=[screan_height//2,screan_width//2]
window.addch(food[0],food[1],curses.ACS_PI)
key=curses.KEY_RIGHT
while True:
   next_key=window.getch()
    