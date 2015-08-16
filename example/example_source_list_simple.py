#!/usr/bin/python

# minimalistic way how to get source list
import sys
sys.path.append( '../src' )
import siuxlib

auth = '<YOUR_API_KEY>'
S = siuxlib.SiUXclient( auth=auth )
retList = S.sourceList()
if retList['statusCode'] == 'OK':
	for line in retList['data']:
		print line
