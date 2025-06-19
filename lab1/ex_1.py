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


def do_ex4():
    ''' Draw circle using turtle'''
    side_length = 5
    n = 100 # многоупольник с большим количеством сторон, приближается к окружности
    angle_to_turn = 360 / n
    turtle.shape('turtle')
    for i in range(n):
        turtle.forward(side_length)
        turtle.left(angle_to_turn)
    turtle.done()


if __name__ == '__main__':
    do_ex4()
