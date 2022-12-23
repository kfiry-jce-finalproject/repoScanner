from datetime import datetime

class RepoFilter:
    def __init__(self):
        self.datetime = datetime.now()
        self.repo_url = None
        self.owner = None
        self.fullname = None
        self.name = None
        self.source = None

    def execute_impl(self):
        pass

    def getMetricResults(self):
        return {}

    def execute(self, repo):
        self.fullname = repo['repo']
        split_name = self.fullname.split('/')
        self.name = split_name[0]
        self.owner = split_name[1]
        self.repo_url = repo['repo_url']
        self.execute_impl()
        return {
            'repo_name': self.fullname,
            'scan_time':self.datetime,
            'source':self.source,
            'results': self.getMetricResults()
               }
