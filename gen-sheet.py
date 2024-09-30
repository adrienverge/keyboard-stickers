#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2014-2016 Adrien Vergé
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from html import escape
import sys

from pysvg.builders import StyleBuilder
from pysvg.shape import Rect, Line
from pysvg.structure import Svg, Image
from pysvg.text import Text


assert sys.version_info[0] >= 3


if len(sys.argv) != 2:
    print('usage: %s OUTPUT' % sys.argv[0], file=sys.stderr)
    sys.exit(1)

OUTPUT_FILE = sys.argv[1]

DENSITY = 300 / 2.54 / 10  # 300 dpi in mm


class LabelType(object):
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy
        self.style = StyleBuilder()
        self.style.setFontFamily(fontfamily='Source Han Sans CN Bold')
        self.style.setFontSize('4.4em')
        self.style.setFilling(fill='white')
        self.style.setTextAnchor('middle')
        self.style.style_dict['dominant-baseline'] = 'middle'


types = {}

types['alphabet'] = LabelType(0.3, 0.5)
types['alphabet'].style.setFontSize('5.6em')

types['digits'] = LabelType(0.22, 0.87)

types['digitsshift'] = LabelType(0.22, 0.39)

types['altgr'] = LabelType(0.96, 0.87)
types['altgr'].style.setTextAnchor('end')
types['altgr'].style.setFilling(fill='#ff6666')
types['altgr'].style.setFontFamily(fontfamily='Verdana')

types['altgrshift'] = LabelType(0.96, 0.39)
types['altgrshift'].style.setTextAnchor('end')
types['altgrshift'].style.setFilling(fill='#ff6666')
types['altgrshift'].style.setFontFamily(fontfamily='Verdana')

types['fnkey'] = LabelType(0.5, 0.6)
types['fnkey'].style.setFontSize('2.8em')
types['fnkey'].style.setFilling(fill='#6699ff')

types['specialkey'] = LabelType(0.5, 0.6)
types['specialkey'].style.setFontSize('3.0em')

types['symbol'] = LabelType(0.5, 0.7)
types['symbol'].style.setFontSize('5.5em')

types['symbolbig'] = LabelType(0.5, 0.75)
types['symbolbig'].style.setFontSize('7.0em')

types['symbolbig'] = LabelType(0.5, 0.75)
types['symbolbig'].style.setFontSize('7.0em')


class Label(object):
    def __init__(self, string, type):
        self.string = string
        self.type = type


class Key(object):
    def __init__(self, *args):
        self.labels = args

    def __repr__(self):
        return ' '.join([l.string for l in self.labels])


