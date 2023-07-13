import requests

def search_good_first_issues(languages):
    # GitHub API endpoint for searching issues
    url = 'https://api.github.com/search/issues'

    languages = languages.split()
    for lang in languages: 
        print(lang)
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

    # If the request was not successful, print the status code and return an empty list
    print('Request failed with status code:', response.status_code)
    return []

languages = input("What languages are you looking to contribute in? Please separate using spaces.\n")
# Call the function to retrieve the issue links
issue_links = search_good_first_issues(languages)

# Print the links
for link in issue_links:
    print(link)
