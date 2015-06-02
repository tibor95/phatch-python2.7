# Phatch - Photo Batch Processor
# Copyright (C) 2007-2008 www.stani.be
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
# along with this program.  If not, see http://www.gnu.org/licenses/
#
# Phatch recommends SPE (http://pythonide.stani.be) for editing python files.
#
# Follows PEP8

# Embedded icon is taken from www.openclipart.org (public domain)

from core import models
from lib.reverse_translation import _t
from lib.imtools import auto_crop

#---PIL


def init():
    global Image, ImageOps
    import Image
    import ImageOps


def crop(image, mode=None, all=0, left=0, right=0, top=0, bottom=0):
    if mode == _t('Auto'):
        image = auto_crop(image)
    elif mode == _t('All'):
        image = ImageOps.crop(image, border=all)
    else:
        w, h = image.size
        box = (
            left,
            top,
            w - right,
            h - bottom)
        image = image.crop(box)
    return image


#---Phatch


class Action(models.CropMixin, models.Action):
    label = _t('Crop')
    author = 'Nadia Alramli'
    email = 'mail@nadiana.com'
    init = staticmethod(init)
    pil = staticmethod(crop)
    version = '0.1'
    tags = [_t('transform'), _t('size')]
    __doc__ = _t('Crop the image')

    icon = \
