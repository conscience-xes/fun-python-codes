import turtle, random
basiclength = 10
elementspercircle = 12
colors  = ["red","green","blue","orange","purple","pink","yellow"] 

length = basiclength
angle = 360/elementspercircle

turtle.pensize(5)

def paintingpainter(directionoffset):
  global length
  global angle
  global colors

  for j in range (4):
    for i in range( elementspercircle + 1):
      turtle.color(random.choice(colors))
      turtle.forward(length)
      turtle.left(angle * directionoffset)
      length = length + directionoffset

paintingpainter(1)
turtle.right(angle * 2)
paintingpainter(-1)