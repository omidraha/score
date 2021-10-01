import github.GithubException
from github import Github

from utility.exception import RepoIsNotExist, InvalidToken, EmptyToken
from utility.util import cal_score


class GitHubAPI:
    """
        This class use to communicate with GitHub API service
        @todo: make an universal interface API to communicate with other svc services such as gitlab, bitbucket
    """

    def __init__(self, token: str):
        self.repo = None
        if token is None:
            raise EmptyToken
        self.token = token
        self.github = Github(login_or_token=token)

    def get_repo(self, repo: str):
        try:
            self.repo = Repository(repo=self.github.get_repo(repo))
        except github.BadCredentialsException:
            raise InvalidToken
        except github.UnknownObjectException:
            raise RepoIsNotExist
        else:
            return self.repo


class Repository:
    """
        The Repository class
    """

    def __init__(self, repo):
        self.repo = repo

    @property
    def name(self):
        return self.repo.name

    @property
    def full_name(self):
        return self.repo.full_name

    @property
    def forks(self):
        return self.repo.forks_count

    @property
    def stars(self):
        return self.repo.stargazers_count

    @property
    def score(self):
        return cal_score(num_forks=self.forks, num_stars=self.stars)
