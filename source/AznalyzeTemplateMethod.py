import pandas as pd
from RepoFetcher import Repo
from RepoAnalyzer import PmdAnalyzer
from GithubDb import *
from RepoAnalyzerCodeql import RepoAnalyzerCodeql

class AnalyzeTemplateMethod:
    def __init__(self, db, topn):
        self.db = db
        self.topn = topn

    def run(self, lang, analyzer):
        df = db.getReposByLanguage(lang)[:self.topn]
        for _, x in df.iterrows():
            repo = Repo(x['repo'])
            print(repo.name)
#            repo.pull(x['repo_url'])
#            analyzer.analyze(repo.name, repo.owner)

#db  = GithubDb('../Data/github-ranking-unique.csv')
db = GitHubDbPostgres('../data/db_conn.json')
#analyzer_pmd = PmdAnalyzer()
analyzer_codeql = RepoAnalyzerCodeql()
template_method = AnalyzeTemplateMethod(db, 100)
#os.chdir('../tmp')
template_method.run('Java', analyzer_codeql)
#template_method.run('Python', analyzer_codeql)

