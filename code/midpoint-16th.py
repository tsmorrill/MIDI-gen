#!/usr/bin/python

import math
import random
import string
import sys

from heightmap import diamond_square
from midiutil.MidiFile import MIDIFile

if len(sys.argv) > 1:
    seed = str(sys.argv[1])
else:
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    seed = ''.join(random.choice(chars) for i in range(8))

iter = 4
length = 2**iter
smoothing = 1

stress_map = diamond_square(iter, smoothing, seed + "stress_map")
# trim to 2^iter square
stress_list = []
for i in range(length // 2):
    stress_list.extend(stress_map[i][:length])
    stress_list.extend(stress_map[i + length//2][:length])

output_file = MIDIFile(1)
track = 0
time = 0
channel = 0
pitch = 60
duration = 1/4
track_name = "16ths " + seed + " {} bar".format(len(stress_list) // 16)
if (len(stress_list) // 16) > 1:
    track_name += "s"
output_file.addTrackName(track, time, track_name)
for index, stress in enumerate(stress_list):
    time = index/4
    # no zero velocity notes
    volume = math.ceil(stress*127)
    volume = max(volume, 1)
    output_file.addNote(track, channel, pitch, time, duration, volume)

filename = track_name + ".mid"
try:
    with open(filename, 'wb') as outf:
        output_file.writeFile(outf)
    print("Created file {}".format(filename))
except:
    print("Write failed.")
