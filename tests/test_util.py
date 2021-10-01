from fastapi.testclient import TestClient

from main import app
from utility.util import cal_score

client = TestClient(app)


def test_cal_score():
    """
        Test `cal_score` util function
    """
    score = cal_score(num_stars=100, num_forks=200)
    assert score == 500
