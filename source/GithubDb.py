import pandas as pd
import psycopg2
import json


class GithubDb:
    def __init__(self, file):
        self.df = pd.read_csv(file)
        self.df.sort_values(by=['forks'])

    def getReposByLanguage(self, lang):
        df = self.df[self.df["language"] == lang]
        return df

class GitHubDbPostgres:
    columns = [ 'repo', 'repo_url']
    def __init__(self, filename):
        f = open(filename)
        dic = json.load(f)
        con_string = f"host={dic['host']} dbname={dic['dbname']} user={dic['user']} password={dic['password']}"
        self.conn = psycopg2.connect(con_string)
        f.close()

    def getReposByLanguage(self, lang):
        cursor = self.conn.cursor()
        query = f"select {','.join(self.columns)} from repos where language = '{lang}' order by forks DESC"
        print(query)
        cursor.execute(query)

        # Naturally we get a list of tupples
        tupples = cursor.fetchall()
        cursor.close()

        # We just need to turn it into a pandas dataframe
        df = pd.DataFrame(tupples, columns=self.columns)
        print(df)
        return df

    def insertCodelQlRecord(self, codeql_record):
        sql = """INSERT INTO CodeQlDbs(repo_id, lang, dbfilename, db_id, created_at,  VALUES ()"""
        self.conn.cur.execute(sql, (value1,value2))
