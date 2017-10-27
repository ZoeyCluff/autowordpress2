#!/usr/bin/python
import os
import shutil
import sys
execfile("./modules/cron/addcron.py")

def checks():

    ssl = str("/etc/nginx/ssl/")
    param = str("openssl dhparam -out /etc/nginx/ssl/dhparam.pem 2048")


    # Make sure secrets file at least exists, not checking if valid at this point
    if not os.path.exists("./modules/app/secrets.py"):
        print("secrets.py missing, please check README.md")
        exit(1)
        print("secrets.py found, continuing")

    if not os.path.exists("/etc/lerenewal.py"):
        print("LetsEncrypt renewal Cronjob missing")
       #  shutil.move("./modules/cron/lecrontab.py", "/etc/lecrontab.py")
        addcron()


    # Make sure nginxconfig.conf exists
    if not os.path.exists("./modules/app/nginxconfig.conf"):
        print("nginxconfig.conf missing, please make sure all files have been downloaded.")
        exit(1)
    print("nginxconfig.conf exists, continuing")

    # make sure ssl folder exists
    if not os.path.exists("/etc/nginx/ssl/"):
        print("ssl folder missing, creating")
        os.mkdir(ssl)
    print("/etc/nginx/ssl/ found, continuing")

    # Generate dhparams if they dont exist
    if not os.path.exists("/etc/nginx/ssl/dhparam.pem"):
        print("dhparams missing, will cause config errors later. generating in a known location")
        os.system(param)
    print("dhparam.pem found, continuing")

    # Make sure wp-config-sample.php exists

    if not os.path.exists("./modules/app/wp-config-sample.php"):
        print("wp-config-sample.php is missing. Make sure all files have been downloaded.")
        exit(1)
    print("WP Config found, continuing")
checks()
