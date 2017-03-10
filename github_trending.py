import datetime as DT
import requests

TOP_SIZE = 20
DAYS_AGO = 7


def starting_date(days_ago):
    today = DT.date.today()
    starting_date = today - DT.timedelta(days=days_ago)
    return starting_date


def get_trending_repositories(top_size):

    url = 'https://api.github.com/search/repositories'
    searching_params = {'q': 'created:>={}'.format(starting_date(DAYS_AGO)),
                        'sort': 'stars'
                        }
    response = requests.get(url, searching_params)
    return response.json()['items'][:top_size]


def get_open_issues_amount(repo_owner, repo_name):

    url = 'https://api.github.com/{}/{}/issues'.format(repo_owner, repo_name)
    response = requests.get(url)
    return len(response.json())


def print_repos(repos):
    for repo in repos:
        print(
            'Name:{}\nurl:{}\nOpen issues:{}\n'.format(
                repo['name'],
                repo['url'],
                get_open_issues_amount(
                    repo['owner'],
                    repo['name'])))


if __name__ == '__main__':

    repos = get_trending_repositories(TOP_SIZE)
    print_repos(repos)
