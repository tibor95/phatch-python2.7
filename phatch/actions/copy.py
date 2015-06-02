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

# Embedded icon is designed by Igor Kekeljevic (http://www.admiror-ns.co.yu).
#
# Follows PEP8


from core import ct, models
from lib.reverse_translation import _t

#no need to lazily import these as they are always imported
import os
import shutil


class Action(models.Action):
    """Defined variables: <filename> <type> <folder> <width> <height>"""

    label = _t('Copy')
    author = 'Stani'
    email = 'spe.stani.be@gmail.com'
    version = '0.1'
    tags = [_t('file')]
    __doc__ = _t('Copy the original image')
    valid_last = True

    def interface(self, fields):
        fields[_t('File Name')] = self.FileNameField(choices=self.FILENAMES)
        fields[_t('In')] = self.FolderField(self.DEFAULT_FOLDER,
                                        choices=self.FOLDERS)

    def apply(self, photo, setting, cache):
        #get info
        info = photo.info
        #get file values
        folder, filename, typ = self.is_done_info(info)
        if setting('overwrite_existing_images') \
                or not os.path.exists(filename):
            #ensure folder
            filename = self.ensure_path_or_desktop(folder, photo, filename)
            #do it
            shutil.copy2(info['path'], filename)
        return photo

    def is_done_info(self, info):
        folder = self.get_field('In', info)
        filename = self.get_field('File Name', info)
        typ = info['type']
        return folder, os.path.join(folder, '%s.%s' % (filename, typ)), typ

    def is_overwrite_existing_images_forced(self):
        """Force overwrite when copying in place."""
        return (self.get_field_string('In') == self.FOLDER) and\
            (self.get_field_string('File Name') == self.FILENAME)

    icon = \
