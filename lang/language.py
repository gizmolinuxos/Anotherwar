
from .bytes import ByteReader, ByteWriter

MAGIC = 'STR0'

# for reference
FORMATS = [
    None,
    '',
    '%s',
    '%s %s',
    '%i',
    '%i %i %i',
    '%i %s',
    '%s %i',
    '%u'
]

class Entry(object):
    value = None
    type = None
    def __init__(self, value, type):
        self.value = value
        self.type = type
    
    def format(self, *arg):
        return self.value % arg

class LanguageFile(object):
    items = None
    def __init__(self, reader = None):
        self.items = []
        if reader is None:
            return
        if reader.read(4) != MAGIC:
            raise NotImplementedError('invalid magic')
        count = reader.readInt(True, False) - 1
        for _ in xrange(count):
            header = reader.readInt(True, False)
            end = reader.tell()
            off = header & 0x00FFFFFF
            type = header >> 24
            reader.seek(off)
            value = reader.readString()
            reader.seek(end)
            self.items.append(Entry(value, type))
    
    def write(self, reader):
        reader.write(MAGIC)
        size = len(self.items)
        start = 8 + size * 4
        reader.writeInt(size + 1, True, False)
        values = ByteWriter()
        for index, item in enumerate(self.items):
            value_offset = values.tell()
            values.writeString(item.value)
            offset = value_offset + start
            reader.writeInt(offset | (item.type << 24), True, False)
        reader.write(str(values))
    
    def generate(self):
        reader = ByteWriter()
        self.write(reader)
        return reader
