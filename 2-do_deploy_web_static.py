#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that
distributes an archive to your web servers
"""

from fabric.api import env, put, run
from os.path import exists
env.hosts = ['54.164.102.153', '54.173.0.133']


def do_deploy(archive_path):
    """distibutes archibe"""
    if exists(archive_path) is False:
        return False
    try:
        name_file = archive_path.split("/")[-1]
        name_archive = name_file.split(".")[0]
        name_dir = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(name_dir, name_archive))
        run('tar -xzf /tmp/{} -C {}{}/'.format(name_file, name_dir, name_archive))
        run('rm /tmp/{}'.format(name_file))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(name_dir, name_archive))
        run('rm -rf {}{}/web_static'.format(name_dir, name_archive))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(name_dir, name_archive))
        return True
    except:
        return False
