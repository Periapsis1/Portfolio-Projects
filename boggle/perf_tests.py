from this import d
import timeit

def set_intersection(number=1000000):
    print('set_intersection: ', end='')
    def f():
        a = {1, 2, 3, 4, 5}
        b = {3, 4, 5, 6, 7, 8}
        c = a & b

    print(timeit.timeit(f, number=number))

def list_intersection(number=1000000):
    print('list_intersection: ', end='')
    def f():
        a = [1, 2, 3, 4, 5]
        b = [3, 4, 5, 6, 7, 8]
        c = [e for e in a if e in b]
    
    print(timeit.timeit(f, number=number))

def set_in_dict_intersection(number=1000000):
    print('set_in_dict_intersection: ', end='')
    def f():
        d = {
            'a':{1, 2, 3, 4, 5},
            'b':{3, 4, 5, 6, 7, 8}
        }
        a = d['a'] & d['b'] | d.get('c',dict())


def list_in_dict_intersection(number=1000000):
    print('list_in_dict_intersection: ', end='')
    def f():
        d = {
            'a':[1, 2, 3, 4, 5],
            'b':[3, 4, 5, 6, 7, 8]
        }

set_intersection(1000000)
list_intersection(1000000)


