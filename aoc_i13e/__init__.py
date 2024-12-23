"""
This module provides a sample entry-point for your aocd "plugin".
advent-of-code-data runner will repeatedly call your entry point
with varying year (2015+), day (1-25) and input data. The only
requirement is: your entry-point should be a callable which must
return a tuple of two values.

Note: On Dec 25 there is only one puzzle, but you should return
a tuple of 2 values anyway, e.g. (part_a_answer, None) the
second value of the tuple will not be used regardless.

Do whatever you want in your entry-point - you can import other
modules, call a function, run a script or a subprocess, etc.
If your existing code reads in data from a file, you could even
write out a scratch file from this entry-point.

For example, a sensible pattern might be something like:

    def mysolve(year, day, data):
        mod_name = "mypackage.aoc{}.day{}".format(year, day)
        mod = importlib.import_module(mod_name)
        a = mod.part_a(data)
        b = mod.part_b(data)
        return a, b

Or you could leave answers in the module namespace:

    mod = importlib.import_module(mod_name)
    return mod.a, mod.b

Or you could even just get them from a .py script print output:

    answers = io.StringIO()
    with redirect_stdout(answers):
        mod = importlib.import_module(mod_name)
    a, b = answers.getvalue().splitlines()

The AOC_SESSION is set before invoking your entry-point, which
means you can continue to use `from aocd import data` if you
want - it's not strictly necessary to define worker functions
which accept the input data as an argument (although, this is
usually a good practice, so that you can easily check your code
provides correct answers for each of the puzzle test cases!)
"""

import importlib


def mysolve(year, day, data):
    # this code auto-submits but there is no delay and doesn't process part_1 part_2 separately
    try:
        mod_name = f"aoc_i13e.aoc{year}.q{day:02d}"
        mod = importlib.import_module(name=mod_name)
    except ModuleNotFoundError:
        return (None, None)
        
    ans_1 = ans_2 = None
    try:
        part_1 = getattr(mod, "part_1")
        ans_1 = part_1(data)
        part_2 = getattr(mod, "part_2")
        ans_2 = part_2(data)
    except AttributeError:
        pass

    return ans_1, ans_2
