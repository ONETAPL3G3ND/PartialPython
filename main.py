from functools import partial

def multi(a, b):
    return a * b

if __name__ == "__main__":
    double = partial(multi, 2)
    print(double(3))