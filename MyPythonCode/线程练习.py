from threading import Thread


class MyThread(Thread):
    def __init__(self, func, args=()):
        super(MyThread, self).__init__()
        self.func = func
        self.args = args

    def run(self):
        self.result = self.func(*self.args)

    def get_result(self):
        try:
            return self.result
        except Exception:
            return None


def inner(num):
    return "I'm {}".format(num)

def inner2(num):
    return "I'm {}".format(num)


t = MyThread(inner,args=("123",))
t2 = MyThread(inner2,args=("435",))
t.start()
t2.start()
t.join()
print(t.get_result())
t2.join()
print(t2.get_result())




