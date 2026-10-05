# Extending Robot Framework workshop

This repository contains training material related to the Extending Robot Framework
workshop organized as part of [WWWW 2026](https://wwww.robotframework.org) on Wednesday, October 7, 2026.

## Installations

- Python 3.10 or newer.
- Robot Framework 7.5. Earlier Robot Framework 7.x versions will work, but you
  cannot run all examples.
- [Python-Markdown](https://python-markdown.github.io/) and
  [Pygments](https://pygments.org/) modules.
- Editor or IDE that supports Python and Robot Framework. VSCode or PyCharm with
  the [RobotCode plugin](https://robotcode.io/) is recommended.
- Suitable admin rights to install additional Python modules if needed.

## Materials

The first step is getting the initial material from this repository. The
recommended approach is cloning the repository using `git`, but you can
also [download the content as a zip file](
https://github.com/pekkaklarck/wwww2026-extending-robot/archive/refs/heads/main.zip).

During the day I push my changes to the `main` branch. If you cloned the repository,
you can then easily pull the changes to your local repository  if needed.  If you
want to work in the same local repository, it is a good idea to  create a branch
for your work by running `git checkout -b <branchname>`. If you also want to push
your changes to GitHub, you need to first fork this repository and clone the fork.

## Topics

Covered topics are listed below and each topic has a dedicated directory for
materials related to it.

- [Libraries](Libraries)
- [Listeners](Listeners)
- [Data and result modifiers](Modifiers)
- [Parsing API](Parsing)