'x\xda\x15\x97\x078\xd4\x7f\x1c\xc7\xef$\x9b\xb2"+\xe3H\xc8&\xc9J\x88\xcbv\
\xce\xc8\xea\x8c${D6eg\xaf\xecqIgvd\x9c\x8b\xec\xbd.\xc9\xdeI\xf8sY!\xeb\xff\
\xed\x9e\xe7\xee\xf7<\xbf\xe7\xf7\xfc\xbe\x9f\xef\xe7\xfd~\xbf>\xdf\x8b\xd1\
\xd7}HK\xc5F\x05\x81@h\xb54\xd5\x0c\xc1U\xfc\xdf\x97\x82\x0c\xfc\x9a\x90\x1c\
G\x81\x0b\xa9\x97\xaa\x16\x82\x02|\x02)\xec\xa2!\x10\xba(-\xb5\xfb\x08\xc7\
\xb0\xba\xac\x00g\x84Ip\x8f\xb2\xaf\x95\xef\xbc\xd8HG\xfe\xce\x9b\xa1\xd0\
\xf8x\x8fV\xbah\xfe\xafeZ\x88\xb4(n\x04{I\x0e\xc2x\xda\t\x8f\xf9d\xfc\xd8\
\xf8Y\x93\xf9-\x1dC~f\xf8\x03\x06&\xc2\x073\xcc\xa3\x9cw\xb4\x8f\x9a\x8c)\
\xa0hCU\xae\x9cp\xda\xc9n\xb9E(\xbbr$\xb6g\xe5\xfa\x8cmb\xcf\xde\xe7\x86\x90\
\xc9\x95\x04r[\xcdP>\xce\xf5y\x9c\x17\xf18x\x98\x18\x10\xfcE\xcaw\x91\xab\
\x8e\xefa\xc27NE\xff\xfd+\xdb\xe3{q:\x8d,W\\\x9e?\x0f\x98FaO\xe34\xd0\x04==\
\xbd\x1b\xb9\x05\x05\x17}U\x96x\xc3CT\x05\x9e\xca\xfd\xbfI\t\x034\xe1\xbf\
\x86\x99\xad\x902dy2\x8cR+\xe5m^\xdeVAV\xd6K\xd4\xdap^&\xf1\xa7\x9f;\x0bT\
\xe9l\x7fLF6gK*\xaa\x03\x0bUI\x81QE\xb43\xa8\xc9\xe7\xe5\x17\xe4\xe4\x9c\xec\
q\xde{\xc1\xd1\xf8\xd8\xb6\xdd\x92D.\xf8\xf4(U\xb7t/(\xae\xabX\x8cJ\x94\x89\
\xea\x11\xa4k%PIO(\xdd\xdf\x1a\x838\x9fzpE1\xad\x85\xddv\x81\xbe\x15\xe7\xb5\
\xf6MJJ\xea\xe2\xc7\x8e_\xb0P\xec2m\xb8\tI\x12,\xc6Y\xf6\xc4E6\'h\x17\xdb\
\xc3E=\x7f+t\xf9d\xde\xefG/}H\x91\xfe/s\xfc\x8b-\xbd:\xf3\xdb)0\x9e\x81]\x9d\
.\x16\xaa\xcbvf\x1a)\xb0P\x81\x08U\x8f?\x93X[\xe5\x16\xa3P"s\xd8JO"\xb1\xaa\
\xa2\xe2t\xd4\xa9\x8e-\x8e\xd7\x8d\xbf\xe5sfE\xf2\x19\xbcd\xd7\x8d+\xe4tgP\
\x91\\\xceg#\r\x9e\xb1zg\xce\xf5\xd0:\xbaX\xb0u\xb7\xcb\\\xd4"\xe5\x1d\xffL\
\x05\xcc*\xc3\x1ebg\xa6D~z\xce\xa8\xa7 \xe17\x02I\xe0\xb8\xbb\\g*R \x9f7\x8c\
\x8cP\xc5\xdaE\xa1\xc4\xe2[\xe1\xe2\xabk\xc2\x9f\x9e-\xea\xbd\xd8\x9a>\xe8\
\xb3$w\x04\xed\xedt\xaa;\x9fv\x96}lg\xf6~2\xae=n\xd9\xa4\xd6\xe8\xd67!\x9dk\
\xa4O\xac\xed\xedWG\x1a\x9c\xa7R\xf0\xb6\xa1\x0f\xa2\xe8nU"7\x95ME2\xbe0\xab\
\x1b\\%\r\xf3\x0c\xcd9\xf8\x1a\x81\xef\xafX\xa8\xc8\x83\x06\x7f~>Q\x95L\xa4u\
\xdf\xffE\x80\x1b0\x85\xd8\xca\xe6\xdc\xd0\x17\xbc\x96b\x8c92\x0c\xf5|k\xb8\
\xd4\xb5\xb9\x80\xee\xba|\xff\x08\x9dw\xcf\x97\xebl\x18\xd2\x93\xc0\x19`Z>~n\
^:v\x17\xaelMiS\xa79\x0bo\xe4\xa6\xa0\x08\xff\xe8m1}\x8d\x98iov\xfe0\xb5o\
\x7f\xf9_\xd7\xbf\xf0\xb7\nW\x7f.\x9e\xacw\x99yT,x\x9eg^i\x85\xe4C2Z\xd3a\
\xb3\x17\r\x97V\x97\x1f\xf1\xc4\xfe\x8e38\x9d^rW\xc0\x07\x9d\xfc)\xda}Z\xd6?\
|1\xb6\xeay6?8\xf8&id-S\xf1\x83E\xa0G\x06\x9ce\xd7\xa9\xdddc\xd5f\xf5\xb0\
\xb7\xe6\x8dy\xa5\xc3P\xb6\x8c2\xc7\xf5\xeb8\x12G\xe4e\xb9\xc0#w\x07\x14J\
\xd5\xef\xcf\xd4S-\x81T&\x1e$I#\xa75ux\xa8j\x91\xa9G\xb7I\xad\xde\xce\x94S]\
\xb6\xcf\xe6w\x8f\xd3#\x0f\xa5\xf3\xa3\x95\xdd>\xb2\xfez\x86\x14\xd8\x94\x86\
\x86\x86\xdf\xd9\xc1D\x9fC\xed/oyO\xdc\xac\xe1\xc8\xda\xde\x00\xd5h\xe5k\xe1\
t8\x13UWM\x15B\xc8\xed\x97pP\x8fC-=\x05\xe9$\xdeW\xac p\x972K\x9b\x0ciZ[\x02\
\t7\xaf|\x11\xa9\xca#\x99ECl9\x11mnn\x96\xe3H \xa6\xa9\xc3\xd5g\x13~\xa7\xab\
\x94\x95\x97C\xfd\xce\x8f\xd7\xd6\x89\xc4\x9b\xd7\xe2$\xa4\xa4\xf8.\xf5\xef\
\xee\xc0;\x8aE\x98\xa8\x8c6\'\xaaK\xab\xab\xaf4\xcc\xe8<~\xcc\xdef\x93TZ\x10\
\x9c\x8d\xc1`\x8c\xbd^\x12\x18\xd4\xe9\xd5\xdf\x1a\xb2W\xda\x95\xda\xa3\x10B\
\xa7\xc1\xca\xa5\xbay\xcb\x8bm\xaf4S:\x0f6\'0UU\x02\x05#\x03"\x15\xd0gX\xb1\
\xb8P\xc8\x07O\x9c\x85R:\xdc\xc0\xda\x1a\x98\x1d\xe5\xef\x9f\r\xc4\xdc\xf9\
\xfe\xd8\xadH_P\x9c-\xfe\x0e\xb3\xb5\xfcL8w\x85|\x87\xb0Oj\xdf\xeb\x915\xdb\
\x85\x96 \x0e\x05\xbf$oy\x1dA&TG$\xad \x13\xd5\xd7\xf5O\xa4\xbf\x06\xd0\xfa\
\n\xf4\x10\x17i6Ea\x8avb\xb6\xf6{*\xf0|\x9b\r7\x07\x1dz\xdc\xe9n\xc0\x1f\x11\
\xba\xa8W\xd3\xd3\xe6?\xd7\xd6L\x98C\xa4\xd8\xd3\x83\xad\xfe*\x82\xea\x95\n\
\xd6\xbaX\xac\xed\xbc\xbd\xd3\xfa\xfa\xb4j\xa6D6\xbfW\xda\xba\xba&8Jg7\xfb\
\xed,\x8fHe\r2s\xd3\xfe\x18\x802\x85\xb2\x8dv\xaf\xec$\xa8\xf1.\xd5\x9bWBK\
\x0cc\x16\x88O\xdd\xdd\xafV"\x07z{)RSS?\xd5\xd7\xa7\xe8\x96f:\x1b:\xc5\x8fwf\
\\\xc2 \x84@\xff\xee\x06\xfd\x95v\xfbr&;\xe5\x9cA \x18|\xb6\x12\xd3@\'{\xcb\
\x0f\x8d\x97\x9b\xac\xb0\x88Z\xf8\xf1\xa7\xf6\xe5\x92\xbf\x0f=N\x87\xc4\xf6\
\xb0\xa9|s\x94\x06\x08\xf0\xda\xfb\xef\xbf\n\\\xe3\x07\x87\xa7O\xfb\xec$\x7f\
x\xde\x15\xb5\xfa\xac\xf9\xfc\xb9p\xb1`\xca\xc8\x9a\xdb\xdb\xe3\xf4\xcf\xd6\
\\\xcc\xcdV\x89c\xebv\x17\xe7g\xb9r\x1e\xe1\xda\x02\x0f`\x0cE%%\x11v\x92ZB\
\xe9\xbc\x0c1?\x80\x0fB:WvD\xb9\xdb\xdb\x13dh\x99\xfa\xa1\xa4*d?\xd6\xf2\x03\
\\W\xb6\xe7\xf0\x0b\x15eee\x86\xe5\xe3\xfb\x87\x87|\xb1\xbc\xb29\xb4\xe5\xe3\
pA\xa6v\x14vtf&nf\x0bl2I\xb7\xd4\xed\xa3\xfaK\xb1f\x87\x86\x99\xbe\xb5\xbd\
\xcf\xbf\xdb\xa9\xbd\xbd\xbdE\xb6r667czV:W<\x98\xa8.\xb3\xdfqE\xd4\xd7\xd7\
\xbb\xce\xd7\xbb<\xae\xc0\xe3OBv\x8fOi\x92,\xbf5\xc1\x02\xd7\xfd\x80HnU\xd6_\
\xce\xab\x19b^\xa3\x9c\x9cb\x1d\xa5\xe1\xd2l%\xb5\xb5\xa9\xb1\xb1T"\xd7\xa8]\
\x1br\x86\x87u\x9d\x9c\x9c\xc4YiHI\xa0\\\xc1GO\xde\x97\x96f\x9a\x95I32C\x11B\
\xcc\xc6\xc6\xc6\xb9w\xbd"}\xe7_F\xe5\xbb_I5\xb9\xf9\xf2g\xd6\xd3\xdeU\xcfwc\
\xcf\xda\x97\xc4\x9f\x7f\xafh[\xd9Y\xf4\x96\xf7\x90\xe3@\x98\x98\xa0\'6m\xef\
\xbd\xf8\xef\x83y\xee\x19\x7f\xa8\xbd\xb0\x7f`\xe0i\xe2\xe6\xc6F\xf6\xa50H\
\x84*4\x1d\x1ea\x88\xe9Da\xaf\xc6ui\n\xa4~\x18w\xda\xd8\xd8`eg\xe7\xcb\x19"\
\x19]X\xd0\xf3\xf2\x92\x82\x970h\xa5 +j\xe4\xf3\xe8\x1af\x86\x02\x88\xcd=a\
\x89t\xee\x7fYJ\xb3|\x07W\x9a\x97\xbb\x96\xdc\x99X\x84\x87\x86\x86\x8e\x02\
\x95\x14\xb8\xae\xa4\xa7\xa7K\xcb\xc8<\xa9\x9d\x9alp+\xd8\xde]\x1d\xa8N\x8b\
\xfd\x02m]\xd99}\x02cx\x16\xdd\xb3\xe2<\xd7\x94\x1e\xa8\xf4%\x8d\xe4\xc0_\
\x11g\x91\xb0\xb4\xf4\xe4\x8d\x06\x9fk\x03{\xb3\xd5\xc8\xe8\xe8\xd5\x17\xf8<\
\x1b\xf1\xe8\x81\xd5v\xd7\x86\xd4\x81\xd5\x8c\x180=@MV\xc1\xc7\xf6\xd333\xeb\
G\x9bt~\xac\xb9\xca\x1e\xbb\xe8\x9b\xc1\x9d\x8b\x8b\xdc\xe1\xdc\xa3\xb3\xb3o\
zV\xc0v\xf5\x8d\x8d\xbb\xce\x0e\x17\xf4\xc4Y\xff\xc9n\'y\xfd\xef\xc9\xc9E~M=\
M\xeb\x92\xfb\xa9j\xc6j?\x0ew\xb7\t\x8f\x9fj\t\xbaW,\xc8KA\x020n\xc0DX\xf7&}\
u_[\x80Q>/\xa1\xa9\xa9\x89?N\x1dm\x00\xc2\x1e\xa6\x12\xaa-\xf0J\xb5\xa8\x95x\
861\xd1\x93\xaf\x18\xa0Yb\xb8\x7fp\x90\xcc\x01\xf7\xbc\x08\x99\x1b\xe1\x9b\
\xb9\xb1\xb4\xbf>vt\x16\x0c\x04\xdf\xf1o\xf6S\xe0\x02)\xd6\xd1\xd1\t\xfc\xdd\
F\x1e\x08\x88`Wk\xa6Zt\x95\x91\x91\xb1\xba\xea\x1aT]Gg(U6\xe7\xf6\xd5\x1850<\
\x80Q\x16\x0fO\x00\t@~\x0b\t\x8e\xfa\xe5\xe3\xac\xf1\x1a\x91QQ\xc0G\x00P\xd9\
\xd9\xd9\xbf67\x1fg\x1f\xe8\x0b\xaaYZr\x06\x7f)\xb8DN\xe7~\xf4\xfb\tH\x1e\
\xc8\xd0\xe0\xf0\xf0\xee\xb7\x8cRq\xe1\xa1\xfd\xfd\xfd\x8f/\xf7\x1c\xc0\xb2J\
\x05\x89\xfd\xfdpP\x08\xe6\xc3\x07\x9b\x91|\xc5\xd7\xaa<\xef\xdf\xbf\x7f\x9b\
\x95UT_\x8f\xa4"{Um\x94\x12\x06g\xc1B\x1c\xcd\xcd\xcd\x13LLL\x94?Ll\xe2<W\
\xa9D3\xa9\xe35:\xba\xe3\xd9_\xee\x13\x1eRFu\x0c\x0e\x0e^M\xec\x89\xe9B\xbd\
\xeex\xf2\xf3\xe7O\xc7g\xcf\xda\x80+\x12{\xaesr\x96\xe0p\xd7\xcd2(\xc9^\xa9\
\xa1\t%uF\xd6\xd6\x89\x1a\xe8\xa2\xdaZ\xc6\x08\xd5\xfb\xb6\xb6\xff\xb4+\x1d\
\x8b\x19[\x7f\x87\xc5&\xb7\xb4(\xd1q\x98\xfa\x9d\xc8\xc9\xcb\xc7\x0e\xac\xaa\
\x96\x8e%k\x0bP\xdf\xd4\xcdu\'\xa9\xad\xd0\'\'U\x19\xb4\x93\xdc\xf3o\x0e.5\
\xafD"\x8d\x8d%$$\xee\x8bf\xda:8D\xe6\xe7sq\xf9-B?\x99\xdf\x86\x97x\xf6\x19\
\xc2KR\xc0\x1d\x0e:rdy:\x80\xfa\xce\xd0\x9d\x05}333\x9a{\x80\xaa\x0f\xd1\x04\
q%%]771\xab\xea\xcc\xc8H2@\x11 \x010\x1f\x1b;\xfb\xf1/t"\x18\x9b|\x99\x03\
\x1eg\x7f}d\x9d\'U\x8a\xf4\xb9\xf3t\x81\x88\x13\x19\x9a\xb0\xe9P\x1a\xe1o\
\xd0\xcb\x85Z\xa5cc\xb6\xb6\xb6\x9c\xe1\xdc\xa7\t\x04Gi\xd3J\xa44\x1b-\xc1\
\x91)^\xe3\x81\x89\t\x0b\x10\x7fc\xc3\x89*\x82\xa4X\xb0\x18Y.\xc1Jc\xd1\xe4M\
\tRBp|WW\x97\x9e\x90@\x07\x94\xbd\xa2t\xc4}\xe9\xd2% \x87$(\xe5\xd1#\xea\xba\
\xba:P\x01\xe0\x17\x80s\x97kC\xed\xd3\x11.2rr-\x18\x03,U\x0b\xd4\x05F\x96\
\xb6\xae.\x1c\x9czN\xc6;;;\x95/Q"1\x9dB*\xc2\x035\xf2\xd7\xe2\x0e\xc0k\xfeV \
\x9f\xdb{D\xc9\xc9\xc9E\x13\x1c\xed\x1c\x1d\xa3\x03\x95F\xde\xeb\xe4$\xc1(\r\
\x98\xe8\xd5\xe9\xd1\x04M\x18\x03\x0f\x07\x9d\x91\x81\xc1\xfd\xa0 E\x87\xda\
\xac\xedmW@\x84dX\xcc\xf7\xef\xc8@\xa5\x85\x94\xa3\xeen\rPX\xc0\xe16\x7f\x9e\
.c\x8c\x9a\xbb|\x1e\x02\x81H\x82\x974\xbe\xd82\xaf)/\xdf\x9c\xd3\x16\xf0\xca\
\xbe\xa8\xee\xc4\xa4\xf3r\xa7\xf9\xa4\xf4\xd9]LN\x9a\x82\xa3E\xb5\x89 Sl\xdd\
\xf3\t\xb0\x91\x04\x98\xd6;\xc3[\xa0\xee\xa9&\x1f\x80\xd3b}\xc1\xab\xea\xf4\
\x80\xa40\xad\\\xe5\x10.\xfc\x9c\xae\xb5\xf5\x8d\x8e\x8e\x0e\xbff+\xd0\xd9\
\x8f\xb0Y\xe2a\xad\xeb\x9c<\x1d\xa7|g\xd4\x8d\xe0hn\n5^zY\xb7ym\x80\xd8t\xb8\
\xc7R{\xc4yXX\x98u\x7f\r\x07\xa9j\xeb\x11\x8aT2\xcd\xb9\xf4\x11\x1f\xb7\x98U\
/V\xbf\xaa\x16g!\xcaF\x17U]\x86(s@\x13\x04\x9b\xe6\\\x81\x04@\x13V\x1a2Q\xeb\
\x16m\xee\xab\x8555\x0c\x10\x10PGip\xcb?  F\x03\xed<\xfd)&;\x9b\r4\x19\xe0\
\x0fP\xd1Y\x96\xbd\xba\xf9\x0f\x1bpW!\x1e\xcf\x0eF\x95\x91\x11H\x1c\xa3\xb6\
\x8e\x8e\xd6\xd3\x91\xfc3\xa2\x9f\xc29\xfb"\x9b8\xc5\xeb\xb0\xbe\xae)\xeb?/P\
\xfc\xa1\xa7\xbc*l\xbd\xbd5\n,\xf1\x1ab@\x99\x82\xb1u\xef\roy\x920H\xa6\xa8e\
\xbbS\x9d\'0\r\xe9\xfdB,\x96\xde,\x83\xe0T\xe7Xg\x9e\xab{\x13H\xdbh!:\xebzG4\
3\x0e\xd8\xad\xbb\xa7\xe7\xe5zI\xe6\xd1\xd7=\xfe\xa2\x13\xd5\xb7\xfe\xda\xce\
S5\x11\xeb\xeb\xcf"##\r---\xbf\xf4\xdbI^\xe0\x05\x03)Xo3\x86\xec\xc1-\xaeE\
\xcc\xa2\x1a\xbf\xaa\xc8&k\x92>|\xf8pO4\xb3\xdc\xaa\x12I\x1d\x1f\x1f\x0f\xa6\
\x0bZ_\xb0\xd7N\x12\xc4m\x1bOTJ\x83\xf3\x17\x0b\xa2\xc4Y\xc5s\x86&\xb7^\x80\
\xe5hii\x03\xc1i\x87C\xce=\xb4:\xe4\xb7\x0cf\xc2\x88"\xe4\xd6\xc7\x93(|V~>\
\x90~\xcd<$\xe4"\xa0F\xc4\xda*\xf7\xf8\x89\xcd\x9b\xd5{\xa3\xec\xc13\xf3\xbf\
\xd9kI\xdf\xb1\xc6\xf0G{\xcb+\xca\x8a\x8b\x8b\x17Nl\xde\xc9\x1ar\x88\x1fY\
\x03\x99\xa0\x8f\xd7\x90\xc8\x19\xa2\xa1\xa1\xd172z5\xe7\xfa\x10\x83\x00\xeb\
\xfd\xf6Sh\x9cs\x9d\xf7[\xa1\x15\xb5l\xfa\xc7T\xec\x8dN\xf1\xd3\x9c\xb0\x02\
\x99\x8b7mm\xf7q\xcd\xcdg?\x80e{\xf83(\xa1\x06\xd7<\x833j\x96}\xeeAV\t\xbd\
\x1f\x93Z$S`\xfcQQQ\xf8\xb5\x9f?\xbf\x03\x06\xe2\xbbPm\x80\x98SS13[\x02\x0c1\
\x85\x08!\xb3Z\x07\xda\xf1\xf1\xf1N\x94\x84U\xd0\xc18\n\x0ec\xa5\xf9*\xfd\
\xbd\xd3\x88=\x7f\xf9G_\xea\x1e\x90I\x11\xcc\xd2\x90\xc7\xbc-\x8eY\xb8.\xacI\
\x10\xda\xfd\x9e[i\x84\xba>\xa7\r47\x94\xe57~n\xbb\xc7w{\xf6\xf8\xed\xc4\xa6\
1\x10\xa1\xe5\xef\x860\x18\x8a\xc0\xdb\xc0\x14\x9e8\x8e\x9bz\xf9\xb0\x82\x11\
)\x19\x99\xae?[3\x06\x18\x84\x1a\xda@7O^FARrW\x89\x1aIy\x9b*\x11+\xbe\xd9\
\x85\xf2\x19\x98\xe0)W/\xfcT\xe9\x88\xc1\xe1p\xeenn\xc4\xa4>;\'\xec\xccV\x19\
\xd0\x13\xb02Z\x8dw\xd2Yv8\xf7\xee\x03\xded\xee\x82\x91Z\x97\x19\xd9*\xab\
\xe6~\x10\x8a\x1fb-G\xcbq\x8e\xd2\xfeI\xab\x19Y\x10\x07\xc1\xf2O\xbe\xd4\x85\
\x14\xd8\x94\x12\x87Wm6\xbeB\xe9e\x87\'g\xc8\xcc\x01ucc\xe6\xad\xad-\xb0\xcd\
@\xa5\x1b\xb29\xf1\xc9\xc9\xf4\xedK\xee\x7fO\x8f\xf7\x88\xa5\x86\x181\x1cAR\
\xcb\xb5C\xd2\x97D\x9f\x0e+\xf2(\xa2ci>,\x0c\xaa\xe3\xe2\xe2\xd2j\'I\x99s\
\xc7\xad\xdbNRBAap\x7f_z!\xf8\xc4\xe5\x08\xccL"<e\xff\xb6xk\xb8O\xec\xb8O\
\xfe\xcc\xa7\xc1<\x92\xb4\xf0Y\x1b\x8c\x1a\xaf\xc4\xd7\xa9\xa9\x97s\x0e\xb5.\
5\xa6"e\x80\x01(\xec\xdb\xc0\xedY\xdc\x82\x06or\xc8\x9a\xa8\xe9OW(\x13\x0f\
\xfcv:\x99\xe4q`\xf0\xdf\xf6\x08jK\x0c\xa2\x8c\'Y3\x1aTw\x91\xad-\xa0w\x9bJ\
\xac\xb2\xac!\xdd\xdeu|\xbb[\xf9@\xd8\x1e\x03/$\x19\xad\xe1\xf6\x0e\xbf\x8c\
\x0f\\\x13\xf1\xba\xf7j!^\xe0c#?9M\xe8u\xf1\x9a\x8f\x1dC5\xdc\xfe\x91\x97\
\xab\x9f\xde\x9az3\xf7\xecD\x99\x87\x13\xd6m\x91`\x0f\x05\x7fQ!Z\xea\xbajU\
\xaa6\xe1\xff\x03|0e\xb7'
