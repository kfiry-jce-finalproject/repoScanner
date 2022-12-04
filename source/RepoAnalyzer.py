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


class RepoFetcherPmd(RepoFilter):

    def __init__(self):
        super().__init__()

    def execute_impl(self):
        folder = f'../tmp/{self.name}'
        s = os.sep
        pmd_exec = f'.{s}..{s}bin{s}pmd{s}bin{s}pmd.bat'
        cmd = f'{pmd_exec} -d {folder} -f csv -R rulesets/java/design.xml --no-cache -r ../data/pmd/{self.name}.csv'
        print(cmd)
        os.system(cmd)
