#!/usr/bin/python3
"""deletes out-of-date archives"""

from fabric.api import *
import os
env.hosts = ['54.164.102.153', '54.173.0.133']


def do_clean(number=0):
    """deletes archives
    Args:
        number (int): num 0f archives to keep
    If number is 0 or 1, keep only the most recent version of your
    archive.
    """

number = 1 if int(number) == 0  else int(number)
ar = sorted(os.listdir("versions"))
[ar.pop() for a in range (number)]
with lcd("versions"):
    [local("rm ./{}".format(b)) for b in ar]

with cd("/data/web_static/releases"):
    ar = run("ls -tr").split()
    ar = [c for c in ar if "web_static_" in c]
    [ar.pop() for j in range(number)]
    [run("rm -rf ./{}".format(k)) for k in ar]

