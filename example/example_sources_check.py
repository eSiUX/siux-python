#!/usr/bin/python
"""
Script test all client sources and last time of check. If max check period boundary was exceeded
  script returns problem lines. If all checks were within boundary 1 is returned
"""

import urllib2
import json
import datetime
import time
import sys

# client api key
apiKey = '<YOUR_API_KEY>'

# boundary in seconds
checkBoundary = 60

req = urllib2.Request('http://www-dev.siux.cz/api/sourceList?api_key=%s' %apiKey)

r = urllib2.urlopen(req)

currentTimestamp=time.time()
currentTime=datetime.datetime.fromtimestamp(currentTimestamp).strftime('%Y-%m-%d %H:%M:%S')

txt= r.read()

obj=json.loads(txt)

errors=0

for line in obj['data']:

	lastChecked=line['lastChecktime']

	# if source was ever measured
	if lastChecked>0:

		timeDiff= time.time()-lastChecked

		# check if time difference is within required boundary
		if timeDiff> checkBoundary:

			errors=errors+1
			print "Domain: %s  -  current time: %s  - last check time: %s  -  time diff: %s s" %(line['url'],currentTime,datetime.datetime.fromtimestamp(line['lastChecktime']).strftime('%Y-%m-%d %H:%M:%S'),timeDiff)

#sript return value is number of errors
sys.exit(errors)

