import os.path

import requests
import json
from RepoAnalyzer import RepoFilter
import zipfile


class RepoAnalyzerCodeql(RepoFilter):
    def __init__(self):
        super().__init__()

    def execute_impl(self):
        lang = 'Java'
        self.dbfile = f'../data/codeqldb/{self.name}/{lang}'

        self.resfolder = f'../data/codeql/{self.name}'
        os.makedirs(self.resfolder, exist_ok=True)

        # C:\GIT\JceFinalProject\repoScanner\data\codeql\1.SARIF C:\Users\kfiry\.codeql\packages\codeql\java-queries\0.4.4\Metrics
        if not os.path.exists(self.dbfile):
            return

        s = os.sep
        cmd = f'..{s}bin{s}codeql{s}codeql database analyze {self.dbfile} --format=sarif-latest --output {self.resfolder}/{lang}.SARIF ..{s}bin{s}codeql{s}packages{s}java-queries{s}0.4.4{s}Metrics'
        os.system(cmd)

# codeql database analyze C:\GIT\JceFinalProject\repoScanner\data\codeqldb\java\piggymetrics_java\codeql_db --format=sarif-latest --output C:\GIT\JceFinalProject\repoScanner\data\codeql\1.SARIF C:\Users\kfiry\.codeql\packages\codeql\java-queries\0.4.4\Metrics
# bqrs decode --output=C:\GIT\JceFinalProject\repoScanner\data\codeql\TPercentaageOfComments.res  --format=csv C:\GIT\JceFinalProject\repoScanner\data\codeqldb\java\piggymetrics_java\codeql_db\results\codeql\java-queries\Metrics\RefTypes\TPercentageOfComments.bqrs