import shutil, errno

def copyanything(src, dst):
    try:
        shutil.copytree(src, dst)
    except OSError as exc: # python >2.5
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else: raise

print 'erase folder in beh public'
try:
	shutil.rmtree('/Users/danielmsheehan/GitHub/beh_public/sullivan')
except:
	print 'the folder was already missing'


#incopy = '/Users/danielmsheehan/GitHub/beh/naas/tasks/201410_pollen_sites/img'
incopy = '/Users/danielmsheehan/GitHub/beh/sullivan'
#outcopy = '/Users/danielmsheehan/GitHub/beh_public/naas/tasks/201410_pollen_sites/img'
outcopy = '/Users/danielmsheehan/GitHub/beh_public/sullivan'

print 'copy sullivan folder to beh public'
copyanything(incopy, outcopy)