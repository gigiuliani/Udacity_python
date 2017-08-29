import turtle

def screen_mgmt():
    window = turtle.Screen()
    window.bgcolor('grey')
    brad = turtle.Turtle()
    brad.speed(0)
    
    for i in range(1,37):
        draw_rhombus(brad)
        brad.right(10)
    brad.forward(10)
    brad.right(90)
    brad.forward(300)
        
    window.exitonclick()
    
def draw_rhombus(x):
    for i in range(1,4):
        x.forward(100)
        x.right(150)
        x.forward(100)
        x.right(30)
    
screen_mgmt()

