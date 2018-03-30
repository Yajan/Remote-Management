import json
import curses
w=curses.initscr()
w.scrollok(1) # enable scrolling
w.timeout(1)  # make 1-millisecond timeouts on `getch`

try:
    while True:
        w.erase()
        w.addstr("\nStatus Report for Install process\n=========\n\n")
        for i in range(1000):
            w.addstr(str(i))
        ignore = w.getch()  # wait at most 1msec, then ignore it
finally:
    curses.endwin()