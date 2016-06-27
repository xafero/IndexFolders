# -*- coding: utf-8 -*-

# Imports
from sys import argv, exit
from os import walk, stat
from os.path import join, splitext
from datetime import datetime
from peewee import *

# Hit exit if not parametrized
if not len(argv) >= 2:
    print 'Usage:', '[folder] ...'
    exit(-1)

# Create database
db = SqliteDatabase('files.db')


# The model
class File(Model):
    folder = CharField()
    name = CharField()
    type = CharField()
    created = DateTimeField()
    modified = DateTimeField()
    accessed = DateTimeField()
    size = BigIntegerField()

    class Meta:
        database = db


# Workers
def on_file(p, n):
    stmp = stat(join(p, n))
    ptmp = splitext(n)
    new_file = File.create(folder=p, name=ptmp[0], type=ptmp[1].lower(), size=stmp.st_size,
                           created=datetime.fromtimestamp(stmp.st_ctime),
                           modified=datetime.fromtimestamp(stmp.st_mtime),
                           accessed=datetime.fromtimestamp(stmp.st_atime))


# Clean everything
File.drop_table(True)
File.create_table(True)

# Print folders
folders = argv[1:]
for folder in folders:
    print 'Root =>', folder
    for root, dirs, files in walk(folder):
        print ' *', root, 'has', len(dirs), 'folder(s) and', len(files), 'file(s)...'
        for f in files:
            on_file(root, f)
