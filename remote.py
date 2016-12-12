#!/usr/bin/env python

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from util import push

BUTTONS = [
    {'label': 'POWER',   'key': 'KEY_POWEROFF',     'x': 0, 'y': 0,  'w': 4, 'h': 1},
    {'label': 'SOURCE',  'key': 'KEY_SOURCE',       'x': 8, 'y': 0,  'w': 4, 'h': 1},
    {'label': '1',       'key': 'KEY_1',            'x': 0, 'y': 1,  'w': 4, 'h': 1},
    {'label': '2',       'key': 'KEY_2',            'x': 4, 'y': 1,  'w': 4, 'h': 1},
    {'label': '3',       'key': 'KEY_3',            'x': 8, 'y': 1,  'w': 4, 'h': 1},
    {'label': '4',       'key': 'KEY_4',            'x': 0, 'y': 2,  'w': 4, 'h': 1},
    {'label': '5',       'key': 'KEY_5',            'x': 4, 'y': 2,  'w': 4, 'h': 1},
    {'label': '6',       'key': 'KEY_6',            'x': 8, 'y': 2,  'w': 4, 'h': 1},
    {'label': '7',       'key': 'KEY_7',            'x': 0, 'y': 3,  'w': 4, 'h': 1},
    {'label': '8',       'key': 'KEY_8',            'x': 4, 'y': 3,  'w': 4, 'h': 1},
    {'label': '9',       'key': 'KEY_9',            'x': 8, 'y': 3,  'w': 4, 'h': 1},
    {'label': 'TTX/MIX', 'key': 'KEY_TTX_MIX',      'x': 0, 'y': 4,  'w': 4, 'h': 1},
    {'label': '0',       'key': 'KEY_0',            'x': 4, 'y': 4,  'w': 4, 'h': 1},
    {'label': 'PRE-CH',  'key': 'KEY_PRECH',        'x': 8, 'y': 4,  'w': 4, 'h': 1},
    {'label': 'VOL +',   'key': 'KEY_VOLUP',        'x': 0, 'y': 5,  'w': 4, 'h': 1},
    {'label': 'MUTE',    'key': 'KEY_MUTE',         'x': 4, 'y': 5,  'w': 4, 'h': 1},
    {'label': 'CH +',    'key': 'KEY_CHUP',         'x': 8, 'y': 5,  'w': 4, 'h': 1},
    {'label': 'VOL -',   'key': 'KEY_VOLDOWN',      'x': 0, 'y': 6,  'w': 4, 'h': 1},
    {'label': 'CHLIST',  'key': 'KEY_CH_LIST',      'x': 4, 'y': 6,  'w': 4, 'h': 1},
    {'label': 'CH -',    'key': 'KEY_CHDOWN',       'x': 8, 'y': 6,  'w': 4, 'h': 1},
    {'label': 'MEDIA P', 'key': 'KEY_W_LINK',       'x': 0, 'y': 6,  'w': 4, 'h': 1},
    {'label': 'MENU',    'key': 'KEY_MENU',         'x': 4, 'y': 6,  'w': 4, 'h': 1},
    {'label': 'GUIDE',   'key': 'KEY_GUIDE',        'x': 8, 'y': 6,  'w': 4, 'h': 1},
    {'label': 'TOOLS',   'key': 'KEY_TOOLS',        'x': 0, 'y': 7,  'w': 4, 'h': 1},
    {'label': 'UP',      'key': 'KEY_UP',           'x': 4, 'y': 7,  'w': 4, 'h': 1},
    {'label': 'INFO',    'key': 'KEY_INFO',         'x': 8, 'y': 7,  'w': 4, 'h': 1},
    {'label': 'LEFT',    'key': 'KEY_LEFT',         'x': 0, 'y': 8,  'w': 4, 'h': 1},
    {'label': 'ENTER',   'key': 'KEY_ENTER',        'x': 4, 'y': 8,  'w': 4, 'h': 1},
    {'label': 'RIGHT',   'key': 'KEY_RIGHT',        'x': 8, 'y': 8,  'w': 4, 'h': 1},
    {'label': 'RETURN',  'key': 'KEY_RETURN',       'x': 0, 'y': 9,  'w': 4, 'h': 1},
    {'label': 'DOWN',    'key': 'KEY_DOWN',         'x': 4, 'y': 9,  'w': 4, 'h': 1},
    {'label': 'EXIT',    'key': 'KEY_EXIT',         'x': 8, 'y': 9,  'w': 4, 'h': 1},
    {'label': 'A',       'key': 'KEY_RED',          'x': 0, 'y': 10, 'w': 3, 'h': 1},
    {'label': 'B',       'key': 'KEY_GREEN',        'x': 3, 'y': 10, 'w': 3, 'h': 1},
    {'label': 'C',       'key': 'KEY_YELLOW',       'x': 6, 'y': 10, 'w': 3, 'h': 1},
    {'label': 'D',       'key': 'KEY_CYAN',         'x': 9, 'y': 10, 'w': 3, 'h': 1},
    {'label': 'P MODE',  'key': 'KEY_PMODE',        'x': 0, 'y': 11, 'w': 4, 'h': 1},
    {'label': 'S MODE',  'key': 'KEY_STB_MODE',     'x': 4, 'y': 11, 'w': 4, 'h': 1},
    {'label': 'DUAL',    'key': 'KEY_DUAL',         'x': 8, 'y': 11, 'w': 4, 'h': 1},
    {'label': 'AD',      'key': 'KEY_AD',           'x': 0, 'y': 12, 'w': 4, 'h': 1},
    {'label': 'P SIZE',  'key': 'KEY_PICTURE_SIZE', 'x': 4, 'y': 12, 'w': 4, 'h': 1},
    {'label': 'SUBT',    'key': 'KEY_SUBT',         'x': 8, 'y': 12, 'w': 4, 'h': 1},
    {'label': 'REWIND',  'key': 'KEY_REWIND',       'x': 0, 'y': 13, 'w': 4, 'h': 1},
    {'label': 'PAUSE',   'key': 'KEY_PAUSE',        'x': 4, 'y': 13, 'w': 4, 'h': 1},
    {'label': 'FORWARD', 'key': 'KEY_FF',           'x': 8, 'y': 13, 'w': 4, 'h': 1},
    {'label': 'RECORD',  'key': 'KEY_REC',          'x': 0, 'y': 14, 'w': 4, 'h': 1},
    {'label': 'PLAY',    'key': 'KEY_PLAY',         'x': 4, 'y': 14, 'w': 4, 'h': 1},
    {'label': 'STOP',    'key': 'KEY_STOP',         'x': 8, 'y': 14, 'w': 4, 'h': 1}
]

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Remote")
        self.set_resizable(False)

        grid = Gtk.Grid()
        grid.set_column_spacing(6)
        grid.set_row_spacing(6)
        self.add(grid)

        for button in BUTTONS:
            btn = Gtk.Button(label=button['label'])
            btn.connect('clicked', self.on_click, button['key'])
            grid.attach(btn, button['x'], button['y'], button['w'], button['h'])

    def on_click(self, object, key):
        print 'Pushing %s' % key
        push(key);

win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
