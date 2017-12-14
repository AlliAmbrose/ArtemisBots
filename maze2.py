import Myro as m 
#import time
init("COM14")

#startTime = time.time()
class Bots():
    def __init__(self):
        self.Banana = m.makeRobot("Scribbler", "com14")   
         
    def checkLine(self):
        [l,r] = getLine()
        le,ri = getIR()
        
        if l==1 and r==1:
            stop()
            backward(1,1)
            turnBy(90)
            forward(1,3)
            #time.sleep(3)
            #turnBy(-90)            
        
        if l==1 and r==0:
            turnBy(-90)
           
        if l==0 and r==1:            
            turnBy(90)
            
        if le==0 or ri==0:
            stop()
            backward(1,1)
            turnBy(90)
            forward(1,1.5)
            turnBy(-90)

        

#mazeBot()