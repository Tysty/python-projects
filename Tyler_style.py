from graphics import *
p1 = Point(250,200)
p2 = Point(500, 210)
p3 = Point(370, 210)
p4 = Point(380, 460)
def Tyler_Style(p1,p2,p3,p4):
    win = GraphWin("Tyler Style", 800,600)
    r1 = Rectangle(p1,p2)
    r1.draw(win)
    r1.setFill('blue')
    r2 = Rectangle(p3,p4)
    r2.draw(win)
    r2.setFill('red')

Tyler_Style(p1, p2, p3, p4)
