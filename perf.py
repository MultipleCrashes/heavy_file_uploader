import time 

def timing(fn):
    def wraps(*args):
        t1 = time.time()
        result = fn(*args)
        t2 = time.time()
        time_diff = t2 - t1
        print "time diff -> ", time_diff 
        print "function name -> ", fn.func_name
        return  time_diff , fn.func_name
    return wraps

@timing
def computation():
    a = [x for x in range(1,10000)]
    sum = 0 
    for x in a:
        sum += x 
    print sum 

computation()
