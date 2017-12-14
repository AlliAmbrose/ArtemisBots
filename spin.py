from Myro import *
init("com14")
class turn(object):
    def spin():
        x = 0
        while x < 20:
            turnBy(180)
            forward(1,.5)
            backward(1,.5)
            x+= 1
turn = turn()
turn.spin