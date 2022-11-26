import pandas as pd
import getopt, sys
from RepoFetcher import Repo
from RepoAnalyzer import PmdAnalyzer
from GithubDb import *
from RepoAnalyzerCodeql import RepoAnalyzerCodeql

class AnalyzeTemplateMethod:
    def __init__(self, db):
        self.db = db

    def run(self, lang, analyzer, topn):
        df = self.db.getReposByLanguage(lang)[:topn]
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
        self.template_method = AnalyzeTemplateMethod(self.db)

def main():
    # os.chdir('../tmp')
    argumentList = sys.argv[1:]
    options = 'n:l:'
    long_options = ['topn=', 'lang']
    topn = 1
    lang = 'Java'
    try:
        # Parsing argument
        arguments, values = getopt.getopt(argumentList, options, long_options)

        # checking each argument
        for currentArgument, currentValue in arguments:
            if currentArgument in ("-n", "--topn="):
                topn = int(currentValue)
            elif currentArgument in ("-l", "--lang"):
                lang = currentValue
    except getopt.error as err:
        # output error, and return with an error code
        print(str(err))

    injector = Injector()
    injector.template_method.run(lang, injector.analyzer_codeql, topn)
    # template_method.run('Python', analyzer_codeql)


if __name__ == "__main__":
    main()

