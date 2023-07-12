import requests

def search_good_first_issues():
    # GitHub API endpoint for searching issues
    url = 'https://api.github.com/search/issues'

    # Parameters for the search query
    params = {
        'q': 'label:"good first issue"',
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

# Call the function to retrieve the issue links
issue_links = search_good_first_issues()

# Print the links
for link in issue_links:
    print(link)
