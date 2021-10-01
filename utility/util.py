def cal_score(num_stars: int, num_forks: int) -> int:
    """
    :param num_stars: The number of starts of github repository
    :param num_forks: The number of forks of github repository
    :return: The score of this github repository based on following algorithm:
        score = num_stars * 1 + num_forks * 2
    """
    return num_stars * 1 + num_forks * 2


