# _*_ coding:utf-8 _*_
"""import time
import hashlib
import pickle
from itertools import chain
cache = {}

def is_obsolete(entry, duration):
    return time.time() - entry['time'] > duration

def compute_key(function, args, kw):
    key = pickle.dumps((function.func_name, args, kw))
    return hashlib.sha1(key).hexdigest()

def memoize(duration=10):
    def _memoize(function):
        def __memoize(*args, **kw):
            key = compute_key(function, args, kw)
            if(key in cache and not is_obsolete(cache[key], duration)):
                print 'we got a winner'
                return cache[key]['value']

            result = function(*args, **kw)
            cache[key] = {'value': result, 'time': time.time()}
            return result
        return __memoize
    return _memoize

@memoize()
def very_very_complex_stuff(a, b):
    return a + b
print very_very_complex_stuff(2, 2)

very_very_complex_stuff(2, 2)
"""

class DistinctError(Exception):
    pass

class distinctdict(dict):
    def __setitem__(self, key, value):
        try:
            value_index = self.values().index(value)
            # 只要dict在两次调用之间没有发生改变
            # keys()和values()将返回相应的列表
            # 否则，dict类型无法保证序列的顺序
            existing_key = self.keys()[value_index]
            if existing_key != key:
                raise DistinctError(("This value already exists for '%s'") % str(self[existing_key]))
        except ValueError:
            pass
        super(distinctdict, self).__setitem__(key, value)

my = distinctdict()
my['key'] = 'value'
my['other_key'] = 'value2'
print my
