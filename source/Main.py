import pandas as pd
import getopt, sys
from RepoFetcher import RepoGitPuller
from RepoAnalyzer import PmdAnalyzer
from GithubDb import *
from RepoAnalyzerCodeql import RepoAnalyzerCodeql
from RepoFetcherCodeql import RepoFetcherCodeql


class AnalyzeTemplateMethod:
    def __init__(self, db, analyzer, fetcher):
        self.db = db
        self.analyzer = analyzer
        self.fetcher = fetcher

    def run(self, lang, topn):
        df = self.db.getReposByLanguage(lang)[:topn]
        for _, x in df.iterrows():
            self.fetcher.execute(x)
            self.analyzer.execute(x)
#            repo.pull(x['repo_url'])
#            analyzer.analyze(repo.name, repo.owner)

class Injector:
    def __init__(self):
        # db  = GithubDb('../Data/github-ranking-unique.csv')
        db = GitHubDbPostgres('../data/db_conn.json')
        # analyzer_pmd = PmdAnalyzer()
        with open('../data/github_access_token.txt', 'r') as f:
            token = f.read()
        fetcher = RepoFetcherCodeql(token)
        analyzer = RepoAnalyzerCodeql()
        self.template_method = AnalyzeTemplateMethod(db, fetcher, analyzer )

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
    injector.template_method.run(lang, topn)


if __name__ == "__main__":
    main()
