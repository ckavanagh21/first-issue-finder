import requests
from requests.exceptions import RequestException, ConnectionError, Timeout, TooManyRedirects


def search_good_first_issues(languages):
    try:
        url = 'https://api.github.com/search/issues'

        languages = languages.split()
        language_query = ' '.join([f'language:{lang}' for lang in languages])

        params = {
            'q': f'label:"good first issue" {language_query}',
            'sort': 'created',
            'order': 'desc'
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            issues = data['items']
            issue_links = [issue['html_url'] for issue in issues]
            return issue_links

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
def get_issue_details(url):
    try:
        api_url = url.replace("https://github.com/", "https://api.github.com/repos/")

        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()

            repo_name = data['repository_url'].split('/')[-1]
            title = data['title']

            print(f"\n📦 Repo: {repo_name}")
            print(f"📝 Title: {title}")
            print(f"🔗 Link: {url}")
            print("-" * 50)

        else:
            print(url)

    except Exception:
        print(url)


# 🔹 INPUT
languages = input("What languages are you looking to contribute in? Please separate using spaces.\n")

# 🔹 FETCH LINKS
issue_links = search_good_first_issues(languages)

# 🔹 DISPLAY RESULTS (UPDATED)
counter = 0
for link in issue_links:
    counter += 1
    get_issue_details(link)

print(f'\nTotal issues found: {counter}')