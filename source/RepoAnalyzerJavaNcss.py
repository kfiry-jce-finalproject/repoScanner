import os.path
from RepoFilter import RepoFilter
import platform

class RepoAnalyzerJavaNcss(RepoFilter):
    def __init__(self):
        super().__init__()

    def execute_impl(self):
        folder = f'../tmp/{self.name}'
        s = os.sep
        ncss_exec = f'.{s}..{s}bin{s}javancss{s}bin{s}'
        if platform.system() == 'Linux':
            ncss_exec += 'javancss'
        else:
            ncss_exec += 'javancss.bat'

        cmd = f'{ncss_exec} -package -xml -out ../data/ncss/{self.name}.xml {folder}'
        print(cmd)
        os.system(cmd)
