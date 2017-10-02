===============
 Github Topics
===============

After you get more than a page full of projects under and owner in github, it's
hard to see exactly what's there. Github topics (a confusing name, but less
confusing once you realize how bad tags would be overloaded) allows for adding
simple keyword metadata to repositories.

Usage
=====

The usage for this is pretty simple:

1. get yourself an application token -
   https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/

2. put this into ``token.txt``

3. run ./tag-projects.py


Data
====

The data for topics is organized through a set of txt files in the ``topics/``
sub directory. Each txt file contains a list of projects that topic should be
applied to.
