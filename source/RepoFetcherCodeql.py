import os
import requests
import json
from RepoAnalyzer import RepoFilter

class RepoFetcherCodeql(RepoFilter):
    def __init__(self, auth_token):
        super().__init__()
        self.auth_token = auth_token

    def downloadloadCodeqlDb(self, lang):

        lang_file = f'{self.localdir}/{lang}.zip'
        if os.path.exists(lang_file):
            print(f"{lang_file} exists..skipping download")
            return;

        headers = {
            'Authorization': f'Bearer {self.auth_token}',
            'Accept': 'application/zip'
        }

        session = requests.Session()
        with session.get(
                f'https://api.github.com/repos/{self.owner}/{self.name}/code-scanning/codeql/databases/{lang}',
                stream=True, headers=headers) as r:
            r.raise_for_status()
            with open(lang_file, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    f.write(chunk)

    def execute_impl(self):

        self.localdir = f'../data/codeqldb/{self.name}'
        os.makedirs(self.localdir,  exist_ok = True)

        headers = {
            'Authorization': f'Bearer {self.auth_token}',
            'Accept': 'application/vnd.github+json'
        }
        response = requests.get(
            f'https://api.github.com/repos/{self.owner}/{self.name}/code-scanning/codeql/databases',
            headers=headers)

        if response.status_code != 200:
            print(f'{self.owner}/{self.name}.. Failed {response.status_code} ')
            return
        res_dict = response.json()
        print(f'{self.owner}/{self.name}..{len(response.json())} scan(s)')
        print(json.dumps(response.json(), indent=4))
        languages = [x['language'] for x in res_dict]
        print(languages)

        # change the token for the purpose of downloading the file.
        headers['Accept'] = 'application/zip'

        for lang in languages:
            self.downloadloadCodeqlDb(lang)

