"""
class A(object):
    x = 1
    gen = (lambda x:(x for _ in xrange(10)))(x)

if __name__ == "__main__":
    print(list(A.gen))

import time
class Timeit(object):
    def __init__(self, func):
        self._wrapped = func
    def __call__(self, *args, **kws):
        start_time = time.time()
        result = self._wrapped(*args, **kws)
        print "elapsed time is %s" % (time.time() - start_time)
        return result

@Timeit
def func():
    time.sleep(1)
    return "invoking function func"

class A(object):
    @Timeit
    def func(self):
        time.sleep(1)
        return 'invoking method func'

if __name__ == "__main__":
    a = A()
    a.func()



class Grade(object):
    def __init__(self):
        self._score = 0

    def __get__(self, instance, owner):
        return self._score

    def __set__(self, instance, value):
        if 0<= value <= 100:
            self._score = value
        else:
            raise ValueError('grade must be between 0 and 100')

class Exam(object):
    math = Grade()
    def __init__(self, math):
        self.math = math

if __name__ == '__main__':
    niche = Exam(math=90)
    print(niche.math)
    snake = Exam(math=75)
    print(snake.math)
    snake.math = 120
    print(snake.math)


class lnit(object):
    def __init__(self, value):
        self.val = value

class Add2(lnit):
    def __init__(self, val):
        super(Add2, self).__init__(val)
        self.val += 2

class Mul5(lnit):
    def __init__(self, val):
        super(Mul5, self).__init__(val)
        self.val *= 5

class Pro(Mul5, Add2):
    pass

class llncr(Pro):
    csup = super(Pro)
    def __init__(self, val):
        self.csup.__init__(val)
        self.val += 1

p = lncr(5)
print(p.val)

class P1(object):
    def foo(self):
        print 'called P1-foo()'

class P2(object):
    def foo(self):
        print 'called P2-foo()'

    def bar(self):
        print 'called P2-bar()'

class C1(P1, P2):
    pass

class C2(P1, P2):
    def bar(self):
        print 'called C2-bar()'

class GC(C1, C2):
    pass

gc = GC()
gc.foo()
gc.bar()
C2.bar(gc)
print GC.mro()
"""
import time
class Timeit(object):
    def __init__(self, func):
        self._wrapped = func
    def __call__(self, *args, **kws):
        start_time = time.clock()
        result = self._wrapped(*args, **kws)
        print "elapsed time is %.8f" % (time.clock() - start_time)
        return result

l1 = [1, 2, 3, 4, 5, 6]
l2 = [1, 2, 3, 4, 5, 6]
@Timeit
def func():
    count = 0
    while count < len(l1):
        print l1[count]
        count += 1

@Timeit
def func2():
    global l2
    while l2:
        print l2[0]
        l2 = l2[1:]

@Timeit
def func3():
    time.sleep(1)

if __name__ == "__main__":
    func()
    func2()
    print l2
    func3()





