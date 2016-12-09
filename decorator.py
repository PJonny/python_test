"""
def deco(func):
    def _deco(a, b):
        print("before myfunc() called.")
        ret = func(a, b)
        print("after myfunc() called. result: %s" % ret)
        return ret
    return _deco

@deco
def myfunc(a, b):
    print("myfunc(%s, %s) called." % (a, b))
    return a + b


def deco(func):
    def _deco(*args, **kwargs):
        print("before %s called." % func.__name__)
        ret = func(*args, **kwargs)
        print("after %s called. result: %s" % (func.__name__, ret))
        return ret
    return _deco

@deco
def myfunc(a, b):
    print("myfunc(%s, %s) called." % (a, b))
    return a+b

@deco
def myfunc2(a, b, c):
    print("myfunc2(%s, %s, %s) called." % (a, b,c))
    return a+b+c

myfunc2(1, 2, 3)

def deco(arg):
    def _deco(func):
        def __deco():
            print("before %s called [%s]." % (func.__name__, arg))
            func()
            print("after %s called [%s]." % (func.__name__, arg))
        return __deco
    return _deco

@deco("mymodoule")
def myfunc():
    print("myfunc() called.")


@deco("module2")
def myfunc2():
    print("myfunc2() called.")

myfunc()
myfunc2()


class locker:
    def __init__(self):
        print("locker.__init__() should be not called.")

    @staticmethod
    def acquire():
        print("locker.acquire() called.-->This is static method")

    @staticmethod
    def release():
        print("locker.release() called.-->")

def deco(cls):
    def _deco(func):
        def __deco():
            print("before %s called [%s]." % (func.__name__, cls))
            cls.acquire()
            try:
                return func()
            finally:
                cls.release()
        return __deco
    return _deco

@deco(locker)
def myfunc():
    print("myfunc() called.")

myfunc()
"""
class mylocker:
    def __init__(self):
        print("mylocker.__init__() called.")

    @staticmethod
    def acquire():
        print("mylocker.acquire() called.")

    @staticmethod
    def unlock():
        print("mylocker.unlock() called.")

class lockerex(mylocker):
    @staticmethod
    def acquire():
        print("lockerex.acquire() called.")

    @staticmethod
    def unlock():
        print("lockerex.unlock() called.")

def lockhelper(cls):
    def _deco(func):
        def __deco(*args, **kwargs):
            print("before %s called." % func.__name__)
            cls.acquire()
            try:
                return func(*args, ** kwargs)
            finally:
                cls.unlock()
        return __deco
    return _deco

class example:
    @lockhelper(mylocker)
    def myfunc(self):
        print("myfunc() called.")

    @lockhelper(mylocker)
    @lockhelper(lockerex)
    def myfunc2(self, a, b):
        print(" myfunc2() called.")
        return a+b

a = example()
a.myfunc()
print(a.myfunc())
print(a.myfunc2(1, 2))
print(a.myfunc2(3, 4))
kk