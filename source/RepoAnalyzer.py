import os

class RepoFilter:
    def __init__(self):
        pass

    def execute_impl(self):
        pass

    def execute(self, repo):
        self.fullname = repo['repo']
        split_name = self.fullname.split('/')
        self.name = split_name[0]
        self.owner = split_name[1]
        self.repo_url = repo['repo_url']
        self.execute_impl()


class PmdAnalyzer:
    pmd_exec = '.\\..\\bin\\pmd\\bin\\pmd.bat'
    def __init__(self):
        print(self.pmd_exec)

    def analyze(self, folder):
        cmd = f'{self.pmd_exec} -d {folder} -f csv -R rulesets/java/design.xml -r ../data/pmd/{folder}.csv'
        print(os.getcwd())
        print(cmd)
        os.system(cmd)
        os.chdir('..')
