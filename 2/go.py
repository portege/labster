#!/usr/bin/python
import sys
import os
import subprocess
import zipfile

from time import gmtime, strftime

#config
dbname = "dbname"
dbuser = "dbuser"
dbpass = "dbpass"

# code
ok = os.getloadavg()

datelabel = strftime("%Y%m%d_%H%M%S", gmtime())

# check load
for c in range(0,2):
  if ok[c]>2:
    print "load > 2, oh nevermind"
    sys.exit()

print "check load: done"

# dump
subprocess.Popen('mysqldump -p'+dbpass+' -u '+dbuser+' '+dbname+' > dump.sql' , shell=True)

print "dump database: done"

# compress
zip = zipfile.ZipFile('backup/backup_'+datelabel+'.zip', 'a')
zip.write('/home/ubuntu/cms/cms/settings.py')
zip.write('dump.sql')
zip.close()

print "compressing: done"

# house keeping
import glob
filelist = sorted(glob.glob("backup/*.zip"))
if len(filelist)>7:
   os.remove(filelist[0])
   print filelist[0] +' deleted'

print "house keeping: done"

print 'all done.'
