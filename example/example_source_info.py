#!/usr/bin/python
"""
	Script returns complete source info based on sourceId.
	The best way to get sourceId is to run example_source_list.py script first
"""

import pprint,  sys

sys.path.append( '../siux' )
import siuxlib


# config
auth = '<YOUR_API_KEY>'

# init
S = siuxlib.SiUXclient( auth=auth )

# your source id
sourceId = '<YOUR_SOURCE_ID>'

# make request to server
print "--- source.info( %s ) ---- " % (sourceId,)
retList = S.sourceInfo( sourceId )

# output
pprint.pprint( retList)

# complete
print
print ".done"


