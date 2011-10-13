#!/usr/bin/python2

"""
Author: shadyabhi (abhijeet[dot]1989[at]gmail[dot]com)

"""

import bencode
import sys
from os import path

if len(sys.argv) < 2:
    print "First argument: File containing trackers"
    print "Second argument: .torrent file"
    sys.exit(0)

tracker_file = open(sys.argv[1])
torrent_file = open(sys.argv[2])

trackers_list = []
trackers_list[:] = (value for value in tracker_file.read().split("\n") if value != '')
decoded_data = bencode.bdecode(torrent_file.read())

print "Trackers Before: "
for tracker in decoded_data['announce-list']:
    print tracker

for tracker in trackers_list:
    if tracker not in decoded_data['announce-list']:
        decoded_data['announce-list'].append([tracker])

print "Now, the trackers in the torrent are: "
for tracker in decoded_data['announce-list']:
    print tracker

#Writing the torrent file
f = open("new_"+path.basename(sys.argv[2]), "w")
f.write(bencode.bencode(decoded_data))
f.close()
