import turtle
import math

def do_ex2():
    ''' This function draws a letter "S" using turtle '''
    turtle.shape('turtle')
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)


def do_ex3():
    ''' Draw square using turtle'''
    turtle.shape('turtle')
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)


def draw_figure(n:int, length:int):
    ''' Draw figure with n angles and side equals length'''
    angle_to_turn = 360 / n
    turtle.shape('turtle')
    for i in range(n):
        turtle.forward(length)
        turtle.left(angle_to_turn)


def do_ex4():
    ''' Draw circle using turtle'''
    draw_figure(n=100, length=5)
    turtle.done()


def do_ex5():
    ''' Draw 10 squares inside each other'''
    delta_x = -10
    delta_y = -10
    n = 4
    side_length = 30
    turtle.speed(1)
    for i in range(10):
        draw_figure(n, side_length)
        turtle.setheading(0)
        x, y = turtle.pos()
        x += delta_x
        y += delta_y
        turtle.up()
        turtle.setpos(x, y)
        turtle.down()
        side_length += 2*abs(delta_y)
    turtle.done()


def do_ex6():
    ''' Draw spider with n legs'''
    n = 12
    leg_length = 100
    angle_to_turn = 360 / n
    turtle.speed(1)
    turtle.shape('turtle')
    for i in range(n):
        turtle.forward(leg_length)
        turtle.stamp()
        turtle.back(leg_length)
        turtle.left(angle_to_turn)
    turtle.done()

def do_ex7():
    ''' Draw spiral of Archimedes'''
    n_circle = 10
    length = 0
    length_speed = 0.1
    angle = 0
    angle_speed = 0.05
    turtle.shape('turtle')
    turtle.speed(3)
    while angle <= n_circle*2*math.pi:
        x = length * math.cos(angle)
        y = length * math.sin(angle)        
        turtle.setpos(x, y)
        length += length_speed
        angle += angle_speed
        
    turtle.done()
    
        
if __name__ == '__main__':
    do_ex7()
