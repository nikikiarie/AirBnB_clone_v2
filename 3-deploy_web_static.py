#!/usr/bin/python3
"""
Fabric script based on the file 2-do_deploy_web_static.py
that creates and distributes an archive to your web servers
"""

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir
env.hosts = ['54.164.102.153', '54.173.0.133']


def do_pack():
    """makes a tgz file"""
    try:
        mom = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        n_file = "versions/web_static_{}.tgz".format(mom)
        local("tar -cvzf {} web_static".format(n_file))
        return n_file
    except:
        return None


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


def deploy():
    """creates and distributes an archive to servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
