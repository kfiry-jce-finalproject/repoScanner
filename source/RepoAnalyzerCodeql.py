import requests
import json


class RepoAnalyzerCodeql:
    def __init__(self):
        pass

    def analyze(self, repo_name, repo_owner):
        headers = {
            'Authorization': 'Bearer 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',
            'Accept': 'application/vnd.github+json'
        }
        response = requests.get(f'https://api.github.com/repos/{repo_owner}/{repo_name}/code-scanning/codeql/databases',
                                headers=headers)

        if response.status_code != 200:
            print(f'{repo_owner}/{repo_name}.. Failed')
            return
        res_dict = response.json()
        print(f'{repo_owner}/{repo_name}..{len(response.json())} scan(s)')
        print(json.dumps(response.json(), indent=4))
        languages = [x['language'] for x in res_dict]
        print(languages)

        headers = {
            'Authorization': 'Bearer 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',
            'Accept': 'application/zip'
        }

        for lang in languages :
            session = requests.Session()
            local_file = f'../data/codeqldb/{repo_name}_{lang}.zip'
            with session.get(
                    f'https://api.github.com/repos/{repo_owner}/{repo_name}/code-scanning/codeql/databases/{lang}',
                    stream=True, headers=headers) as r:
                r.raise_for_status()
                with open(local_file, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=1024):
                        f.write(chunk)
