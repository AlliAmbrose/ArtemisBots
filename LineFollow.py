
from Myro import*
import time
init("com14")
setForwardness("scribbler-forward")
start = time.time
def checkAgain():
    for seconds in timer(2):
            if l==1 and r==1 and start() < 2:
                turnBy(90) 
        

def followLine():
    while True:
        [l,r]=getLine()
        
        if l==1 and r==1:
            backward(1,1)
            turnLeft(1,.5)
            start()
        
        checkAgain()
            
            
        elif l==1 and r==0:
            turnRight(1,.5)
           
        elif l==0 and r==1:
        
            
            turnLeft(1,.5)
    
        else:
            forward(1)    

followLine()






## def obstacleAvoid():
##     if(getObstacle(0,1,2) <= 100):
##         beep(0.2,990)
##         speak("Nothing is in my way")        
##         #followLine()
##         
##     
##     else:
##         speak("MOVE")

## obstacleAvoid()    



#
#show(takePicture())        
       