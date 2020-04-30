# Initiation Code
import datetime
from time import time

def alert(txt):
    timeS = datetime.datetime.now().strftime("%X")
    print("%s: %s" % (timeS,txt))

times = [time()]

alert("Rendering Graphs")

exec(open('/Users/nathanmihm/Math Graphics/covid/graphs.py').read())

alert("Graphs rendered in %.3f" % (time()-times[-1]))

times.append(time())
alert("Rendering Table")

exec(open('/Users/nathanmihm/Math Graphics/covid/covidTable.py').read())

alert("Table rendered in %.3f" % (time()-times[-1]))

times.append(time())
alert("Rendering Main png")

exec(open('/Users/nathanmihm/Math Graphics/covid/main.py').read())

alert("Main png rendered in %.3f" % (time()-times[-1]))
alert('total render time: %.3f' % (time()-times[0]))
