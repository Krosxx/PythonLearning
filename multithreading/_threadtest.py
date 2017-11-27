# Python3 线程中常用的两个模块为：
# _thread
# threading(推荐使用)
import _thread
import time
count=0
def print_time( threadName, delay):
    while True:
        global count
        time.sleep(delay)
        count+=1
        print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

try:
   th1=_thread.start_new_thread( print_time, ("Thread-1", 0.1) )
   th2=_thread.start_new_thread( print_time, ("Thread-2", 1) )
except:
   print ("Error: 无法启动线程")

while count<10:
    pass