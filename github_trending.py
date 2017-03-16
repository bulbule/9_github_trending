import datetime
import requests


TOP_SIZE = 20
DAYS_AGO = 7


def get_starting_date(days_ago):
    today = datetime.date.today()
    starting_date = today - datetime.timedelta(days=days_ago)
    return starting_date


def get_trending_repositories(top_size):

    url = 'https://api.github.com/search/repositories'
    searching_params = {'q': 'created:>={}'.format(get_starting_date(DAYS_AGO)),
                        'sort': 'stars',
                        'per_page': top_size
                        }
    response = requests.get(url, searching_params).json()
    return response['items']


def print_repos(repos):
    for repo in repos:
        print(
            'Name: {}\nurl: {}\nOpen issues: {}\n'.format(
                repo['name'],
                repo['url'],
                repo['open_issues']))


if __name__ == '__main__':

    repos = get_trending_repositories(TOP_SIZE)
    print_repos(repos)
