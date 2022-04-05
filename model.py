'''
Agent-based Model 

Version 1

Author: 201466497, University of Leeds

As produced for GEOG5990: Assignment 1

To be run in the command prompt as per the README documentation
'''


# Packages and modules

# Import the packages and modules required for the model

# Standard library packages
import random 
import operator 
import tkinter 
import csv 
import argparse 

# Third party packages
import requests
import bs4
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.backends.backend_tkagg
import matplotlib.pyplot
import matplotlib.animation

# Local application modules
import agentframework

print("Libraries and modules imported")


# Command line run set up

# Model parameters set up to be input at the command line (with default 
#                                                         parameters used when 
#                                                         none are specified)
# Command line argument source code adapted from:
    # https://docs.python.org/3/library/argparse.html
parser = argparse.ArgumentParser(description = 'Agent-based model')
parser.add_argument("num_of_agents", type = int, nargs ='?', const = 10, 
                    default = 10, help = "This sets the number of agents as \
                        an integer")
parser.add_argument("num_of_iterations", nargs = '?', type = int, const = 100,
                    default = 100, help = "This sets the number of iterations \
                        as an integer")
parser.add_argument("neighbourhood", nargs = '?', type = int, const = 20,
                    default = 20, help = "This sets the neighbourhood as an \
                        integer")

args = parser.parse_args()
num_of_agents = args.num_of_agents
num_of_iterations = args.num_of_iterations
neighbourhood = args.neighbourhood
# Confirm the parameters used
print("Parameters used: Agents =",num_of_agents,", Iterations =",
      num_of_iterations,", Neighbourhood =",neighbourhood)


# Environment                  
                                                             
# Read in the environment as raster data
f = open('in.txt', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

# Create an environment container
environment = []

# Append the raster data to the environment as a 2D list 
for row in reader: 
    rowlist = []
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)
f.close()
# Uncomment to check the raster environment
'''
print(environment)
'''


# Agents

# Create agents container
agents = []

# Scrape starting y and x coordinates for agents from webpage:
    # http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html
# BeautifulSoup (BS4) source code adapted from:
    # https://www.crummy.com/software/BeautifulSoup/bs4/doc/
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
# Uncomment to check the coordinates obtained
'''
print(td_ys)
print(td_xs)
'''

# Create agents and assign starting coordinates as scraped above
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment, agents, y, x))

#  Starting coordinates assigned to agents
print("Starting agent coordinates:")
for agent in agents:
    print(agent)
    
# Figure set up

# Set the matplotlib figure and axis size
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


# Run model

carry_on = True
def update(frame_number):
    '''
    Function to define what is undertaken during each iteration:
     Clears the figure.
     The order that the agents run through their functions are randomly 
     shuffled. 
     Each agent runs through move, eat and share with neighbour functions.
     A stopping condition is defined where all agents stores meet the store 
     limit.
     Updates the environment and the plotted agents as an animation.
    
    Parameters
    ----------
    frame_number :
        THE NUMBER OF ITERATIONS THE UPDATE FUNCTION IS RAN THROUGH.
    
    Returns 
    -------
    Prints confirmation of the met stopping condition.
    '''
    fig.clear() 
    global carry_on
    # Check that the model is running through the iterations.
    '''
    print("Model updating")
    '''
    
    # Uncomment the for statements above and below random.shuffle to check that 
    # the order of which the agents are ran through their functions are 
    # randomly shuffled
    '''
    for a in agents:
        print("Before shuffle:", a.x, a.y)
    '''
    random.shuffle(agents)
    '''
    for a in agents:
        print("After shuffle:", a.x, a.y) # test shuffle 
    '''
    
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
   
    full_count = 0
    store_limit = 500
    for i in range(num_of_agents):
        if agents[i].store > store_limit:
            full_count = full_count + 1
            # Uncomment to check that each agents stores are filling
            '''
            print("Agent store full")
            '''
            
    if full_count == num_of_agents:
        carry_on = False
        print("Stopping condition: All agents stores full")
        
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x, agents[i].y, c='red')


def gen_function():
    ''' 
    Function to continue through the model iterations as per the 
    update function until stopping conditions are met:
     a) Maximum number of iterations as set at command line met. 
     b) Agents store limit met.
    
    Returns
    -------
    Prints confirmation that the model has met one of the stopping conditions.
    Prints the iteration number that the model's stopping condition is met at.
    Prints the final coordinates of each agent.
    Prints the final stores of each agent.
    '''
    a = 0
    global carry_on
    while (a < num_of_iterations) & (carry_on):
        yield a
        a = a + 1
    print("MODEL END")
    print("Iteration number at stopping condition:", a)
    #  Final coordinates assigned to agents
    print("Final agent coordinates:")
    for agent in agents:
        print(agent)
    print("Final agent stores:")
    for agent in agents:
        print(agent.store)


def run():
    '''
    Function to run the model as an animation

    Returns
    -------
    Prints confirmation that the model has started to run through the update
    function.

    '''
    global animation 
    animation = matplotlib.animation.FuncAnimation(fig, update,
                                                   frames=gen_function,
                                                   repeat=False, interval = 1)
    print("MODEL START")
    canvas.draw()
    

def close():
    '''
    Function to close the model

    Returns
    -------
    Prints confirmation that the model GUI has been closed.

    '''
    root.quit()
    root.destroy()
    print("MODEL CLOSED")


# GUI set up

root = tkinter.Tk()
root.protocol("WM_DELETE_WINDOW", close)
root.wm_title("Agent-based Model")

canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)
model_menu.add_command(label="Close model", command=close)

tkinter.mainloop()