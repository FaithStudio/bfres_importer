def unpack10bit(val):
    if type(val) in (list, tuple):
        val = val[0] # grumble grumble struct is butts
    res = []
    for i in range(3):
        s = (val >> (i*10)) & 0x200
        v = (val >> (i*10)) & 0x1FF
        if s: v = -v
        res.append(v / 511)
    return res


typeRanges = { # name: (min, max)
    'b': (       -128,        127),
    'B': (          0,        255),
    'h': (     -32768,      32767),
    'H': (          0,      65535),
    'i': (-2147483648, 2147483647),
    'I': (          0, 4294967295),
}


# attribute format ID => struct fmt
# type IDs do NOT match up with gx2Enum.h (wrong version?)
attrFmts = {
    0x0201: {
        'fmt':   'B',   # struct fmt
        'ctype': 'int', # type name for eg Collada file
        'name':  'u8',  # for debug display
    },
    0x0901: {
        'fmt':   '2B',
        'ctype': 'int',
        'name':  'u8[2]',
    },
    0x0B01: {
        'fmt':   '4B',
        'ctype': 'int',
        'name':  'u8[4]',
    },
    0x1201: {
        'fmt':   '2H',
        'ctype': 'int',
        'name':  'u16[2]',
    },
    0x1501: {
        'fmt':   '2h',
        'ctype': 'int',
        'name':  'u16[2]',
    },
    0x1701: {
        'fmt':   '2i',
        'ctype': 'int',
        'name':  's32[2]',
    },
    0x1801: {
        'fmt':   '3i',
        'ctype': 'int',
        'name':  's32[3]',
    },
    0x0B02: {
        'fmt':   '4B',
        'ctype': 'int',
        'name':  'u8[4]',
    },
    0x0E02: {
        'fmt':   'I',
        'ctype': 'float',
        'name':  '10bit',
        'func':  unpack10bit,
    },
    0x1202: {
        'fmt':   '2h',
        'ctype': 'int',
        'name':  's16[2]',
    },
    0x0203: {
        'fmt':   'B',
        'ctype': 'int',
        'name':  'u8',
    },
    0x0903: {
        'fmt':   '2B',
        'ctype': 'int',
        'name':  'u8[2]',
    },
    0x0B03: {
        'fmt':   '4B',
        'ctype': 'int',
        'name':  'u8[4]',
    },
    0x1205: {
        'fmt':   '2e',   # half float
        'ctype': 'float',
        'name':  'half[2]',
    },
    0x1505: {
        'fmt':   '4e',
        'ctype': 'float',
        'name':  'half[4]',
    },
    0x1705: {
        'fmt':   '2f',
        'ctype': 'float',
        'name':  'float[2]',
    },
    0x1805: {
        'fmt':   '3f',
        'ctype': 'float',
        'name':  'float[3]',
    },
}

for id, fmt in attrFmts.items():
    typ = fmt['fmt'][-1]
    if typ in typeRanges:
        if 'min' not in fmt: fmt['min'] = typeRanges[typ][0]
        if 'max' not in fmt: fmt['max'] = typeRanges[typ][1]
