import Myro as m
import starfleetcom
import time 
import string
import json


class MazeRobot(object):
  
    NO_LIGHT = 0
    IS_LIGHT = 1
    
    NO_WALL = 3
    IS_WALL = 4
    
    NO_OBSTACLE = 5
    IS_OBSTACLE = 6
    
    currentState = [NO_LIGHT,NO_WALL,NO_OBSTACLE]
   
    def __init__(self, alarm=1):
        self.Banana = m.makeRobot("Scribbler", "com14")
        self.alarm = 1
        self.resetAlarm()
        self.Command = 0
   
    def isAlarm(self):
       return self.stop-self.start >= self.alarm
    
    def resetAlarm(self):
       self.start = self.stop = 0
    
    def currentStateReset(self):
        self.currentState = self.currentState = [self.NO_LIGHT,self.NO_WALL,self.NO_OBSTACLE]
   
    def setTimer(self, duration):
       self.alarm = duration
       self.start = time.clock()
       self.stop = self.start
    
    def lightDetected(self):
        self.minLight = 30000
        
        if self.Banana.getLight("center") < self.minLight:
            return True
        elif self.Banana.getLight('right') < self.minLight:
            return True
        elif self.Banana.getLight('left') < self.minLight:
            return True
        else:
            return False    
    
    def lineDetected(self):
       self.L,self.R = self.Banana.getLine()
       if self.L == 1 or self.R == 1:
            self.Banana.stop()
            return True
       return False
        
    def obstacleDetected(self):
       L,R = self.Banana.getIR()
       if L == 0 or R == 0:
           return True
       return False

    def detectionCheck(self):  
        if self.lightDetected():
            self.currentState[0] == self.IS_LIGHT
            return True
        elif self.lineDetected():
            self.currentState[1] == self.IS_WALL
            return True
        elif self.obstacleDetected():
            self.currentState[2] == self.IS_OBSTACLE
            return True
        return False
                    
    def touchDown():
       self.pictureList = []  #Start with an empty list.
       self.pic = self.Banana.takePicture()
       for i in range(4):
            self.pictureList = self.pictureList + [self.pic]  #Append the new picture
            self.Banana.turnBy(90)
       m.savePicture(self.pictureList,r"C:\Users\allis\Desktop\StarFleet Pics") #change filename as needed   
       self.Banana.stop()
            
    def avoidObstacle(self):
        def avoidRight():
            self.Avoiding = True
            self.Banana.turnBy(-90)
            self.Banana.forward(1,1)
            while self.Avoiding:
                self.Banana.turnBy(90)
                self.detectionCheck()
                if currentState[3] == IS_OBSTACLE:  
                    self.Banana.turnBy(-90)
                    self.Banana.forward(1,1)
                    continue
                else:
                    self.Avoiding = False
    
        def avoidLeft():
            Avoiding = True
            self.Banana.turnBy(90)
            self.Banana.forward(1,1)
            while Avoiding:
                self.Banana.turnBy(-90)
                self.detectionCheck()
                if self.currentState[3] == self.IS_OBSTACLE:  
                    self.Banana.turnBy(90)
                    self.Banana.forward(1,1)
                    continue
                else:
                    Avoiding = False
        
        
        if self.currentState[2] == self.IS_OBSTACLE:  
           self.Banana.turnBy(180) 
           self.Banana.savePicture(self.Banana.takePicture(),r'C:\Users\allis\Desktop\StarFleet Pics"')
           starfleetcom.postImage(r'http://localhost:8080/robot', r'C:\Users\allis\Desktop\StarFleet Pics"')
           self.Banana.wait(10)
           self.jsonComDict = json.loads(starfleetcom.getCommand(r'http://localhost:8080/robot')) #create json Dictionary
           self.Command = self.jsonComDict['order']
           
           if self.Command == "avoidRight":
                self.Banana.avoidRight()
                starfleetcom.deleteCommand(r'http://localhost:8080/control')
           elif self.Command == "avoidLeft":
                self.Banana.avoidLeft()
                starfleetcom.deleteCommand(r'http://localhost:8080/robot')
        
        self.currentStateReset()
    
    def seekLight(self):
        if self.currentState[0] == self.IS_LIGHT:
            self.motors(.5,.5) #Move forward autonomously toward light(there's specific code for this)
       
            
    
    def walkMaze(self):
        def move(self):
            self.Banana.forward(1)
            
        def checkLine(self):
            self.Banana.stop()
            self.Banana.turnBy(-90)
            self.Banana.setTimer()
        
        def avoidLine(self):
            self.Banana.backward(1,2)
            self.Banana.turnBy(-90)
            
        while True:
          self.detectionCheck()
          self.Banana.motors(.5,.5)
          self.setTimer(2)
          if self.lineDetected():
            self.avoidLine()
            self.setTimer(2)
          elif self.isAlarm():
            self.detectionCheck
            self.checkLine()
            self.Banana.Timer()
          elif self.detectionCheck():
            break
    
    def findSample(self):
        #Acceptable Commands from Starfleet : avoidLeft, avoidRight, retry, (integer)....
        
        while True:
            starfleetcom.deleteCommand(r'http://localhost:8080/control')
            starfleetcom.postImage(r'http://localhost:8080/robot',r'C:\Users\allis\Desktop\StarFleet Pics"')
            jsonCommandDict = json.loads(starfleetcom.getCommand(r'http://localhost:8080/control')) #extract command from json dictionary
            self.Command = jsonCommandDict['order']
            
            if self.Command == '':
               self.touchDown()
            elif self.Command == 'retry':
                self.touchDown()
                continue
            else:
                self.Banana.stop()
                self.Banana.turnBy(int(self.Command))
                starfleetcom.deleteCommand(r'http://localhost:8080/control')
                break
               
        while True:
            self.walkMaze() #start with walking the maze, if other sensors are activated, change state and break 
            
            if self.currentState[0] == self.IS_LIGHT: #should be replaced by corresponding state
                self.Banana.stop()
                self.seekLight()
          
            elif self.currentState[2] == self.IS_OBSTACLE: #should be replaced by corresponding state
                self.Banana.stop()
                self.avoidObstacle()
            
            elif self.currentState[1] == self.IS_WALL:
                self.Banana.stop()
                continue 


MazeRobot = MazeRobot()
MazeRobot.avoidObstacle()
#MazeRobot.touchDown
#MazeRobot.findSample()     
    