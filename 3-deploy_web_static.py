#!/usr/bin/python3
#!/usr/bin/python3
from fabric.api import *
import os.path
import re
from datetime import datetime
env.hosts = ['35.196.71.231', '3.89.186.246']
env.user = 'ubuntu'


def do_pack():
    """
    Comment empty
    """
    try:
        local("mkdir -p versions")
        now = datetime.now()
        todayDate = now.strftime("%Y%m%d%H%M%S")
        cPath = "versions/web_static_" + todayDate
        local("tar -cvzf {}.tgz web_static".format(cPath))
        return cPath
    except:
        return None

def do_deploy(archive_path):
    """
    Deploy archive!
    """
    try:
        if not os.path.exists(archive_path):
            return False
        put(archive_path, "/tmp/")
        fileComp = archive_path.split("/")[1].split(".")[0]
        path = "/data/web_static/releases/{}".format(fileComp)

        run("mkdir -p {}".format(path))
        run("tar -xvzf /tmp/{}.tgz -C {}".format(fileComp, path))
        run("sudo rm /tmp/{}.tgz".format(fileComp))
        run("sudo rm /data/web_static/current")
        run("sudo ln -sf /data/web_static/releases/{}\
        /data/web_static/current".format(fileComp))
        run("sudo mv /data/web_static/releases/{}/web_static/* \
        /data/web_static/releases/{}/".format(fileComp, fileComp))
        run("rm -rf /data/web_static/releases/{}/web_static".format(fileComp))
        return True
    except:
        return False

def deploy():
    """
    Full deployment
    """
    f_path = do_pack()
    if f_path is None:
        return False
    ready = do_deploy(f_path)
    return ready
