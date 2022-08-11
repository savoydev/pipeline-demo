from django.test import TestCase
import time
# Create your tests here.
def func(x):
    return x + 1


def test_answer():
    time.sleep(5)
    assert func(3) == 4