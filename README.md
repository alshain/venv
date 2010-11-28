venv
====

A python package that redirects imports
to specified directories.

This allows for the creation of entirely
virtual python environments without
having to actually copy or link any files/directories.

Instead, you simply set the target directory in which certain
packages or subsets of packages are contained.

Use-Case
--------

When working on a project that consists of multiple git
repositories, it is cumbersome to change files across repositories,
and have run your python project without having to syncrhonize
the files continuously.

To make this worse, the files needed for python to work are
nested in the repository which makes often makes it impossible
to use them directly with python without mounting directories
and other nasty stuff.

Using `venv` you you no longer have to worry about the location
of your python files, they can be in any directory. The most
direct parent doesn't even have to be named like the package you
want to access them through.

Instead, you let `venv` redirect all of your imports.
This is done on a per directory basis.
You can define a package (dotted notation allowed) and map
it to a certain directory.

	venv.map('sqlalchemy', 'libs/sqlalchemy/lib/sqlalchemy/')

This allows you to keep the entire sqlalchemy repositoriy in a
subdirectory named `libs/sqlalchemy` and still be able to simply
import sqlalchemy without having to adjust the python path.

Furthermore, you could now easily keep multiple versions of
a library and change the version being used on a local scale,
that does not affect your entire python installation.

venv is greedy
--------------

You can also redirect submodules instead of only redirecting entire
packages. If you do both at the same time, you might wonder
which one takes precendence.

`venv` will take the best match, that is the longest. So `venv` will 
import what intuitively makes sense.

You could also say `venv`is greedy.
