#!/usr/bin/python
"""
	Script test one particular source and his uptime from last error.
	Main purpose of script is to create check that can be automatically added to your regular system checks.
	This example uses siux lib to connect to monitored server.
"""

import  sys, pprint,time, datetime, urlparse
sys.path.append( '../src' )
import siuxlib

if len(sys.argv) <= 1:
	print "Usage source_uptime.py www.yoursource.com"
	sys.exit(1)

# config
auth = '<YOUR_API_KEY>'

# init
S = siuxlib.SiUXclient( auth=auth )

# make request to server
retList = S.sourceList()

# print return value in case of debugging
#pprint.pprint( retList )

# current time settings
tsNow = int( time.time() )

# check response code from server
if retList['statusCode'] != 'OK':
	pprint.pprint( retList )
	sys.exit(1)

# data from api -> sourceList()
for line in retList['data']:

	# from url address to hostname
	hostname = urlparse.urlparse( line['url'] ).netloc

	if sys.argv[1] != hostname:
		continue

	errTime 	= line['lastErrChecktime']
	sourceId	= line[ 'sourceId' ]
	url		= line[ 'url' ]
	state		= line[ 'status' ]

	# only active source
	if state != 'active':
		continue

	# if last return value is not 200 OK
	if errTime == 0:
		print '%s | %s | %s' % (0, 0, url)
		continue

	retInfo = S.sourceInfo( sourceId )

	# error status for sourceInfo()
	if retInfo[ 'statusCode' ] != 'OK':
		pprint.pprint( retInfo )
		continue

	errTime2 = retInfo['data']['lastErrChecktime']
	uptimeSeconds = round( tsNow - errTime2 )
	timeText = '%s s' % uptimeSeconds

	if uptimeSeconds > 60 and uptimeSeconds < 3600:
		timeText="%s m" %  int(uptimeSeconds/60)
	elif uptimeSeconds >= 3600 and uptimeSeconds < 86400:
		timeText="%s h" % int(uptimeSeconds/3600)
	elif uptimeSeconds >= 84000 :
		timeText="%s d" % int(uptimeSeconds/84000)

	print '%s | %s | %s' % (datetime.datetime.fromtimestamp(errTime2).strftime('%Y-%m-%d %H:%M:%S'), timeText, url )

print
print '.done'
