#!/usr/bin/python

import pprint, sys

sys.path.append( '../src' )
import siuxlib

# config
auth = '<YOUR_API_KEY>'

# init
S = siuxlib.SiUXclient( auth=auth )

# source.list()
print "--- source.list() ---- "
retList = S.sourceList()
pprint.pprint( retList )
print

# source.info()
if retList['statusCode']=='OK':

	sourceId = retList['data'][0]['sourceId']

	print "--- source.info( %s ) ---- " % (sourceId,)
	pprint.pprint( S.sourceInfo( sourceId ) )
	print

print
print '.done'

