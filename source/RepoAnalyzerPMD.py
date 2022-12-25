from RepoFilter import RepoFilter
import os
import platform
import pandas as pd

class RepoAnalyzerPmd(RepoFilter):

    def __init__(self):
        super().__init__()
        self.source = 'pmd'

    def execute_impl(self):
        folder = f'../tmp/{self.name}'
        s = os.sep
        pmd_exec = f'.{s}..{s}bin{s}pmd{s}bin{s}'
        if platform.system() == 'Linux':
            pmd_exec += 'run.sh pmd'
        else:
            pmd_exec += 'pmd.bat'

        cmd = f'{pmd_exec} -d {folder} -f csv -R category/java/design.xml --no-cache -r ../data/pmd/{self.name}.csv'
        print(cmd)
        os.system(cmd)

    def getMetricResults(self):
        infile = f'../data/pmd/{self.name}.csv'
        # create element tree object
        df = pd.read_csv(infile)
        if len(df) == 0:
            return {}
        tmp_dic = df[['Rule','Line']].groupby(['Rule']).count()['Line'].to_dict()
        totals = {key: str(value) for key, value in tmp_dic.items()}
        return totals
