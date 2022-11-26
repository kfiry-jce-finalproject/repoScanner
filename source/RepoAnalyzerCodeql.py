import os

import requests
import json


class RepoAnalyzerCodeql:
    def __init__(self, auth_token):
        self.auth_token = auth_token

    def analyze(self, repo_name, repo_owner, ):
        headers = {
            'Authorization': f'Bearer {self.auth_token}',
            'Accept': 'application/vnd.github+json'
        }
        response = requests.get(f'https://api.github.com/repos/{repo_owner}/{repo_name}/code-scanning/codeql/databases',
                                headers=headers)

        if response.status_code != 200:
            print(f'{repo_owner}/{repo_name}.. Failed {response.status_code} ')
            return
        res_dict = response.json()
        print(f'{repo_owner}/{repo_name}..{len(response.json())} scan(s)')
        print(json.dumps(response.json(), indent=4))
        languages = [x['language'] for x in res_dict]
        print(languages)

        # change the token for the purpose of downloading the file.
        headers['Accept'] = 'application/zip'

        for lang in languages:
            if os.path.exists(f'../data/codeqldb/{lang}') == False:
                os.mkdir(f'../data/codeqldb/{lang}')

            session = requests.Session()
            local_file = f'../data/codeqldb/{lang}/{repo_name}.zip'
            with session.get(
                    f'https://api.github.com/repos/{repo_owner}/{repo_name}/code-scanning/codeql/databases/{lang}',
                    stream=True, headers=headers) as r:
                r.raise_for_status()
                with open(local_file, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=1024):
                        f.write(chunk)
