"""Upload a directory of files recursively.

From https://gist.github.com/larssono/db35917cf58440fe0b19

Using ``upload_directory_tree``
-------------------------------

    >>> res = upload_directory_tree(project='syn2778315',
                                    start_path=".", syn=syn)

"""

import os
import synapseclient

def upload_directory_tree(project, start_path=".", syn):
    """Upload a directory recursively to a project's root.

    """

    parents = {start_path: project}

    for dirpath, dirnames, filenames in os.walk(start_path):

        #Add the subfolders
        for dirname in dirnames:
            print 'creating directory %s' % dirname

            f = syn.store(synapseclient.Folder(dirname,
                                               parent=parents[dirpath]))
            parents[os.path.join(dirpath, dirname)] = f.id

            #Add the files
            for name in filenames:
                path = os.path.join(dirpath, name)

                if os.stat(path).st_size>0:
                    print 'uploading file %s' % path
                    f = synapseclient.File(path,
                                           parent=parents[dirpath],
                                           name=name)
                    syn.store(f, forceVersion=forceVersion)
