#!/usr/bin/python
"""
	Script test all client sources and last time of check. If max check period boundary was exceeded
	script returns problem lines. If all checks were within boundary 1 is returned.
	Main purpose of script is to create check that can be automatically added to your regular system checks.
	This example uses siux lib to connect to server.
"""

import  sys, time, datetime
sys.path.append( '../src' )
import siuxlib

# config
auth = '<YOUR_API_KEY>'

# boundary in seconds
checkBoundary = 60

# current time settings
currentTimestamp = time.time()
currentTime = datetime.datetime.fromtimestamp(currentTimestamp).strftime('%Y-%m-%d %H:%M:%S')

# init
S = siuxlib.SiUXclient( auth=auth )

# make request to server
retList = S.sourceList(auth)

#print return value in case of debugging
#print retList

errors = 0

#check response code from server
if retList['statusCode'] == 'OK':

	for line in retList['data']:

		lastChecked=line['lastChecktime']

		# if source was ever measured
		if lastChecked > 0:

			timeDiff = time.time()-lastChecked

			# check if time difference is within required boundary
			if timeDiff > checkBoundary:

				errors = errors + 1
				print "Domain: %s  -  current time: %s  - last check time: %s  -  time diff: %s s" %(line['url'],currentTime,datetime.datetime.fromtimestamp(line['lastChecktime']).strftime('%Y-%m-%d %H:%M:%S'),timeDiff)

	#sript return value is number of errors
	sys.exit(errors)
else:
	sys.exit(1)

