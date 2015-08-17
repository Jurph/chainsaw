# Modules

Python uses the term "module" to describe a file that is executed by the interpreter.

It's that simple.

Every script you've been working on so far consists of a single module. Now we're going to work
on a program that's spread across two modules.

## import

You've seen the `import` keyword before: It was used to get functionality from another Python
libraries into your program.

Imports are almost always at the top of the file, because they affect the behavior of everything
in that file.

Import also affects _scope_. When you import another module, you're bringing that module into
your module's scope.

## Variations

There's a few ways to use `import`:

* `import foo` - This puts `foo` in your module's scope. A variable called `bar` in the `foo`
module can be accessed as `foo.bar` in your module.
* `from foo import bar` - This puts `foo.bar` specifically in your module's scope as `bar`. No
other parts of `foo` will be available.
* `from foo import bar as baz` - Like the previous statement, this brings `bar` into your
module's scope but renames it so that it is accessed as `baz`. This is often used when there
might be ambiguity over which `bar` to use.

There are other less common ways to use import but you'll almost never encounter them.

## Trying It Out

**Exercise:** _Fix lesson.py._ The lesson script tries to access some variables from the settings
module. It doesn't do it right. There are at least two ways to fix this: By changing how the
variables are addressed or by changing the import statement.

**Exercise:** _Add more interaction between lesson and settings._ Once you've fixed lesson.py,
try adding some more variables in settings.py. They don't all have to be named in all-caps,
that's just a convention for definitions that aren't expected to change.

You can also add a function in settings and call it in lesson. See if you can figure out the
syntax for that.

## Module Behavior

One thing you may notice about the `settings` module is that if you ran it directly, it wouldn't
do anything. Well-behaved modules won't do anything by themselves. They exist entirely to be
imported into other modules.

You may have seen something like this in some Python scripts:

    if __name__ == '__main__':
        do_something()

That syntax is common in modules that can run themselves *or* be imported into another module. If
the module is run on a command line, Python will set the run-time variable "name" (with
underscores) to be "main" (with underscores) and that block of code will get run. If the module
is imported into another module, the "name" will be the module name -- and that code will never run.

(Underscores have formatting meaning to Markdown, which is why they're not written out in
the previous paragraph. Sorry if that causes any confusion. In Python, things that start and end
in double underscores have special behavior and you shouldn't usually name things that way in your
own programs.)

# Objectives

This lesson introduced the concept of modules and gave you a framework to experiment on
accessing variables from one file in another. You learned:

* What a Python "module" is
* Variations of the `import` statement
* Different ways to access parts of another module

