from graphics import *
import random
win = GraphWin("square maker", 500,500)
message = Text(Point(250,15), "Click on the window to make squares and circles")
message.draw(win)
count = 1
while True:
    random_ = random.randint(1,500)
    click = win.getMouse()
    colors = random.choice(['red','blue','yellow','green'])
    if count % 2:
        clickX = click.getX()
        clickY = click.getY()
        r = Rectangle(Point(clickX,clickY),Point(clickX+random_,clickY+random_))
        r.draw(win)
        r.setFill(colors)
    else:
        c = Circle(click,random.randint(10,100))
        c.draw(win)
        c.setFill(colors)
    count = count+1
win.close()
