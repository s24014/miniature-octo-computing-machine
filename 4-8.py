def show_how_it_works(func):
    def my_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('keyword arguments:', kwargs)
        print('Result:', result)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return my_function

def add_two_numbers(a, b)
    return a + b

add_two_numbers(1, 8)

decolated_func = show_how_it_work(add_two_numbers)
decolated_func(1, 8)
