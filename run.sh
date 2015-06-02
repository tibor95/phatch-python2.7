#!/bin/bash

#the purpose of this file is to start phatch without installing and to avoid any
#troubles with paths (as phatch.py is sensitive to paths)
#this file must be left in its original "relative" location to other components of phatch
#though it can be run from any directory (f.e. referencing absolute or relative path)



#this is to switch current working directory to a directory where script is located
cd $(dirname $(readlink -f $0))

python2.7 phatch/phatch.py
