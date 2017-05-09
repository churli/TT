import atexit
from time import clock

def secondsToStr(t):
    return "%d:%02d:%02d.%03d" % \
        reduce(lambda ll,b : divmod(ll[0],b) + ll[1:],
            [(t*1000,),1000,60,60])

line = "="*40
def log(s, elapsed=None, previous=None):
    curtime = clock()
    #print line
    if previous:
        print secondsToStr(curtime), '-', s, '-', "Timediff from event at ", secondsToStr(previous), " = ", secondsToStr(curtime-previous)
        return curtime, secondsToStr(curtime-previous)
    elif elapsed:
        print secondsToStr(curtime), '-', s, '-', "Elapsed time", " = ", secondsToStr(curtime-elapsed)
        return curtime, secondsToStr(curtime-elapsed)
    else:
        print secondsToStr(curtime), '-', s
    #print line
    #print
    return curtime

def endlog():
    end = clock()
    elapsed = start
    log("End Program", elapsed)

def now():
    return secondsToStr(clock())

start = clock()
atexit.register(endlog)
log("Start Program")
