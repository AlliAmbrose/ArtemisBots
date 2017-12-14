from Myro import *
import time
init("COM14")

#startTime = time.time()
def mazeBot():  
    while True:
        forward(1)
        
        [l,r] = getLine()
        le,ri = getIR()
          
        if l==1 and r==1:
            stop()
            backward(1,1)
            turnBy(90)
            forward(1,3)
            #time.sleep(3)
            turnBy(-90)            
        
            
        
        if l==1 and r==0:
            turnRight(1,.5)
           
        if l==0 and r==1:
        
            
            turnLeft(1,.5)
            
        
        

        
        else:
            forward(1)
            continue

mazeBot()