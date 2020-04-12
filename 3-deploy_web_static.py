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
        cPath = "versions/web_static_" + todayDate
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(cPath))
        print("Archivo empaquetado")
        return cPath
    except:
        print("No se pudo empaquetar")
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
        print(fileComp)
        print(path)
        put(archive_path, "/tmp/{:s}.tgz".format(fileComp))
        print("Archivo puesto")
        run("mkdir -p {}".format(path))
        print("Carpeta path creada")
        run("tar -xzf /tmp/{}.tgz -C {}/".format(fileComp, path))
        print("Descomprimido")
        run("sudo mv /data/web_static/releases/{}/web_static/* \
        /data/web_static/releases/{}/".format(fileComp, fileComp))
        print("Archivos movidos")
        run("sudo rm -rf /tmp/{}.tgz".format(fileComp))
        print("Archivo tgz eliminado")
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -sf /data/web_static/releases/{}\
        /data/web_static/current".format(fileComp))
        print("Simbolik link ready")
        run("rm -rf /data/web_static/releases/{}/web_static".format(fileComp))
        print("Eliminando web_static remotamente")
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
