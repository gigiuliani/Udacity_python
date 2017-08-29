import turtle

def screen_mgmt():
    window = turtle.Screen()
    window.bgcolor('grey')
    brad = turtle.Turtle()
    
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)
        
    window.exitonclick()
    
def draw_square(x):
    for i in range(1,5):
        x.forward(100)
        x.left(90)

#def draw_circle():
 #   angie = turtle.Turtle()
#    angie.shape('arrow')
#    angie.color('blue')
#    angie.circle(100)

#def draw_triangle():
#    bob = turtle.Turtle()
#    bob.shape('arrow')
#    bob.color('yellow')
#    j = 1
#    while j<=3:
#        bob.forward(100)
#        bob.left(120)
#        j = j+1

    
screen_mgmt()

