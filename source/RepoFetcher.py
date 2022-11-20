
import os

class Repo:
    def __init__(self, name):
        self.fullname = name
        split_name = self.fullname.split('/')
        self.name = split_name[0]
        self.owner = split_name[1]

    def pull(self, repo_url):
        if os.path.exists(self.name) == False:
            cmd = f'git clone ' + repo_url
            print(cmd)
            os.system(cmd)
        else:
            os.chdir(self.name)
            cmd = 'git pull'
            print(cmd)
            os.system(cmd)
            os.chdir('../')
