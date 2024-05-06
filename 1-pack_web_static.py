#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
f the web_static folder
"""

from fabric.api import *
from datetime import datetime


def do_pack():
    """archives static files"""

    mom = datetime.now()
    ar = 'web_static_' + mom.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    fon = local('tar -cvzf versions/{} web_static'.format(ar))
    if fon is not None:
        return ar
    else:
        return None
