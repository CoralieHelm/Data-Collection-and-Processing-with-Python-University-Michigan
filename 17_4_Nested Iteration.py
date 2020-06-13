#June 12 2020
#17.4. Nested Iteration


#Task 1. nested-3-1: Now try rearranging these code fragments to make a function that counts all the *leaf* items in
#a nested list like nested1 above, the items at the lowest level of nesting (8 of them in nested1).

nested1 = [['a', 'b', 'c'],['d', 'e'],['f', 'g', 'h']]
for x in nested1:
    print("level1: ")
    for y in x:
        print("     level2: " + y)

def count_leaves(n):
    count = 0
    for L in n:
        for x in L:
            count += 1
    return count
print(count_leaves(nested1))
print("*******")
#Task 2. Below, we have provided a list of lists that contain information about people.
#Write code to create a new list that contains every person’s last name, and save that list as last_names.
#Below, we have provided a list of lists that contain information about people. Write code to create a new list that contains every person’s last name, and save that list as last_names.
info = [['Tina', 'Turner', 1939, 'singer'], ['Matt', 'Damon', 1970, 'actor'], ['Kristen', 'Wiig', 1973, 'comedian'], ['Michael', 'Phelps', 1985, 'swimmer'], ['Barack', 'Obama', 1961, 'president']]
last_names = []

for celebrity in info:
    last_names.append(celebrity[1])
print(last_names)
print("*******")
#Task 3. Below, we have provided a list of lists named L. Use nested iteration to save every string containing “b” into a new list named b_strings.
L = [['apples', 'bananas', 'oranges', 'blueberries', 'lemons'], ['carrots', 'peas', 'cucumbers', 'green beans'], ['root beer', 'smoothies', 'cranberry juice']]
b_strings = []

for fruits in L:
    for fruit in fruits:
        if "b" in fruit:
            b_strings.append(fruit)
print(b_strings)
