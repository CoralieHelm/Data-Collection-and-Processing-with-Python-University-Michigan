#June 12 2020
#17.1. Introduction: Nested Data and Nested Iteration
#17.1.1. Lists with Complex Items

#Check Your Understanding
#1. Below, we have provided a list of lists. Use indexing to assign the element ‘horse’ to the variable name idx1.
animals = [['cat', 'dog', 'mouse'], ['horse', 'cow', 'goat'], ['cheetah', 'giraffe', 'rhino']]

idx1 = animals[1][0]
print(idx1)

#2. Using indexing, retrieve the string ‘willow’ from the list and assign that to the variable plant.

data = ['bagel', 'cream cheese', 'breakfast', 'grits', 'eggs', 'bacon', [34, 9, 73, []], [['willow', 'birch', 'elm'], 'apple', 'peach', 'cherry']]

plant = data[7][0][0]
print(plant)
