from typing import Optional

import pytest
from fastapi.testclient import TestClient

import settings
from main import app
from utility.exception import InvalidToken, RepoIsNotExist, EmptyToken
from utility.github_api import GitHubAPI

client = TestClient(app)


@pytest.fixture(scope='class')
def github_api():
    return GitHubAPI(token=settings.GITHUB_ACCESS_TOKEN)


@pytest.fixture(scope='class')
def python_repo(github_api):
    return github_api.get_repo('python/cpython')


class TestGitHubAPI:
    """
    Test GitHubAPI class
    """

    def test_empty_token(self):
        with pytest.raises(EmptyToken):
            # noinspection PyTypeChecker
            GitHubAPI(token=None)

    def test_invalid_token(self):
        g = GitHubAPI(token='invalid_token')
        with pytest.raises(InvalidToken):
            g.get_repo('python/cpython')

    def test_invalid_repo(self, github_api):
        with pytest.raises(RepoIsNotExist):
            github_api.get_repo('invalid_repo/not_exist')


class TestRepository:
    """
    Test Repository class
    """

    def test_get_repo(self, python_repo):
        assert python_repo.name == 'cpython'
        assert python_repo.full_name == 'python/cpython'

    def test_forks(self, python_repo):
        # @Note: because forks dynamically increase over the time
        assert python_repo.forks >= 20259

    def test_stars(self, python_repo):
        # @Note: because stars dynamically increase over the time
        assert python_repo.stars >= 40454

    def test_score(self, python_repo):
        # @Note: because score dynamically increase over the time
        assert python_repo.score >= 80972
