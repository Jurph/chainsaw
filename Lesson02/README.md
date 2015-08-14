# Virtual Environments

Many software packages change their behavior over time. Because of this, programs that rely on other
software packages sometimes require a specific version of the external package.

For example, an application called Foo might require the library Bar to be version 3 (dot
anything), but another application called Baz requires Bar 2.1.4 (specifically). Which version of
Bar should you have on your system? How do you keep both of them installed so they don't
interfere with each other and you can run both Foo and Baz?

Or worse, what if Foo requires Python 2.5 (a rather old version) and Baz requires Python 2.7 or
newer?

Python has several built-in features that help manage these dependencies.

The most important one for now is that it has a concept of "virtual environments." A virtual
environment is an isolated copy of Python (the interpreter) and any libraries or other software
packages you install. It's very common for each Python application on a system to have its own
virtual environment, often managed by the installer in such a way that you never even knew it was
created.

Any Python script that runs using that virtual environment (virtualenv) will automatically only see
the packages in that virtualenv and not even know about any others on the computer.

**Exercise:** _Create a virtual environment for these tutorials._

This is incredibly easy to do in PyCharm. If you pull up the "Preferences" menu (under PyCharm or
File depending on your platform) and expand the "Project: chainsaw" bullet, you'll see an item
called "Project Interpreter." Click on that and you'll see something like
[this screenshot.](01-interpreter-options.png).

Click on the gear in the top-right and one of the choices will be "Create VirtualEnv." Select that
and a dialog will pop up asking for info about the virtualenv to create. The [defaults should be
just about right.](02-create-virtual-env.png) (Don't worry if it selected a different Python
version -- nothing we're doing in these tutorials is particularly version-specific.)

Once you've created the virtualenv, the Python interpreter in that virtualenv will have been
selected as the default for this project. You may also notice that the list of software packges
installed in the virtualenv is nearly empty.

**Exercise:** _Install a yaml library._

YAML (Yet Another Markup Language) is a convenient standard for exchanging data between apps. It's
a readable plain-text format that stores records with all their named fields.

While still on the project interpreter preferences page, click the [plus icon in the bottom
corner.](03-add-package.png) It will bring up a list of all the Python software available through
PyPI (the Python Package Index). Look through the list for the PyYAML package and install it.

It will now be included in your virtualenv. Any Python script you run now will use that
virtualenv and have access to the PyYAML library.

**Exercise:** _Run a program that requires yaml._

The lesson.py in this folder won't work without yaml. If you tried running it before creating the
virtualenv, you may have noticed that it crashed out with a trace back. If you run it now, it
should successfully parse the text string which contains some YAML data and output a
neatly-formatted Python dict.

If you're not familiar with a dict yet, don't worry. We'll be covering tons about them later.

# Objectives

This lesson taught you a bit about isolating Python scripts into virtual environments. You
hopefully were able to:

* Create a virtualenv for this project
* Install a non-standard Python library
* Run a script that used that library
