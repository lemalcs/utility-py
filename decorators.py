from datetime import datetime 

# Get the elapsed time when executing a function
def get_execution_time(func):
    # Accept any number of parameters with `*args`
    # Accept any number of named parameters witn `**kwargs`
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        end_time = datetime.now()
        elapsed_time = end_time - initial_time
        print("Time elapsed: " + str(elapsed_time.total_seconds()) + " seconds.")

    return wrapper

# Add `execution_time` decorator to get the time elapsed in seconds
@get_execution_time
def random_func():
    for _ in range(0, 100000000):
        pass

@get_execution_time
def sum(a: int, b: int):
    return a + b

@get_execution_time
def greeting(name):
    print("Hello " + name)

random_func()
sum(23,88)
greeting("You")