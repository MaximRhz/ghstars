import requests
import argparse


def print_starred_repos(login):
    try:
        r = requests.get('https://api.github.com/users/{}/starred'.format(login))
    except requests.ConnectionError:
        print('Connection error')
        return
    if r.status_code == 404:
        print('User {} not found'.format(login))
        return
    request_json = r.json()
    if len(request_json) == 0:
        print('Account have no stars')
        return
    for repo in request_json:
        print(repo['name'], repo['stargazers_count'])


def get_from_console():
    parser = argparse.ArgumentParser()
    parser.add_argument("login",  help='a GitHub username')
    args = parser.parse_args()
    print_starred_repos(args.login)

