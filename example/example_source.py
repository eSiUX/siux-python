#!/usr/bin/python

import pprint, sys

sys.path.append( '../src' )
import siuxlib

# config
auth = '<YOUR_API_KEY>'

# init
S = siuxlib.SiUXclient( auth=auth )

# source.list()
print "--- source.list( %s ) ---- " % auth
retList = S.sourceList(auth)
pprint.pprint( retList )
print

# source.info()
if retList['statusCode']=='OK':

	sourceId = retList['data'][0]['sourceId']

	print "--- source.info(%s, %s) ---- " % (auth, sourceId)
	pprint.pprint( S.sourceInfo( auth, sourceId ) )
	print

