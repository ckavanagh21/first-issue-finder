import requests, math
from requests.exceptions import RequestException, ConnectionError, Timeout, TooManyRedirects
from tqdm import tqdm

def search_good_first_issues(languages):
    try:
        url = 'https://api.github.com/search/issues'

        languages = languages.split()
        language_query = ' '.join([f'language:{lang}' for lang in languages])

        params = {
            'q': f'label:"good first issue" {language_query} state:open',
            'sort': 'created',
            'order': 'desc'
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            issues = data['items']
            return issues

    except Timeout:
        print('Error - The request timed out.')
    except ConnectionError:
        print('Error - Connection error! Check your internet.')
    except TooManyRedirects:
        print('Too many redirects.')
    except RequestException as err:
        print(f"Request error: {err}")
    except Exception as err:
        print(f'Unexpected error: {err}')

    return []


# 🔥 NEW FUNCTION (your contribution)
def get_issue_details(issue):
    repo_name = issue['repository_url'].split('/')[-1]
    title = issue['title']
    url = issue['html_url']

    tqdm.write(f"📦 Repo: {repo_name}")
    tqdm.write(f"📝 Title: {title}")
    tqdm.write(f"🔗 Link: {url}")
    tqdm.write("-" * 50)


# 🔹 INPUT
languages = input("What languages are you looking to contribute in? Please separate using spaces.\n")

# 🔹 FETCH LINKS
print("\nSearching for open good first issues...")
issue_links = search_good_first_issues(languages)
print("\nSearch complete. Printing")

# 🔹 DISPLAY RESULTS (UPDATED)
for issue in tqdm(issue_links, desc="Fetching issues"):
    get_issue_details(issue)

counter = len(issue_links)
print(f'\nTotal issues found: {counter}')