

class RepoFilter:
    def __init__(self):
        self.repo_url = None
        self.owner = None
        self.fullname = None
        self.name = None

    def execute_impl(self):
        pass

    def execute(self, repo):
        self.fullname = repo['repo']
        split_name = self.fullname.split('/')
        self.name = split_name[0]
        self.owner = split_name[1]
        self.repo_url = repo['repo_url']
        self.execute_impl()
