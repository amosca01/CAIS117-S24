from graphics import *

def main():
    width = 600
    height = 400
    win = GraphWin("CAIS117 Animated Ball", width, height)
    circ = Circle(Point(50,50), 10)
    circ.setFill( 'red' )
    circ.draw(win)
    
    # set initial direction of ball
    dx = 1.5
    dy = 0.25

    # move ball on screen
    while win.checkMouse() == None:
        
        circ.move(dx, dy)

        x = circ.getCenter().getX()
        y = circ.getCenter().getY()
        
        if (x < 0 or x > width):
            dx = -dx
        if (y < 0 or y > height):
            dy = -dy

    win.close() # Close window when done

main()
