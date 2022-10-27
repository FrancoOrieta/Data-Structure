import turtle

back = turtle.Screen()
back.bgcolor("#8B8B8B")
back.setup(800,600)

squr = turtle.Turtle()
squr.shape("square")
squr.speed(5)
squr.up()

def trazo(color, pos_x, pos_y, cantidad):
    for i in range(cantidad):
        x = 25*i
        squr.color(color)
        squr.goto(pos_x + x, pos_y)
        squr.stamp()

#CABEZA#
trazo("red", 0,250,6)

trazo("red",-25,225,10)

trazo("brown",-25,200,3)
trazo("#E2CAAE",50,200,3)
trazo("black",125,200,1)
trazo("#E2CAAE",150,200,1)

trazo("brown",-50,175,1)
trazo("#E2CAAE",-25,175,1)
trazo("brown",0,175,1)
trazo("#E2CAAE",25,175,4)
trazo("black",125,175,1)
trazo("#E2CAAE",150,175,3)

trazo("brown",-50,150,1)
trazo("#E2CAAE",-25,150,1)
trazo("brown",0,150,2)
trazo("#E2CAAE",50,150,4)
trazo("black",150,150,1)
trazo("#E2CAAE",175,150,3)

trazo("brown",-50,125,2)
trazo("#E2CAAE",0,125,5)
trazo("black",125,125,4)

trazo("#E2CAAE",0,100,8)
#########################

#ROPA#
trazo("red",-25,75,2)
trazo("blue",25,75,1)
trazo("red",50,75,4)

trazo("red",-50,50,3)
trazo("blue",25,50,1)
trazo("red",50,50,2)
trazo("blue",100,50,1)
trazo("red",125,50,3)

trazo("red",-75,25,4)
trazo("blue",25,25,4)
trazo("red",125,25,4)

trazo("#E2CAAE",-75,0,2)
trazo("red",-25,0,1)
trazo("blue",0,0,1)
trazo("yellow",25,0,1)
trazo("blue",50,0,2)
trazo("yellow",100,0,1)
trazo("blue",125,0,1)
trazo("red",150,0,1)
trazo("#E2CAAE",175,0,2)

trazo("#E2CAAE",-75,-25,3)
trazo("blue",0,-25,6)
trazo("#E2CAAE",150,-25,3)

trazo("#E2CAAE",-75,-50,2)
trazo("blue",-25,-50,9)
trazo("#E2CAAE",175,-50,2)

trazo("blue",-25,-75,3)
trazo("blue",100,-75,3)

trazo("brown",-50,-100,3)
trazo("brown",125,-100,3)

trazo("brown",-75,-125,4)
trazo("brown",125,-125,4)

turtle.exitonclick()