import os
import pip

def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
        pip.main(['install', package]) 
import_or_install('GitPython')
import_or_install('pytest')

from git import Repo
from sys import platform
from datetime import datetime

timestamp = datetime.now()

PATH_OF_GIT_REPO = r'.git'
COMMIT_MESSAGE = 'py commit @ ' + timestamp.strftime('%x-%X')

def git_push():
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(update=True)
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Some error occured while pushing the code. Contact the instructor')    


if platform == "linux" or platform == "linux2" or platform == "darwin":
    # linux or Mac
    os.system("python3 -m pytest")
elif platform == "win32":
    # Windows...
    os.system("pytest")
git_push()
