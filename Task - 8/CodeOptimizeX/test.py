from profiler.profiler import run_with_profiler, profile_function


def helper_fast():
    return sum(range(100_000))

def helper_slow():
    return sum(range(800_000))

def slow_function():
    a = helper_fast()
    b = helper_slow()
    return a + b


# Method 1: Direct call
if __name__ == "__main__":
    run_with_profiler(slow_function)