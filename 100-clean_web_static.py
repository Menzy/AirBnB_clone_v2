#!/usr/bin/python3
"""script (based on the file 3-deploy_web_static.py) that deletes out-of-date
 archives, using the function do_clean
"""
from fabric.api import *
import os

env.hosts = ['100.24.238.31', '18.206.202.49']


def do_clean(number=0):
    """
    Deletes out-of-date archives
    number is the number of the archives, including the most
    recent, to keep
    """
    number = int(number)
    if number < 0:
        return None
    elif number == 0 or number == 1:
        number = 1
    else:
        number += 1

    with lcd("versions"):
        local("ls -t | tail -n +{} | xargs rm -rf --".format(number))

    with cd("/data/web_static/releases"):
        run("ls -t | tail -n +{} | xargs rm -rf --".format(number))
