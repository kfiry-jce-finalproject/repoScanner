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
        df = self.db.getReposByLanguage(lang)[:self.topn]
        for _, x in df.iterrows():
            repo = Repo(x['repo'])
            print(repo.name)
#            repo.pull(x['repo_url'])
            analyzer.analyze(repo.name, repo.owner)

class Injector:
    def __init__(self):
        #db  = GithubDb('../Data/github-ranking-unique.csv')
        self.db = GitHubDbPostgres('../data/db_conn.json')
        #analyzer_pmd = PmdAnalyzer()
        with open('../data/github_access_token.txt', 'r') as f:
            token = f.read()

        self.analyzer_codeql = RepoAnalyzerCodeql(token)
        self.template_method = AnalyzeTemplateMethod(self.db, 10)

def main():
    injector = Injector()
    # os.chdir('../tmp')
    injector.template_method.run('Java', injector.analyzer_codeql)
    # template_method.run('Python', analyzer_codeql)


if __name__ == "__main__":
    main()

