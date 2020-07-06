import random
import string

import mylib
import mylib_cython

# Pure Python function
def count_doubles(val) -> int:
    total = 0
    for c1, c2 in zip(val, val[1:]):
        if c1 == c2:
            total += 1
    return total


# generate 1M of random letters to test it
val = ''.join(random.choice(string.ascii_letters) for i in range(1000000))

def test_pure_python(benchmark):
    benchmark(count_doubles, val)

def test_cython(benchmark):
    benchmark(mylib_cython.count_doubles, val)

def test_rust(benchmark):
    benchmark(mylib.count_doubles, val)
