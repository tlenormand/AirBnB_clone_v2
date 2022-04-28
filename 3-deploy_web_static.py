#!/usr/bin/python3
"""fabric script that generates a .tgz archive
from the contents of the web_static folder"""
from fabric.api import local
from datetime import datetime
from fabric.api import put, run, env
from os.path import exists
env.hosts = ['34.139.172.50', '35.243.158.214']


def do_pack():
    """generates a .tgz archive from the contents of the web_static folder

    Return:
        archive path on success
        None otherwise
    """
    now = datetime.now().strftime('%Y%m%d%H%M%S')
    archivePath = 'versions/web_static_' + now + '.tgz'

    local('mkdir -p versions/')
    result = local('tar -cvzf {} web_static/'.format(archivePath))

    if not result.succeeded:
        return None

    return archivePath

def do_deploy(archive_path):
    """
    distributes an archive to the web servers
    
    Arguments:
        archive_path: path to the archive
    
    Return:
        true on success
        false otherwise
    """
    if exists(archive_path) is False:
        return False

    try:
        fileName = archive_path.split("/")[-1]
        no_ext = fileName.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(fileName, path, no_ext))
        run('rm /tmp/{}'.format(fileName))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True

    except Exception:
        pass

    return False

def deploy():
    """
    creates and distributes an archive to your web servers

    Return:
        True on success
        False otherwise
    """
    archive_path = do_pack()
    if archive_path is None:
        return False

    return do_deploy(archive_path)
