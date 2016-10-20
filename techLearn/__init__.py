import logging


def foo():
    print "I am foo"
    logging.info("foo is funning")


def use_logging(func):
    def wrapper(*args):
        logging.warn("%s is running" % func.__name__)
        return func(*args)
    return wrapper


@use_logging
def bar(a):
    print "I am bar, %s" % a

bar("kerry demo")