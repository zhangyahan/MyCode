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

lst = []
for i in range(1,10):
    t = MyThread(inner,args=(i,))
    lst.append(t)
    t.start()

with open("./num.txt",'a') as f:
    for i in lst:
        i.join()
        f.write(i.get_result())







