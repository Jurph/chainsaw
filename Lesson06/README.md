# functions

You've definitely seen functions in the previous lessons. They were used to demonstrate **scope**
in Python. We're going to dig a bit more into them in this lesson.

A function is a named chunk of code that you can use elsewhere in your program by **calling** it.
The code inside a function doesn't actually get executed until the call occurs.

Some functions are built-in to Python like `print()` and `range()` that you've seen before. They
each take **parameters** that go inside the parentheses and tell the function what to operate on.

Not all functions take parameters. Some functions take many parameters. Some can take a varying
amount depending on how they're called.

## Positional Paramters

The `factorial` function in lesson.py takes a single parameter: a number `n`. If you try to call
it as `factorial(2, 4)` Python will raise an exception and quit with an error message. No matter
what number you pass to `factorial` (or what variable name), it will call the value it receives
`n` in the function's scope. It doesn't even know that it's being called with a variable named
`x` in the for loop -- all it sees is the number.

There's at least two problems with `factorial` though.

**Exercise:** _Fix factorial's type checking._ What happens if you pass a string to `factorial()
`? Or a list? Or something other than a number? It's going to try to use that value in a
less-than-or-equal comparison and explode. Try to make it a little smarter. If it is passed
something other than a number, have it return a 0 right away before getting into the rest of the
function.

A function that will help is `isinstance()`, which is built in to Python. `isinstance()` takes
two parameters. The first is a variable or value and the second is a Python type like `int` or
`str` or `list`. It returns True or False (the Python boolean values which by the way must be
capitalized this way).

Once you've made `factorial` a little sturdier, let's look at it's other major problem.

## Recursion

As you work on `factorial()` you may notice that it calls itself. This is perfectly acceptable.
Each time it's called, the state of the program is saved and another copy of the function is
called. It's kind of like those wooden dolls that nest inside each other.

That said, there's a slight mathematical error in what the function does with the return vaule of
itself. It's not properly calculating the factorial.

**Exercise:** _Fix factorial's logic._ Figure out where `factorial()` is going awry in its
calculation. For reference, 1! = 1. 3! = 6. 5! = 120.

## Named Parameters, Default Parameters

Functions in Python can also be called with **named** parameters. For example:

    take_photograph(shutter_speed=0.5, aperture=1.4, iso=800)

If the function definition includes named parameters, then you can specify them in any order. The
following calls get the same result as the first:

    take_photograph(iso=800, shutter_speed=0.5, aperture=1.4)
    take_photograph(aperture=1.4, iso=800, shutter_speed=0.5)

    take_photograph(aperture=1.4,
                    iso=800,
                    shutter_speed=0.5)

    take_photograph(
        aperture=1.4,
        iso=800,
        shutter_speed=0.5
    )

You can use whichever is easiest to read or maintain later. (Note that positional parameters, the
kind you've seen in functions so far, can also be specified on different lines, too. It's just
more common with named parameters since they make the function calls longer.)

When you define a function with named parameters, you can set **default** values that will be
used in case that parameter isn't specified when the function is called, like this:

    def take_photograph(aperture=1.0, iso=100, shutter_speed=1.0, focal_distance=100.0):

The previous function calls would have worked fine even though they didn't specify focal_distance
because it had a default. You could even call `take_photograph()` without any parameters and it
would work.

Now let's put this to use.

There's a whole separate function in this lesson.py that isn't even being executed. You may
notice it calls the `print()` function a number of times and in your debugging of `factorial()`
you hopefully never saw that output anywhere.

**Exercise:** _Alter the for loop at the bottom of the script so it calls factorial() and
print_factors() for each number._

There are two ways you can call `print_factors()`. See what happens if you do it each way.

## Bonus Exercise

If you want to be fancy, see if you can make the factors and the factorial functions behave a bit
more similarly to each other: either they both print or neither prints.

# Objectives

In playing around with these functions you hopefully picked up some info about:

* Positional parameters
* Named parameters
* Default parameters
* Recursive functions
