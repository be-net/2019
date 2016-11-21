#!/usr/bin/env python3
from yaml import load
from jinja2 import Environment
from sys import argv
import glob
import os



# get program file from command line
yam = argv[1]
with open(yam) as fd:
    data = load(fd.read())
data['talks'] = {}
data['posters'] = {}
participants = []
for f in glob.glob('abs/*.yaml'):
    with open(f, 'r') as fd:
        _data = load(fd.read())
    name = os.path.basename(f)[:-5]

    if 'talk' in name:
        data['talks'][name] = _data
        # participants.extend(_data['Authors'])
        participants.append(_data['Authors'][0])
    elif 'poster' in name:
        data['posters'][name] = _data
        participants.append(_data['Authors'][0])
    elif 'affs' in name:
        data['affs'] = _data
    elif 'regi' in name:
        data['reg'] = _data
        participants.extend(_data)
    else:
        data['talks'][name] = _data
        participants.append(_data['Authors'][0])

data['participants'] = participants

# get template from command line
tmp = argv[2]
with open(tmp) as fd:
    template = fd.read()

# set parameters
env = Environment(lstrip_blocks=True, trim_blocks=True)
if tmp.endswith("tex.jinja"):
    env.block_start_string = "[[%"
    env.block_end_string = "%]]"
    env.variable_start_string = "[["
    env.variable_end_string = "]]"
    env.comment_start_string = "[[="
    env.comment_end_string = "=]]"


# custom filter
def timeformat(mins):
    return '{}:{:02d}'.format(mins // 60, mins % 60)


def readtime(string):
    n = list(map(int, string.split(':')))
    return n[0]*60 + n[1]


def update_time(times, event, lenghts, quiet=False):
    if 'start' in event.keys():
        now = readtime(event['start'])
        times[-1] = now
    else:
        now = times[-1]

    if 'lenght' in event.keys():
        delta = int(event['lenght'])
    else:
        delta = int(lenghts)

    times.append(now+delta)

    if quiet:
        return ''
    return timeformat(now)


def aff_filter(allaffs, affs, quiet=False):
    ind = []
    for aff in affs:
        if aff not in allaffs:
            allaffs[aff] = len(allaffs) + 1
            ind.append(allaffs[aff])
        else:
            ind.append(allaffs[aff])
    if quiet:
        return ""
    return sorted(ind)


def filter_bykey(allaffs, keylist):
    return [allaffs[k] for k in keylist]


def update_dict(dictionary, key, value=None):
    if value is None:
        if isinstance(key, list):
            for k in key:
                dictionary[k] += 1
        else:
            print(key)
            dictionary[key] += 1
    else:
        if isinstance(key, list):
            for k in key:
                dictionary[k] = int(value)
        else:
            dictionary[key] = int(value)
    return ""

env.filters['update_time'] = update_time
env.filters['aff_filter'] = aff_filter
env.filters['filter_bykey'] = filter_bykey
env.filters['update_dict'] = update_dict

render = env.from_string(template)
print(render.render(data))