'x\xda\x01\x0f\t\xf0\xf6\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x000\x00\
\x00\x000\x08\x06\x00\x00\x00W\x02\xf9\x87\x00\x00\x00\x04sBIT\x08\x08\x08\
\x08|\x08d\x88\x00\x00\x08\xc6IDATh\x81\xed\x99ml[\xd5\x19\xc7\xff\xe7\x9c{\
\xaf}\xed&\xae\xed\xd4I\x1cRX\x1a\x9a\x86\xb5\xa1*[\xd3\x97\xa1\x82B\xb5}\
\xd9\x97\xbd|\xa1b\x13\xe2\x03SU6\xd1M\xac\x03M\x8c\x82\x04\x88\xa1U\x9b\xd4\
\x15\xb5\xa2\xbc\x08\xb4\xb4\xd3\x18]\xa0\xdb\x8a\nk\xd3\xb2\x90\xa2TaDj\x8b\
\x1d\x9a8ql\xc7\x8d\x13\xfb\xbe\xf9\xde{\xce>\\\x07\x15\xd6\xb4I!\t\x93\xf8}\
\xb1\xe4{\xef\xd1\xffy\xces\x9e\xf3\xbf\xe7\x02_\xf1\xc5p\xe8\xd0\xa1pggg\
\xeb\\\x9f\xa3\xf3!f\xae\xbc\xfa\xea\xab\x9b\x1d\xc7\xf9\xd8q\x9c\x9b\xe7\
\xfa\xec\xa2\x07\xf0\xd2K/5\x9b\xa6y\xd4q\x9cg\xb7m\xdbv\xa4\xa2i\xd6\xba\
\xc8\xfcI\xbb6===\xd1|>\xff\xef\xc6\xc6\xc6\x8bk\xd6\xac\xb9\x0b\x80\x04@\
\x06`\x03p\x16S\xdb5)\x97\xcb\x91K\x97.\xf5MLLd\x85\x10\xcb\xe1\t\x0f\x02\
\xf0\xcde\x1ci^\xd4]\x83\xc9\xc9I\x9fa\x18\xcfs\xce\xd7\n!\xee!\x84\xa4\x00T\
\xc1\xcb\xbc\xb5\x18\x9a\xe6D.\x97;\x90N\xa7\xc5\xe8\xe8\xe8\xd3\x95\xbf\xc2\
\x00B\x00\xd8\\\xc7Z\xf0\x19\x18\x19\x19\xf9\xbd\xae\xeb\xf7\xd9\xb6\xdd}\
\xe0\xc0\x81\xc7\x01D\x01\x08\x00\x1a\x00w\xae\xe3-\xe8"N&\x93\xf7\xbb\xae\
\xfbG\xdb\xb6\xcdt:}WGG\xc7yxY\x9f\x04`^\xcf\x98\x0b6\x03\xe7\xce\x9d\xbb\
\xd70\x8c}\xb6mcbbbGGG\xc7\x00\x80\x00\x80"\xaeS<\xb0@3\xd0\xdf\xdf\x7f\x07\
\xe7\xfcX\xb9\\\x96\x0c\xc3xy\xcb\x96-\xdb)\xa5a\xcey\t@\x01^\t]\x17\xf3>\
\x03g\xce\x9ci6\x0c\xe3/\xae\xebJ\x96e\r\xbf\xf8\xe2\x8b\xcf\x00\x88p\xceM\
\x00S\xf8\x1c\xe2\x81y\x0e\xa0\xbb\xbb\xbb\xce4\xcd~\xd7uU\xc7q\xd0\xdb\xdb\
\xfb\xe0\x0b/\xbc0\x9d\xf1I\xccb\xd1\xee\xdb\xb7\x8fp\xce\x19!D&\x84\x84\x85\
\x107\x01\xc8\x0e\r\r\r>\xf9\xe4\x93\xee\xbc\x05p\xf2\xe4\xc9\xaar\xb9\xfcw\
\xd7uU\xd7u\x91J\xa5\x1e\xdf\xb5k\xd7)B\x88*\x84\xc8a\x86~\x7f\xf0\xe0A\xc9\
\xb2\xac\x9b\x85\x10\xab\x00\xdc$\x84h%\x84\xb4\x11BV\t!B\xb6m\x1b\xa5Ri`xxx\
/\x80\xa3\xf3\x16\x80\xa6i\xc7\x85\x10\xb7r\xceQ(\x14\xdey\xf4\xd1G\x0f\x01\
\xa8\x16Bd\x01\x94\xa6\xef{\xee\xb9\xe7\x96\n!\xd6q\xce\xbfK\x08\xd9d\x9a\
\xe6\nx;\xb2\x04@"\x84\xc0\xb2\xacT:\x9d\xfe\xdb\xd9\xb3g\xff\xd5\xd3\xd3s\
\xce\xb2\xac)]\xd73\x00&f\\\xc4\xb2,+\x84\x90F\xc6\x185\x0c\xe3\xc2l\x85wuu\
\xc9\x9c\xf3?\x01\xf8\x9e\x10\x02\xba\xaeO\xbe\xf9\xe6\x9bw\xe7\xf3\xf9\xe2\
\x86\r\x1b\xd4\x15+V,1Ms\xa5m\xdb\x1b\x85\x10\xedB\x88ZB<\x19\x84\x10p\xce\
\x1d\xdb\xb63\x86a\\\xcc\xe5r}\xa7O\x9f>\xfe\xee\xbb\xef&\x00L\x000\x18cE\
\xd7u?\xe9ZW\x0c \x16\x8b\xfd4\x9f\xcf? \xcb\xb2-I\x92!IR\xb2P(\xfcp6\x01\
\x1c>|\xf8YJ\xe9N!\x84(\x97\xcb$\x1a\x8d\xa6\x00L\x9a\xa6\x195\x0c\xa3Z\xd7\
\xf5\x80eY\x10B\x80\x10\x82i\xf1\xa5R\xa9\x7fll\xec\x9d\xb3g\xcf\xbe?::\x9a\
\x1b\x18\x18\x18\x050\x0e\xaf\xcd\x1a\x84\x10G\x08\xf1?\x0b\xfeS\x01\xac^\
\xbdz\xa5,\xcb\xc7.\\\xb8\x00\xd34\xb7;\x8e\xf3\xc6\xd2\xa5K\x99$I\x17(\xa5\
\xa7}>\xdf\x03\x8c1U\x92\xa4\xe5\x8c\xb1\r\x92$\xc5B\xa1\xd0\x89\x1d;v\x8c\
\x06\x83\xc1u~\xbf\x7fk>\x9f\xbf\x9bR\n\xce9TU\x15\xa1P\x88\x14\x8bEh\x9a\
\x06]\xd7a\xdb68\xe7\x16\xe7|\xd2\xb2\xac\xa1d2\xd9\xf5\xdak\xaf\x9dH\xa7\
\xd39x\x0et\xba\xb5j\x98E\x87\xfad\r\xd4\xd5\xd5m\xd6u\xfd\xaf\x99L\xe6uM\
\xd3\xee\x87\xd7!\x82\x85B\xc1\x89\xc5b\x1fH\x92\xb4\x8d\x10\xf2\x1dJ\xa9L)\
\xad\xa6\xd4\xb3\xec+W\xae\xfc\xd5\xb2e\xcb\x10\x0e\x87\x91H$PWW\'2\x99\x0c8\
\xe7\xf0\xfb\xfd\xa4P(@\xd34\x94J\xa5\xe2\xd4\xd4T\xff\xf8\xf8xO*\x95:\xff\
\xde{\xef}\x94H$R\x00\x8c\x8aX\x03\xde\xc2\x9e\x93\x9d\x90\x00 \x10\x08\xdc\
\xe2\xba\xee\x1b\xc9d\xb2O\x96\xe5\x9f\xc0\xb3\xb6\xd5\x00\x9ch4\xba\x841\
\xb6\x921\x06\xc6X\x841F\x18c\x90$\t\x94R\xd1\xda\xda\xfa\xd1\x9a5kn\xee\xea\
\xeaBCC\x03\xb2\xd9,\xb1m[\x84B!Q,\x16K###\'\xfb\xfa\xfa\x8e\x1c9rd\xa0P(h\
\x00\xca\xf0\xfa\xffT%\xdb\x9f\xcb\xf7\x13\x00\x92,\xcb\xdd\x8e\xe34\x13B\
\x1a8\xe7\x1c\x80\xac\xaajTU\xd5o\xca\xb2\xbc]\x96\xe5\x0eUU\xa1(\n(\xa5\x10\
Bp\xc6\xd8\x90\x10\xa2/\x99L>\xbdg\xcf\x9enUU%\xc6\x98 \x84\xf0\xa1\xa1\xa1\
\x97\xcf\x9f?\x7fb\xff\xfe\xfd\xfd\xf0j\xd8\x01\xa0_\x96\xe9/\xeceE\x02p\x93\
\xe38\xed\x92$\xfd\xc7\xb6m\xae(\xca\xb7eY\xbe7\x10\x08\xdc\x1e\x8dF#555LQ\
\x14X\x96U\xd04\xed\x94\xa6ioMLL\xf4\x99\xa6\xa9i\x9aVnoo\x0fp\xce%\x9f\xcf\
\'(\xa5$\x95J\x9dx\xe4\x91G\xf6\x97\xcb\xe5K\x00r\x95\x00l|\xce\x1dw&\x08\
\x00H\x92\x94\x0f\x87\xc3\x91H$\x82H$\x82\x9a\x9a\x1aTWW\xa7,\xcbJd2\x99S\
\x83\x83\x83\xc7S\xa9\xd4Ex\xa6\xcbWy\xae\x0c/\x9b\xb9\xbd{\xf7\xfev\xd9\xb2\
e?\xd7u=\xbf{\xf7\xeem\x89Db\x04@\x12^\xd6\xe7\x15\t\x00\x84\x10\xdf\xaf\xaf\
\xaf\x7f\xa8\xa5\xa5\x85\x16\x8b\xc5\xdeL&\xd3\xdb\xdb\xdb\x9b\x1e\x1b\x1b\
\x1b\x87\xf7\x82-*\x82Mx\xfd\xb8\xac(\x8aS.\x97\x05\x00\xa8\xaaJ4M\xc3\xe1\
\xc3\x87\x1fL$\x12Y\x00\xc3\x0b!\x1e\xf8t\x1b\xf5\x03XZ\xf9e\xf0\xba\x81U\
\x11b\xe0\ne\xb0i\xd3\xa6\x1f\xcb\xb2\xbc\xf3\xc6\x1bol\xa3\x94\xbe\xdd\xd9\
\xd9\xf9\x1b\xc30>\x020\xba\x10\xe2\x81O\x9b\xb92*\x9bFEl\x19^\x10W\xac\xdd\
\xf6\xf6\xf6_\x08!\x9eq\x1c\x07\xd9l\x16\xa6in\x0c\x87\xc35\x86a\x0c\xc2K\
\xcc\xbc\xd4\xfcg\xb9<\x00\x0e\xafK\\\x93\xdbn\xbb\xedv\xce\xf9c\x84\x10\xa8\
\xaa*\x08!\xee\xf0\xf0\xf0\xafGGGS\xf0\\\xe6\x82\x88\x07\xae\xc3N\xb7\xb5\
\xb5E\\\xd7}\x9e\x10\x12 \x84\x80RJ\x86\x86\x86\xf6%\x12\x89\xb7\x00|\x0c\
\xaf\xbf/\x18s>\x99\x13Bt\t!\x9a]\xd7\x15~\xbf\x1f\x85B\xe1\xd4\x87\x1f~\xf8\
g\x00#\xf0,\xc0\x822\xa7\x00Z[[\x9f\xe0\x9co\x14B\x08I\x92@\x08\xb1\x86\x87\
\x87;\x01d\xe0\x19\xaf\x05g\xd6%\xd4\xdc\xdc|\xa7\xeb\xba\xbb\x08!p]\x97(\
\x8a\x02]\xd7\xb3\xb9\\\xee\x1c\x80\x14\x16\xb0\xee/gV3\xb0|\xf9\xf2zB\xc8\
\xf1\xaa\xaa*6\xedh)\xa5\xd0u}\xd8q\x9c1\xccr\xf1\xcf\x07\xd7\x0c\xa0\xaa\
\xaa*\x14\x0c\x06\x8f666BQ\x14T\x02\x10\x84\x10\xd8\xb6]\x82\xb7\xb9-J\xf6\
\x81Y\x94P}}\xfdc\xb1X\xec\xd6\x8b\x17/\xda\x86a\x1c\xf4\xf9|,\x18\x0c\xdeW\
\tD\x9d\x7f\x89W\xe7\xaa\x01\xd4\xd6\xd6\xfe(\x1c\x0e\xfflpp05>>\xfe\xb0\xae\
\xeb\xff\x00\x90mkk[!\x84\xb8\x83\x10"\xe3:\x8e\x03\xbfHf,!I\x92\xbe\xb5n\
\xdd\xba}ccc\xf9l6\xfb\xb0\xae\xeb\xff\x94$)\x07\x00\xae\xeb\xfa\\\xd7\x85m\
\xdbyx\xbb\xf7\x97\x0bUUC\xeb\xd7\xaf\x1fhjjr\x03\x81\xc0/\x01\xd4M_\x8b\xc7\
\xe3_kii\x11\xabV\xad\x12\xb1X\xec!,r\x19]q\x06\xea\xeb\xeb_\x99\x9a\x9aj\
\xcdd2\xbf\xd3u\xfd\x15Jif\xfa\x9a\xdf\xef\xff\x83\xdf\xef\x87\xe38\xd9l6\
\xfb:<\xef\xf4\xe5\xa1\xb6\xb6\xf6\x89\xb6\xb66\xe1\xf7\xfb\xdf\x06\xb0\x16\
\x979\xd6P(\xb4\xb1\xa3\xa3\x83755\x89X,\xb6\x13\x8b\xf4\x81dF\x96,Y\xb21\
\x1e\x8f[\xaa\xaa\x1a\x8a\xa2\xfc\x00\x9e\xb5\x9e&\xb8e\xcb\x96ck\xd7\xae\
\x15\r\r\r\xdd\xb2,\xd7.\x96\xce\x19\t\x04\x02\xdd\xc1`P(\x8a\xb2\x07\xde\
\x87\x87i\xe4x<\xbe{\xeb\xd6\xad\xe2\x86\x1bn\xd0\x02\x81\xc0\xd7\x17K\xe3\
\xd5\x08\xcb\xb2,\x14E\xc9\x03X\x0f\xefdB\x06\xd0\x10\x89D\x9e\xda\xbcy\xb3h\
nn\x9e\n\x87\xc3w,\xaa\xca\xab\xf0\rB\x88`\x8ce\x01\xdc\t\xe0\x16\xc6\xd8=\
\xf1x\xfc\xfd\x96\x96\x16\x11\x8f\xc7\'\xbf\xcc\xe2\x01\x00\x84\x90\t\xc6\
\x98P\x14%\xef\xf7\xfb\xd3\xa1PH\xd4\xd6\xd6fC\xa1\xd0S\x8b\xadm&>{6\xdaD)\
\xbd\x871\x16e\x8ce(\xa5\x1f\xd8\xb6\xddm\xdb\xf6\xa5EQ\xf7\x15\xff\x07\xfc\
\x17\tF\x13\xe0\x81\x7f;\x1a\x00\x00\x00\x00IEND\xaeB`\x82[\t[T'
