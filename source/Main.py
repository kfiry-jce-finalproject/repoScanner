import getopt, sys
from RepoFetcher import RepoGitPuller
from RepoAnalyzerPMD import RepoAnalyzerPmd
from GithubDb import *
from RepoAnalyzerCodeql import RepoAnalyzerCodeql
from RepoFetcherCodeql import RepoFetcherCodeql
from RepoAnalyzerJavaNcss import RepoAnalyzerJavaNcss

class AnalyzeTemplateMethod:
    def __init__(self, db, metric_db, fetcher, analyzer):
        self.db = db
        self.metric_db = metric_db
        self.analyzer = analyzer
        self.fetcher = fetcher

    def run(self, lang, topn):
        print("numofrepos=", topn)
        df = self.db.getReposByLanguage(lang)[:topn]
        for _, x in df.iterrows():
            self.fetcher.execute(x)
            res = self.analyzer.execute(x)
#            print(res)
            self.metric_db.insert_record(res)

class Injector:
    def __init__(self, type):
        db = GitHubDbPostgres('../data/db_conn.json')
        metric_db = GitHubDbMongoDb('../data/mongo.json')
        with open('../data/github_access_token.txt', 'r') as f:
            token = f.read()
        if type == 'pmd':
            fetcher = RepoGitPuller()
            analyzer = RepoAnalyzerPmd()
        elif type == 'javancss':
            fetcher = RepoGitPuller()
            analyzer = RepoAnalyzerJavaNcss()
        else:
            fetcher = RepoFetcherCodeql(token)
            analyzer = RepoAnalyzerCodeql()
        self.template_method = AnalyzeTemplateMethod(db, metric_db, fetcher, analyzer)

def main():
    # os.chdir('../tmp')
    argumentList = sys.argv[1:]
    options = 'n:l:a:'
    long_options = ['topn=', 'lang', 'analyzer']
    topn = 1
    lang = 'Java'
    analyzer_type = 'javancss'
    try:
        # Parsing argument
        arguments, values = getopt.getopt(argumentList, options, long_options)

        # checking each argument
        for currentArgument, currentValue in arguments:
            if currentArgument in ("-n", "--topn="):
                topn = int(currentValue)
            elif currentArgument in ("-l", "--lang"):
                lang = currentValue
            elif currentArgument in ("-a", "--analyzer"):
                analyzer_type = currentValue
    except getopt.error as err:
        # output error, and return with an error code
        print(str(err))
    print(topn)
    injector = Injector(analyzer_type)
    injector.template_method.run(lang, topn)

if __name__ == "__main__":
    main()