KEYS = (
    #Key(Label('Q', 'alphabet')),
    #Key(Label('W', 'alphabet')),
    #Key(Label('E', 'alphabet')),
    #Key(Label('R', 'alphabet')),
    #Key(Label('T', 'alphabet')),
    #Key(Label('Y', 'alphabet')),
    Key(Label('~', 'digitsshift'),
        Label('`', 'digits')),
    Key(Label('!', 'digitsshift'), Label('¹', 'altgrshift'),
        Label('1', 'digits'), Label('¡', 'altgr')),
    Key(Label('@', 'digitsshift'),
        Label('2', 'digits'), Label('²', 'altgr')),
    Key(Label('#', 'digitsshift'),
        Label('3', 'digits'), Label('³', 'altgr')),
    Key(Label('$', 'digitsshift'), Label('£', 'altgrshift'),
        Label('4', 'digits'), Label('¤', 'altgr')),
    Key(Label('%', 'digitsshift'),
        Label('5', 'digits'), Label('€', 'altgr')),
    Key(Label('^', 'digitsshift'),
        Label('6', 'digits'), Label('¼', 'altgr')),
    Key(Label('&', 'digitsshift'),
        Label('7', 'digits'), Label('½', 'altgr'), Label('7', 'fnkey')),
    Key(Label('*', 'digitsshift'),
        Label('8', 'digits'), Label('¾', 'altgr'), Label('8', 'fnkey')),
    Key(Label('(', 'digitsshift'),
        Label('9', 'digits'), Label('‘', 'altgr'), Label('9', 'fnkey')),
    Key(Label(')', 'digitsshift'),
        Label('0', 'digits'), Label('’', 'altgr'), Label('/', 'fnkey')),
    Key(Label('_', 'digitsshift'),
        Label('-', 'digits'), Label('¥', 'altgr')),
    Key(Label('+', 'digitsshift'), Label('÷', 'altgrshift'),
        Label('=', 'digits'), Label('×', 'altgr')),
    Key(Label('{', 'digitsshift'), Label('“', 'altgrshift'),
        Label('[', 'digits'), Label('«', 'altgr')),
    Key(Label('}', 'digitsshift'), Label('”', 'altgrshift'),
        Label(']', 'digits'), Label('»', 'altgr')),
    Key(Label(':', 'digitsshift'), Label('°', 'altgrshift'),
        Label(';', 'digits'), Label('¶', 'altgr'), Label('-', 'fnkey')),
    Key(Label('"', 'digitsshift'), Label('¨', 'altgrshift'),
        Label('\'', 'digits'), Label('´', 'altgr')),
    Key(Label('|', 'digitsshift'), Label('¦', 'altgrshift'),
        Label('\\', 'digits'), Label('¬', 'altgr')),
    Key(Label('<', 'digitsshift'), Label('Ç', 'altgrshift'),
        Label(',', 'digits'), Label('ç', 'altgr')),
    Key(Label('>', 'digitsshift'),
        Label('.', 'digits'), Label('.', 'fnkey')),
    Key(Label('?', 'digitsshift'),
        Label('/', 'digits'), Label('¿', 'altgr'), Label('+', 'fnkey')),
    Key(Label('Suppr', 'specialkey')),
    Key(Label('Écran', 'specialkey')),
    Key(Label('Inser', 'specialkey')),
    Key(Label('Alt', 'specialkey')),
    Key(Label('Alt Gr', 'specialkey')),
    Key(Label('Ctrl', 'specialkey')),
    Key(Label('\u2328', 'symbol')),
    Key(Label('\u260E', 'symbolbig')),
    Key(Label('\u2301', 'symbolbig')),
    Key(Label('\u21DE', 'symbol')),
    Key(Label('\u21DF', 'symbol')),
    Key(Label('\u232B', 'symbol')),
    Key(Label('\u21E7', 'symbolbig')),
    Key(Label('\u21F1', 'symbol')),
    Key(Label('\u21F2', 'symbol')),
    Key(Label('\u2190', 'symbol')),
    Key(Label('\u2191', 'symbol')),
    Key(Label('\u2192', 'symbol')),
    Key(Label('\u2193', 'symbol')),
    Key(Label('vim.svg', 'image')),
    Key(),
)


class Keyboard(object):
    def __init__(self, inverted=False):
        self.w = 210 * DENSITY
        self.h = 297 * DENSITY
        self.svg = Svg("keyboard", width=self.w, height=self.h)

        if inverted:
            self.bg = "white"
        else:
            self.bg = "black"

    def draw_key(self, x, y, key):
        margin = 1 * DENSITY
        w = 11 * DENSITY
        h = 11 * DENSITY
        r = Rect(x - 0.8 * margin, y - 0.3 * margin,
                 w + 2 * 0.8 * margin, h + 2 * 0.3 * margin)
        r.set_fill(self.bg)
        self.svg.addElement(r)

        l = Line(x, y - 2 * margin, x, y + h + 2 * margin)
        l.set_stroke("black")
        l.set_stroke_width(0.3 * DENSITY)
        self.svg.addElement(l)
        l = Line(x + w, y - 2 * margin, x + w, y + h + 2 * margin)
        l.set_stroke("black")
        l.set_stroke_width(0.3 * DENSITY)
        self.svg.addElement(l)
        l = Line(x - 2 * margin, y, x + w + 2 * margin, y)
        l.set_stroke("black")
        l.set_stroke_width(0.3 * DENSITY)
        self.svg.addElement(l)
        l = Line(x - 2 * margin, y + h, x + w + 2 * margin, y + h)
        l.set_stroke("black")
        l.set_stroke_width(0.3 * DENSITY)
        self.svg.addElement(l)

        for label in reversed(key.labels):
            if label.type != 'image':
                type = types[label.type]
                t = Text(escape(label.string),
                         x + type.dx * w, y + type.dy * h)
                t.set_style(type.style.getStyle())
                self.svg.addElement(t)
            else:
                i = Image(x=x + 0.2 * w, y=y + 0.2 * h,
                          width=0.6 * w, height=0.6 * h)
                i.set_xlink_href(label.string)
                self.svg.addElement(i)

    def save(self, stream):
        self.svg.save(stream, encoding='utf-8')

