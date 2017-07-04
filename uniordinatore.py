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
>>>>>>> f26c0c467a4961fc593ee902b5b2332c07c1d400
