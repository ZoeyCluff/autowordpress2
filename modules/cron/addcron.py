#!/usr/bin/python
import shutil
from crontab import CronTab
import os
copy = "cp ./lecrontab.py /etc/lerenewal.py"
def addcron():
    os.system(copy)
    my_cron = CronTab(user='root')
    job = my_cron.new(command='python /etc/lecrontab.py')
    job.day.on(27)
    my_cron.write()

addcron()
