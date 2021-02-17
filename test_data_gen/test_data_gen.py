import numpy as np


class TestDataGenerator():

    @staticmethod
    def create_id_from_string(string):
        return abs(hash(string)) % (10 ** 8)

    @staticmethod
    def log_normal(mean):
        rng = np.random.default_rng()
        mu = 1.0  # mean
        sigma = 0.6  # standard deviation
        return round(float(rng.lognormal(mu, sigma, 1)[0] * mean), 2)

    @staticmethod
    def choose_log(list):
        ninety_nine_percentile = 4.6
        rng = np.random.default_rng()
        list_length = len(list)
        choice = int(round(rng.exponential(list_length/ninety_nine_percentile, 1)[0] - 0.5, 0))
        if choice >= list_length:
            item = 0
        else:
            item = choice
        return list[item]
