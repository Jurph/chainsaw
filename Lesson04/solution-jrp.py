# Original script prints a triangle with its base at the bottom & hypotenuse angling down to the right
# Objective is to update the script to print the original triangle's "mirror image"
# n.b. No matter which mirror image triangle you find most intuitive, you should do all three.

# This version  makes a triangle of size_max with its base at the top, angling from NW-to-SE
# with a flourish
size_max = 16
for x in range(1, size_max):
    output = ''
    for y in range(1, x):
        output += ' '
    for y in range(x, size_max):
        # Yeah I'm that jerk who always has to throw in a backflip to show off
        if x == int((size_max - y)/2):
            output += 'o'
        else:
            output += '*'
    print(output)

# This one makes a triangle of size_max with base at the top, angling from NE-to-SW.
for j in range(1, size_max):
    output = ''
    for k in range(size_max, j, -1): #Using the "Step" property of range to use a non-traditional increment.
        output += '*'
    for k in range(j,1, -1):
        output += ' '
    print(output)

# This one makes a triangle of size_max with base at the bottom, angling from SW to NE
for q in range(1, size_max):
    output = ''
    for p in range(1, size_max-q):
        output += ' '
    for p in range(1, q):
        output += '*'
    print(output)

# New Kids can't Triforce
#     ?
#    ??
