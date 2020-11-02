
def main():
   
    class cm_timer (object):
        def __init__(self):
                print('__init__')

        def __enter__(self):
                self.start = time.time()
                return self
        def __exit__(self, type, value, traceback):
                self.end = time.time()
                print('time: ',self.end-self.start)
                return True  


    with cm_timer() as cm_object:
            for i in range(1000):
                print(i)
   
   

if __name__ == '__main__':
    main()
