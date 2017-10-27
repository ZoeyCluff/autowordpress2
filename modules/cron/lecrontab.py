#!/usr/bin/python
import os
os.system(str("sudo systemctl stop nginx"))
os.system(str("sudo letsencrypt renew"))
os.system(str("sudo systemctl start nginx"))

