# Loops

If you've done programming in any other language before, you've hopefully encountered loops.

While, For, and Do-Until loops are fairly standard methods of controlling instruction flow in a
program. The syntax may be slightly different in each language, but the behavior is generally the
same: Repeat a step (or steps) several times, unless it's time to stop.

Python has while loops that are fairly ordinary, such as:

       while instruction != "quit":
           instruction = get_user_command()
           process_command(instruction)

or:

        while True:
             game_loop()


The second is an "infinite loop": it will loop forever. Presumably in the `game_loop()` function
there will be some way to exit the program directly.

Python's for loops, on the other hand, have some neat properties. Whereas C-style for loops
require three statements (an initialization, a repeating instruction, and a comparison), Python's
for loops work on an iterator. There is an iterator built into many of the basic types (lists,
dictionaries) and some other variable types you'll encounter later.

The program in this lesson will use the `range()` function. This takes two values and returns a
list of all the elements between them. If you haven't dealt with a list in Python, it will be
covered in much more detail later, but the short version is that a Python list looks like this:
`my_list = [4, 8, 20, 1, 0, 4, 4, 'pony', 7]`. It contains several elements, each of which can be
any data type. They are stored in an ordered fashion and can be accessed by number, e.g. `print
(my_list[2])` will output the 3rd element: 20. (The entries are counted from 0.)

**Exercise:** _Read through lesson.py._ It outputs stars that form a shape. What shape do you
think will be printed? What will its dimensions be?

Run the script and see if you were right.

**Exercise:** _Edit the script to print the shape's mirror image._

If I were doing that, I'd try to print a bunch of spaces in place of stars, but you may come up
with a different procedure.

It sure would be nice to have some way to send your solution somewhere, wouldn't it? Maybe we
should revisit that source code collaboration material soon...

# Objectives

In this (short) lesson you got some experience working with for loops and possibly were
introduced to lists, including:

* Reading nested loops and determining their behavior
* Writing a script that uses for loops

