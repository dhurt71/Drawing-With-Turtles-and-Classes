# CSUF CPSC 305
# Mini-Project 6
#
# Group Members:
#   Devon Hurt
#   

#Test functions
def squareTest():
  mars = makeWorld()
  Jerry = makeTurtle(mars)
  square(Jerry,50,50,50)

def polygonTest():
  mars = makeWorld()
  Jerry = makeTurtle(mars)
  polygon(Jerry,100,100,50,7)

# Use turtle to draw a square, starting at top-left corner (x, y),
# with each side w long. 
def square(turtle, x, y, w):
  turtle.penUp()
  turtle.moveTo(x,y)
  turtle.penDown()
  for i in range(0,4):
    turtle.turn(90)
    turtle.forward(w)

# Use turtle to draw a sides-sided regular polygon (i.e. every side is
# the same length), starting at top-left corner (x, y), with each side
# w long.
def polygon(turtle, x, y, w, sides):
  turtle.penUp()
  turtle.moveTo(x,y)
  turtle.penDown()
  sumAngles = (sides - 2)*180
  intAngles = sumAngles/sides
  for i in range(0,sides):
    turtle.turn(180-intAngles)
    turtle.forward(w)

# Subclass of Turtle that alternates between yellow and black pen
# color every time forward() is called. 
class BeeTurtle(Turtle):
  def __init__(self, world):
    Turtle.__init__(self, world)
    self.counter = 0
  def forward(self,num):
    Turtle.forward(self,num)
    if self.counter%2 == 0:
      self.setPenColor(yellow)
      self.counter = self.counter + 1
    else:
      self.setPenColor(black)
      self.counter = self.counter + 1
# The following are testing functions.

def drawShapes(turtle):
  square(turtle, 10, 10, 5)
  square(turtle, 20, 10, 10)
  square(turtle, 40, 10, 20)
  square(turtle, 70, 10, 30)
  square(turtle, 110, 10, 40)
  
  polygon(turtle, 10, 100, 20, 3)
  polygon(turtle, 40, 100, 18, 4)
  polygon(turtle, 70, 100, 16, 5)
  polygon(turtle, 120, 100, 14, 6)

def testRed():
  w = makeWorld()
  t = makeTurtle(w)
  t.setPenColor(red)
  drawShapes(t)

def testBlue():
  w = makeWorld()
  t = makeTurtle(w)
  t.setPenColor(blue)
  drawShapes(t)

def testBee():
  w = makeWorld()
  t = BeeTurtle(w)
  t.setPenColor(black)
  drawShapes(t)
