# import packages

import random
import operator
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.backends.backend_tkagg
import matplotlib.pyplot
import matplotlib.animation
import tkinter
import agentframework
import csv
import requests
import bs4
import argparse


print("packagesimported")

def quit_me():
    print('quit')
    root.quit()
    root.destroy()

    
parser = argparse.ArgumentParser(description = 'Agent-based model')
parser.add_argument("num_of_agents", default = 10, type = int, help = "This sets the number of agents as an integer")
parser.add_argument("num_of_iterations", default = 100, type = int, help = "This sets the number of iterations")
parser.add_argument("neighbourhood", default = 20, type = int, help = "This sets the neighbourhood")


args = parser.parse_args()
num_of_agents = args.num_of_agents
num_of_iterations = args.num_of_iterations
neighbourhood = args.neighbourhood
print(num_of_agents, num_of_iterations, neighbourhood)


# read environment raster txt file 

f = open('in.txt', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

environment = []
for row in reader: 
    rowlist = []
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)
f.close()

print(environment)

# show environment
'''
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()
'''



# check Agent class assigns random coords to a when called and then move)
'''
a = agentframework.Agent()
print(a.y, a.x)
a.move()
print(a.y, a.x)
'''




# create function for calculating distance between agents (no longer need)
'''
def distance_between(agents_row_a, agents_row_b): 
    return (((agents_row_a.x - agents_row_b.x)**2) + ((agents_row_a.y - agents_row_b.y)**2))**0.5
'''



# control number of agents
'''
num_of_agents = 10

# control number of iterations (of steps)

num_of_iterations = 100


neighbourhood = 20
'''
agents = []


r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
print(td_ys)
print(td_xs)

for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment, agents, y, x))


fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
ax.set_autoscale_on(False)

# make the agents (10)

for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))
'''
# check original agents coords
    print(agents[i].x, agents[i].y)
'''
for agent in agents:
    print(agent)

carry_on = True

def update(frame_number):
    print("updating")
    global carry_on
    fig.clear() 

    # move the agents 
    
    #for a in agents:
        #print("Before shuffle:", a.x, a.y) # test shuffle 
    random.shuffle(agents)
    #for a in agents:
        #print("After shuffle:", a.x, a.y) # test shuffle 
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
    
    if random.random() < 0.1:
        carry_on = False
        print("stopping condition")
        
        

    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x, agents[i].y)

        
'''
# check agents coords post steps
for i in range(num_of_agents):
    print(agents[i].x, agents[i].y)
'''



# def update(frame_number):
    
#     fig.clear()
#     global carry_on

# # eat

#     for j in range(num_of_iterations):
#         for i in range(num_of_agents):
#             agents[i].move()
#             agents[i].eat()
       




# plot agents and environment 

    # matplotlib.pyplot.ylim(0, 99)
    # matplotlib.pyplot.xlim(0, 99)
    # matplotlib.pyplot.imshow(environment)
    # for i in range(num_of_agents):
    #     matplotlib.pyplot.scatter(agents[i].x, agents[i].y)

def gen_function(b= [0]):
    a = 0
    global carry_on
    while (a < 1) & (carry_on):
        yield a
        a = a + 1


def run():
    global animation 
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=num_of_iterations, repeat=False, interval = 1)
    canvas.draw()
    
root = tkinter.Tk()
root.protocol("WM_DELETE_WINDOW", quit_me)
root.wm_title("Model")

canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)
'''
print("animationdone")
'''

tkinter.mainloop()
    
#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=10)



# matplotlib.pyplot.show()




# calculate distance between agents (no longer need)
'''
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
'''

#Key = good comments and prints 
#Add arg parse to run in command prompt not spyder 
#Agents use all environment not just top left 