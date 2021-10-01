from fastapi.testclient import TestClient
from fastapi import status

from main import app
from utility.exception import RepoIsNotExist

client = TestClient(app)


class TestScoreView:
    """
        Test `score` view API
    """

    def test_score_api_valid_repo(self):
        """
            Test `score` API while repo is valid
        """
        response = client.post("/score/",
                               json={'repo': 'python/cpython', })

        assert response.status_code == status.HTTP_200_OK
        # @Note: because score dynamically increase over the time
        assert response.json()["score"] >= 80972
        assert response.json()["repo"] == 'python/cpython'

    def test_score_api_invalid_repo(self):
        """
            Test `score` API while repo is not valid
        """
        response = client.post("/score/",
                               json={'repo': 'invalid_repo/not_exist', })

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.json()["message"] == RepoIsNotExist.message
