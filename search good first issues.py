import requests
from requests.exceptions import RequestException, ConnectionError, Timeout, TooManyRedirects

def search_good_first_issues(languages):
    try:
        # GitHub API endpoint for searching issues
        url = 'https://api.github.com/search/issues'

        # Split languages into a list of strings
        languages = languages.split()
        language_query = ' '.join([f'language:{lang}' for lang in languages])

        # Parameters for the search query
        params = {
            'q': f'label:"good first issue" {language_query}',
            'sort': 'created',
            'order': 'desc'
        }

        # Send GET request to the GitHub API
        response = requests.get(url, params=params)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Extract the relevant information
            issues = data['items']
            issue_links = [issue['html_url'] for issue in issues]

        # Return the list of issue links
            return issue_links

    except Timeout as err:
        print('Error - The request timed out.')
    except ConnectionError as err:
        print('Error - Connection error! Make sure you are connected to the internet.')
    # Too many redirects is when the url points to 1 url which points back to the first url, meaning
    # it's stuck in a loop. Eventually your browser gives up and displays the 'too many redirects' error
    except TooManyRedirects as err:
        print('Too many redirects. Check the url or website configuration.')
    except RequestException as err:
        print(f"An error occurred during the request: {err}")
    except Exception as err:
        print(f'An unexpected error occurred: {err}')

    # If the request was not successful return an empty list
    return []

# Ask what languages you want to search for, saves as a string
languages = input("What languages are you looking to contribute in? Please separate using spaces.\n")
# Call the function to retrieve the issue links
issue_links = search_good_first_issues(languages)

# Print the links
# Displays the number of links printed
counter = 0
for link in issue_links:
    counter += 1
    print(link)
print(f'Number of links: {counter}')