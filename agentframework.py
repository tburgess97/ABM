'''
Agent class
Contains agents attributes and their behaviours

As ran through model.py

Version 1

Author: 201466497, University of Leeds

As produced for GEOG5990: Assignment 1
'''

# Packages

# Import the packages required for the class

# Standard library packages
import random


# Agent class

# Initiate an Agent class for the agents and define their behaviours as 
# functions

class Agent:

    
    def __init__(self, environment, agents, y = None, x = None):
        '''
        Function to initiate the agent; reads in the environment and sets y and
        x coordinates, assigns random y and x coordinates if none are read
        and sets the agents store 

        Parameters
        ----------
        environment :
            THE ENVIRONMENT AS A 2D LIST FROM model.py.
        agents :
            THE AGENT LIST FROM model.py.
        y : 
            THE Y COORDINATE OF THE AGENT FROM model.py. The default is None 
            if none are passed.
        x : 
            THE X COORDINATE OF THE AGENT FROM model.py. The default is None 
            if none are passed.

        Returns
        -------
        None.

        '''
        self._y = random.randint(0,299)
        self._x = random.randint(0,299)
        self.environment = environment
        self.store = 0
        self.agents = agents
        
        if (x == None):
            self._x = random.randint(0,299)
        else:
            self._x = x
            
        if (y == None):
            self._y = random.randint(0,299)
        else:
            self._y = y
        
        
    def __str__(self):
        '''
        Function that defines its own values as a string

        Returns
        -------
        Its own values as a string.

        '''
        return " x " + str(self._x) + " y " + str(self._y)
        
    
    def getx(self):
        return self._x
        '''
        A get function for the x coordinate 
        
        Returns
        -------
        The read x coordinate.
        '''
    
    
    def setx(self, value):
        self._x = value
        '''
         A set function for the x coordinate 
        
        Returns
        -------
        The set x coordinate.
        '''
    
        
    def gety(self):
        return self._y
        '''
        A get function for the y coordinate 
        
        Returns
        -------
        The read y coordinate.
        '''
       
        
    def sety(self, value):
        self._y = value
        '''
        A set function for the y coordinate 
        
        Returns
        -------
        The set y coordinate.
        '''
        
    x = property(getx, setx, "I'm the 'x' property")
    y = property(gety, sety, "I'm the 'y' property")
    
    
    def move(self):
        '''
        A function to move the agent by one step in a random direction and 
        apply a fence boundary affect to the agent

        Returns
        -------
        The new y coordinate.
        THe new x coordinate.

        '''
        if random.random() < 0.5:
            self._y = (self._y + 1) 
        else:
            self._y = (self._y - 1) 
            
        if random.random() < 0.5:
            self._x = (self._x + 1)
        else:
            self._x = (self._x - 1)
    
        # Fence boundary affect to keep the agent within the environment limits
        if self._y < 0:
            self._y = 0
        if self._y > 299:
            self._y = 299
        
        if self._x <0:
            self._x = 0
        if self._x > 299:
            self._x = 299


    def eat(self):
        '''
        A function that defines the agent's eat behaviour; to remove 10 units
        from the environment at the coordinates it has

        Returns
        -------
        The new environment value.
        The new agent store value.

        '''
        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10

            
    def distance_between(self, agent):
        '''
        A function that defines the agent's eucalidian distance between itself
        and other agents

        Parameters
        ----------
        agent :
            THE AGENT LIST FROM model.py.

        Returns
        -------
        The eucalidan distance value. 

        '''
        return (((self._x - agent._x)**2) + ((self._y - agent._y)**2))**0.5
   
    
    def share_with_neighbours (self, neighbourhood):
        '''
        A function to make the agent share its store with the closest agent if
        the distance is less than the neighbourhood parameter assigned at the 
        command line

        Parameters
        ----------
        neighbourhood : 
            NEIGHBOURHOOD PARAMETER VALUE FROM model.py.

        Returns
        -------
        The agents new store value.

        '''
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum / 2
                self.store = ave
                agent.store = ave
                # Uncomment to check that agents are sharing with their 
                # neighbours 
                '''
                print("sharing" + str(dist) + " " + str(ave))
                '''
                
    