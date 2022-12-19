from RepoFilter import RepoFilter
import os
import platform

class RepoAnalyzerPmd(RepoFilter):

    def __init__(self):
        super().__init__()

    def execute_impl(self):
        folder = f'../tmp/{self.name}'
        s = os.sep
        pmd_exec = f'.{s}..{s}bin{s}pmd{s}bin{s}'
        if platform.system() == 'Linux':
            pmd_exec += 'run.sh pmd'
        else:
            pmd_exec += 'pmd.bat'

        cmd = f'{pmd_exec} -d {folder} -f test -R categoty/java/design.xml --no-cache -r ../data/pmd/{self.name}_c.csv'
        print(cmd)
        os.system(cmd)
