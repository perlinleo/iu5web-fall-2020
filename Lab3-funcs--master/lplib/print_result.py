def print_result(func):
    def wrapper(*arg):
        print(func.__name__)
        a = func(*arg)
        if type(a) == list:
            for i in a:
                print(i)
        elif type(a) == dict:
            for key in a:
                print(key, ' = ' , a[key])
        else:
             print(a)
        return a
    return wrapper



if __name__ == '__main__':
    @print_result
    def test_1():
        return 1


    @print_result
    def test_2():
        return 'iu5'


    @print_result
    def test_3():
        return {'a': 1, 'b': 2}


    @print_result
    def test_4():
        return [1, 2]

    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()