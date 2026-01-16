import cProfile
import sys

sys.setrecursionlimit(6000)


def heavy_factorial(n):

    if n == 0:
        return 1

    else:

        return n * heavy_factorial(n - 1)


def light_factorial(n):

    result = 1

    for i in range(1, n + 1):

        result *= i

    return result


def main():

    heavy_factorial(5000)
    light_factorial(5000)


if __name__ == "__main__":

    cProfile.run("main()", "factorial_profile.prof")
