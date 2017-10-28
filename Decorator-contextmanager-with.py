# https://realpython.com/blog/python/primer-on-python-decorators/
# https://jeffknupp.com/blog/2016/03/07/python-with-context-managers/
# http://preshing.com/20110920/the-python-with-statement-by-example/

################################################################

# 1. Decorator

##  Put simply, decorators wrap a function, modifying its behavior. ##

def my_decorator(some_function):
    def wrapper():
        print("Something is happening before some_function() is called.")
        some_function()
        print("Something is happening after some_function() is called.")
    return wrapper

## Use case 1:
def just_some_function():
    print("Wheee!")
just_some_function = my_decorator(just_some_function)

## Use case 2:
@my_decorator
def just_some_function():
    print("Wheee!")

just_some_function()

#################################################################

# 2. ContextManager


## Use case 1: Define __enter__ and __exit__
## Implementing the Context Manager as a Class
class File():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
    def __enter__(self):
        self.open_file = open(self.filename, self.mode)
        return self.open_file
    def __exit__(self, *args):
        self.open_file.close()

with File('foo.txt', 'w') as infile:
    infile.write('foo')

## Use Decorator , without __enter__ and __exit__ function
## Implementing the Context Manager as a Generator
@contextmanager
def open_file(path, mode):
    the_file = open(path, mode)  # __enter__
    yield the_file
    the_file.close()             # __exit__

# better ?
@contextmanager
def open_file(path, mode):
    the_file = open(path, mode)      # __enter__
    try:
        yield the_file
    finally:
        the_file.close()             # __exit__

with open_file('foo.txt', 'w') as infile:
    files.append(infile)

## Use case 3: ContextDecorator (Mix of above 2?)
class makeparagraph(ContextDecorator):
    def __enter__(self):
        print('<p>')
        return self
    def __exit__(self, *exc):
        print('</p>')
        return False
##
@makeparagraph()
def emit_html():
    print('Here is some non-HTML')
emit_html()

##
with makeparagraph() as m:
    print('Here is some non-HTML')


########################################################################
# 3. With statement

with something_that_returns_a_context_manager() as my_resource:
    do_something(my_resource)
    ...
    print('done using my_resource')

## more details (Exceptions etc)
## http://preshing.com/20110920/the-python-with-statement-by-example/
