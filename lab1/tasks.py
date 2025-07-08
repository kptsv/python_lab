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
    
        
def do_ex8():
    ''' Draw square spiral'''    
    angle = 90
    n_squares = 10
    side_length = 5
    small_piece = 5
    turtle.shape('turtle')    
    for i in range(n_squares):
        for j in range(4):
            turtle.forward(side_length)
            turtle.left(angle)
            side_length += small_piece

    turtle.done()    


def draw_polygon(n_angles:int, radius_out_circle):
    ''' Draw a polygon
        n_angles - number of angles of the polygon
        radius_out_circle - radius of the out circle of polygon
    '''
    if int(n_angles) <=2:
        return "Error! Number of angles must be more than 2."    
    angle = 180 * (n_angles - 2) / n_angles
    angles = [180 - angle / 2] + [180 - angle]*(n_angles - 1)
    side_length = 2 * radius_out_circle * math.sin(math.pi/n_angles)
    for angle_to_turn in angles:
        turtle.left(angle_to_turn)
        turtle.forward(side_length)
        

def draw_cycle(radius_out_circle=50, n_angles=180, isLeft=True):
    ''' Draw a cycle as a polygon with many angles
        radius_out_circle - radius of the out circle of polygon
    '''
    if int(n_angles) <=2:
        return "Error! Number of angles must be more than 2."    
    angle = 180 * (n_angles - 2) / n_angles
    angles = [180 - angle]*n_angles
    side_length = 2 * radius_out_circle * math.sin(math.pi/n_angles)
    for angle_to_turn in angles:
        if isLeft:
            turtle.left(angle_to_turn)
        else:
            turtle.right(angle_to_turn)
        turtle.forward(side_length)

    
def do_ex9():
    ''' Draw 10 right polygons inside each other'''
    turtle.shape('turtle')
    turtle.speed(1)
    radius = 30
    dr = 15
    for n in range(3, 13):
        draw_polygon(n, radius) 
        turtle.setheading(0)
        turtle.up()
        turtle.forward(dr)
        turtle.down()
        radius += dr

    turtle.done()


def do_ex10():
    ''' Draw flower using circles'''
    angles_count = 150
    radius = 50
    turtle.shape('turtle')
    turtle.speed(0)
    directions = [270, 90, 315, 135, 225, 45]
    for direction in directions:        
        turtle.setheading(direction)        
        draw_polygon(angles_count, radius)
    turtle.done()


def do_ex11():
    ''' Draw the butterfly using circles'''
    n_cycles = 10
    radiuses = range(30, 130, 10)
    turtle.shape('turtle')
    turtle.setheading(90)
    for radius in radiuses:
        draw_cycle(radius)
        draw_cycle(radius, isLeft=False)
    turtle.done()
    
    
def draw_arc(radius_of_arc=50, isLeft=True):
    ''' Draw an arc (half an cycle) 
        param: radius_of_arc is a radius of arc
        param: isLeft shows direction of drawing arc        
    '''
    pass
    
    
def do_ex12():
    ''' Draw a spring '''
    pass
    
    
