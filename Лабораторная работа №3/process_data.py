import sys
import json

from lplib.cm_timer import cm_timer
from lplib.print_result import print_result
from lplib.unique import Unique
from lplib.gen_random import gen_random
from lplib.field import field


path ="data_light.json"

with open(path) as f:
    data = json.load(f)


@print_result
def f1(arg):
    return sorted(Unique(field(arg,'job-name'),ignore_case=True))

@print_result
def f2(arg):
    return list(filter(lambda x: "программист" in x.lower(), arg))

@print_result
def f3(arg):
    return list(map(lambda x: x + " с опытом Python", arg))

def f4(arg):
    return dict(zip(arg, gen_random(len(arg), 100000, 200000)))
if __name__ == '__main__':
    with cm_timer():
        f4(f3(f2(f1(data)))) 