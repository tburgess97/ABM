import random


class Agent:
    
# initiate new instance of the agent class and assign random coords; __init__
# method sets initial state of object (an agent)


    def __init__(self, environment, agents, y = None, x = None):
        self._y = random.randint(0,99)
        self._x = random.randint(0,99)
        self.environment = environment
        self.store = 0
        self.agents = agents
        
        if (x == None):
            self._x = random.randint(0,99)
        else:
            self._x = x
            
        if (y == None):
            self._y = random.randint(0,99)
        else:
            self._y = y
        
        
    def __str__(self):
        return " x " + str(self._x) + " y " + str(self._y)
        
# get and set functions for coords
    def getx(self):
        return self._x
    
    def setx(self, value):
        self._x = value
        
    def gety(self):
        return self._y
       
    def sety(self, value):
        self._y = value
        
    x = property(getx, setx, "I'm the 'x' property")
    y = property(gety, sety, "I'm the 'y' property")
    
    
# move instance by 1 step (one x step, one y step) and boundary affect
    def move(self):
        if random.random() < 0.5:
            self._y = (self._y + 1) % 100
        else:
            self._y = (self._y - 1) % 100
            
        if random.random() < 0.5:
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100
    
    def eat(self):
        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10
            
   
    def share_with_neighbours (self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave
                #print("sharing" + str(dist) + " " + str(ave))# check print 
                
    def distance_between(self, agent):
        return (((self._x - agent._x)**2) + ((self._y - agent._y)**2))**0.5