import os
from RepoAnalyzer import RepoFilter


class RepoGitPuller(RepoFilter):
    def __init__(self):
        super().__init__()

    def execute_impl(self):
        os.chdir('../tmp')
        if not os.path.exists(self.name):
            cmd = f'git clone ' +  self.repo_url
            print(cmd)
            os.system(cmd)
        else:
            os.chdir(self.name)
            cmd = 'git pull'
            print(cmd)
            os.system(cmd)
            os.chdir('../')
        os.chdir('../source')
