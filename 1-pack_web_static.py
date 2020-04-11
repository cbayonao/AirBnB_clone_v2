#!/usr/bin/python3
from fabric.api import local
from datetime import datetime


def do_pack():
    try:
        local("mkdir -p versions")
        now = datetime.now()
        todayDate = now.strftime("%Y%m%d%H%M%S")
        cPath = "versions/web_static_" + todayDate
        local("tar -cvzf {}.tgz web_static".format(cPath))
        return cPath
    except Exception as err:
        print('The file could not be compressed')
