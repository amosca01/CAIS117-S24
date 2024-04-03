from graphics import *

def main():
  win = GraphWin("My Circle", 600, 400)
  c = Circle(Point(50,50), 10)
  c.setFill("red")
  c.draw(win)
  #while win.checkMouse() == None:
  for i in range(200): 
    
    dx = 3
    dy = 2
    c.move(dx,dy) # The move function takes two values, dx and dy
    
    # Add code to make the ball bounce
    # get X and get Y
    currX = c.getCenter().getX()
    currY = c.getCenter().getY()
    if currX > 600:
        dx = -dx
    if currY > 400:
        dy = -dy
    
  win.getMouse() # Pause to view result
  win.close() # Close window when done

if __name__ == "__main__":
    main()
