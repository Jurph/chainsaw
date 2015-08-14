# Packages

In the previous lesson, you learned a bit about Python modules. You got to try out the `import`
command, instead of just seeing it in use. Prior to Lesson 07, you saw the `import` statement
being used to load Python libraries or "packages."

What is a Python package? It's just a directory with a module or several in it.

In this folder, we have a directory called "riddler." It has two modules inside: one called
`__init__` and one called `db`. The init module (with the underscores) it what makes the
directory a package.

Like a module, you can import a whole package. If a script were to `import riddler` then
`foo` in `__init__.py` could be accessed as `riddler.foo` and `bar` in `db.py` could be accessed
as `riddler.db.bar`. You can see how this naming can get long and unwieldy when a large package
contains sub-packages, that's on reason why the `from` syntax is more common -- By writing `from
riddler.db import bar` at the top of your script, you can just call `bar` each time
instead of `riddler.db.bar`.

**Exercise:** _Look through the structure of the Riddler package._ There's a single function at
the base level (init) which references data in the `db` module. How much does the `lesson` module
need to know about `db`? How much of `db` can it see by default?

**Exercise:** _Add a joke to the database._ When you did this, what changed in the `lesson`
program? Did the behavior of lesson change at all by changing the `riddler` package?

**Exercise:** _Modify lesson to show all the jokes in the Riddler package._ How much more did
`lesson` need to know about `riddler` to accomplish this? Why might this be a good or bad thing?

# Objectives

You were introduced to Python's package system, which behaves a lot like the module system in
that it makes software more (sorry) modular. Chunks of code can be reused in other applications
easily without having to know details of how something is implemented.

