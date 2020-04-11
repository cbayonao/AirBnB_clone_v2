#!/usr/bin/python3
from fabric.api import *
import os.path
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
        print("Archivo empaquetado")
        return cPath
    except:
        print("No se pudo empaquetar")
        return None


def do_deploy(archive_path):
    """
    Deploy archive!
    """
    try:
        fileComp = archive_path.split("/")[1].split(".")[0]
        path = "/data/web_static/releases/{}".format(fileComp)

        put(archive_path, "/tmp/")
        print("Archivo puesto")

        run("mkdir -p {}".format(path))
        print("Carpeta path creada")

        run("tar -xvzf /tmp/{}.tgz -C {}".format(fileComp, path))
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
    archive_path = do_pack()

    if archive_path is None:
        print("No hay archive_path en Deploy")
        return False

    return do_deploy(archive_path)
