import turtle

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


if __name__ == '__main__':
    do_ex4()
