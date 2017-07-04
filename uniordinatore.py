<<<<<<< HEAD
import sys

def readstream(stream):
    r = stream.readline()
    if r == '':
        r = sys.maxsize
        stream.close()
    return int(r)
    
def uniordinatore(stream1 = 'stream1', stream2 = 'stream2', stream3 = 'stream3'):
    try:
        stream = [open(stream1), open(stream2), open(stream3)]
    except FileNotFoundError as exc:
        print(exc)
        return -1

    val = [readstream(stream[0]), readstream(stream[1]), readstream(stream[2])]

    while not (stream[0].closed and stream[1].closed and stream[2].closed):
        m = min(val)
        print(m)
        m = val.index(m)
        val[m] = readstream(stream[m])

if __name__ == '__main__':
    while len(sys.argv) < 4:
        sys.argv.append("stream" + str(len(sys.argv)))
    uniordinatore(sys.argv[1],sys.argv[2],sys.argv[3])
=======
import sys
while len(sys.argv)<4: sys.argv.append("stream"+str(len(sys.argv)))
stream1=open(sys.argv[1],"rb")
stream2=open(sys.argv[2],"rb")
stream3=open(sys.argv[3],"rb")
a=stream1.readline()
if a==b'': stream1.close()
else: a=int(a)
b=stream2.readline()
if b==b'': stream2.close()
else: b=int(b)
c=stream3.readline()
if c==b'': stream3.close()
else: c=int(c)
while not stream1.closed and not stream2.closed and not stream3.closed:
    if a<=b and a<=c:
        print(a)
        a=stream1.readline()
        if a==b'': stream1.close()
        else: a=int(a)
    elif b<=a and b<=c:
        print(b)
        b=stream2.readline()
        if b==b'': stream2.close()
        else: b=int(b)
    else:
        print(c)
        c=stream3.readline()
        if c==b'': stream3.close()
        else: c=int(c)
while not stream2.closed and not stream3.closed:
    if b<=c:
        print(b)
        b=stream2.readline()
        if b==b'': stream2.close()
        else: b=int(b)
    else:
        print(c)
        c=stream3.readline()
        if c==b'': stream3.close()
        else: c=int(c)
while not stream1.closed and not stream3.closed:
    if a<=c:
        print(a)
        a=stream1.readline()
        if a==b'': stream1.close()
        else: a=int(a)
    else:
        print(c)
        c=stream3.readline()
        if c==b'': stream3.close()
        else: c=int(c)
while not stream1.closed and not stream2.closed:
    if a<=b:
        print(a)
        a=stream1.readline()
        if a==b'': stream1.close()
        else: a=int(a)
    else:
        print(b)
        b=stream2.readline()
        if b==b'': stream2.close()
        else: b=int(b)
if not stream1.closed:
    print(a)
    for a in stream1: print(int(a))
elif not stream2.closed:
    print(b)
    for b in stream2: print(int(b))
else:
    print(c)
    for c in stream3: print(int(c))
>>>>>>> f26c0c467a4961fc593ee902b5b2332c07c1d400
