# Agent-based Model
**[This model](https://github.com/tburgess97/ABM)** builds agents into an environment in which the agents can interact with each other and the environment and displays the output as an animation.

It was produced for GEOG5990: Assignment 1 as part of MSc River Basin Dynamics and Management with GIS 

### Model Summary
**[The model](https://github.com/tburgess97/ABM):**
- Is ran in the command prompt by the user with customisable parameters
- Builds a customisable number of agents into a space
- Initialises the starting locations of agents from a web-scraped source
- Reads in a raster environment 
- Displays the model as an animation
- Is contained within a graphical user interface
- Allows the agents to:

  1. Randomly move within the environment by a customisable number of steps
  2. Eat the environment and fill their stores
  3. Share their stores with nearby agents to a customisable distance
  4. Randomises the order of agents actions
  5. Automatically stops the model when all the agents stores are full or the set number of steps is met

## User Guide

### Repository Contents

**1. README.md:** README file containing the model documentation and the user guide

**2. model.py:** Core model code

**3. agentframework.py:** Agent class code

**4. in.txt:** txt file containing the environment data

**5. LICENSE:**

### List of Dependencies

The model requires the following packages to be installed locally:


### Running the Model

- Download [the model repository](https://github.com/tburgess97/ABM) and extract to a local directory
- Navigate to the directory the model is stored locally within the command prompt 
- Install the packages required (as listed in the dependences above) locally using pip install 
- Run the model from the command prompt using the command: python model.py 
  - Running the model as command 'python model.py' uses the default parameters: Number of agents = 10, number of iterations = 100, neighbourhood = 20
  - Running the model as command 'python model.py x y z' will set the paramaters as input integer values
    - x = number of agents (as an integer)
    - y = number of iterations (as an integer)
    - z = neighbourhood; distance at which agents will share their store with another (as an integer)
  - Run model is selected from the GUI drop-down menu to run the model using the input parameters
  - The model is displayed as an animation with the GUI
  - The model returns the starting agent coordinates, and once the stopping condition is met; the final agent coordinates and their stores 
  - The model is closed from the GUI drop-down menu using Close model

### Model Checks 

A series of checks have been left in the model code as commented out statements. To run the model with checks returned, the check statements should be uncommented:
- Line 85: Environment read in and appended to a 2D list 
- Line 105-106: Inital agent coordinates are scraped from a websource 
- Line 154: Model is running through each iteration 
- Line 161-167: The order at which agents act is shuffled randomly with each iteration
- Line 182: Each agents stored is filled

## Author
**Student ID:** gy21t2b, The University of Leeds

## License 
The repository is licensed under the [MIT License](https://github.com/tburgess97/ABM/blob/main/LICENSE)

## Acknowledgements
The model was developed following the guidance of https://www.geog.leeds.ac.uk/courses/computing/study/core-python/