# Définition des « cases » où imprimer une touche

cases = []

page_bordure = int(6 * DENSITY)
bordure = int(4.5 * DENSITY)
espace = int(13 * DENSITY)
groupe = int(210 / 3.0 * DENSITY)

colonnes = (set(range(page_bordure,
                      1 * groupe - int(2.5 * DENSITY),
                      espace)) |
            set(range(1 * groupe + bordure,
                      2 * groupe - bordure,
                      espace)) |
            set(range(2 * groupe + int(2.5 * DENSITY),
                      3 * groupe - page_bordure,
                      espace)))
colonnes = sorted(list(colonnes))

page_bordure = int(12 * DENSITY)
bordure = int(1 * DENSITY)
groupe = int(297 / 8.0 * DENSITY)
espace = int(12 * DENSITY)
rangees = (set(range(page_bordure, 1 * groupe - int(4.5 * DENSITY), espace)) |
           set(range(1 * groupe + bordure, 2 * groupe - bordure, espace)) |
           set(range(2 * groupe + bordure, 3 * groupe - bordure, espace)) |
           set(range(3 * groupe + bordure, 4 * groupe - bordure, espace)) |
           set(range(4 * groupe + bordure, 5 * groupe - bordure, espace)) |
           set(range(5 * groupe + bordure, 6 * groupe - bordure, espace)) |
           set(range(6 * groupe + bordure, 7 * groupe - bordure, espace)) |
           set(range(7 * groupe + bordure, 8 * groupe - bordure, espace)))
rangees = sorted(list(rangees))

for y in rangees:
    for x in colonnes:
        cases.append((x, y))

# Création de la feuille

kb = Keyboard(inverted=False)

for i in range(30):
    cases.pop(0)

for i in range(4):
    for k in KEYS:
        print(k)
        x, y = cases.pop(0)
        kb.draw_key(x, y, k)
    while len(cases) % 15 != 0 and len(cases) % 15 < 9:
        cases.pop(0)
    while len(cases) % 5 > 0:
        cases.pop(0)

kb.bg = 'white'
types['alphabet'].style.setFilling(fill='black')
types['digits'].style.setFilling(fill='black')
types['digitsshift'].style.setFilling(fill='black')
types['altgr'].style.setFilling(fill='#990000')
types['altgrshift'].style.setFilling(fill='#990000')
types['fnkey'].style.setFilling(fill='#336699')
types['specialkey'].style.setFilling(fill='black')
types['symbol'].style.setFilling(fill='black')
types['symbolbig'].style.setFilling(fill='black')

for i in range(3):
    for k in KEYS:
        print(k)
        x, y = cases.pop(0)
        kb.draw_key(x, y, k)
    while len(cases) % 15 != 0 and len(cases) % 15 < 9:
        cases.pop(0)
    while len(cases) % 5 > 0:
        cases.pop(0)

kb.save(OUTPUT_FILE)

print(len(KEYS))
