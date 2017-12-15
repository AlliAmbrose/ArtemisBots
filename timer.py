from Myro import*
import time
init("com4")
setForwardness("scribbler-forward")
def timer(t):
    while t >= 0:
        ##print(t)
        forward(1,1)
        t = t-1 
        if t == 0:
            turnBy(90)
            forward(.5,1)
            break
def followLine():
    while True:
        [l,r]=getLine()
        if l==1 and r==1:
            turnRight(1,.5)
        if timer(2) and l==1 and r==1:
             turnBy(90)    
        elif l==1 and r==0:
            lastTurn=1
            backward(1,1)
            turnRight(1,.5)
        elif l==0 and r==1:
            lastTurn=2
            backward(1,1)
            turnLeft(1,.5)
        else:
            forward(1)
timer(2)    
followLine()
