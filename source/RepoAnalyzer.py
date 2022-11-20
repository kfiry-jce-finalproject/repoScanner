import os

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
