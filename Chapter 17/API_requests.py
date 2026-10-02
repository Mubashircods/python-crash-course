import requests


url =   "https://api.github.com/search/repositories?q=language:python+sort:stars+stars:>10000"
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url=url, headers=headers)
print(f"Status Code: {r.status_code}")

response_dict = r.json()
print(f"Totle repositories: {response_dict['total_count']}")
print(f"Complete result: {not response_dict['incomplete_results']}")