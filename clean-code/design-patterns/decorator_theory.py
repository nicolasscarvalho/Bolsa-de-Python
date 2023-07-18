#=============================================
# Primeiro caso: Uma modificação adicional

def my_function():
    print('Done something...')

def decorator(function):

    print('Processing something...')
    function()
    print('Processing other thing...')

decorator(my_function)

#=============================================
# Segundo caso: Duas duas modificações adicionais

def my_function():
    print('Done something...')

def decorator_one(function):

    print('Processing something from decorator_one...')
    function()
    print('Processing other thing from decorator_one...')

def decorator_two(function):
    print('Processing something from decorator_two...')
    function()
    print('Processing other thing from decorator_two...')

# TypeError: 'NoneType' object is not callable
#decorator_one(decorator_two(my_function))

#=============================================
# Primeiro caso: Uma modificação, um decorator

def decorator(function):

    def wrapper():
        print('Processing something...')
        return function()
        print('Processing other thing...')

    return wrapper


@decorator
def my_function():
    print('Done something')


my_function()

#=============================================
# Primeiro caso: Uma modificação, dois decorators

def decorator_one(function):

    def wrapper():
        print('Processing something from decorator_one...')
        function()
        print('Processing other thing from decorator_one...')

    return wrapper


def decorator_two(function):

    def wrapper():
        print('Processing something from decorator_two...')
        function()
        print('Processing other thing from decorator_two...')

    return wrapper


@decorator_one
@decorator_two
def my_function():
    print('Done something...')


my_function()