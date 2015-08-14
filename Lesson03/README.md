# Scope

"Scope" is more than just mouthwash. (har de har)

It's also the context in which your programs identifiers are resolved.

Python, like many languages, has several naming scopes. Some of them overlap, which can make
things confusing.

**Exercise:** _Read this lesson's `lesson.py` and guess what values of `bar` will be printed._

`bar` is assigned a value in two different places and it is printed in two different places. Will
the value of bar be the same both times?

Run the program and see if you were right.

The scopes at play here are **file** scope (also called **module** scope, since Python calls script
files "modules") and **function** scope.

An identifier at the function scope only exists in that function -- it can't be read or written
outside of that function.

An identifier at the module scope is essentially global. It can be read anywhere in the file,
including inside functions. It can only be written, however, outside of functions. If you're inside
a function and try to write to a variable of the same name, Python will create a new variable
that has function scope and that function will no longer be able to "see" the module-level one.

EXCEPT! There's a way to allow a function to use a module-level identifier as if it were local,
and that's the `global` keyword.  Before accessing `bar` in a function, you can add the
instruction `global bar` and it will use the module's `bar` instead of creating a function-bar.

**Exercise:** _Edit the script to print different values of bar._

If you add `global bar` at the line `# Comment 1`, then `set_bar()` will use the module's `bar`.
Before running the script, what do you think will be output the two times it tries to print?

Okay, comment out that `global` statement and replace `# Comment 2` with something like `bar =
42`. How will *that* affect the output? Since `bar` in `test()` is a local variable, it won't
change the output at the end of the script.

Comment out the second change you did and assign `bar` a value below comment 3, but before the
call to the test function. This time, you're modifying the global. What will happen?

# Objectives

In this lesson, you got to experiment a bit with the scope of variables. You should have a basic
understanding of file-level scope (or module-level scope) and function-level scope. There are a
couple other scopes we'll encounter in later lessons so make sure you understand the difference now.

