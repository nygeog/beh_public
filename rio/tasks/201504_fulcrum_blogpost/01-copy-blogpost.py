import shutil, errno

def copyanything(src, dst):
    try:
        shutil.copytree(src, dst)
    except OSError as exc: # python >2.5
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else: raise

shutil.rmtree('/Users/danielmsheehan/GitHub/beh_public/rio/tasks/201504_fulcrum_blogpost')

incopy = '/Users/danielmsheehan/GitHub/beh/rio/tasks/201504_fulcrum_blogpost'
outcopy = '/Users/danielmsheehan/GitHub/beh_public/rio/tasks/201504_fulcrum_blogpost'

copyanything(incopy, outcopy)