import pandas as pd
import psycopg2
import pymongo
import json

class GithubDb:
    def __init__(self, file):
        self.df = pd.read_csv(file)
        self.df.sort_values(by=['forks'])

    def getReposByLanguage(self, lang):
        df = self.df[self.df["language"] == lang]
        return df

class GitHubDbPostgres:

    def __init__(self, filename):
        with open(filename) as f:
            dic = json.load(f)
        con_string = f"host={dic['host']} dbname={dic['dbname']} user={dic['user']} password={dic['password']}"
        self.conn = psycopg2.connect(con_string)
    def getReposByLanguage(self, lang):
        columns = ['repo', 'repo_url']
        cursor = self.conn.cursor()
        query = f"select {','.join(columns)} from repos where language = '{lang}' order by forks DESC"
        print(query)
        cursor.execute(query)

        # Naturally we get a list of tupples
        tupples = cursor.fetchall()
        cursor.close()

        # We just need to turn it into a pandas dataframe
        df = pd.DataFrame(tupples, columns=columns)
        print(df)
        return df

class GitHubDbMongoDb:
    def __init__(self, filename):
        with open(filename) as f:
            dic = json.load(f)
        con_string = f"mongodb://{dic['user']}:{dic['password']}@{dic['host']}:{dic['port']}/"
        self.client = pymongo.MongoClient(con_string)
        self.db = self.client[dic['dbname']]
        self.metric_col = self.db['projectInternalMetric']
    def insert_record(self, row):
        self.metric_col.insert_one(row)


