import os
from RepoAnalyzer import RepoFilter


class RepoGitPuller(RepoFilter):
    def __init__(self, record):
        super().__init__(self)

    def execute_impl(self, repo_url):
        if not os.path.exists(self.name):
            cmd = f'git clone ' + repo_url
            print(cmd)
            os.system(cmd)
        else:
            os.chdir(self.name)
            cmd = 'git pull'
            print(cmd)
            os.system(cmd)
            os.chdir('../')
