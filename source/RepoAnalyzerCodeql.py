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
        self.dbfolder = f'../data/codeqldb/{self.name}/{lang}'

        self.resfolder = f'../data/codeql/{self.name}'
        os.makedirs(self.resfolder, exist_ok=True)

        if not os.path.exists(self.dbfolder):
            print(f'No {lang} codeql db for {self.fullname}, skipping' )
            return

        folders = ['codeql_db', 'java']
        db_analysisfolder = f'{self.dbfolder}/codeql_db'
        for x in folders:
            db_analysisfolder = f'{self.dbfolder}/{x}'
            if os.path.exists(f'{db_analysisfolder}/codeql-database.yml'):
                break

        # C:\GIT\JceFinalProject\repoScanner\data\codeql\1.SARIF C:\Users\kfiry\.codeql\packages\codeql\java-queries\0.4.4\Metrics
        s = os.sep
        cmd = f'..{s}bin{s}codeql{s}codeql database analyze {db_analysisfolder} --format=sarif-latest --output {self.resfolder}/{lang}.SARIF ..{s}bin{s}codeql{s}packages{s}java-queries{s}0.4.4{s}Metrics'
        print(f'executing.. {cmd}')
        os.system(cmd)
        self.output_result(db_analysisfolder)

    def output_result(self, db_analysisfolder):
        s = os.sep
        ext = '.bqrs'
        for root, _, files in os.walk(db_analysisfolder):
            for filename in files:
                file_path = os.path.join(root, filename)
                if file_path[-(len(ext)):] == ext:
                    cmd = f'..{s}bin{s}codeql{s}codeql bqrs decode --output={self.resfolder}/{filename[:-len(ext)]}.csv --format=csv {file_path}'
                    print(f'executing.. {cmd}')
                    os.system(cmd)



# codeql database analyze C:\GIT\JceFinalProject\repoScanner\data\codeqldb\java\piggymetrics_java\codeql_db --format=sarif-latest --output C:\GIT\JceFinalProject\repoScanner\data\codeql\1.SARIF C:\Users\kfiry\.codeql\packages\codeql\java-queries\0.4.4\Metrics
# bqrs decode --output=C:\GIT\JceFinalProject\repoScanner\data\codeql\TPercentaageOfComments.res  --format=csv C:\GIT\JceFinalProject\repoScanner\data\codeqldb\java\piggymetrics_java\codeql_db\results\codeql\java-queries\Metrics\RefTypes\TPercentageOfComments.bqrs