import os
import sys
import time

# 多进程
def inner():
    time.sleep(3)
    print("我是耳机紫禁城")


def father():
    time.sleep(1)
    print("我是父进程")


pid = os.fork()

if pid == 0:
    pid1 = os.fork()
    if pid1 == 0:
        inner()
    else:
        sys.exit("紫禁城脱出")
else:
    father()
    os.wait()