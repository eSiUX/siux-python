#!/usr/bin/python
"""
	Script adds one source to monitor to your account.
"""

import  sys, pprint

sys.path.append( '../siux' )
import siuxlib

# config
auth = '<YOUR_API_KEY>'

# init
S = siuxlib.SiUXclient( auth=auth )

# name of the source
name = "siux"

# url to be checked
url = "www.esiux.net"

# make request to server
retList = S.sourceAdd( name , url )

# print return value in case of debuging
pprint.print( retList )

#check response code from server
if retList['statusCode'] == 'OK':

	for line in retList['data']:

		print line

# complete
print
print ".done"
