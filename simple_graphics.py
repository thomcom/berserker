from graphics import *
from math import sin
from math import cos
from math import pi

def main():
    win = GraphWin("Simplest Possible Game", 400, 300)
    #my_circle = Circle(Point(0,150),40)
    my_circle = Rectangle(Point(0,150),Point(50,200))
    my_circle.draw(win)
    dx       = 1
    num_runs = 0
    while(True):
       if( num_runs > 400 ):
          num_runs = 0
          dx = dx  * -1
       num_runs = num_runs + 1
       pi_x = sin((num_runs-200)*(pi/200))
       dy = sin((num_runs+1-200)*(pi/200)) - pi_x
       my_circle.move(dx,dy*100)
       #my_circle.move(dx,0)
       #my_point = win.getMouse()
    win.close()    # Close window when done

main()

