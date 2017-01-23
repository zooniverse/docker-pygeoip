#!/usr/bin/env python

import fileinput

from geoip import geolite2

def match(ip):
    ip = ip.strip()
    match = geolite2.lookup(ip)
    if match is not None:
        print "{} {}".format(ip, match.country)

map(match, fileinput.input())
