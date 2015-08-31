#!/usr/bin/python
"""
	Script returns all sources/checks list
"""
import sys, pprint

sys.path.append( '../siux' )
import siuxlib

# client api key
auth = '<YOUR_API_KEY>'

# init
S = siuxlib.SiUXclient( auth = auth )

# source.list()
print "--- source.list() ---- "
retList = S.sourceList()

# check response code from server
if retList['statusCode'] != 'OK':
	pprint.pprint( retList )
	sys.exit(1)

# output
for line in retList['data']:

	print line
	print

# complete
print
print ".done"
