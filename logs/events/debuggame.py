current_id = 0


def write_packet(data):
    global current_id
    open('packets/%s.dat' % current_id, 'wb').write(str(data))
    current_id += 1


def open_debug_log(file_name='debug.log'):
    DebugLog.filehandle = open(file_name, 'w')


def get_refcounts():
    d = {}
    import sys
    from pyspades import types
    # collect all classes
    for m in list(sys.modules.values()):
        for sym in dir(m):
            o = getattr(m, sym)
            if type(o) is type:
                d[o] = sys.getrefcount(o)
    # sort by refcount
    pairs = [(x[1], x[0]) for x in list(d.items())]
    pairs.sort()
    pairs.reverse()
    return pairs


def print_top_100():
    if DebugLog.filehandle:
        DebugLog.filehandle.write('***Reference counts\n')
        for n, c in get_refcounts()[:100]:
            DebugLog.filehandle.write('%10d %s\n' % (n, c.__name__))
        DebugLog.filehandle.flush()


def debug_csv_line(listdata):
    if DebugLog.filehandle:
        DebugLog.filehandle.write(','.join(map(str, listdata)))
        DebugLog.filehandle.write('\n')
        DebugLog.filehandle.flush()


class DebugLog:
    filehandle = None
