#!/usr/bin/python3
#!/usr/bin/python3
"""
A fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo
"""
from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """
    Creates a compressed archive of the web_static folder
    Returns the path to the archive if successful, None otherwise
    """
    try:
        if not os.path.exists("versions"):
            local("mkdir versions")
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(timestamp)
        local("tar -cvzf {} web_static".format(archive_path))
        print("web_static packed: {} -> {}Bytes".format(archive_path, os.path.getsize(archive_path)))
        return archive_path
    except Exception as e:
        return None
