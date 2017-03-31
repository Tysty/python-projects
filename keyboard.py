from graphics import *
win = GraphWin("keyboard",500,500)
s = Rectangle(Point(250,250),Point(285,285))
s.draw(win)
s.setFill('blue')
s2 = Rectangle(Point(250,450),Point(300,500))
s2.draw(win)
s2.setFill('red')
currXr = 285
currXl = 250
currYr = 285
currYl = 250
chX = 30
chY = 30
#c.move(30,0)
while True:
    currentKey=win.getKey() #Get input from keyboard
    #square --> add in shape code here
    xd = currXl-250
    yd = currYr-450
    if(currentKey == "Right"):
        #Do something here if the key has been pressed!
        chX = 30
        if currXr + 30 > 500:
            chX = 0
        s.move(chX,0)
        currXr = currXr + chX
        currXl = currXl + chX
    if(currentKey == "Left"):
    #Do something here if the key has been pressed!
        chX = -30
        if currXl -30 < 0:
            chX = 0
        s.move(chX,0)
        currXr = currXr + chX
        currXl = currXl + chX
    if(currentKey == "Up"):
        #Do something here if the key has been pressed!
        chY = -30
        if currYl - 30 < 0:
            chY = 0
        s.move(0,chY)
        currYl = currYl + chY
        currYr = currYr + chY
    if(currentKey == "Down"):
        #Do something here if the key has been pressed!
        chY = 30
        if currYr + 30 > 500:
            chY = 0
        s.move(0,chY)
        currYl = currYl + chY
        currYr = currYr + chY
