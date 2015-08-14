# Version Control and Collaboration

## Background

Very few programs these days are written by a single developer. More programmers working together
make it easier to spot and fix bugs and generally promote writing better quality code.

In the past ten years there has been a revolution in tools available for cooperating on software.
Version control in particular has made huge strides with tools that make it easy to have
multiple new features being developed simultaneously without interference.

The lessons ahead will use "git" for version control and the online service "Github." You're
probably reading this document on Github, so hopefully you have at least passing familiarity with
the site, even if you don't know much about the "git" program.

**Exercise:** Before we go much further, if you don't have one, now is a good time to
_create a Github account_. If you have one already, _make sure you have the username and password_.

Thanks to modernization, you don't have to know anything about how git works or any of its
command-line options. Most IDEs handle it all for you!

**Exercise:** _Copy this repository to your workspace._ When you launch PyCharm, it will ask if
you want to open a project. One of the choices on that screen is "Check out from version control."
If you click on that and select Github from the drop-down menu, you'll be asked for Github
credentials and eventually it will ask for the repository URL.

Enter the URL for this project, which can be found on the main project page (see
[screenshot](project-page.png)). On the same screen it will ask where you want to save the project.
Pick the workspace directory you created in the previous lesson. The screen should look [something
like this](clone-repository.png).  Click "Clone" and it will perform a `git clone` operation without
you needing to even open the terminal.

This will create a complete copy of the repository on your computer, including all the metadata
about different versions. Your copy is _just as authoritative_ as the copy on Github. This is one
of the defining features of git over other version control systems like CVS or Subversion: it is
inherently distributed.

**Exercise:** Run some Python! The repository you just cloned has a script called "lesson.py" in
the directroy "Lesson01." Open it up in your IDE (double-click in PyCharm) and run it. To run a
script in PyCharm (for now) right-click on the tab containing the script and then click on the
"Run" command. This should open an output window and show the script's output.

Success?

## Git Vocabulary

(This will go fast. This may be a good time to have Wikipedia open. Even if you've used git before,
this may be a good review.)

The main element in git is a **commit**. A commit is a combined set of changes to the files in the
repository. It can be as small as adding or removing one character in one file, or changing every
single file in the repository: Every commit has to change something.

Each commit has a **parent** commit. That is to say, the commit represents the difference between
an older state and some newer state. If you follow the chain of commits all the way back, you
eventually will find the initial commit where the repo was created.

A complete sequence of commits from the newest end (which is called the **head**) to the initial
commit is a **branch**. There may be multiple branches in a repository, but they all share a common
parent at *some* point in the family tree.

In most cases, a new branch is created to work on a specific new feature. The developer(s) writing
that feature will make a series of commits that implement that feature (anywhere from 1 commit to
1000s depending on the complexity and check-in practices on the team). Once a branch is finished,
someone can **merge** that branch into another branch, probably one named "master" or "develop."
(There are many conventions for what to name things in git but they're all conventions. "master" has
no special meaning to git itself. The main branch of a project could be called "bozo-the-clown" for
all it cares.)

To switch between branches, a developer can **checkout** a different one. Checkout is also used to
move to a different place on the same branch, such as forward or backward in time (up or down the
tree).

The way people working on a repository copy their changes between repositories is either through
**push** or **fetch**. These two commands upload or download all the commits and branches that the
other party doesn't have, keeping everyone in sync. There's also the **pull** operation which does
a fetch followed by a checkout of the newest commit on the current branch.

Github mixes this up a little with their own term, a **pull request** which is basically a message
to the repository maintainer that someone has a branch they think is ready to be merged in. The
repository maintainer can then evaluate it and merge if they want to.

## Versioning

**Exercise:** _Check out a different branch of the repository._ The default branch of this
repository is "master" but as you can see it only has two lessons in it: Lesson00 and this one,
Lesson01. There's a bunch more lessons hidden away in the branch "tutorials."

PyCharm manages all the checkouts and branching for you. If you click on the bottom right of the
screen where it says "Git: master."  Find the branch called "tutorials" and try to switch to it.

If it works, another script should show up in the Lesson01 folder. Load that one up and run it as
well.