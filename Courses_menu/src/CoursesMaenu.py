'''
Created on 25-11-2012

@author: wemstar
'''


import curses 
import random
class Menu:
    def __init__(self):
        self.stdscr=curses.initscr()
        curses.noecho()
        self.stdscr.keypad(True)
        curses.start_color()
        curses.init_pair(1,curses.COLOR_WHITE,curses.COLOR_RED)
        self.win=curses.newwin(10,40,10,10)
        self.win.border()
        OPT=['Raz','Dwa','Trzy','Cztery','Piec','Szesc','Siedem','Osiem','dzwiec','Dziesiec']
        self.OPTS=OPT
        self.act=0
    def maluj(self):
        while 1:
                for (i,j) in enumerate(self.OPTS[self.act:self.act+3]):
                        if self.act==(self.act+i):
                                style=curses.color_pair(1)|curses.A_BOLD  
                        else:   
                                style=curses.color_pair(0)
                        self.win.addstr(1+i,1,j,style)
                        self.stdscr.addstr(0,0,str(self.act))
                self.stdscr.refresh()
                self.win.refresh()
                key=self.stdscr.getch()      
                if key==curses.KEY_DOWN:
                    self.act+=1
                if key==curses.KEY_UP:
                        self.act-=1
                if key==ord('q'):
                        break
                if self.act<0:
                        #act=0
                        self.act=0
                if self.act>=len(self.OPTS):
                        
                        self.act=len(self.OPTS)-1
                self.stdscr.clear()
        curses.endwin()
        
        