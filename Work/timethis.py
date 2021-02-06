# timethis.py
#
# Exercise 7.10
import time

def timethis(func):
    """
    함수를 수행하는 데 얼마나 시간이 걸리는지 출력하는 데코레이터 함수
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        try:
            return func(*args, **kwargs)
        finally:
            end = time.time()
            print('%s.%s: %f' % (func.__module__, func.__name__, end - start))
    return wrapper

if __name__ == '__main__':
    @timethis
    def countdown(n):
        while n > 0:
            n -= 1

    countdown(1000000)