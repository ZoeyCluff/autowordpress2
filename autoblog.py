#!/usr/bin/python
from __future__ import print_function
from tempfile import mkstemp

# import passwords and API keys to make it easier to link people to this without giving away users/passwords.

from distutils.dir_util import copy_tree
from random import randint, choice
import os
import sys
import traceback
import fileinput
import string
import zipfile
import urllib
import secrets
import shutil
import tarfile
import pwd
import grp
import socket
import time
import requests
import json
from twindb_cloudflare.twindb_cloudflare import CloudFlare, CloudFlareException
import MySQLdb
import pathlib
from six.moves import input
execfile("./modules/checks.py")
execfile("./secrets.py")
from secrets import *
checks()


def main(testing = False):
    global config

    www = str('www'+domainLong)
    config = "/etc/nginx/sites-enabled" +domainLong + ".conf"
    cf = CloudFlare(CLOUDFLARE_EMAIL, CLOUDFLARE_AUTH_KEY)

    # MySql password generation
    mysqlpass = string.ascii_letters + string.punctuation.replace("\"", "").replace("'", "") + string.digits
    mysqlpassword1 = "".join(choice(mysqlpass) for x in range(randint(8, 16)))
    mysqlpassword = ('%s' % mysqlpassword1)



    db = MySQLdb.connect(''+mysqlServer, ''+mysqlUser, ''+mysqlRootPassword)

    # Create a Cursor object to execute queries.
    cur = db.cursor()

    # Select data from table using SQL query.
    cur.execute("CREATE DATABASE IF NOT EXISTS " + domainShort)

    cur.execute("GRANT ALL PRIVILEGES ON " +domainShort + ".* TO %s@%s IDENTIFIED BY %s ", (domainShort, ipv4, mysqlpassword))
    cur.execute("FLUSH PRIVILEGES")
    db.commit()
    db.close()
