# git: revisited

## Review

After the previous version control lesson, you should have a basic understanding of the "structure"
of a git repository:

* **commit**s are changes
* each commit has a **parent**
* a **branch** is a sequence of commits

And be familiar with the actions you can perform on a repository:
* **clone** a repository to make a complete copy of it
* **checkout** a branch
* **push** stuff to another repository
* **fetch** stuff from another repository
* **pull**, which is a combination of a fetch and a checkout

In the previous lesson when you cloned this repository to your computer, git (through PyCharm)
created a configuration for a **remote** repository and named it "origin," which is the default
remote if you don't otherwise specify one.

## Forks

**Exercise:** _Create a fork of this repository._ Github has a concept of **forks** which are
clones of repositories owned by someone other than the owner of the original. If you go to this
project's page on Github, there's a "Fork" button in the top right. When you click that (assuming
you're logged in), Github will make you your own copy of the repository. You'll have full
read/write privileges in this copy and the owner of the original won't even have to know you've
made changes.

Once you've made your fork, the local repository on your development environment still doesn't know
anything about it.

## Managing Git Remotes

**Exercise:** _Add the fork as another remote to your local git repository._ This will involve the
command line, because PyCharm can't manage git remotes.

Open up a command line and cd to your workspace directory and then into `chainsaw`. Then, rename
the existing origin to be something else (any string will do):

    git remote rename origin qwerty

Now add your fork (the URL is on the fork's project page):

    git remote add origin (URL)

Now your fork is the default for remote operations.  Run a `git fetch --all` and the local repo
will query both Github repositories for info.

We're done with the command line now. You can relax.

## Branching

**Exercise:** _Make a new branch._ Previously you've checked out a different branch using the git
menu in the bottom right-hand corner of PyCharm. The same menu will let you create a new branch
by clicking on the big green plus. Call it whatever you like.

It's always a good idea to work on development in a branch. That way you can get all your code
working before you merge it into the working copy that everyone else shares. You don't have to
worry about your changes interfering with what anyone else is working on or vice-versa.

This new branch needs some changes in it and this lesson hasn't even had any programming yet!

**Exercise:** _Fix the lesson script._ Lesson.py in this directory takes a list of things and
filters it using a for loop and a comparison. The list inside the `for` loop knows about some
animals, but not enough. Expand that list to include the animals that are in `things`, so that
when the script is run it outputs just the animals. You can add some entries to `things` while
you're at it.

That shouldn't be too hard of a task. Once your script is working, let's save a copy of it.

**Exercise:** _Save your changes to a commit._ To create a commit, first you need to specify
which files' changes go into the commit. You may notice that while you've been working through
these tutorials, the file names change color on the left. Grey filenames represent files with no
changes, blue filenames represent version-controlled files with changes, and red filenames are
new files you've created.

Right-click on the blue `lesson.py` in this folder then the "Git" menu and then select "Add."

You can now create a commit. Do this by clicking the "VCS" menu, and then "Commit changes". (It's
called VCS instead of Git because PyCharm can handle a number of version control systems besides
just git. That menu changes based on whatever format the project folder is in.)

The menu that pops up asks for [a whole bunch of info.](commit-interface.png) You'll need to
enter some sort of description -- how detailed is up to you. The rest of the interface is safe to
ignore for now, but you may want to edit some of the options on other commits.

Hold the mouse button down when you click on the "Commit" button and it will give you additional
options. "Commit and push" is the one we're going to use for this change.

This *should* save your changes, add the description to them, and upload the commit to your new
branch on *your* Github fork.

## Pull Requests

Github has a feature called a "pull request" which sends a message to another developer that a
finished branch could be merged in.

**Exercise:** _Send me a pull request._ Back on the Github web interface, there will be a
notification that your new branch has been created with a green button next to it. Clicking the
button will bring up the interface to create a pull request. Every pull request consists of three
things: The branch to merge in, the branch to be merged into, and info about the request (a title
and description). Since your branch only has one commit, it will use your commit message to
populate the title/description fields.

Be as descriptive as you like, and send me the pull request with your "bug fixes" for the animal
list script. (Don't worry, I won't make fun of your code.  I won't merge it into my version either.)

# Objectives

This lesson didn't involve a lot of programming but hopefully you picked up on some good
collaboration practices:

* How to create a branch
* How to set up a git remote
* How to send changes to another repository
* How to open a pull request to let someone else know you're "done"
