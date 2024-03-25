from graphics import *

def main():
    win = GraphWin("CAIS117 Animated Ball", 600, 400)
    circ = Circle(Point(50,50), 10)
    circ.setFill( 'red' )
    circ.draw(win)
    
    # set initial direction of ball
    dx = 1.5
    dy = 0.25

    # move ball on screen
    while win.checkMouse() == None:
        circ.move( dx, dy )

        x = circ.getCenter().getX()
        y = circ.getCenter().getY()

        

        
        
    win.close() # Close window when done

main()
