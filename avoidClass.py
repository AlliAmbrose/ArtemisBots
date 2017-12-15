from Myro import*
init('sim')
import time 
class obstacleSensor:
    def __init__(self,L1,R1):
        self.L1 = L1    
        self.R1 = R1
        
    def avoidObstacle(L1,R1):
        while True:
            forward(5,5)
            [L1,R1] = getIR()
            if L1 == 1 and R1 == 1:
               backward(1,1)
               turnBy(180)
            elif L1 == 0 and R1 == 1:
                backward(1,1)
            elif L1 == 1 and R1 == 0:
                backward(1,1)           
            else:
                speak("MOVE")
                turnRight(1,2)
                forward(2,5)
                print(getIR())
obstacleSensor.avoidObstacle(L1,R1)