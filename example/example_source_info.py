#!/usr/bin/python
"""
	Script returns complete source info based on source id.
	The best way to get sourceId is to run example_source_list.py scritp first
"""

import pprint,  sys
sys.path.append( '../src' )
import siuxlib

# config
auth = '<YOUR_API_KEY>'

# init
S = siuxlib.SiUXclient( auth=auth )

#your source id
sourceId="<your sourceId>"
#sourceId=<your sourceId>

# make request to server
retList = S.sourceInfo(auth,sourceId)

pprint.pprint(retList)


