from RepoFilter import RepoFilter
import os
import platform
import pandas as pd

class RepoAnalyzerDesigniteJava(RepoFilter):

    def __init__(self):
        super().__init__()
        self.source = 'designiteJava'

    def execute_impl(self):
        folder = f'../tmp/{self.name}'
        s = os.sep
        _exec = f'java  -Xmx8192m -jar .{s}..{s}bin{s}DesigniteJava{s}DesigniteJava.jar'
        cmd = f'{_exec} -i {folder} -o ../data/designiteJava/{self.name}'
        print(cmd)
        os.system(cmd)

    def getMetricResults(self):
        infile = f'../data/designiteJava/{self.name}/designCodeSmells.csv'
        # create element tree object
        totals = {}
        if os.path.exists(infile):
            df = pd.read_csv(infile)
            if len(df) != 0:
                tmp_dic = df[['Type Name', 'Code Smell']].groupby(['Code Smell']).count()['Type Name'].to_dict()
                totals = {key: str(value) for key, value in tmp_dic.items()}

        infile = f'../data/designiteJava/{self.name}/implementationCodeSmells.csv'
        # create element tree object
        if os.path.exists(infile):
            df = pd.read_csv(infile)
            if len(df) != 0:
                tmp_dic = df[['Type Name', 'Code Smell']].groupby(['Code Smell']).count()['Type Name'].to_dict()
                for key, value in tmp_dic.items():
                    totals[key] = str(value)

        return totals
