import redis
from redis_lru import RedisLRU

client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)


@cache
def f(x):
    y = x**2
    return y


if __name__ == '__main__':
    f(3)
    f(3)
