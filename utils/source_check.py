#!/usr/bin/python
"""
	Script test all client sources and last time of check. If max check period boundary was exceeded
	script returns problem lines. If all checks were within boundary 1 is returned.
	Main purpose of script is to create check that can be automatically added to your regular system checks.
	This example uses siux lib to connect to server.
"""

import  sys, time, datetime, pprint
sys.path.append( '../src' )
import siuxlib

# config
auth = '<YOUR_API_KEY>'

# boundary in seconds
checkBoundary = 65

# init
S = siuxlib.SiUXclient( auth=auth )

while 1:

	# current time settings
	tsNow = time.time()
	nowDate = time.strftime('%Y-%m-%d', time.localtime(tsNow) )
	nowTime = time.strftime('%H:%M:%S', time.localtime(tsNow) )

	# make request to server
	retList = S.sourceList()

	# print return value in case of debugging
	#pprint.pprint( retList )

	errNo = 0

	# check response code from server
	if retList['statusCode'] != 'OK':
		pprint.pprint( retList )
		sys.exit(1)

	print "%7s | %10s | %5s | %s" % ('State', 'Last check', 'Diff', 'Url' )
	print "------------------------------------------------------------------------"
	for line in retList['data']:

		lastChecked = line[ 'lastChecktime' ]
		lastStatus  = line[ 'lastStatusCode' ]
		sourceType  = line[ 'sourceType' ]

		# if source was ever measured
		if lastChecked == 0:
			continue

		diffTime = time.time() - lastChecked

		# check if time difference is within required boundary
		if diffTime > checkBoundary:
		
			# hack for RUM (real user monitoring) source
			if sourceType == 'rum':
				__state = 'OK'
			else:
				errNo = errNo + 1
				__state = 'RUN ERR'

		# last status code
		else:
			if lastStatus == 200:
				__state = 'OK'
			else:
				__state = 'ERR'
				errNo = errNo + 1

		# format for last check time 
		lastCheckDate = time.strftime('%Y-%m-%d', time.localtime(lastChecked) )
		lastCheckTime = time.strftime('%H:%M:%S', time.localtime(lastChecked) )

		if lastCheckDate == nowDate:
			__lastTime = lastCheckTime
		else:
			__lastTime = lastCheckDate

		# output
		print "%7s | %10s | %3s s | %s" % \
			(__state,  __lastTime, int(diffTime), line['url'] )

	print "------------------------------------------------------------------------"
	print "Now   : %s %s" % ( nowDate, nowTime)
	print "Sleep : %s s" % (checkBoundary,)
	print "Errors: %s x" % (errNo,)

	print
	time.sleep( checkBoundary )

# complete
print 
print ".done"
