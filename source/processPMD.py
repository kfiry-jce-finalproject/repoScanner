import pandas as pd
import os
from RepoFetcher import Repo
from RepoAnalyzer import PmdAnalyzer
from GithubDb import GithubDb


class AnalyzeTemplateMethod:
    def __init__(self, db, topn):
        self.db = db
        self.topn = topn

    def run(self, lang, analyzer):
        df = db.getReposByLanguage(lang)[:self.topn]
        for _, x in df.iterrows():
            repo = Repo(x['repo'])
            repo.pull(x['repo_url'])
            analyzer.analyze(repo.name)


db  = GithubDb('../Data/github-ranking-unique.csv')
analyzer_pmd = PmdAnalyzer()
template_method = AnalyzeTemplateMethod(db, 1)
os.chdir('../tmp')
template_method.run('Java', analyzer_pmd)

