from numpy.random import randint
import random
import time

class Random_Integer:
    @staticmethod
    def get_random_int(min, max):
        now = int(time.time())
        random.seed(now)
        range = 50
        values = randint(min, max, range)
        return values[0]


# print(Random_Integer.get_random_int(0, 20))
# print(Random_Integer.get_random_int(0, 20))
# print(Random_Integer.get_random_int(0, 20))
