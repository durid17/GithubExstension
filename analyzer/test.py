from fetching import Fetcher
import sys
sys.path.append("./PyGithub");
from github import Github
import json
import getpass


username = input("Github Username: ")
password = getpass.getpass()
account = Github(username, password)
repo_name = input("Name of Repository: ")
repository = None
for repo in account.get_user().get_repos():
        if repo.name == repo_name:
            repository = repo

fetcher = Fetcher(repository)
contributors = fetcher.get_contributors()
print(contributors)