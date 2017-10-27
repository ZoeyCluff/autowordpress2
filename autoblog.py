#!/usr/bin/python
from __future__ import print_function
import os, sys, traceback, fileinput, string, zipfile, urllib, shutil, tarfile, pwd, grp, socket, time, requests, json, MySQLdb, pathlib
from twindb_cloudflare.twindb_cloudflare import CloudFlare, CloudFlareException
from distutils.dir_util import copy_tree
from random import randint, choice

from tempfile import mkstemp
from six.moves import input
execfile("./modules/checks.py")
execfile("./modules/database.py")
# import passwords and API keys to make it easier to link people to this without giving away users/passwords.
execfile("./secrets.py")
from secrets import *

# run pre-req checks to make sure all files are in the proper location.
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



    createDB(mysqlUser, mysqlRootPassword, domainShort, ipv4, mysqlpassword)
