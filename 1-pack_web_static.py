#!/usr/bin/python3
"""fabric script that generates a .tgz archive
from the contents of the web_static folder"""
from fabric.api import local
from datetime import datetime


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
