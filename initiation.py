# Initiation Code
import datetime
from time import time

def alert(txt):
    timeS = datetime.datetime.now().strftime("%X")
    print("%s: %s" % (timeS,txt))

times = [time()]

alert("Rendering Graphs")

exec(open('covid/graphs.py').read())

alert("Graphs rendered in %.3f" % (time()-times[-1]))

times.append(time())
alert("Rendering Table")

exec(open('covid/covidTable.py').read())

alert("Table rendered in %.3f" % (time()-times[-1]))

times.append(time())
alert("Rendering Main png")

exec(open('covid/main.py').read())

alert("Main png rendered in %.3f" % (time()-times[-1]))
alert('total render time: %.3f' % (time()-times[0]))
