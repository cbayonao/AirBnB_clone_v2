#!/usr/bin/python3
from fabric.api import *
import os
from datetime import datetime
env.hosts = ['35.196.71.231', '3.89.186.246']


def do_pack():
    """
    Comment empty
    """
    try:
        now = datetime.now()
        todayDate = now.strftime("%Y%m%d%H%M%S")
        cPath = "versions/web_static_{:s}.tgz".format(todayDate)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(cPath))
        return cPath
    except:
        return None


def do_deploy(archive_path):
    """
    Deploy archive!
    """
    if not os.path.isfile(archive_path):
        return False
    try:
        fileComp = archive_path.split("/")[1].split(".")[0]
        path = "/data/web_static/releases/{}".format(fileComp)
        put(archive_path, "/tmp/{:s}.tgz".format(fileComp))
        run("mkdir -p {}".format(path))
        run("tar -xzf /tmp/{}.tgz -C {}/".format(fileComp, path))
        run("sudo mv /data/web_static/releases/{}/web_static/* \
        /data/web_static/releases/{}/".format(fileComp, fileComp))
        run("sudo rm -rf /tmp/{}.tgz".format(fileComp))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -sf /data/web_static/releases/{}\
        /data/web_static/current".format(fileComp))
        run("rm -rf /data/web_static/releases/{}/web_static".format(fileComp))
        return True
    except:
        return False


def deploy():
    """
    Full deployment
    """
    try:
        pack = do_pack()
        return do_deploy(pack)
    except Exception:
        return False
