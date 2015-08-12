#!/usr/bin/python
"""
	Script returns all sources list
"""
import sys
sys.path.append( '../src' )
import siuxlib

# client api key
auth = '<YOUR_API_KEY>'

# init
S = siuxlib.SiUXclient( auth = auth )

# source.list()
print "--- source.list( %s ) ---- " % auth
retList = S.sourceList( auth )

#check response code from server
if retList['statusCode'] == 'OK':

	for line in retList['data']:

		print line