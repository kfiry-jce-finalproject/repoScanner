import os.path

import requests
import json
from RepoAnalyzer import RepoFilter


class RepoAnalyzerCodeql(RepoFilter):
    def __init__(self):
        super().__init__()

    def execute_impl(self):
        self.localdir = f'../data/codeqldb/{self.name}'
        pass

# codeql database analyze C:\GIT\JceFinalProject\repoScanner\data\codeqldb\java\piggymetrics_java\codeql_db --format=sarif-latest --output C:\GIT\JceFinalProject\repoScanner\data\codeql\1.SARIF C:\Users\kfiry\.codeql\packages\codeql\java-queries\0.4.4\Metrics
# bqrs decode --output=C:\GIT\JceFinalProject\repoScanner\data\codeql\TPercentaageOfComments.res  --format=csv C:\GIT\JceFinalProject\repoScanner\data\codeqldb\java\piggymetrics_java\codeql_db\results\codeql\java-queries\Metrics\RefTypes\TPercentageOfComments.bqrs